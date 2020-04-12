# sprites.py

"""
Importe le code du fichier <<ai_system.py>>
"""

from ai_system import * #import code from settings


"""
Classe Map
- But : dessiner une carte donnee en fonction du niveau de jeu selectionne
- Fonctionnement : redimensionne la carte en fonction de la resolution de l'ecran. Gere le deplacement de la carte et partage sa position avec la classe Prgm()
- Utilisation : est ajoutee a la classe Virtuals() au debut d'une partie et est lue a chaque boucle
"""
class Map():
    def __init__(self, glob):
        self.glob = glob
        self._layer = 0
        self._type = "func_sprite_prime"

        self.indicative_width = 2.5
        self.indicative_height = 1
        self.indicative_pos = vec(0,0.075)

        self.spd = vec(0, 0)
        self.acc = vec(0, 0)

        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
        
        i = self.glob.game_lvl*(15/95)
        self.image = self.glob.sprite["map"][int(i)]
        self.image = pg.transform.scale(self.image, (math.ceil(self.indicative_width * self.glob.data["screen_width"]), math.ceil(self.indicative_height * self.glob.data["screen_height"])))
        self.rect = self.image.get_rect()

        self.mouse1_x = self.glob.mouse_pos.x
        self.mouse2_x = self.glob.mouse_pos.x

        self.map_offset = 0

        self.rect.x = self.pos.x
        self.rect.y = self.pos.y

        self.glob.map_instance = self

        self.glob.all_virtuals.add([self])

    """
    Fonction update
    - Fonctionnement : est lue a chaque boucle et effectue des calculs de vitesse de glissment de la carte
    """
    def update(self):

        self.acc = vec(0, 0)
        self.keyboard_scroll()
        
        self.acc.x += self.spd.x * - 0.4
        self.spd.x += self.acc.x
        speedX = int(self.spd.x * self.glob.fps_stab * (self.glob.data["screen_height"]/720))

        if self.glob.mouse_pos.y > self.pos.y and self.glob.mouse_pos.y < self.pos.y + self.rect.h:
            self.mouse_scroll()
        
        self.pos.x += speedX


        if self.pos.x + self.spd.x > 0 or self.pos.x + self.spd.x < self.glob.data["screen_width"] - self.rect.w:
            if self.pos.x + self.spd.x > 0:
                self.spd.x = 0
                self.pos.x = 0
                self.acc = vec(0,0)
            if self.pos.x + self.spd.x < self.glob.data["screen_width"] - self.rect.w:
                self.spd.x = 0
                self.pos.x = self.glob.data["screen_width"] - self.rect.w
                self.acc = vec(0,0)
            """position change var to be transfered to virtual change
            create virtual change var such as I can write a modif for all + parametrics"""

        self.map_offset = self.pos.x - self.rect.x

        self.glob.map_instance = self
        
        self.rect.x = self.pos.x
        self.rect.y = self.pos.y
    

    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille de la carte si la resolution de l'ecran est modifiee
    """
    def prime_update(self):
        
        if self.glob.Resol_Check.change:
            if self.glob.data["screen_height"] == 720:
                self.pos = self.pos * (2/3)
            else:
                self.pos = self.pos * (3/2)
                
            self.image = pg.transform.scale(self.image, (math.ceil(self.indicative_width * self.glob.data["screen_width"]), math.ceil(self.indicative_height * self.glob.data["screen_height"])))
            self.rect = self.image.get_rect()
            self.rect.x = self.pos.x
            self.rect.y = self.pos.y

            self.spd.x = 0
            self.map_offset = 0
            self.glob.map_instance = self
        
    """
    Fonction mouse_scroll
    - Fonctionnement : si le bouton droit de la souris est active : calcule la distance en abscisse entre la position de la souris actuelle et celle de la boucle precedente et fait coulisser la carte
    """
    def mouse_scroll(self):

        self.mouse1_x = self.glob.mouse_pos.x
        if pg.mouse.get_pressed()[2]:
            self.spd.x = (self.mouse1_x - self.mouse2_x) / self.glob.fps_stab
            speedX = int(self.spd.x * self.glob.fps_stab)
            self.acc = vec(0,0)
        self.mouse2_x = self.glob.mouse_pos.x
    
    """
    Fonction keyboard_scroll
    - Fonctionnement : si un bouton directionnel du clavier est active : fait coulisser la carte
    """
    def keyboard_scroll(self):

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.acc += vec(15, 0)
        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.acc -= vec(15, 0)


"""
Classe Turret
- But : gerer les parametres de la tourelle
- Fonctionnement : selon ses parametres, la tourelle sera positionnee par rapport a la position relative du chassis. Elle va acquerir la cible et engager un protocole de combat en envoyant des projectiles kinetics.
- Utilisation : la classe sera liee au chassis par un partage de variables. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle. 
"""
class Turret():
    def __init__(self, glob, image_file, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite_prime"
        
        self.pos = self.glob.pos
        self.pos_adj = vec(0,0)
        self.recoil = vec(0,0)
        self.recoil_act = False
        self.recoil_phase = "back"
        self.fire = False
        self.fire_range = 0
        self.fire_rate = 0

        
        self.go = False
        self.salvo = 1
        self.salvo_count = 0
        self.salvo_interval = 0.001
        
        self.rot = self.glob.rot
        self.former_rot = 0
        self.rot_speed = 2
        self.rot_target = 0

        self.timer = Timer()
        self.timer1 = Timer()
        self.timer2 = Timer()
        self.timer3 = Timer()
        

        self.image_file = image_file
        self.image = image_file
        self.image = pg.transform.scale(self.image, (math.ceil((self.image.get_rect().w / DIVIDENT) * (self.glob.glob.data["screen_height"]/720)), math.ceil((self.image.get_rect().h / DIVIDENT) * (self.glob.glob.data["screen_height"]/720))))
        self.image = pg.transform.rotate(self.image, -90)
        self.original_image = self.image.copy()
        
        self.projectile_image = 0
        self.projectile_speed = 0
        self.projectile_damage = 0
        self.fire_sound = 0
        self.explosion_anim = 0
        self.explosion_sound = 0
        self.trail_anim = 0
        
        self.rect = self.image.get_rect()

    """
    Fonction update
    - Fonctionnement : elle va modifier la position de la tourelle en fonction de la position du chassis. Elle va s'occuper de l'acquisition de la cible et engager un protocole de combat definit par des parametres de depart.
    """
    def update(self):
        self.fire = False

        self.pos = self.glob.pos + self.pos_adj.rotate(-self.glob.rot) + self.recoil.rotate(-self.rot)
        if self.glob.hp > 0:
            Turret_AI(self)
            if self.fire:
                self.go = True
            
            if self.go == True:
                if self.timer3.chrono(self.salvo_interval):
                    self.recoil_act = True
                    self.recoil.x = 0
                    self.recoil_phase = "back"
                    Kinetic_Projectile(self ,self.projectile_image, self.projectile_speed , self.projectile_damage, self.fire_sound, self.trail_anim, self.explosion_anim, self.explosion_sound)
                    self.salvo_count += 1
                    if self.salvo_count >= self.salvo:
                        self.go = False
                        self.salvo_count = 0




            if self.recoil_act:
                if self.timer1.chrono(self.fire_rate/50):
                    if self.recoil_phase == "back" and self.recoil.x > -0.003 * self.glob.glob.data["screen_width"]:
                        self.recoil.x -= 2 * 0.0007813 * self.glob.glob.data["screen_width"]
                    elif self.recoil_phase == "back":
                        self.recoil.x -= 0.0007813 * self.glob.glob.data["screen_width"]
                    if self.recoil.x <= -0.005 * self.glob.glob.data["screen_width"]:
                        self.recoil_phase = "forward"
                    if self.recoil_phase == "forward" and self.recoil.x < 0:
                        self.recoil.x += 0.0007813 * self.glob.glob.data["screen_width"]
                    elif self.recoil_phase == "forward":
                        self.recoil_act = False
                        self.recoil_phase = "back"
                        self.recoil.x = 0

        if self.former_rot >= self.rot + 5 or self.former_rot <= self.rot -5:
            self.image = pg.transform.rotate(self.original_image, self.rot)
            self.former_rot = self.rot
        
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
    

    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille de la tourelle si la resolution de l'ecran est modifiee
    """
    def prime_update(self):
        
        if self.glob.glob.Resol_Check.change:

            if self.glob.glob.data["screen_height"] == 720:
                self.pos_adj = self.pos_adj * (2/3)
                self.recoil = self.recoil * (2/3)
                self.pos = self.glob.pos + self.pos_adj.rotate(-self.glob.rot) + self.recoil.rotate(-self.rot)
            else:
                self.pos_adj = self.pos_adj * (3/2)
                self.recoil = self.recoil * (3/2)
                self.pos = self.glob.pos + self.pos_adj.rotate(-self.glob.rot) + self.recoil.rotate(-self.rot)

            self.image = self.image_file
            self.image = pg.transform.scale(self.image, (math.ceil((self.image.get_rect().w / DIVIDENT) * (self.glob.glob.data["screen_height"]/720)), math.ceil((self.image.get_rect().h / DIVIDENT) * (self.glob.glob.data["screen_height"]/720))))
            self.image = pg.transform.rotate(self.image, -90)
            self.original_image = self.image.copy()
            self.image = pg.transform.rotate(self.original_image, self.rot)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            

