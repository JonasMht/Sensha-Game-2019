# ai_systeme.py

"""
Importe le code du fichier <<settings.py>>
"""
from settings import * #import code from settings


"""
Fonction Troop_AI
- Fonctionnement: tant que le tank est en vie, continuer l'autoguidage du tank
"""
def Troop_AI(self):
    if self.hp > 0:
        Driving(self)

"""
Fonction Turret_AI
- Fonctionnement: si une cible est detectee, faire pivoter la tourelle et engager le protocole de combat. Autrement, jouer une animation de scan (gauche - droite)
"""
def Turret_AI(self):
    if self.glob.target:
        rads = math.atan2(self.glob.pin.y - self.pos.y, self.glob.pin.x - self.pos.x)
        rads %= -2 * math.pi
        self.rot_target = math.degrees(-rads)
            
        if self.rot >= self.rot_target - 3 and self.rot <= self.rot_target + 3:
            self.rot = self.rot_target
            if self.glob.target_dist <= self.fire_range and self.timer.chrono(self.fire_rate):
                self.fire = True
        Targeting(self)
        
    else:
        if self.glob.banner == "Ally":
            sweep = 45
        else:
            sweep = 135

        rot_speed = 0.5 * self.glob.glob.fps_stab

        if self.rot_target != sweep and self.rot_target != 360 - sweep:
            self.rot_target = sweep
        if self.rot >= 360 - sweep - 3 and self.rot <= 360 - sweep + 3:
            self.rot_target = sweep
        if self.rot >= sweep - 3 and self.rot <= sweep + 3:
            self.rot_target = 360 - sweep
        
        if self.rot < self.rot_target and not self.rot + 180 < self.rot_target:
            self.rot += rot_speed
        elif self.rot + 180 < self.rot_target:
            self.rot -= rot_speed
        if self.rot > self.rot_target and not self.rot - 180 > self.rot_target:
            self.rot -= rot_speed
        elif self.rot - 180 > self.rot_target:
            self.rot += rot_speed
        if self.rot > 360:
            self.rot = 0
        if self.rot < 0:
            self.rot = 360
    
"""
Fonction Base_AI
- Fonctionnement: /
"""
def Base_AI(self):
    pass


"""
Fonction Driving
- Fonctionnement: dirige le tank vers un point vectoriel de la carte
"""
def Driving(self):
    GoTo = self.pin
    
    distance = math.sqrt((self.pos.x - GoTo.x)**2 + (self.pos.y - GoTo.y)**2)

    rads = math.atan2(GoTo.y - self.pos.y, GoTo.x - self.pos.x)
    rads %= -2 * math.pi
    self.rot_target = math.degrees(-rads)
    
    if distance > self.hold_range:
        self.acc.x = self.max_acc
    else:
        self.rot_target = self.rot
    Targeting(self)
    

"""
Fonction Targeting
- Fonctionnement: permets la rotation de la tourelle ou du tank vers une rotation ciblee (self.rot_target)
"""
def Targeting(self):
    try:
        rot_speed = self.rot_speed * self.glob.fps_stab
    except:
        try:
            rot_speed = self.rot_speed * self.glob.glob.fps_stab
        except:
            rot_speed = self.rot_speed * self.glob.glob.glob.fps_stab
        
    if self.rot < self.rot_target and not self.rot + 180 < self.rot_target:
        self.rot += rot_speed
    elif self.rot + 180 < self.rot_target:
        self.rot -= rot_speed
    if self.rot > self.rot_target and not self.rot - 180 > self.rot_target:
        self.rot -= rot_speed
    elif self.rot - 180 > self.rot_target:
        self.rot += rot_speed
    if self.rot > 360:
        self.rot = 0
    if self.rot < 0:
        self.rot = 360

