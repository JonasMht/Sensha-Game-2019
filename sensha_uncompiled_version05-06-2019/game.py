# game.py

"""
Importe le code du fichier <<hangar.py>>
"""
from hangar import * #import code from settings


"""
Class Player
- But : initialiser la base alliee, intialiser l'energie max pour le joueur
- Fonctionnement : chaque boucle une qqt d'energie va etre rajoutee au joueur
- Utilisation : la classe Player() est appelee dans le jeu. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Player():
    def __init__(self, glob):
        self.glob = glob
        self._layer = 0
        self._type = "func_prime"

        self.energy = 0 # Changed
        self.energy_max = 100 + 25 * self.glob.data["energy_storage_lvl"] ** 2

        self.timer = Timer()

        self.ally_base = Base(self.glob, "Base", "Ally")

        self.glob.all_virtuals.add([self])

    """
    Fonction update
    - Fonctionnement : va rajouter une certaine qqt d'energie au joueur en fonction des ameliorations economiques
    """
    def update(self):
        # Game economy
        if self.timer.chrono(0.05 * (5 / (self.glob.data["energy_production_lvl"] + 1))):
            self.energy += int(1 * (1 + self.glob.data["energy_production_lvl"] / 5))

            if self.energy > self.energy_max:
                self.energy = self.energy_max

    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / quand le joueur est dans le menu d'amelioration, va prendre en compte la modification economique
    """
    def prime_update(self):
        self.energy_max = 100 + 25 * self.glob.data["energy_storage_lvl"] ** 2