"""
Classe Launcher
- But : gerer les parametres du lance missile
- Fonctionnement : selon ses parametres, la tourelle sera positionnee par rapport a la position relative du chassis. Elle va acquerir la cible et engager un protocole de combat en envoyant des missiles balistiques.
- Utilisation : la classe sera liee au chassis par un partage de variables. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Launcher():
    def __init__(self, glob, image_file, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite_prime"
        
        self.pos = self.glob.pos
        self.pos_adj = vec(0,0)
        self.recoil = vec(0,0)
        self.recoil_act = False
        self.recoil_phase = "back"
        self.fire = False
        self.fire_range = 0
        self.fire_rate = 0
        # How many roclets per batch?
        self.salvo = 0
        # How much time between two rockets
        self.salvo_interval = 0
        # When to shoot?
        self.go = False
        # How many salvos fired?
        self.salvo_count = 0
        
        self.rot = self.glob.rot
        self.former_rot = 0
        self.rot_speed = 2
        self.rot_target = 0


        self.timer = Timer()
        self.timer1 = Timer()
        self.timer2 = Timer()
        self.timer3 = Timer()


        self.image_file = image_file
        self.image = image_file
        self.image = pg.transform.scale(self.image, (math.ceil((self.image.get_rect().w / DIVIDENT) * (self.glob.glob.data["screen_height"]/720)), math.ceil((self.image.get_rect().h / DIVIDENT) * (self.glob.glob.data["screen_height"]/720))))
        self.image = pg.transform.rotate(self.image, -90)
        self.original_image = self.image.copy()
        
        self.projectile_image = 0
        self.projectile_speed = 0
        self.projectile_damage = 0
        self.fire_sound = 0
        self.explosion_anim = 0
        self.explosion_sound = 0
        self.trail_anim = 0
        self.missile_rot_speed = 0

        
        self.rect = self.image.get_rect()


    """
    Fonction update
    - Fonctionnement : elle va modifier la position du lance missile en fonction de la position du chassis. Elle va s'occuper de l'acquisition de la cible et engager un protocole de combat definit par des parametres de depart.
    """
    def update(self):
        self.fire = False

        self.pos = self.glob.pos + self.pos_adj.rotate(-self.glob.rot) + self.recoil.rotate(-self.rot)

        if self.glob.hp > 0:
            Turret_AI(self)
            if self.fire:
                self.go = True
            
            if self.go == True:
                if self.timer3.chrono(self.salvo_interval):
                    self.recoil_act = True
                    self.recoil.x = 0
                    self.recoil_phase = "back"
                    Ballistic_Missile(self ,self.projectile_image, self.projectile_speed, self.missile_rot_speed, self.projectile_damage, self.fire_sound, self.trail_anim, self.explosion_anim, self.explosion_sound)
                    self.salvo_count += 1
                    if self.salvo_count >= self.salvo:
                        self.go = False
                        self.salvo_count = 0
                        self.recoil.x = 0

                
            if self.recoil_act:
                if self.timer1.chrono(self.fire_rate/50):
                    if self.recoil_phase == "back" and self.recoil.x > -0.003 * self.glob.glob.data["screen_width"]:
                        self.recoil.x -= 2 * 0.0007813 * self.glob.glob.data["screen_width"]
                    elif self.recoil_phase == "back":
                        self.recoil.x -= 0.0007813 * self.glob.glob.data["screen_width"]
                    if self.recoil.x <= -0.005 * self.glob.glob.data["screen_width"]:
                        self.recoil_phase = "forward"
                    if self.recoil_phase == "forward" and self.recoil.x < 0:
                        self.recoil.x += 0.0007813 * self.glob.glob.data["screen_width"]
                    elif self.recoil_phase == "forward":
                        self.recoil_act = False
                        self.recoil_phase = "back"
                        self.recoil.x = 0

        if self.former_rot >= self.rot + 5 or self.former_rot <= self.rot -5:
            self.image = pg.transform.rotate(self.original_image, self.rot)
            self.former_rot = self.rot

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille du lance missile si la resolution de l'ecran est modifiee
    """
    def prime_update(self):
        
        if self.glob.glob.Resol_Check.change:

            if self.glob.glob.data["screen_height"] == 720:
                self.pos_adj = self.pos_adj * (2/3)
                self.recoil = self.recoil * (2/3)
                self.pos = self.glob.pos + self.pos_adj.rotate(-self.glob.rot) + self.recoil.rotate(-self.rot)
            else:
                self.pos_adj = self.pos_adj * (3/2)
                self.recoil = self.recoil * (3/2)
                self.pos = self.glob.pos + self.pos_adj.rotate(-self.glob.rot) + self.recoil.rotate(-self.rot)

            self.image = self.image_file
            self.image = pg.transform.scale(self.image, (math.ceil((self.image.get_rect().w / DIVIDENT) * (self.glob.glob.data["screen_height"]/720)), math.ceil((self.image.get_rect().h / DIVIDENT) * (self.glob.glob.data["screen_height"]/720))))
            self.image = pg.transform.rotate(self.image, -90)
            self.original_image = self.image.copy()
            self.image = pg.transform.rotate(self.original_image, self.rot)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

"""
Classe Body
- But : gerer les parametres du corps et son ombre
- Fonctionnement : dessine le corps et son ombre
- Utilisation : la classe sera liee au chassis par un partage de variables. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Body():
    def __init__(self, glob, image_file, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite_shadow_prime"
        
        self.pos = self.glob.pos
        self.rot = 0
        self.former_rot = 0


        self.image_file = image_file
        self.image = image_file
        self.image = pg.transform.scale(self.image, (math.ceil((self.image.get_rect().w / DIVIDENT) * (self.glob.glob.data["screen_height"]/720)), math.ceil((self.image.get_rect().h / DIVIDENT) * (self.glob.glob.data["screen_height"]/720))))
        self.image = pg.transform.rotate(self.image, -90)
        self.original_image = self.image.copy()
        
        
        self.rect = self.image.get_rect()

        self.shadow = self.image.copy()
        self.shadow.fill((0, 0, 0, 90), None, pg.BLEND_RGBA_MULT)
        self.original_shadow = self.shadow.copy()

        
        self.shadow_rect = self.shadow.get_rect()

    """
    Fonction update
    - Fonctionnement : elle va modifier la position du corps et de l'ombre en fonction de la position du chassis.
    """
    def update(self):
        
        self.pos = self.glob.pos
        self.rot = self.glob.rot

        if self.former_rot >= self.rot + 5 or self.former_rot <= self.rot -5:


            self.image = pg.transform.rotate(self.original_image, self.rot)
            self.rect = self.image.get_rect()
            self.shadow = pg.transform.rotate(self.original_shadow, self.rot)
            self.shadow_rect = self.image.get_rect()

            self.former_rot = self.rot
            

        self.rect.center = self.pos
        self.shadow_rect.center = self.pos + vec(-5,5)
    
    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille du corps et de l'ombre si la resolution de l'ecran est modifiee.
    """
    def prime_update(self):
        
        if self.glob.glob.Resol_Check.change:
            self.image = self.image_file
            self.image = pg.transform.scale(self.image, (math.ceil((self.image.get_rect().w / DIVIDENT) * (self.glob.glob.data["screen_height"]/720)), math.ceil((self.image.get_rect().h / DIVIDENT) * (self.glob.glob.data["screen_height"]/720))))
            self.image = pg.transform.rotate(self.image, -90)
            self.original_image = self.image.copy()
            self.image = pg.transform.rotate(self.original_image, self.rot)
            self.rect = self.image.get_rect()
            self.shadow = self.image.copy()
            self.shadow.fill((0, 0, 0, 90), None, pg.BLEND_RGBA_MULT)
            self.original_shadow = self.shadow.copy()
            self.shadow_rect = self.shadow.get_rect()
            self.rect.center = self.pos
            self.shadow_rect.center = self.pos + vec(-5,5)


"""
Classe Kinetic_Projectile
- But : gerer les parametres du projectile cinetique
- Fonctionnement : dessiner le projectile et le fait avancer selon sa vitesse. Si collision, transmettre le dommage et jouer l'animation d'explosion.
- Utilisation : la classe Kinetic_Projectile() sera appelee quand la tourelle tire. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Kinetic_Projectile():
    def __init__(self, glob, image_file, speed, damage, fire_sound, trail_anim, explosion_anim, explosion_sound):
        self.glob = glob
        self._layer = 5 # Layer of projectiles
        self._type = "func_sprite_prime"

        self.damage = damage
        self.rot = self.glob.rot
        self.spd = vec(speed * (self.glob.glob.glob.data["screen_height"]/720), 0) # to be defined
        self.max_dist = self.glob.fire_range # to be defined
        self.pos = self.glob.pos + vec(self.glob.rect.w/2, 0).rotate(-self.rot) # to be defined
        self.start_pos = vec(self.pos.x, self.pos.y)

        self.hit = False
        self.trail_anim = trail_anim
        self.explosion_anim = explosion_anim
        self.explosion_sound = explosion_sound

        self.image_file = image_file
        self.image = image_file
        self.image = pg.transform.scale(self.image, (math.ceil((self.image.get_rect().w / DIVIDENT) * (self.glob.glob.glob.data["screen_height"]/720)), math.ceil((self.image.get_rect().h / DIVIDENT) * (self.glob.glob.glob.data["screen_height"]/720))))
        self.image = pg.transform.rotate(self.image, -90)
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.w/2)

        self.timer = Timer()
        self.timer1 = Timer()
        
        self.glob.glob.glob.sound_repertoire.append(fire_sound)
        
        
        self.image = pg.transform.rotate(self.original_image, self.rot)
        self.glob.glob.glob.all_virtuals.add([self])
    
    """
    Fonction update
    - Fonctionnement : elle va modifier la position du projectile cinetique en fonction de sa vitesse.
    """
    def update(self):

        self.pos += self.spd.rotate(-self.rot) * self.glob.glob.glob.fps_stab
        self.pos.x += self.glob.glob.glob.map_instance.map_offset
        self.start_pos.x += self.glob.glob.glob.map_instance.map_offset
        
        if self.max_dist <= math.sqrt((self.pos.x - self.start_pos.x)**2 + (self.pos.y - self.start_pos.y)**2):
            self.hit = True


        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.Explode()
        
        if self.hit == False and self.trail_anim != "None" and self.timer1.chrono(0.01):
            pos = vec(self.pos.x/self.glob.glob.glob.data["screen_width"], self.pos.y/self.glob.glob.glob.data["screen_height"])
            Animation_Player(self.glob.glob.glob, self.trail_anim, 0.01, pos + vec(-0.005,0).rotate(-self.rot), self.rot, 0.003, 0.02, 6)
    
    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille du projectile cinetique si la resolution de l'ecran est modifiee.
    """
    def prime_update(self):

        if self.glob.glob.glob.Resol_Check.change:
            if self.glob.glob.glob.data["screen_height"] == 720:
                self.pos = self.pos * (2/3)
            else:
                self.pos = self.pos * (3/2)

            self.image = self.image_file
            self.image = pg.transform.scale(self.image, (math.ceil((self.image.get_rect().w / DIVIDENT) * (self.glob.glob.glob.data["screen_height"]/720)), math.ceil((self.image.get_rect().h / DIVIDENT) * (self.glob.glob.glob.data["screen_height"]/720))))
            self.image = pg.transform.rotate(self.image, -90)
            self.original_image = self.image.copy()
            self.image = pg.transform.rotate(self.original_image, self.rot)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            self.radius = int(self.rect.w/2)
            
        
        

    """
    Fonction Explode
    - Fonctionnement : est lue dans la boucle update et verifie la condition self.hit. Si self.hit positif, alors lancer l'animation de l'explsion.
    """
    def Explode(self):
        if self.hit == True:
            self.glob.glob.glob.sound_repertoire.append(self.explosion_sound)
            pos = vec(self.pos.x/self.glob.glob.glob.data["screen_width"], self.pos.y/self.glob.glob.glob.data["screen_height"])
            Animation_Player(self.glob.glob.glob, self.explosion_anim, 0.01, pos, self.rot, 0.04, 0.071, 6)
            self.glob.glob.glob.all_virtuals.remove([self])