"""
Classe Check_Master
- But : verifier differentes conditions entre deux objets (tanks / bases / projectiles) comme par exemple la distance, les angles relatifs ou encore la collision entre un objet et un autre 
- Fonctionnement : utilise les positions d'objets pour calculer des distances et des angles (trigonometrie). Gere l'aspect de detection des cibles avec des calculs de rayons. Ajoute des forces contraires si deux objets sont en collision.
- Utilisation : chaque boucle, la classe verifie ces conditions
"""
class Check_Master():
    def __init__(self, glob):
        self.glob = glob
        self._layer = 0
        self._type = "func"

        self.glob.all_virtuals.add([self])


    def update(self):

        # Targets:
        virtual_t = self.glob.all_virtuals.all_virtuals[2] + self.glob.all_virtuals.all_virtuals[1]
        total_t = len(virtual_t)
        
        for t in virtual_t:
                t.target_dist = 9999
                # make this the ennemy base when done
                t.target = False
                if t.banner == "Ally":
                    t.pin = vec(self.glob.map_instance.pos.x + self.glob.map_instance.rect.w + self.glob.data["screen_width"], t.pos.y)
                if t.banner == "Foe":
                    t.pin = vec(self.glob.map_instance.pos.x - self.glob.data["screen_width"], t.pos.y)

        for i in range(0, total_t):

            if i != total_t:
                for k in range(i+1, total_t):
                    distance = math.sqrt((virtual_t[i].pos.x - virtual_t[k].pos.x)**2 + (virtual_t[i].pos.y - virtual_t[k].pos.y)**2)
                    
                    # collision:
                    if virtual_t[i] not in self.glob.all_virtuals.all_virtuals[1] and virtual_t[k] not in self.glob.all_virtuals.all_virtuals[1]:
                        if distance <= virtual_t[i].radius + virtual_t[k].radius:
                            rads = math.atan2(virtual_t[k].pos.y - virtual_t[i].pos.y, virtual_t[k].pos.x - virtual_t[i].pos.x)

                            rads %= 2 * math.pi

                            var1 = vec((-math.cos(rads)*virtual_t[k].radius - math.cos(rads)*virtual_t[i].radius + virtual_t[k].pos.x), (-math.sin(rads)*virtual_t[k].radius - math.sin(rads)*virtual_t[i].radius + virtual_t[k].pos.y))
                            var2 = vec((math.cos(rads)*virtual_t[i].radius + math.cos(rads)*virtual_t[k].radius + virtual_t[i].pos.x), (math.sin(rads)*virtual_t[i].radius + math.sin(rads)*virtual_t[k].radius + virtual_t[i].pos.y))
                        
                            virtual_t[i].pos, virtual_t[k].pos = var1, var2
                            
                            if virtual_t[i].rot < 90 or virtual_t[i].rot > 270:
                                if virtual_t[i].acc.x > 0:
                                    if virtual_t[i].pos.y < virtual_t[k].pos.y:
                                        virtual_t[i].rot += 3
                                    else:
                                        virtual_t[i].rot -= 3

                            if virtual_t[k].rot < 90 or virtual_t[k].rot > 270:
                                if virtual_t[k].acc.x > 0:
                                    if virtual_t[k].pos.y < virtual_t[i].pos.y:
                                        virtual_t[k].rot += 3
                                    else:
                                        virtual_t[k].rot -= 3
                
                    # targeting
                    if virtual_t[i].hp > 0 and virtual_t[k].hp > 0:
                        if virtual_t[i].banner != virtual_t[k].banner:

                            if virtual_t[i].target_dist > distance:
                                virtual_t[i].target_dist = distance
                                if virtual_t[i].detection_range >= virtual_t[i].target_dist:
                                    virtual_t[i].target = True
                                    virtual_t[i].pin = virtual_t[k].pos

                        if virtual_t[k].banner != virtual_t[i].banner:

                            if virtual_t[k].target_dist > distance:
                                virtual_t[k].target_dist = distance
                                if virtual_t[k].detection_range >= virtual_t[k].target_dist:
                                    virtual_t[k].target = True
                                    virtual_t[k].pin = virtual_t[i].pos
        
        # Projectiles:
        for i in self.glob.all_virtuals.all_virtuals[5]:
            for k in self.glob.all_virtuals.all_virtuals[2] + self.glob.all_virtuals.all_virtuals[1]:
                if k.banner != i.glob.glob.banner and k.hp > 0:
                    distance = math.sqrt((i.pos.x - k.pos.x)**2 + (i.pos.y - k.pos.y)**2)
                    if distance <= i.radius + k.radius:
                        k.hp -= i.damage
                        i.hit = True

    # map limits:
        for i in self.glob.all_virtuals.all_virtuals[2]:
            if i.pos.y - i.radius <= self.glob.map_instance.pos.y:
                i.pos.y = self.glob.map_instance.pos.y + i.radius
            
            if i.pos.y + i.radius >= self.glob.map_instance.pos.y + 0.825 * self.glob.data["screen_height"]:
                i.pos.y = (self.glob.map_instance.pos.y + 0.825 * self.glob.data["screen_height"]) - i.radius