"""
Class Foe
- But : initialiser la base ennemie, IA qui envoie des ennemis
- Fonctionnement : adapte les ennemis envoyes en fonction du niveau du joueur (cela prends en compte plusieurs parametres : ex : la vie de l'ennemi)
- Utilisation : la classe Foe() est appelee dans le jeu. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Foe():
    def __init__(self, glob):
        self.glob = glob
        self._layer = 0
        self._type = "func"

        self.foe_base = Base(self.glob, "E_Base", "Foe")

        self.rage = False


        self.glob.all_virtuals.add([self])
        self.cluster_interval = random.randint(3,10)
        self.cluster_timer = Timer()
        self.spawn_interval = 0.001
        self.spawn_timer = Timer()

        self.spawn_amount = 0
        self.spawn_tracker = 0
        self.green_light = False


    """
    Fonction update
    - Fonctionnement : tant que la base ennemie est encore en vie, envoyer differents ennemis a differents intervalles de temps (IA de l'ennemi)
    """
    def update(self):
        #AI
        if self.foe_base.hp > 0:
            if self.cluster_timer.chrono(self.cluster_interval):

                self.cluster_interval = random.randint(int(10 + (100 - self.glob.game_lvl)/20) ,int(20 - (self.glob.game_lvl)/20)) #intervalle de temps en secondes entre les vagues
                self.spawn_amount = random.randint(int(1 + (self.glob.game_lvl)/66) ,int(3 + (self.glob.game_lvl)/33)) #nombre de tank a spawner
                
                self.green_light = True
            
            if self.rage == False and self.foe_base.hp/self.foe_base.hp_max < 0.5:
                    self.rage = True
                    self.green_light = True
                    self.spawn_amount = int(7 * (1 + self.glob.game_lvl/33))
                    self.spawn_interval = 0.001

            if self.green_light == True and self.spawn_timer.chrono(self.spawn_interval):

                self.spawn_tracker += 1
                self.spawn_interval = random.uniform(0.1,2)

                i = self.glob.game_lvl*(1/5)

                spawn_type = random.randint(0,int(i))
                if spawn_type == 0:
                    Vehicle(self.glob,"E_1","Foe")
                if spawn_type == 1:
                    Vehicle(self.glob,"E_2","Foe")
                if spawn_type == 2:
                    Vehicle(self.glob,"E_3","Foe")
                if spawn_type == 3:
                    Vehicle(self.glob,"E_4","Foe")
                if spawn_type == 4:
                    Vehicle(self.glob,"E_5","Foe")
                if spawn_type == 5:
                    Vehicle(self.glob,"E_6","Foe")
                if spawn_type == 6:
                    Vehicle(self.glob,"E_7","Foe")
                if spawn_type >= 7:
                    Vehicle(self.glob,"E_8","Foe")


                if self.spawn_tracker >= self.spawn_amount:
                    self.green_light = False
                    self.spawn_tracker = 0



"""
Class Game_Equip_Frame
- But : menu permettant au joueur d'equiper des unites dans la barre de selection rapide
- Fonctionnement : va adapter le menu en fonction des unites debloques par le joueur
- Utilisation : la classe Game_Equip_Frame() est appelee dans le jeu, quand le joueur appuis sur le bouton equipement. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Game_Equip_Frame():
    def __init__(self, glob):
        self.glob = glob
        self._layer = 8
        self._type = "func"

        self.fond = Image(self.glob, pg.Surface((50,50), pg.SRCALPHA), vec(0.5, 0.487) , 1, 0.825, 8)
        self.fond.image.fill((0,0,0,128))

        Image(self.glob, self.glob.sprite["interface"][0], vec(0.5,0.5), 0.9, 0.8, 8)


        self.button_dim = vec(0.0391,0.0695)
        self.button_pos = vec(0.42, 0.25)

        self.resume_button = Button(self.glob, "B A C K", "Roboto-Light", 30, vec(0.85, 0.875), 0.15, 0.05, 8)
        
        self.rover_selection_button = Button(self.glob, "R O V E R", "Roboto-Light", 17, vec(0.3, 0.1),  0.1, 0.05, 8)
        self.rocket_selection_button = Button(self.glob, "R O C K E T", "Roboto-Light", 17, vec(0.4, 0.1),  0.1, 0.05, 8)
        self.panther_selection_button = Button(self.glob, "P A N T H E R", "Roboto-Light", 17, vec(0.5, 0.1),  0.1, 0.05, 8)
        self.flak_selection_button = Button(self.glob, "F L A K", "Roboto-Light", 17, vec(0.6, 0.1),  0.1, 0.05, 8)
        self.tanker_selection_button = Button(self.glob, "T A N K E R", "Roboto-Light", 17, vec(0.7, 0.1),  0.1, 0.05, 8)

        Decorated_Text(self.glob, "R O V E R", WHITE, "Kanit-Regular", 25, vec(0.5,0.15), 0.2, 0.05, 9)
        for i in range(1, self.glob.data["rover_lvl"] + 1):
            Selection_Button(self.glob, vec(self.button_pos.x + self.button_dim.x * (i - 1), self.button_pos.y), self.button_dim.x, self.button_dim.y, "Rover_{}".format(i), i, 9)


        Text(self.glob, "Right click to unselect and get 10 Credit", WHITE, "Roboto-Light", 19, vec(0.5,0.85), 8)

        self.glob.all_virtuals.freeze([0,1,2,3,4,5,6,7])

        self.glob.all_virtuals.add([self])
        

    """
    Fonction update
    - Fonctionnement : va faire apparaitre les differentes unites deja debloques en fonction de la page selectionnee par le joueur.
    """
    def update(self):

        if self.rover_selection_button.active:
            self.glob.all_virtuals.clear_layer([9])
            Decorated_Text(self.glob, "R O V E R", WHITE, "Kanit-Regular", 25, vec(0.5,0.15), 0.2, 0.05, 9)
            for i in range(1, self.glob.data["rover_lvl"] + 1):
                Selection_Button(self.glob, vec(self.button_pos.x + self.button_dim.x * (i - 1), self.button_pos.y), self.button_dim.x, self.button_dim.y, "Rover_{}".format(i), i, 9)

        if self.rocket_selection_button.active:
            self.glob.all_virtuals.clear_layer([9])
            Decorated_Text(self.glob, "R O C K E T", WHITE, "Kanit-Regular", 25, vec(0.5,0.15), 0.2, 0.05, 9)
            for i in range(1, self.glob.data["rocket_lvl"] + 1):
                Selection_Button(self.glob, vec(self.button_pos.x + self.button_dim.x * (i - 1), self.button_pos.y), self.button_dim.x, self.button_dim.y, "Rocket_{}".format(i), i, 9)
            if self.glob.data["rocket_lvl"] == 0:
                Text(self.glob, "NO VEHICLE !", WHITE, "Kanit-Regular", 25, vec(0.5,0.5), 9)

        if self.panther_selection_button.active:
            self.glob.all_virtuals.clear_layer([9])
            Decorated_Text(self.glob, "P A N T H E R", WHITE, "Kanit-Regular", 25, vec(0.5,0.15), 0.2, 0.05, 9)
            for i in range(1, self.glob.data["panther_lvl"] + 1):
                Selection_Button(self.glob, vec(self.button_pos.x + self.button_dim.x * (i - 1), self.button_pos.y), self.button_dim.x, self.button_dim.y, "Panther_{}".format(i), i, 9)
            if self.glob.data["panther_lvl"] == 0:
                Text(self.glob, "NO VEHICLE !", WHITE, "Kanit-Regular", 25, vec(0.5,0.5), 9)

        if self.flak_selection_button.active:
            self.glob.all_virtuals.clear_layer([9])
            Decorated_Text(self.glob, "F L A K", WHITE, "Kanit-Regular", 25, vec(0.5,0.15), 0.2, 0.05, 9)
            for i in range(1, self.glob.data["flak_lvl"] + 1):
                Selection_Button(self.glob, vec(self.button_pos.x + self.button_dim.x * (i - 1), self.button_pos.y), self.button_dim.x, self.button_dim.y, "Flak_{}".format(i), i, 9)
            if self.glob.data["flak_lvl"] == 0:
                Text(self.glob, "NO VEHICLE !", WHITE, "Kanit-Regular", 25, vec(0.5,0.5), 9)

        if self.tanker_selection_button.active:
            self.glob.all_virtuals.clear_layer([9])
            Decorated_Text(self.glob, "T A N K E R", WHITE, "Kanit-Regular", 25, vec(0.5,0.15), 0.2, 0.05, 9)
            for i in range(1, self.glob.data["tanker_lvl"] + 1):
                Selection_Button(self.glob, vec(self.button_pos.x + self.button_dim.x * (i - 1), self.button_pos.y), self.button_dim.x, self.button_dim.y, "Tanker_{}".format(i), i, 9)
            if self.glob.data["tanker_lvl"] == 0:
                Text(self.glob, "NO VEHICLE !", WHITE, "Kanit-Regular", 25, vec(0.5,0.5), 9)

        keys = pg.key.get_pressed()
        if self.resume_button.active or "k_escape" in self.glob.key_event:
            if "k_escape" in self.glob.key_event:
                self.glob.key_event.remove("k_escape")

            self.glob.all_virtuals.unfreeze([0,1,2,3,4,5,6,7])
            self.glob.all_virtuals.clear_layer([8,9])



"""
Class Game_Research_Frame
- But : menu permettant au joueur d'ameliorer ses unites, ses tourelles et des boosts.
- Fonctionnement : va adapter le menu en fonction des ameliorations debloques par le joueur.
- Utilisation : la classe Game_Research_Frame() est appelee dans le jeu, quand le joueur appuis sur le bouton ameliorations. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Game_Research_Frame():
    def __init__(self, glob):
        self.glob = glob
        self._layer = 8
        self._type = "func"

        self.fond = Image(self.glob, pg.Surface((50,50), pg.SRCALPHA), vec(0.5, 0.487) , 1, 0.825, 8)
        self.fond.image.fill((0,0,0,128))

        Image(self.glob, self.glob.sprite["interface"][0], vec(0.5,0.5), 0.9, 0.8, 8)


        self.button_dim = vec(0.0391,0.0695)
        self.button_pos = vec(0.42, 0.25)

        self.resume_button = Button(self.glob, "B A C K", "Roboto-Light", 30, vec(0.85, 0.875), 0.15, 0.05, 8)

        self.base_selection_button = Button(self.glob, "B A S E", "Roboto-Light", 17, vec(0.4, 0.1),  0.1, 0.05, 8)
        self.vehicle_selection_button = Button(self.glob, "V E H I C L E", "Roboto-Light", 17, vec(0.5, 0.1),  0.1, 0.05, 8)
        self.economy_selection_button = Button(self.glob, "E C O N O M Y", "Roboto-Light", 17, vec(0.6, 0.1),  0.1, 0.05, 8)

        Decorated_Text(self.glob, "B A S E", WHITE, "Kanit-Regular", 25, vec(0.5,0.15), 0.2, 0.05, 9)

        #Cannon 1
        Decorated_Text(self.glob, "1 - Gatling :", WHITE, "Roboto-Light", 19, vec(0.23,0.25), 0.09, 0.05, 9)
        for i in range(1, 9 + 1):
            Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25), self.button_dim.x, self.button_dim.y, "cannon_1_lvl", i, 9)


        #Cannon 2
        Decorated_Text(self.glob, "2 - Gatling :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y), 0.09, 0.05, 9)
        for i in range(1, 9 + 1):
            Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y), self.button_dim.x, self.button_dim.y, "cannon_2_lvl", i, 9)


        #Cannon 3
        Decorated_Text(self.glob, "3 - Cannon :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*2), 0.09, 0.05, 9)
        for i in range(1, 9 + 1):
            Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*2), self.button_dim.x, self.button_dim.y, "cannon_3_lvl", i, 9)


        #Cannon 4
        Decorated_Text(self.glob, "4 - Launcher :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*3), 0.09, 0.05, 9)
        for i in range(1, 9 + 1):
            Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*3), self.button_dim.x, self.button_dim.y, "cannon_4_lvl", i, 9)

        #Shield
        Decorated_Text(self.glob, "Shielding :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*4), 0.09, 0.05, 9)
        for i in range(1, 9 + 1):
            Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*4), self.button_dim.x, self.button_dim.y, "base_shielding_lvl", i, 9)

        #Build Time
        Decorated_Text(self.glob, "Build Time :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*6), 0.09, 0.05, 9)
        for i in range(1, 9 + 1):
            Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*6), self.button_dim.x, self.button_dim.y, "build_time_lvl", i, 9)
        
        #Build cost
        Decorated_Text(self.glob, "Equip Cost :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*7), 0.09, 0.05, 9)
        for i in range(1, 9 + 1):
            Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*7), self.button_dim.x, self.button_dim.y, "equip_cost_lvl", i, 9)
        
        #Build Slots
        Decorated_Text(self.glob, "Build Slots :", WHITE, "Roboto-Light", 19, vec(0.3,0.25 + self.button_dim.y*8), 0.09, 0.05, 9)
        for i in range(1, 7 + 1):
            Upgrade_Button(self.glob, vec(0.37 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*8), self.button_dim.x, self.button_dim.y, "build_slots", i, 9)

        self.glob.all_virtuals.freeze([0,1,2,3,4,5,6,7])

        self.glob.all_virtuals.add([self])


    """
    Fonction update
    - Fonctionnement : va faire apparaitre les differentes ameliorations deja debloquees en plus d'une amelioration qui n'est pas encore debloquee.
    """
    def update(self):

        if self.base_selection_button.active:
            self.glob.all_virtuals.clear_layer([9])
            Decorated_Text(self.glob, "B A S E", WHITE, "Kanit-Regular", 25, vec(0.5,0.15), 0.2, 0.05, 9)

            #Cannon 1
            Decorated_Text(self.glob, "1 - Gatling :", WHITE, "Roboto-Light", 19, vec(0.23,0.25), 0.09, 0.05, 9)
            for i in range(1, 9 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25), self.button_dim.x, self.button_dim.y, "cannon_1_lvl", i, 9)


            #Cannon 2
            Decorated_Text(self.glob, "2 - Gatling :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y), 0.09, 0.05, 9)
            for i in range(1, 9 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y), self.button_dim.x, self.button_dim.y, "cannon_2_lvl", i, 9)


            #Cannon 3
            Decorated_Text(self.glob, "3 - Cannon :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*2), 0.09, 0.05, 9)
            for i in range(1, 9 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*2), self.button_dim.x, self.button_dim.y, "cannon_3_lvl", i, 9)


            #Cannon 4
            Decorated_Text(self.glob, "4 - Launcher :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*3), 0.09, 0.05, 9)
            for i in range(1, 9 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*3), self.button_dim.x, self.button_dim.y, "cannon_4_lvl", i, 9)

            #Shield
            Decorated_Text(self.glob, "Shielding :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*4), 0.09, 0.05, 9)
            for i in range(1, 9 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*4), self.button_dim.x, self.button_dim.y, "base_shielding_lvl", i, 9)

            #Build Time
            Decorated_Text(self.glob, "Build Time :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*6), 0.09, 0.05, 9)
            for i in range(1, 9 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*6), self.button_dim.x, self.button_dim.y, "build_time_lvl", i, 9)
            
            #Build cost
            Decorated_Text(self.glob, "Build Cost :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*7), 0.09, 0.05, 9)
            for i in range(1, 9 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*7), self.button_dim.x, self.button_dim.y, "equip_cost_lvl", i, 9)
            
            #Build Slots
            Decorated_Text(self.glob, "Build Slots :", WHITE, "Roboto-Light", 19, vec(0.3,0.25 + self.button_dim.y*8), 0.09, 0.05, 9)
            for i in range(1, 7 + 1):
                Upgrade_Button(self.glob, vec(0.37 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*8), self.button_dim.x, self.button_dim.y, "build_slots", i, 9)


        if self.vehicle_selection_button.active:
            self.glob.all_virtuals.clear_layer([9])
            Decorated_Text(self.glob, "V E H I C L E", WHITE, "Kanit-Regular", 25, vec(0.5,0.15), 0.2, 0.05, 9)
        
            # Rover
            Decorated_Text(self.glob, "Rover :", WHITE, "Roboto-Light", 19, vec(0.23,0.25), 0.09, 0.05, 9)
            for i in range(1, 5 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25), self.button_dim.x, self.button_dim.y, "rover_lvl", i, 9)


            # Rocket
            Decorated_Text(self.glob, "Rocket :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y), 0.09, 0.05, 9)
            for i in range(1, 4 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y), self.button_dim.x, self.button_dim.y, "rocket_lvl", i, 9)
            
            # Panther
            Decorated_Text(self.glob, "Panther :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*2), 0.09, 0.05, 9)
            for i in range(1, 4 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*2), self.button_dim.x, self.button_dim.y, "panther_lvl", i, 9)
            
            # Flak
            Decorated_Text(self.glob, "Flak :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*3), 0.09, 0.05, 9)
            for i in range(1, 5 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*3), self.button_dim.x, self.button_dim.y, "flak_lvl", i, 9)
            
            # Tanker
            Decorated_Text(self.glob, "Tanker :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*4), 0.09, 0.05, 9)
            for i in range(1, 4 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*4), self.button_dim.x, self.button_dim.y, "tanker_lvl", i, 9)
    

        if self.economy_selection_button.active:
            self.glob.all_virtuals.clear_layer([9])
            Decorated_Text(self.glob, "E C O N O M Y", WHITE, "Kanit-Regular", 25, vec(0.5,0.15), 0.2, 0.05, 9)
            
            # energy_production_lvl
            Decorated_Text(self.glob, "Energy prod :", WHITE, "Roboto-Light", 19, vec(0.23,0.25), 0.09, 0.05, 9)
            for i in range(1, 9 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25), self.button_dim.x, self.button_dim.y, "energy_production_lvl", i, 9)


            # energy_storage_lvl
            Decorated_Text(self.glob, "Energy stor :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y), 0.09, 0.05, 9)
            for i in range(1, 9 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y), self.button_dim.x, self.button_dim.y, "energy_storage_lvl", i, 9)
            
            # credit_gain_lvl
            Decorated_Text(self.glob, "Credit gain :", WHITE, "Roboto-Light", 19, vec(0.23,0.25 + self.button_dim.y*2), 0.09, 0.05, 9)
            for i in range(1, 9 + 1):
                Upgrade_Button(self.glob, vec(0.3 + (i-1) * self.button_dim.x,0.25 + self.button_dim.y*2), self.button_dim.x, self.button_dim.y, "credit_gain_lvl", i, 9)
    



        keys = pg.key.get_pressed()
        if self.resume_button.active or "k_escape" in self.glob.key_event:
            if "k_escape" in self.glob.key_event:
                self.glob.key_event.remove("k_escape")

            self.glob.all_virtuals.unfreeze([0,1,2,3,4,5,6,7])
            self.glob.all_virtuals.clear_layer([8,9])






"""
Class Build_Button
- But : bouton de la barre de construction rapide qui va contenir une unite et va permettre de la construire.
- Fonctionnement : affiche un prix qui sera debite lors du clique, le bouton verifie les conditions: rest, hover et active (curseur au repos, curseur au-dessus, clique). Si clique, construire l'unite.
- Utilisation : la classe Build_Button() est appelee dans le jeu. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Build_Button():

    def __init__(self, glob, player, pos, w, h, button_num, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite_prime"

        self.indicative_width = w
        self.indicative_height = h
        self.width = self.indicative_width * self.glob.data["screen_width"]
        self.height = self.indicative_height * self.glob.data["screen_height"]
        self.indicative_pos = pos
        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])


        self.player = player
        self.button_num = button_num
        self.object = self.glob.data["build_b{}".format(self.button_num)]
        self.price = 0
        self.build_time = 0

        # Has it got a tank? is it locked?
        self.state = "None"

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

        self.price_tag = Decorated_Text(self.glob, "-{}".format(self.price), YELLOW, "Roboto-Light", 10, self.indicative_pos - vec(0, 0.04), self.indicative_width , 0.02, self._layer)

        if self.glob.data["build_slots"] < self.button_num:
            self.state = "Locked"
            self.image = self.inactive_image.copy()
            icon(self, self.glob.sprite["interface"][25], vec(0,0), 0.7)
            self.price_tag.hidden = True
            self.price_tag.change()


        elif self.object == "None":
            self.state = "None"
            self.image = self.inactive_image.copy()
            self.price_tag.hidden = True
            self.price_tag.change()

        else:
            self.state = "Linked"
            self.image = self.rest_image.copy()
            self.estimation()
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
    - Fonctionnement : elle va verifier les differents conditions du bouton en fonction de la position et l'etat de la souris (clique) et va construire l'unite et debiter un prix donnee si un clique est detecte.
    """
    def update(self):

        if self.state == "Locked" and self.glob.data["build_slots"] >= self.button_num:
            self.state = "None"
            self.image = self.inactive_image.copy()


        elif self.state != "Locked" and self.state != "None" and self.object == "None":
            self.state = "None"
            self.image = self.inactive_image.copy()


        elif self.state == "None" and self.object != "None":
            self.state = "Linked"
            self.price_tag.hidden = False
            self.estimation()

            self.image = self.rest_image.copy()

        elif self.state == "Linked" and self.price > self.player.energy:
            self.image = self.inactive_image.copy()
            phenotype(self)

        if self.state == "Linked" and self.price < self.player.energy:

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

        # state of the button
        if self.active == True:
            self.active = False
            self.glob.sound_repertoire.append(self.glob.sounds[11])
            self.image = self.rest_image.copy()
            phenotype(self)
            self.player.energy -= self.price
            # Spawn process
            Build_Process(self.glob, self.object, self.build_time, len(self.glob.build_phase), 7)


        if self.state == "Locked" and self.glob.data["build_slots"] > self.button_num:
            self.state = "None"
            self.image = self.rest_image.copy()
            self.price_tag.hidden = True
            self.price_tag.change()

        if self.glob.mouse_select_holder != "None" and self.state != "Locked":
            if self.state == "None":
                self.image = self.inactive_image.copy()
            if self.state == "Linked":
                self.image = self.rest_image.copy()
                phenotype(self)
            if self.button_num == self.glob.data["build_slots"]:
                self.glob.mouse_select_holder = "None"


    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / permets d'equiper une unite quand le joueur est dans le menu des unites. Change la position et la taille du bouton si la resolution de l'ecran est modifiee.
    """
    def prime_update(self):

        if self.glob.Resol_Check.change:

            self.width = self.indicative_width * self.glob.data["screen_width"]
            self.height = self.indicative_height * self.glob.data["screen_height"]
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
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
            
            self.image = self.rest_image.copy()
            phenotype(self)

            self.rect = self.image.get_rect()
            self.rect.center = self.pos

        # select state

        if self.glob.mouse_select_holder != "None" and self.state != "Locked":
            self.image = self.active_image.copy()
            if self.state == "Linked":
                phenotype(self)

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
                self.click = False

        elif self.state == "Locked":
            self.image = self.inactive_image.copy()
            icon(self, self.glob.sprite["interface"][25], vec(0,0), 0.7)

        elif self.state == "Linked":
            self.image = self.rest_image.copy()
            phenotype(self)

        elif self.state == "None":
            self.image = self.inactive_image.copy()

        # state of the button
        if self.active == True:
            self.glob.sound_repertoire.append(self.glob.sounds[7])
            self.active = False
            self.object = self.glob.mouse_select_holder
            self.glob.data["build_b{}".format(self.button_num)] = self.object
            self.state = "Linked"
            self.glob.mouse_select_holder = "None"
            self.estimation()
            self.price_tag.text = "-{}".format(self.price)
            self.price_tag.hidden = False
            self.price_tag.change()

        if self.state == "Linked":
            if self.glob.mouse_pos.x > self.pos.x - (self.rect.w/2) and self.glob.mouse_pos.x < self.pos.x + (self.rect.w/2) and self.glob.mouse_pos.y > self.pos.y - (self.rect.h/2) and self.glob.mouse_pos.y < self.pos.y + (self.rect.h/2):
                # change button style to hover
                self.image = self.hover_image.copy()
                phenotype(self)

                if pg.mouse.get_pressed()[2]:
                    # change button style to pressing
                    self.click = True
                    self.image = self.active_image.copy()
                    phenotype(self)
                else:
                    if self.click:
                        self.click = False
                        self.state = "None"
                        self.object = "None"
                        self.price_tag.hidden = True
                        self.price_tag.change()
                        self.glob.data["build_b{}".format(self.button_num)] = self.object
                        self.glob.data["credit"] += 10
            else:
                self.click = False

        if self.state == "Locked" and self.glob.data["build_slots"] >= self.button_num:
            self.state = "None"
            self.image = self.inactive_image.copy()

    
    def change(self):
        self.rect.center = self.pos


    """
    Fonction estimation
    - Fonctionnement : sera lue dans la boucle principale update de la classe / estime le prix des unites et leur temps de construction en fonction du nom de l'objet.
    """
    def estimation(self):
        if self.object == "Rover_1":
            self.price = 35
            self.build_time = 5

        elif self.object == "Rover_2":
            self.price = 65
            self.build_time = 7

        elif self.object == "Rover_3":
            self.price = 125
            self.build_time = 8

        elif self.object == "Rover_4":
            self.price = 225
            self.build_time = 10

        elif self.object == "Rover_5":
            self.price = 400
            self.build_time = 12

        elif self.object == "Rocket_1":
            self.price = 75
            self.build_time = 12

        elif self.object == "Rocket_2":
            self.price = 175
            self.build_time = 12

        elif self.object == "Rocket_3":
            self.price = 255
            self.build_time = 12

        elif self.object == "Rocket_4":
            self.price = 500
            self.build_time = 12

        elif self.object == "Panther_1":
            self.price = 45
            self.build_time = 12

        elif self.object == "Panther_2":
            self.price = 85
            self.build_time = 12

        elif self.object == "Panther_3":
            self.price = 165
            self.build_time = 12

        elif self.object == "Panther_4":
            self.price = 320
            self.build_time = 12

        elif self.object == "Flak_1":
            self.price = 45
            self.build_time = 12

        elif self.object == "Flak_2":
            self.price = 75
            self.build_time = 12

        elif self.object == "Flak_3":
            self.price = 140
            self.build_time = 12

        elif self.object == "Flak_4":
            self.price = 280
            self.build_time = 12

        elif self.object == "Flak_5":
            self.price = 560
            self.build_time = 12

        elif self.object == "Tanker_1":
            self.price = 65
            self.build_time = 12

        elif self.object == "Tanker_2":
            self.price = 150
            self.build_time = 12

        elif self.object == "Tanker_3":
            self.price = 300
            self.build_time = 12

        elif self.object == "Tanker_4":
            self.price = 500
            self.build_time = 12
        
        phenotype(self)