"""
Classe Ballistic_Missile
- But : gerer les parametres du missile balistique
- Fonctionnement : dessiner le missile et le fait avancer selon sa vitesse et sa cible. Si collision, transmettre le dommage et jouer l'animation d'explosion, sinon dessiner une trainee de fumee.
- Utilisation : la classe Ballistic_Missile() sera appelee quand le lance missile tire. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Ballistic_Missile():
    def __init__(self, glob, image_file, speed, missile_rot_speed, damage, fire_sound, trail_anim, explosion_anim, explosion_sound):
        self.glob = glob
        self._layer = 5 # Layer of projectiles
        self._type = "func_sprite_prime"

        self.damage = damage
        self.rot = self.glob.rot + random.randint(-60,60)
        self.former_rot = 0
        self.rot_speed = missile_rot_speed
        self.spd = vec(speed * (self.glob.glob.glob.data["screen_height"]/720), 0) # to be defined
        self.max_dist = self.glob.fire_range # to be defined
        self.pos = self.glob.pos + vec(self.glob.rect.w/2, 0).rotate(-self.rot) # to be defined
        self.start_pos = vec(self.pos.x, self.pos.y)

        self.rot_target = 0

        self.hit = False
        self.trail_anim = trail_anim
        self.explosion_anim = explosion_anim
        self.explosion_sound = explosion_sound


        self.image_file = image_file
        self.image = image_file
        self.image = pg.transform.scale(self.image, (math.ceil((self.image.get_rect().w / DIVIDENT) * (self.glob.glob.glob.data["screen_height"]/720)), math.ceil((self.image.get_rect().h / DIVIDENT) * (self.glob.glob.glob.data["screen_height"]/720))))
        self.image = pg.transform.rotate(self.image, -90)
        self.original_image = self.image.copy()
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.w/2)

        self.timer = Timer()
        self.timer1 = Timer()
        
        self.glob.glob.glob.sound_repertoire.append(fire_sound)
        
        if self.former_rot >= self.rot + 5 or self.former_rot <= self.rot -5:
            self.image = pg.transform.rotate(self.original_image, self.rot)
            self.former_rot = self.rot

        self.glob.glob.glob.all_virtuals.add([self])
        

    """
    Fonction update
    - Fonctionnement : elle va modifier la position du missile balistique en fonction de sa vitesse et de sa cible.
    """
    def update(self):

        rads = math.atan2(self.glob.glob.pin.y - self.pos.y, self.glob.glob.pin.x - self.pos.x)
        rads %= -2 * math.pi
        self.rot_target = math.degrees(-rads)

        Targeting(self)

        self.pos += self.spd.rotate(-self.rot) * self.glob.glob.glob.fps_stab
        self.pos.x += self.glob.glob.glob.map_instance.map_offset
        self.start_pos.x += self.glob.glob.glob.map_instance.map_offset
        
        if self.max_dist <= math.sqrt((self.pos.x - self.start_pos.x)**2 + (self.pos.y - self.start_pos.y)**2):
            self.hit = True
        
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.Explode()

        if self.hit == False and self.trail_anim != "None" and self.timer1.chrono(0.01):
            pos = vec(self.pos.x/self.glob.glob.glob.data["screen_width"], self.pos.y/self.glob.glob.glob.data["screen_height"])
            self.image = pg.transform.rotate(self.original_image, self.rot)
            Animation_Player(self.glob.glob.glob, self.trail_anim, 0.05, pos + vec(-0.01,random.uniform(-0.002,0.002)).rotate(-self.rot), self.rot, 0.006, 0.05, 6)
    

    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille du missile balistique si la resolution de l'ecran est modifiee.
    """
    def prime_update(self):

        if self.glob.glob.glob.Resol_Check.change:
            if self.glob.glob.glob.data["screen_height"] == 720:
                self.pos = self.pos * (2/3)
            else:
                self.pos = self.pos * (3/2)

            self.image = self.image_file
            self.image = pg.transform.scale(self.image, (math.ceil((self.image.get_rect().w / DIVIDENT) * (self.glob.glob.glob.data["screen_height"]/720)), math.ceil((self.image.get_rect().h / DIVIDENT) * (self.glob.glob.glob.data["screen_height"]/720))))
            self.image = pg.transform.rotate(self.image, -90)
            self.original_image = self.image.copy()
            self.image = pg.transform.rotate(self.original_image, self.rot)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            self.radius = int(self.rect.w/2)


    """
    Fonction Explode
    - Fonctionnement : est lue dans la boucle update et verifie la condition self.hit. Si self.hit positif, alors lancer l'animation de l'explsion.
    """
    def Explode(self):
        if self.hit == True:
            self.glob.glob.glob.sound_repertoire.append(self.explosion_sound)
            pos = vec(self.pos.x/self.glob.glob.glob.data["screen_width"], self.pos.y/self.glob.glob.glob.data["screen_height"])
            Animation_Player(self.glob.glob.glob, self.explosion_anim, 0.01, pos, self.rot, 0.04, 0.071, 6)
            self.glob.glob.glob.all_virtuals.remove([self])