"""
Class Build_Process
- But : icone de l'unite qui est en construction contenant une barre de progression representant le pourcentage d'avancee.
- Fonctionnement : va determiner la progression en fonction temps de construction ecoule. Cette progression est partagee avec une barre liee.
- Utilisation : la classe Build_Process() est appelee dans le jeu, lorsqu'un vehicule est achete. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Build_Process():
    def __init__(self, glob, Object, build_time, num, layer):
        # button num or evel lvl
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite_prime"

        self.glob.build_phase.append(self)

        self.num = num

        self.indicative_width = 0.0391
        self.indicative_height = 0.0695
        self.width = self.indicative_width * self.glob.data["screen_width"]
        self.height = self.indicative_height * self.glob.data["screen_height"]
        self.indicative_pos = vec(0.0391/2 + 0.0391 * self.num,0.0695/2)
        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])

        self.build_time = build_time - int(build_time * (self.glob.data["build_time_lvl"] / 13))
        self.time = 0.01

        self.object = Object


        #Tank frame icons
        self.frame = []

        self.border = 4 * (self.glob.data["screen_width"]/1280)

        self.rest_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])), pg.SRCALPHA)
        self.rest_image.fill((61, 209, 177, 255))
        self.rest_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
        self.rest_image_boder.fill((27, 32, 26, 230))
        self.rest_image.blit(self.rest_image_boder, (self.border/2,self.border/2))

        # progress bar:
        self.pr_bar = Progression_Bar(self.glob, self.indicative_pos + vec(0,0.04), self.indicative_width, 0.01, ORANGE, "Left", 7)

        self.image = self.rest_image.copy()
        phenotype(self)

        self.rect = self.image.get_rect()

        self.rect.center = self.pos

        self.glob.all_virtuals.add([self])

    """
    Fonction update
    - Fonctionnement : va deteremniner la position de l'icone de construction en fonction des icones existantes, pour eviter de les chevaucher. Fait avancer la barre de progression en fonction du temps. Une fois la progression a 100%, suppr la classe et faire apparetre une unitee.
    """
    def update(self):

        self.pr_bar.progression = round(self.time/self.build_time,2)
        self.pr_bar.change()

        if self.time >= self.build_time:
            Vehicle(self.glob, self.object, "Ally")
            self.glob.sound_repertoire.append(self.glob.sounds[9])
            self.glob.all_virtuals.remove([self, self.pr_bar])
            self.glob.build_phase.remove(self)

        elif self.glob.build_phase.index(self) != self.num:
            self.num = self.glob.build_phase.index(self)
            self.change()
        
        self.time += self.glob.fps_stab/60


    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / change la position et la taille de l'icone si la resolution de l'ecran est modifiee.
    """
    def prime_update(self):
        
        if self.glob.Resol_Check.change:

            self.width = self.indicative_width * self.glob.data["screen_width"]
            self.height = self.indicative_height * self.glob.data["screen_height"]
            self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
            self.border = 4 * (self.glob.data["screen_width"]/1280)

            self.pr_bar.pos.x = self.pos.x -  0.04
            self.pr_bar.change()

            self.rest_image = pg.Surface(((self.indicative_width * self.glob.data["screen_width"]),(self.indicative_height * self.glob.data["screen_height"])), pg.SRCALPHA)
            self.rest_image.fill((61, 209, 177, 255))
            self.rest_image_boder = pg.Surface(((self.indicative_width * self.glob.data["screen_width"])-self.border,(self.indicative_height * self.glob.data["screen_height"])-self.border), pg.SRCALPHA)
            self.rest_image_boder.fill((27, 32, 26, 230))
            self.rest_image.blit(self.rest_image_boder, (self.border/2,self.border/2))
            self.image = self.rest_image.copy()
            phenotype(self)

            self.rect = self.image.get_rect()
            self.rect.center = self.pos
            

    """
    Fonction change
    - Fonctionnement : quand la fonction change est appelee, mettre a jour la position en fonction des parametres de l'ecran et de sa place dans la file d'atante.
    """
    def change(self):
        self.indicative_pos = vec(0.0391/2 + 0.0391 * self.num,0.0695/2)
        self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
        self.rect.center = self.pos
        self.pr_bar.pos.x = self.pos.x -  0.04
        self.pr_bar.change()