"""
Classe Button
- But : gerer les differents parametres du bouton
- Fonctionnement : verifie les conditions: rest , hover et active (curseur au repos, curseur au-dessus, clique)
- Utilisation : la classe Button() est appelee dans les interfaces utilisateurs (menu/menu cheat). Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Button():
    def __init__(self, glob, text, font, size, pos, w, h, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite_prime"

        self.text = text
        self.font = font
        self.size = size
        self.indicative_width = w
        self.indicative_height = h
        self.indicative_pos = pos
        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
        
        self.border = 4 * (self.glob.data["screen_width"]/1280)

        self.rest_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])), pg.SRCALPHA)
        self.rest_image.fill((61, 209, 177, 255))
        self.rest_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
        self.rest_image_boder.fill((27, 32, 26, 230))
        self.rest_image.blit(self.rest_image_boder, (self.border/2,self.border/2))
        self.original_rest_image = self.rest_image.copy()

        self.hover_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])), pg.SRCALPHA)
        self.hover_image.fill((83, 252, 241, 255))
        self.hover_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
        self.hover_image_boder.fill((27, 32, 26, 230))
        self.hover_image.blit(self.hover_image_boder, (self.border/2,self.border/2))
        self.original_hover_image = self.hover_image.copy()

        self.active_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])), pg.SRCALPHA)
        self.active_image.fill((221, 150, 37, 255))
        self.active_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
        self.active_image_boder.fill((27, 32, 26, 230))
        self.active_image.blit(self.active_image_boder, (self.border/2,self.border/2))
        self.original_active_image = self.active_image.copy()

        
        self.image = self.rest_image.copy()
        
        
        self.rect = self.image.get_rect()

        
        
        self.click = False
        self.active = False
        self.trigger = False

        self.rect.center = self.pos

        self.glob.all_virtuals.add([self])

        self.caption = Text(self.glob, self.text, WHITE, self.font, self.size, pos, self._layer)


    """
    Fonction update
    - Fonctionnement : elle va verifier les differents conditions du bouton en fonction de la position et l'etat de la souris (clique).
    """
    def update(self):
        if self.glob.Resol_Check.change:
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
            self.rest_image = pg.transform.scale(self.original_rest_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.hover_image = pg.transform.scale(self.original_hover_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.active_image = pg.transform.scale(self.original_active_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.image = self.rest_image.copy()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
        
        if self.active == True:
            self.active = False
        
        if self.glob.mouse_pos.x > self.pos.x - (self.rect.w/2) and self.glob.mouse_pos.x < self.pos.x + (self.rect.w/2) and self.glob.mouse_pos.y > self.pos.y - (self.rect.h/2) and self.glob.mouse_pos.y < self.pos.y + (self.rect.h/2):
            # change button style to hover
            self.image = self.hover_image.copy()

            if pg.mouse.get_pressed()[0]:
                # change button style to pressing
                self.click = True
                self.image = self.active_image.copy()
            else:
                if self.click:
                    self.click = False
                    self.active = True
                    self.trigger = True
        else:
            self.click = False
            self.image = self.rest_image.copy()
        
        if self.active:
            self.glob.sound_repertoire.append(self.glob.sounds[12])


    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille du bouton si la resolution de l'ecran est modifiee.
    """
    def prime_update(self):

        if self.glob.Resol_Check.change:
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
            self.rest_image = pg.transform.scale(self.original_rest_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.hover_image = pg.transform.scale(self.original_hover_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.active_image = pg.transform.scale(self.original_active_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.image = self.rest_image.copy()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos


    def change(self):
        self.caption.text = self.text
        self.caption.change()
        self.rect.center = self.pos



"""
Classe Image_Button
- But : gerer les differents parametres du bouton a image
- Fonctionnement : verifie les conditions: rest , hover et active (curseur au repos, curseur au-dessus, clique)
- Utilisation : la classe Image_Button() est appelee dans les interfaces utilisateurs (crossfader dans le menu option). Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Image_Button():
    def __init__(self, glob, rest_image, hover_image, active_image, pos, w, h, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite_prime"

        self.indicative_width = w
        self.indicative_height = h
        self.indicative_pos = pos
        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
        
        self.original_rest_image = rest_image.copy()
        self.rest_image = pg.transform.scale(self.original_rest_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
        self.original_hover_image = hover_image.copy()
        self.hover_image = pg.transform.scale(self.original_hover_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
        self.original_active_image = active_image.copy()
        self.active_image = pg.transform.scale(self.original_active_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))

        self.image = self.rest_image.copy()
        
        self.rect = self.image.get_rect()

        
        self.click = False
        self.active = False
        self.trigger = False

        self.rect.center = self.pos

        self.glob.all_virtuals.add([self])
        
    """
    Fonction update
    - Fonctionnement : elle va verifier les differents conditions du bouton image en fonction de la position et l'etat de la souris (clique).
    """
    def update(self):

        if self.glob.Resol_Check.change:
                self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
                self.rest_image = pg.transform.scale(self.original_rest_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
                self.hover_image = pg.transform.scale(self.original_hover_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
                self.active_image = pg.transform.scale(self.original_active_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
                self.image = self.rest_image.copy()
                self.rect = self.image.get_rect()
                self.rect.center = self.pos

        if self.active == True:
            self.active = False

        if self.image == self.hover_image:
            self.image = self.rest_image

        if self.glob.mouse_pos.x > self.pos.x - (self.rect.w/2) and self.glob.mouse_pos.x < self.pos.x + (self.rect.w/2) and self.glob.mouse_pos.y > self.pos.y - (self.rect.h/2) and self.glob.mouse_pos.y < self.pos.y + (self.rect.h/2):
            # change button style to hover
            self.image = self.hover_image

            if pg.mouse.get_pressed()[0]:
                # change button style to pressing
                self.click = True
            else:
                if self.click:
                    self.click = False
                    self.active = True
                    self.trigger = True


        if self.click == True and pg.mouse.get_pressed()[0]:
            self.image = self.active_image
        elif self.click == True:
            self.click = False
            self.image = self.rest_image

        if self.active:
            self.glob.sound_repertoire.append(self.glob.sounds[12])

    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille du bouton image si la resolution de l'ecran est modifiee.
    """
    def prime_update(self):

        if self.glob.Resol_Check.change:
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
            self.rest_image = pg.transform.scale(self.original_rest_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.hover_image = pg.transform.scale(self.original_hover_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.active_image = pg.transform.scale(self.original_active_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.image = self.rest_image.copy()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos


    def change(self):
        self.rect.center = self.pos



"""
Classe Text
- But : gerer les differents parametres du texte
- Fonctionnement : transfomre un texte en image selon des parametres definis
- Utilisation : la classe Text() est appelee dans les interfaces utilisateurs (menu/menu cheat). Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Text():
    def __init__(self, glob, text, color, font_name, size, pos, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite_prime"

        self.text = text
        self.color = color
        self.font_name = font_name
        self.size = size
        self.font = self.Roboto_Light_Font = pg.font.Font('files/fonts/{}.ttf'.format(self.font_name), int(self.size * (self.glob.data["screen_width"]/1280)))

        self.hidden = False
        self.indicative_pos = pos
        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
        self.image = self.font.render("{}".format(self.text), False, self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.glob.all_virtuals.add([self])
        
    """
    Fonction update
    - Fonctionnement : change la position et la taille du texte si la resolution de l'ecran est modifiee.
    """    
    def update(self):
        #Check for resol. change and update
        if self.glob.Resol_Check.change:
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
            self.font = self.Roboto_Light_Font = pg.font.Font('files/fonts/{}.ttf'.format(self.font_name), int(self.size * (self.glob.data["screen_width"]/1280)))
            self.image = self.font.render("{}".format(self.text), False, self.color)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille du texte si la resolution de l'ecran est modifiee.
    """    
    def prime_update(self):

        if self.glob.Resol_Check.change:
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
            self.font = self.Roboto_Light_Font = pg.font.Font('files/fonts/{}.ttf'.format(self.font_name), int(self.size * (self.glob.data["screen_width"]/1280)))
            self.image = self.font.render("{}".format(self.text), False, self.color)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

            if self.hidden:
                self.image.set_alpha(0)
            else:
                self.image.set_alpha(255)

    """
    Fonction change
    - Fonctionnement : valide les modifications de texte ou de position faites par une classe associee.
    """
    def change(self):
        self.image = self.font.render("{}".format(self.text), False, self.color)

        if self.hidden:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)

        self.rect = self.image.get_rect()
        self.rect.center = self.pos


"""
Classe Decorated_Text
- But : encadrer un texte dans un rectangle colore
- Fonctionnement : transfomre un texte en image selon des parametres definis et le colle par dessus un rectange de couleur
- Utilisation : la classe Decorated_Text() est appelee dans les interfaces utilisateurs principalement comme titre (menu/menu cheat). Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Decorated_Text():
    def __init__(self, glob, text, color, font, size, pos, w, h, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite_prime"

        self.text = text
        self.font = font
        self.size = size
        self.indicative_width = w
        self.indicative_height = h
        self.indicative_pos = pos
        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
        
        self.border = 4 * (self.glob.data["screen_width"]/1280)

        self.bar_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])))
        self.bar_image.fill((221, 150, 37, 255))
        self.bar_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border))
        self.bar_image_boder.fill((27, 32, 26, 230))
        self.bar_image.blit(self.bar_image_boder, (self.border/2,self.border/2))

        self.original_bar_image = self.bar_image.copy()

        
        self.image = self.bar_image.copy()
        
        self.hidden = False
        
        
        self.rect = self.image.get_rect()

        

        self.rect.center = self.pos


        self.glob.all_virtuals.add([self])
        self.caption = Text(self.glob, self.text, color, self.font, self.size, pos, self._layer)
        
    """
    Fonction update
    - Fonctionnement : change la position et la taille du texte, ainsi que son rectangle si la resolution de l'ecran est modifiee.
    """
    def update(self):

        if self.glob.Resol_Check.change:
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
            self.bar_image = pg.transform.scale(self.original_bar_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.image = self.bar_image.copy()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            
            self.caption.pos = self.pos
            self.caption.change()
    """
    Fonction prime_update
    - Fonctionnement : change la position et la taille du texte, ainsi que son rectangle si la resolution de l'ecran est modifiee.
    """    
    def prime_update(self):
        
        if self.glob.Resol_Check.change:
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
            self.bar_image = pg.transform.scale(self.original_bar_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.image = self.bar_image.copy()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            
            self.caption.pos = self.pos
            self.caption.change()
            
            if self.hidden:
                self.image.set_alpha(0)
                self.caption.hidden = True
            else:
                self.image.set_alpha(255)
                self.caption.hidden = False

            self.caption.pos = self.pos
            self.caption.change()


    """
    Fonction change
    - Fonctionnement : valide les modifications de texte, de taille de rectangle ou de position faites par une classe associee.
    """
    def change(self):
        self.caption.text = self.text
        if self.hidden:
            self.image.set_alpha(0)
            self.caption.hidden = True
        else:
            self.image.set_alpha(255)
            self.caption.hidden = False

        self.caption.pos = self.pos
        self.caption.change()
    
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

"""
Classe Progression_Bar
- But : gerer les differents parametres d'une barre de progression.
- Fonctionnement : va dessiner un rectangle de couleur proportionnel à progression (self.progression).
- Utilisation : la classe Progression_Bar() est appelee dans le jeu pour representer une progression (vie, temps de contruction, [...]). Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Progression_Bar():
    def __init__(self, glob, pos, w, h, color, direct, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite_prime"

        self.indicative_width = w
        self.indicative_height = h
        self.width = self.indicative_width * self.glob.data["screen_width"]
        self.height = self.indicative_height * self.glob.data["screen_height"]
        self.indicative_pos = pos
        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
        
        self.progression = 1
        self.direct = direct

        self.color = color

        self.image = pg.Surface(((self.width),(self.height)))
        self.bar_image = pg.Surface((self.width,self.height))
        self.bar_image.fill((27, 32, 26, 230))
        self.prg_bar_image = pg.Surface(((self.width),self.height))
        self.prg_bar_image.fill(self.color)
        
        self.image.blit(self.bar_image, (0,0))
        
        self.hidden = False
        
        self.rect = self.image.get_rect()

        self.rect.center = self.pos

        self.glob.all_virtuals.add([self])

    def update(self):
        pass

    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille de la barre de progression si la resolution de l'ecran est modifiee.
    """    
    def prime_update(self):
        if self.glob.Resol_Check.change:
            self.width = self.indicative_width * self.glob.data["screen_width"]
            self.height = self.indicative_height * self.glob.data["screen_height"]
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
            
            self.image = pg.Surface(((self.width),(self.height)))
            self.bar_image = pg.Surface((self.width,self.height))
            self.bar_image.fill((27, 32, 26, 230))
            self.prg_bar_image = pg.Surface((self.width,self.height))
            self.prg_bar_image.fill(self.color)
            self.image.blit(self.bar_image, (0,0))
            
            if self.direct == "Left":
                self.image.blit(self.prg_bar_image, (-self.width*(1-self.progression),0))
            else:
                self.image.blit(self.prg_bar_image, (self.width*(1-self.progression),0))
            
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

            if self.hidden:
                self.image.set_alpha(0)
            else:
                self.image.set_alpha(255)
        
    """
    Fonction change
    - Fonctionnement : valide les modifications de la barre de progression (prends en compte la variable self.progression), de taille de rectangle ou de position faites par une classe associee.
    """
    def change(self):
        if self.hidden:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)
        
        self.image = pg.Surface(((self.width),(self.height)))
        self.image.blit(self.bar_image, (0,0))
        
        if self.direct == "Left":
            self.image.blit(self.prg_bar_image, (-self.width*(1-self.progression),0))
        else:
            self.image.blit(self.prg_bar_image, (self.width*(1-self.progression),0))

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

"""
Classe Sound_Pitcher
- But : gerer les differents parametres cross fader et permettre a l'utilisateur de changer le volume sonore.
- Fonctionnement : modifie le volume sonore selon la position du curseur (crossfader).
- Utilisation : la classe Sound_Pitcher() est appelee dans les le menu options. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Sound_Pitcher():
    def __init__(self, glob, pos, width, data_name, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_prime"

        self.data_name = data_name
        
        self.indicative_pos = pos
        self.indicative_width = width
        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
        self.width = self.indicative_width * self.glob.data["screen_width"]
        self.cursor_pos_x = self.glob.data[self.data_name]*((self.indicative_pos.x + self.indicative_width/2) - (self.indicative_pos.x - self.indicative_width/2)) + (self.indicative_pos.x - self.indicative_width/2)
        #self.fond = Picture(self.glob, pg.Surface((500,500)), self.pos, self.width, 10, 7)
        #self.fond.image.fill(BLACK)
        self.line = Image(self.glob, pg.Surface((1,1), pg.SRCALPHA), self.indicative_pos, self.indicative_width, 0.0025, self._layer)
        self.line.image.fill((255,255,255,200))
        Image(self.glob, self.glob.sprite["interface"][4], self.indicative_pos + vec(-self.indicative_width/2 - 0.012,0), 0.007, 0.025, self._layer)
        Image(self.glob, self.glob.sprite["interface"][5], self.indicative_pos + vec(self.indicative_width/2 + 0.012,0), 0.007, 0.025, self._layer)
        self.button = Image_Button(self.glob, self.glob.sprite["interface"][1],self.glob.sprite["interface"][2], self.glob.sprite["interface"][3], vec(self.cursor_pos_x, self.indicative_pos.y), 0.015625, 0.0277778, self._layer)
        #self.button = Button(self.glob, dimensions de base, position, redimensionnage (x,y), layer 7)

        self.glob.all_virtuals.add([self])

        Text(self.glob, self.data_name, WHITE, "Kanit-Regular", 25, self.indicative_pos + vec(0,-0.05), self._layer)
        
    """
    Fonction update
    - Fonctionnement : elle va verifier les differents conditions du cross fader en fonction de la position du curseur.
    """    
    def update(self):

        if self.glob.Resol_Check.change:
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
            self.width = self.indicative_width * self.glob.data["screen_width"]
            self.cursor_pos_x = self.glob.data[self.data_name]*((self.indicative_pos.x + self.indicative_width/2) - (self.indicative_pos.x - self.indicative_width/2)) + (self.indicative_pos.x - self.indicative_width/2)
            self.button.pos.x = self.cursor_pos_x * self.glob.data["screen_width"]
            self.button.change()
            self.line.image.fill((255,255,255,200))

        if self.button.click:
            self.button.pos.x = self.glob.mouse_pos.x
            if self.button.pos.x < self.pos.x - self.width/2:
                self.button.pos.x = self.pos.x - self.width/2
            elif self.button.pos.x > self.pos.x + self.width/2:
                self.button.pos.x = self.pos.x + self.width/2
            try:
                self.glob.data[self.data_name] = (self.button.pos.x - (self.pos.x - self.width/2))/((self.pos.x + self.width/2) - (self.pos.x - self.width/2))
            except:
                self.glob.data[self.data_name] = 0
            
            if self.data_name == "music_sound_lvl":
                pg.mixer.music.set_volume(self.glob.data["music_sound_lvl"])
            elif self.data_name == "fx_sound_lvl":
                for i in self.glob.sounds:
                    i.set_volume(self.glob.data["fx_sound_lvl"])

            self.button.change()

    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille du cross fader si la resolution de l'ecran est modifiee.
    """    
    def prime_update(self):
        if self.glob.Resol_Check.change:
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
            self.width = self.indicative_width * self.glob.data["screen_width"]
            self.cursor_pos_x = self.glob.data[self.data_name]*((self.indicative_pos.x + self.indicative_width/2) - (self.indicative_pos.x - self.indicative_width/2)) + (self.indicative_pos.x - self.indicative_width/2)
            self.button.pos.x = self.cursor_pos_x * self.glob.data["screen_width"]
            self.button.change()
            self.line.image.fill((255,255,255,200))
    
    def change(self):
        pass


"""
Classe Image()
- But : gerer les differents parametres d'une image.
- Fonctionnement : transfomre et positionne une image en fonction des parametres definis.
- Utilisation : la classe Image() est appelee dans les interfaces utilisateurs (menu). Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Image():
    def __init__(self, glob, image, pos, w, h, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite_prime"

        self.indicative_width = w
        self.indicative_height = h
        self.indicative_pos = pos
        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])

        self.original_image = image
        self.image = pg.transform.scale(self.original_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.glob.all_virtuals.add([self])

    """
    Fonction update
    - Fonctionnement : change la position et la taille de l'image, ainsi que son rectangle si la resolution de l'ecran est modifiee.
    """
    def update(self):
        if self.glob.Resol_Check.change:
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
            self.image = pg.transform.scale(self.original_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille de l'image, ainsi que son rectangle si la resolution de l'ecran est modifiee.
    """ 
    def prime_update(self):
        if self.glob.Resol_Check.change:
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
            self.image = pg.transform.scale(self.original_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.rect = self.image.get_rect()
            self.rect.center = self.pos
    

    def change(self):
        self.image = pg.transform.scale(self.original_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        
"""
Classe Animation_Player
- But : jouer une animation de sprites
- Fonctionnement : a intervalle regulier, va lire progressivement (du debut a la fin) toutes les images contenues dans une liste.
- Utilisation : la classe Animation_Player() est appelee par des classes (exposion des projectiles, feu d'un tank détruit). Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Animation_Player():
    def __init__(self, glob, animation, interval, pos, rot, w, h, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite_prime"

        self.indicative_width = w
        self.indicative_height = h
        self.indicative_pos = pos
        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
        self.rot = rot

        self.animation = animation
        self.anim_count = 0
        self.interval = interval
        self.sprite_count = len(self.animation)
        self.original_image = animation[0]

        self.image = pg.transform.scale(self.original_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
        self.image = pg.transform.rotate(self.image, self.rot - 90)

        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.timer =Timer()

        self.glob.all_virtuals.add([self])
    """
    Fonction update
    - Fonctionnement : lit selon un intervalle defini une suite d'images resulant en une animation
    """
    def update(self):
        self.pos.x += self.glob.map_instance.map_offset
        if self.timer.chrono(self.interval):
            self.anim_count += 1
            self.image = pg.transform.scale(self.animation[self.anim_count], (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.image = pg.transform.rotate(self.image, self.rot - 90)
            self.rect = self.image.get_rect()
        
        self.rect.center = self.pos

        if self.anim_count + 1 >= self.sprite_count:
            self.glob.all_virtuals.remove([self])
    
    
    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille des frames de l'animation si la resolution de l'ecran est modifiee.
    """     
    def prime_update(self):
        
        if self.glob.Resol_Check.change:

            if self.glob.data["screen_height"] == 720:
                self.pos = self.pos * (2/3)
            else:
                self.pos = self.pos * (3/2)

            self.image = pg.transform.scale(self.animation[self.anim_count], (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
            self.image = pg.transform.rotate(self.image, self.rot - 90)
            self.rect = self.image.get_rect()
            self.rect.center = self.pos

"""
Classe Game_Frame
- But : placer la barre du haut et la barre du bas dans l'interface du jeu
- Fonctionnement : placer les barres du jeu.
- Utilisation : la classe Game_Frame() est appelee dans les le jeu. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Game_Frame():
    def __init__(self, glob,layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite_prime"

        self.pos = vec(self.glob.data["screen_width"]/2, self.glob.data["screen_height"]/2)
        
        self.border = 2 * (self.glob.data["screen_width"]/1280)

        self.top_bar = pg.Surface(((1.0 * self.glob.data["screen_width"]),(0.08 * self.glob.data["screen_height"])), pg.SRCALPHA)
        self.top_bar.fill((61, 209, 177, 255))
        self.top_bar_boder = pg.Surface(((1.0 * self.glob.data["screen_width"])-self.border,(0.08 * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
        self.top_bar_boder.fill((27, 32, 26, 230))
        self.top_bar.blit(self.top_bar_boder, (self.border/2,self.border/2))

        self.bottom_bar = pg.Surface(((1.0 * self.glob.data["screen_width"]),(0.1 * self.glob.data["screen_height"])), pg.SRCALPHA)
        self.bottom_bar.fill((61, 209, 177, 255))
        self.bottom_bar_boder = pg.Surface(((1.0 * self.glob.data["screen_width"])-self.border,(0.1 * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
        self.bottom_bar_boder.fill((27, 32, 26, 230))
        self.bottom_bar.blit(self.bottom_bar_boder, (self.border/2,self.border/2))
        
        self.image = pg.Surface((self.glob.data["screen_width"],self.glob.data["screen_height"]), pg.SRCALPHA)
        self.image.blit(self.top_bar, (0,0))
        self.image.blit(self.bottom_bar, (0,(0.9 * self.glob.data["screen_height"])))
        
        
        
        self.rect = self.image.get_rect()

        self.rect.center = self.pos


        self.glob.all_virtuals.add([self])

    def update(self):
        pass
    
    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille des barres si la resolution de l'ecran est modifiee.
    """     
    def prime_update(self):
        
        if self.glob.Resol_Check.change:

            self.pos = vec(self.glob.data["screen_width"]/2, self.glob.data["screen_height"]/2)
            self.border = 2 * (self.glob.data["screen_width"]/1280)

            self.top_bar = pg.Surface(((1.0 * self.glob.data["screen_width"]),(0.08 * self.glob.data["screen_height"])), pg.SRCALPHA)
            self.top_bar.fill((61, 209, 177, 255))
            self.top_bar_boder = pg.Surface(((1.0 * self.glob.data["screen_width"])-self.border,(0.08 * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
            self.top_bar_boder.fill((27, 32, 26, 230))
            self.top_bar.blit(self.top_bar_boder, (self.border/2,self.border/2))

            self.bottom_bar = pg.Surface(((1.0 * self.glob.data["screen_width"]),(0.1 * self.glob.data["screen_height"])), pg.SRCALPHA)
            self.bottom_bar.fill((61, 209, 177, 255))
            self.bottom_bar_boder = pg.Surface(((1.0 * self.glob.data["screen_width"])-self.border,(0.1 * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
            self.bottom_bar_boder.fill((27, 32, 26, 230))
            self.bottom_bar.blit(self.bottom_bar_boder, (self.border/2,self.border/2))
            
            self.image = pg.Surface((self.glob.data["screen_width"],self.glob.data["screen_height"]), pg.SRCALPHA)
            self.image.blit(self.top_bar, (0,0))
            self.image.blit(self.bottom_bar, (0,(0.9 * self.glob.data["screen_height"])))
        
            self.rect = self.image.get_rect()
            self.rect.center = self.pos


"""
Classe Selection_Button
- But : gerer la selection des vehicules a placer dans la barre de construction.
- Fonctionnement : va contenir un prix, un nom de vehicule et une image. Va communiquer ses donnees avec Build_Button() pour placer un vehicule dans le menu de construction.
- Utilisation : la classe Selection_Button() est appelee dans les le menu de selection. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Selection_Button():
    def __init__(self, glob, pos, w, h, Object, button_num, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite"

        self.indicative_width = w
        self.indicative_height = h
        self.width = self.indicative_width * self.glob.data["screen_width"]
        self.height = self.indicative_height * self.glob.data["screen_height"]
        self.indicative_pos = pos
        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])


        self.button_num = button_num
        self.object = "{}".format(Object)
        self.price = 0
        self.selection = False

        
        #Tank frame icons
        self.frame = []

        self.border = 4 * (self.glob.data["screen_width"]/1280)

        self.rest_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])), pg.SRCALPHA)
        self.rest_image.fill((61, 209, 177, 255))
        self.rest_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
        self.rest_image_boder.fill((27, 32, 26, 230))
        self.rest_image.blit(self.rest_image_boder, (self.border/2,self.border/2))

        self.hover_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])), pg.SRCALPHA)
        self.hover_image.fill((83, 252, 241, 255))
        self.hover_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
        self.hover_image_boder.fill((27, 32, 26, 230))
        self.hover_image.blit(self.rest_image_boder, (self.border/2,self.border/2))

        self.active_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])), pg.SRCALPHA)
        self.active_image.fill((221, 150, 37, 255))
        self.active_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
        self.active_image_boder.fill((27, 32, 26, 230))
        self.active_image.blit(self.rest_image_boder, (self.border/2,self.border/2))

        self.inactive_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])), pg.SRCALPHA)
        self.inactive_image.fill((41, 109, 97, 255))
        self.inactive_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
        self.inactive_image_boder.fill((17, 22, 16, 230))
        self.inactive_image.blit(self.rest_image_boder, (self.border/2,self.border/2))

        
        self.price_tag = Decorated_Text(self.glob, "-{}".format(self.price), WHITE_BLUE, "Roboto-Light", 10, self.indicative_pos - vec(0, 0.04), self.indicative_width , 0.02, self._layer)


        self.image = self.rest_image.copy()
        self.estimation()
        #self.price += self.price * reduc
        #self.build_time += self.build_time * reduc
        self.price_tag.text = "-{}".format(self.price)
        self.price_tag.change()
            
            
        
        self.rect = self.image.get_rect()

        
        
        self.click = False
        self.active = False
        self.trigger = False

        self.rect.center = self.pos

        self.glob.all_virtuals.add([self])
        
    """
    Fonction update
    - Fonctionnement : elle va verifier les differentes conditions du bouton de selection en fonction de la position du curseur et partager ses donnees avec self.glob.mouse_select_holder.
    """  
    def update(self):
        if self.price <= self.glob.data["credit"]:

            if self.glob.mouse_pos.x > self.pos.x - (self.rect.w/2) and self.glob.mouse_pos.x < self.pos.x + (self.rect.w/2) and self.glob.mouse_pos.y > self.pos.y - (self.rect.h/2) and self.glob.mouse_pos.y < self.pos.y + (self.rect.h/2):
                # change button style to hover
                self.image = self.hover_image.copy()
                phenotype(self)

                if pg.mouse.get_pressed()[0]:
                    # change button style to pressing
                    self.click = True
                    self.image = self.active_image.copy()
                    phenotype(self)
                else:
                    if self.click:
                        self.click = False
                        self.active = True
                        self.trigger = True
            else:
                self.image = self.rest_image.copy()
                phenotype(self)
                self.click = False
        else:
            self.image = self.inactive_image.copy()
            phenotype(self)
        
        if self.object == self.glob.mouse_select_holder:
            self.image = self.active_image.copy()
            phenotype(self)

        
        # state of the button
        if self.active == True:
            self.active = False
            self.selection = True
            self.glob.mouse_select_holder = self.object

        if self.selection == True and self.glob.mouse_pos.y < 0.9 * self.glob.data["screen_height"]:
            if pg.mouse.get_pressed()[0] or pg.mouse.get_pressed()[1] or pg.mouse.get_pressed()[2]:
                self.selection = False
                self.glob.mouse_select_holder = "None"
        
        if self.selection == True and self.glob.mouse_select_holder == "None" and self.glob.mouse_pos.y > 0.9 * self.glob.data["screen_height"]:
            self.glob.data["credit"] -= self.price
            self.selection = False
        
        
    
    def change(self):
        self.rect.center = self.pos

    """
    Fonction estimation
    - Fonctionnement : va lier un prix a un nom de tank.
    """  
    def estimation(self):
        if self.object == "Rover_1":
            self.price = 25

        elif self.object == "Rover_2":
            self.price = 40

        elif self.object == "Rover_3":
            self.price = 60

        elif self.object == "Rover_4":
            self.price = 85
            
        elif self.object == "Rover_5":
            self.price = 120
        
        elif self.object == "Rocket_1":
            self.price = 50
        
        elif self.object == "Rocket_2":
            self.price = 65
        
        elif self.object == "Rocket_3":
            self.price = 95
        
        elif self.object == "Rocket_4":
            self.price = 140
        
        elif self.object == "Panther_1":
            self.price = 40
            
        elif self.object == "Panther_2":
            self.price = 60
            
        elif self.object == "Panther_3":
            self.price = 85
        
        elif self.object == "Panther_4":
            self.price = 120
            
        elif self.object == "Flak_1":
            self.price = 35
            
        elif self.object == "Flak_2":
            self.price = 50
            
        elif self.object == "Flak_3":
            self.price = 75
            
        elif self.object == "Flak_4":
            self.price = 100
            
        elif self.object == "Flak_5":
            self.price = 120

        elif self.object == "Tanker_1":
            self.price = 50

        elif self.object == "Tanker_2":
            self.price = 85

        elif self.object == "Tanker_3":
            self.price = 125

        elif self.object == "Tanker_4":
            self.price = 150
        
        
        self.price -= int(self.price * (self.glob.data["equip_cost_lvl"] / 15))
        
        phenotype(self)


"""
Classe Upgrade_Button
- But : gerer les differents parametres du bouton d'amelioration et permettre a l'utilisateur de debloquer des amelioration.
- Fonctionnement : le bouton contient un prix qui est soustrait aux credits du joueur s'il le selectionne et va debloquer une amelioration.
- Utilisation : la classe Upgrade_Button() est appelee dans les le menu des emelioration. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Upgrade_Button():
    def __init__(self, glob, pos, w, h, Object, button_num, layer):
        # button num or evel lvl
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite"

        self.indicative_width = w
        self.indicative_height = h
        self.width = self.indicative_width * self.glob.data["screen_width"]
        self.height = self.indicative_height * self.glob.data["screen_height"]
        self.indicative_pos = pos
        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])


        self.button_num = button_num
        self.object = "{}".format(Object)
        self.price = 0
        self.selection = False

        self.state = "None"

        
        #Tank frame icons
        self.frame = []

        self.border = 4 * (self.glob.data["screen_width"]/1280)

        self.rest_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])))
        self.rest_image.fill((61, 209, 177, 255))
        self.rest_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
        self.rest_image_boder.fill((27, 32, 26, 230))
        self.rest_image.blit(self.rest_image_boder, (self.border/2,self.border/2))

        self.hover_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])))
        self.hover_image.fill((83, 252, 241, 255))
        self.hover_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
        self.hover_image_boder.fill((27, 32, 26, 230))
        self.hover_image.blit(self.rest_image_boder, (self.border/2,self.border/2))

        self.active_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])))
        self.active_image.fill((221, 150, 37, 255))
        self.active_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border))
        self.active_image_boder.fill((27, 32, 26, 230))
        self.active_image.blit(self.rest_image_boder, (self.border/2,self.border/2))

        self.inactive_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])))
        self.inactive_image.fill((41, 109, 97, 255))
        self.inactive_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border))
        self.inactive_image_boder.fill((17, 22, 16, 230))
        self.inactive_image.blit(self.rest_image_boder, (self.border/2,self.border/2))
    
        
        self.price_tag = Decorated_Text(self.glob, "-{}".format(self.price), WHITE_BLUE, "Roboto-Light", 10, self.indicative_pos - vec(0, 0.04), self.indicative_width , 0.02, self._layer)
        

        if self.glob.data["{}".format(self.object)] < self.button_num:
            self.state = "Locked"
            self.image = self.inactive_image.copy()
            self.estimation()
            self.price_tag.text = "-{}".format(self.price)
            icon(self, self.glob.sprite["interface"][25], vec(0,0), 0.7)
            self.price_tag.hidden = False
            
            if self.glob.data["{}".format(self.object)] + 1 < self.button_num:
                self.image.set_alpha(0)
                self.price_tag.hidden = True

            self.price_tag.change()
            
        elif self.glob.data["{}".format(self.object)] >= self.button_num:
            self.state = "Earned"
            self.image = self.active_image.copy()
            phenotype(self)
            self.image.set_alpha(255)
            self.price_tag.hidden = True
            self.price_tag.change()


        self.rect = self.image.get_rect()

        
        self.click = False
        self.active = False
        self.trigger = False

        self.rect.center = self.pos

        self.glob.all_virtuals.add([self])
        
    """
    Fonction update
    - Fonctionnement : elle va verifier les differentes conditions du bouton amelioration en fonction de la position du curseur et partager ses donnees avec self.glob.data[objet].
    """
    def update(self):
        if self.state == "Locked" and self.glob.data["{}".format(self.object)] + 1 >= self.button_num:
            self.image.set_alpha(255)
            if self.price <= self.glob.data["credit"]:

                if self.glob.mouse_pos.x > self.pos.x - (self.rect.w/2) and self.glob.mouse_pos.x < self.pos.x + (self.rect.w/2) and self.glob.mouse_pos.y > self.pos.y - (self.rect.h/2) and self.glob.mouse_pos.y < self.pos.y + (self.rect.h/2):
                    # change button style to hover
                    self.image = self.hover_image.copy()
                    phenotype(self)

                    if pg.mouse.get_pressed()[0]:
                        # change button style to pressing
                        self.click = True
                        self.image = self.active_image.copy()
                        phenotype(self)
                    else:
                        if self.click:
                            self.click = False
                            self.active = True
                            self.trigger = True
                else:
                    self.image = self.rest_image.copy()
                    phenotype(self)
                    self.click = False
            else:
                self.image = self.inactive_image.copy()
                phenotype(self)
            icon(self, self.glob.sprite["interface"][25], vec(0,0), 0.7)
            self.price_tag.hidden = False
            self.price_tag.text = "-{}".format(self.price)
            self.change()

            
            # state of the button
            if self.active == True:
                self.active = False
                self.glob.sound_repertoire.append(self.glob.sounds[10])
                self.state = "Earned"
                self.image = self.active_image.copy()
                phenotype(self)
                self.price_tag.hidden = True
                self.price_tag.change()
                self.glob.data["{}".format(self.object)] += 1
                self.glob.data["credit"] -= self.price
         
    
    def change(self):
        self.rect.center = self.pos
        self.price_tag.change()

    """
    Fonction estimation
    - Fonctionnement : va lier un prix a un nom d'amelioration.
    """ 
    def estimation(self):
        if self.object == "credit_gain_lvl":
            self.price = 250 + 150 * (self.button_num - 1)

        elif self.object == "cannon_1_lvl":
            self.price = 50 + 75 * (self.button_num - 1)
        
        elif self.object == "cannon_2_lvl":
            self.price = 50 + 75 * (self.button_num - 1)
        
        elif self.object == "cannon_3_lvl":
            self.price = 85 + 75 * (self.button_num - 1)
        
        elif self.object == "cannon_4_lvl":
            self.price = 150 + 100 * (self.button_num - 1)
            
        elif self.object == "base_shielding_lvl":
            self.price = 75 + 45 * (self.button_num - 1)
            
        elif self.object == "energy_production_lvl":
            self.price = 75 + 75 * (self.button_num - 1)

        elif self.object == "energy_storage_lvl":
            self.price = 50 + 75 * (self.button_num - 1)

        elif self.object == "build_time_lvl":
            self.price = 85 + 75 * (self.button_num - 1)
        
        if self.object == "equip_cost_lvl":
            self.price = 65 + 75 * (self.button_num - 1)

        elif self.object == "build_slots":
            self.price = 50 + 125 * (self.button_num - 1)

        elif self.object == "rover_lvl":
            self.price = 50 + 125 * (self.button_num - 1)
        
        elif self.object == "rocket_lvl":
            self.price = 150 + 125 * (self.button_num - 1)
        
        elif self.object == "panther_lvl":
            self.price = + 75 + 125 * (self.button_num - 1)
        
        elif self.object == "flak_lvl":
            self.price = 75 + 125 * (self.button_num - 1)
        
        elif self.object == "tanker_lvl":
            self.price = 100 + 125 * (self.button_num - 1)

        phenotype(self)


"""
Fonction icon
- Fonctionnement : permets de coller une image sur une autre image en modifiant sa position et/ou sa taille.
"""
# Separate function
def icon(self, img, pos_adj, shrink):
    height = int((img.get_rect().h * (self.height / img.get_rect().h) - self.border)*shrink)
    width = int((img.get_rect().w * (height/img.get_rect().h)))
    
    center = vec((self.width - width)/2 + pos_adj.x * self.glob.data["screen_width"] , (self.height - height)/2+ pos_adj.y * self.glob.data["screen_width"])
    self.image.blit(pg.transform.scale(img, (width , height)), (center.x,center.y))



  
"""
Fonction phenotype
- Fonctionnement : permets de faire un collage de differents images permettant de creer une icone complexe en fonction du nom de l'objet.
"""
def phenotype(self):
    
    if self.object == "Rover_1":
        self.frame.append(icon(self, self.glob.sprite["obj"][2], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][41], vec(0,0.002), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][11], vec(0.008,0.008), 0.4))

    elif self.object == "Rover_2":
        self.frame.append(icon(self, self.glob.sprite["obj"][3], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][42], vec(0,0.002), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][12], vec(0.008,0.008), 0.4))

    elif self.object == "Rover_3":
        self.frame.append(icon(self, self.glob.sprite["obj"][4], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][43], vec(0,0.002), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][13], vec(0.008,0.008), 0.4))

    elif self.object == "Rover_4":
        self.frame.append(icon(self, self.glob.sprite["obj"][5], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,-0.009), 0.5))
        self.frame.append(icon(self, self.glob.sprite["obj"][44], vec(0,0.002), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][14], vec(0.008,0.008), 0.4))
        
    elif self.object == "Rover_5":
        self.frame.append(icon(self, self.glob.sprite["obj"][6], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][40], vec(0,-0.009), 0.3))
        self.frame.append(icon(self, self.glob.sprite["obj"][45], vec(0,0.002), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][15], vec(0.008,0.008), 0.4))
    
    elif self.object == "Rocket_1":
        self.frame.append(icon(self, self.glob.sprite["obj"][7], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,-0.003), 0.5))
        self.frame.append(icon(self, self.glob.sprite["obj"][46], vec(0,0.0085), 0.3))
        self.frame.append(icon(self, self.glob.sprite["interface"][11], vec(0.008,0.008), 0.4))
    
    elif self.object == "Rocket_2":
        self.frame.append(icon(self, self.glob.sprite["obj"][8], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,-0.003), 0.5))
        self.frame.append(icon(self, self.glob.sprite["obj"][47], vec(0,0.0085), 0.3))
        self.frame.append(icon(self, self.glob.sprite["interface"][12], vec(0.008,0.008), 0.4))
    
    elif self.object == "Rocket_3":
        self.frame.append(icon(self, self.glob.sprite["obj"][9], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,-0.003), 0.5))
        self.frame.append(icon(self, self.glob.sprite["obj"][48], vec(0,0.0085), 0.3))
        self.frame.append(icon(self, self.glob.sprite["interface"][13], vec(0.008,0.008), 0.4))
    
    elif self.object == "Rocket_4":
        self.frame.append(icon(self, self.glob.sprite["obj"][11], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,-0.003), 0.5))
        self.frame.append(icon(self, self.glob.sprite["obj"][49], vec(0,0.0085), 0.3))
        self.frame.append(icon(self, self.glob.sprite["interface"][14], vec(0.008,0.008), 0.4))
    
    elif self.object == "Panther_1":
        self.frame.append(icon(self, self.glob.sprite["obj"][11], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][50], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][11], vec(0.008,0.008), 0.4))
        
    elif self.object == "Panther_2":
        self.frame.append(icon(self, self.glob.sprite["obj"][12], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][51], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][12], vec(0.008,0.008), 0.4))
        
    elif self.object == "Panther_3":
        self.frame.append(icon(self, self.glob.sprite["obj"][13], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][52], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][13], vec(0.008,0.008), 0.4))
        
    elif self.object == "Panther_4":
        self.frame.append(icon(self, self.glob.sprite["obj"][14], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][53], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][14], vec(0.008,0.008), 0.4))
        
    elif self.object == "Flak_1":
        self.frame.append(icon(self, self.glob.sprite["obj"][11], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][54], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][11], vec(0.008,0.008), 0.4))
        
    elif self.object == "Flak_2":
        self.frame.append(icon(self, self.glob.sprite["obj"][12], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][55], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][12], vec(0.008,0.008), 0.4))
        
    elif self.object == "Flak_3":
        self.frame.append(icon(self, self.glob.sprite["obj"][13], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][56], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][13], vec(0.008,0.008), 0.4))
        
    elif self.object == "Flak_4":
        self.frame.append(icon(self, self.glob.sprite["obj"][14], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][57], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][14], vec(0.008,0.008), 0.4))
        
    elif self.object == "Flak_5":
        self.frame.append(icon(self, self.glob.sprite["obj"][14], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][58], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][15], vec(0.008,0.008), 0.4))

    elif self.object == "Tanker_1":
        self.frame.append(icon(self, self.glob.sprite["obj"][15], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,0), 0.5))
        self.frame.append(icon(self, self.glob.sprite["interface"][11], vec(0.008,0.008), 0.4))

    elif self.object == "Tanker_2":
        self.frame.append(icon(self, self.glob.sprite["obj"][16], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,0), 0.5))
        self.frame.append(icon(self, self.glob.sprite["interface"][12], vec(0.008,0.008), 0.4))

    elif self.object == "Tanker_3":
        self.frame.append(icon(self, self.glob.sprite["obj"][17], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,0), 0.5))
        self.frame.append(icon(self, self.glob.sprite["interface"][13], vec(0.008,0.008), 0.4))

    elif self.object == "Tanker_4":
        self.frame.append(icon(self, self.glob.sprite["obj"][18], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,0), 0.5))
        self.frame.append(icon(self, self.glob.sprite["interface"][14], vec(0.008,0.008), 0.4))
    
    elif self.object == "BaseDefence_1":
        self.frame.append(icon(self, self.glob.sprite["obj"][24], vec(0,0), 1))

    elif self.object == "BaseDefence_2":
        self.frame.append(icon(self, self.glob.sprite["obj"][29], vec(0,0), 1))

    elif self.object == "BaseDefence_3":
        self.frame.append(icon(self, self.glob.sprite["obj"][30], vec(0,0), 1))
    
    elif self.object == "credit_gain_lvl":
        self.frame.append(icon(self, self.glob.sprite["interface"][23], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][8], vec(-0.008,-0.008), 0.4))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))

    elif self.object == "cannon_1_lvl":
        self.frame.append(icon(self, self.glob.sprite["obj"][29], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][21], vec(-0.008,-0.008), 0.4))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))
    
    elif self.object == "cannon_2_lvl":
        self.frame.append(icon(self, self.glob.sprite["obj"][29], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][21], vec(-0.008,-0.008), 0.4))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))
    
    elif self.object == "cannon_3_lvl":
        self.frame.append(icon(self, self.glob.sprite["obj"][28], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][21], vec(-0.008,-0.008), 0.4))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))
    
    elif self.object == "cannon_4_lvl":
        self.frame.append(icon(self, self.glob.sprite["obj"][30], vec(0,0), 0.7))
        self.frame.append(icon(self, self.glob.sprite["interface"][21], vec(-0.008,-0.008), 0.4))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))

    elif self.object == "base_shielding_lvl":
        self.frame.append(icon(self, self.glob.sprite["interface"][22], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][21], vec(-0.008,-0.008), 0.4))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))
        
    elif self.object == "energy_production_lvl":
        self.frame.append(icon(self, self.glob.sprite["interface"][20], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][6], vec(-0.008,-0.008), 0.6))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))

    elif self.object == "energy_storage_lvl":
        self.frame.append(icon(self, self.glob.sprite["interface"][7], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][6], vec(-0.008,-0.008), 0.6))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))

    elif self.object == "build_time_lvl":
        self.frame.append(icon(self, self.glob.sprite["interface"][20], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][21], vec(-0.008,-0.008), 0.4))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))
    
    elif self.object == "equip_cost_lvl":
        self.frame.append(icon(self, self.glob.sprite["interface"][26], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][8], vec(-0.008,-0.008), 0.4))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))

    elif self.object == "build_slots":
        self.frame.append(icon(self, self.glob.sprite["interface"][21], vec(0,0), 1))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))

    elif self.object == "rover_lvl":
        if self.button_num == 1:
            self.frame.append(icon(self, self.glob.sprite["obj"][2], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][41], vec(0,0.002), 1))

        elif self.button_num == 2:
            self.frame.append(icon(self, self.glob.sprite["obj"][3], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][42], vec(0,0.002), 1))

        elif self.button_num == 3:
            self.frame.append(icon(self, self.glob.sprite["obj"][4], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][43], vec(0,0.002), 1))

        elif self.button_num == 4:
            self.frame.append(icon(self, self.glob.sprite["obj"][5], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,-0.009), 0.5))
            self.frame.append(icon(self, self.glob.sprite["obj"][44], vec(0,0.002), 1))
            
        elif self.button_num == 5:
            self.frame.append(icon(self, self.glob.sprite["obj"][6], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][40], vec(0,-0.009), 0.3))
            self.frame.append(icon(self, self.glob.sprite["obj"][45], vec(0,0.002), 1))
        
        self.frame.append(icon(self, self.glob.sprite["interface"][21], vec(-0.008,-0.008), 0.4))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))

    elif self.object == "rocket_lvl":
        if self.button_num == 1:
            self.frame.append(icon(self, self.glob.sprite["obj"][7], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,-0.003), 0.5))
            self.frame.append(icon(self, self.glob.sprite["obj"][46], vec(0,0.0085), 0.3))
            self.frame.append(icon(self, self.glob.sprite["interface"][11], vec(0.008,0.008), 0.4))
        
        elif self.button_num == 2:
            self.frame.append(icon(self, self.glob.sprite["obj"][8], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,-0.003), 0.5))
            self.frame.append(icon(self, self.glob.sprite["obj"][47], vec(0,0.0085), 0.3))
            self.frame.append(icon(self, self.glob.sprite["interface"][12], vec(0.008,0.008), 0.4))
        
        elif self.button_num == 3:
            self.frame.append(icon(self, self.glob.sprite["obj"][9], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,-0.003), 0.5))
            self.frame.append(icon(self, self.glob.sprite["obj"][48], vec(0,0.0085), 0.3))
            self.frame.append(icon(self, self.glob.sprite["interface"][13], vec(0.008,0.008), 0.4))
        
        elif self.button_num == 4:
            self.frame.append(icon(self, self.glob.sprite["obj"][11], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,-0.003), 0.5))
            self.frame.append(icon(self, self.glob.sprite["obj"][49], vec(0,0.0085), 0.3))
            self.frame.append(icon(self, self.glob.sprite["interface"][14], vec(0.008,0.008), 0.4))

        self.frame.append(icon(self, self.glob.sprite["interface"][21], vec(-0.008,-0.008), 0.4))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))

    elif self.object == "panther_lvl":
        if self.button_num == 1:
            self.frame.append(icon(self, self.glob.sprite["obj"][11], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][50], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["interface"][11], vec(0.008,0.008), 0.4))
            
        elif self.button_num == 2:
            self.frame.append(icon(self, self.glob.sprite["obj"][12], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][51], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["interface"][12], vec(0.008,0.008), 0.4))
            
        elif self.button_num == 3:
            self.frame.append(icon(self, self.glob.sprite["obj"][13], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][52], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["interface"][13], vec(0.008,0.008), 0.4))
            
        elif self.button_num == 4:
            self.frame.append(icon(self, self.glob.sprite["obj"][14], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][53], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["interface"][14], vec(0.008,0.008), 0.4))

        self.frame.append(icon(self, self.glob.sprite["interface"][21], vec(-0.008,-0.008), 0.4))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))

    elif self.object == "flak_lvl":
        if self.button_num == 1:
            self.frame.append(icon(self, self.glob.sprite["obj"][11], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][54], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["interface"][11], vec(0.008,0.008), 0.4))
            
        elif self.button_num == 2:
            self.frame.append(icon(self, self.glob.sprite["obj"][12], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][55], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["interface"][12], vec(0.008,0.008), 0.4))
            
        elif self.button_num == 3:
            self.frame.append(icon(self, self.glob.sprite["obj"][13], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][56], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["interface"][13], vec(0.008,0.008), 0.4))
            
        elif self.button_num == 4:
            self.frame.append(icon(self, self.glob.sprite["obj"][14], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][57], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["interface"][14], vec(0.008,0.008), 0.4))
            
        elif self.button_num == 5:
            self.frame.append(icon(self, self.glob.sprite["obj"][14], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][58], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["interface"][15], vec(0.008,0.008), 0.4))

        self.frame.append(icon(self, self.glob.sprite["interface"][21], vec(-0.008,-0.008), 0.4))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))
    
    elif self.object == "tanker_lvl":
        if self.button_num == 1:
            self.frame.append(icon(self, self.glob.sprite["obj"][15], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,0), 0.5))
            self.frame.append(icon(self, self.glob.sprite["interface"][11], vec(0.008,0.008), 0.4))

        elif self.button_num == 2:
            self.frame.append(icon(self, self.glob.sprite["obj"][16], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,0), 0.5))
            self.frame.append(icon(self, self.glob.sprite["interface"][12], vec(0.008,0.008), 0.4))

        elif self.button_num == 3:
            self.frame.append(icon(self, self.glob.sprite["obj"][17], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,0), 0.5))
            self.frame.append(icon(self, self.glob.sprite["interface"][13], vec(0.008,0.008), 0.4))

        elif self.button_num == 4:
            self.frame.append(icon(self, self.glob.sprite["obj"][18], vec(0,0), 1))
            self.frame.append(icon(self, self.glob.sprite["obj"][39], vec(0,0), 0.5))
            self.frame.append(icon(self, self.glob.sprite["interface"][14], vec(0.008,0.008), 0.4))

        self.frame.append(icon(self, self.glob.sprite["interface"][21], vec(-0.008,-0.008), 0.4))
        self.frame.append(icon(self, self.glob.sprite["interface"][10 + self.button_num], vec(0.008,0.008), 0.4))
