# display.py

"""
Importe le code du fichier <<game.py>>
"""
from game import *

"""
Classe Load_Page_Display
- But : va charger les donnees du programme et ordonner le contenu de la page de chargement.
- Fonctionnement : va jouer la musique du menu, charger les donnees dans Prgm() avec File_Loader(glob) et placer le contenu de la page.
- Utilisation : la classe Load_Page_Display() est appelee au lancement du programme. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Load_Page_Display():
    def __init__(self, glob):
        
        self.glob = glob
        self._layer = 0
        self._type = "func"

        glob.window.fill(BLACK)

        self.cheat = False
        
        
        #pg.mixer.music.load("files/sound/music/menu_music.ogg")
        #pg.mixer.music.play(-1,0)
        
        Image(self.glob, pg.image.load("files/img/sprites/poster.png").convert_alpha(), vec(0.5,0.5), 1, 1, 0)

        self.glob.all_virtuals.update()
        
        pg.display.flip()

        File_Loader(glob)


        self.timer = Timer()
        self.text = Text(self.glob, "CLICK TO START !", WHITE, "Kanit-Regular", 25, vec(0.5,0.5), 0)

        
        self.glob.all_virtuals.add([self])
        
        
    """
    Fonction update:
    - Fonctionnement : fait apparaitre et disparaitre le texte, attends que l'utilsateur clique sur l'ecran, si il y a clique: supprimer tout ce qui se trouve dans la bibliotheque all_virtuals et appeler Menu_Page_Display().
    """
    def update(self):
        # diplay load screen
        if self.timer.chrono(0.7):
            if self.text.hidden == False:
                self.text.hidden = True
                self.text.change()
            else:
                self.text.hidden = False
                self.text.change()

        if "mouse_press" in self.glob.key_event or "k_escape" in self.glob.key_event:
            
            # empty specific
            self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8])
            Menu_Page_Display(self.glob)
        
        keys = pg.key.get_pressed()
        if self.glob.cheat == False and keys[pg.K_u] and keys[pg.K_d] and keys[pg.K_s] and keys[pg.K_t]:
            self.glob.cheat = True
            Image(self.glob, self.glob.img_rb, vec(0.98,0.04), 0.04, 0.07, 10) 
            # spawn cheat menu


    


            
"""
Classe Menu_Page_Display
- But : ordonner le contenu de la page menu.
- Fonctionnement : placer le contenu de la page.
- Utilisation : la classe Menu_Page_Display() peut-etre appelee par differentes classes "pages". Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Menu_Page_Display():
    def __init__(self, glob):
        
        self.glob = glob
        self._layer = 0
        self._type = "func"

        self.Timer = Timer()
        # menue assembly into sprites

        #self.menu_frame = Picture(self.glob, self.glob.sprite['interface'][0], vec(0.5, 0.5), 0.5, 0.5, 1)
        Image(self.glob, self.glob.img_poster, vec(0.5,0.5), 1, 1, 0)

        Image(self.glob, self.glob.img_title, vec(0.5,0.5), 0.3, 0.53, 0)

        self.start_button = Button(self.glob, "S T A R T", "Roboto-Light", 30, vec(0.20, 0.9), 0.15, 0.05, 0)
        self.level_button = Button(self.glob, "L E V E L", "Roboto-Light", 30, vec(0.35, 0.9), 0.15, 0.05, 0)
        self.session_button = Button(self.glob, "S E S S I O N", "Roboto-Light", 30, vec(0.50, 0.9), 0.15, 0.05, 0)
        self.options_button = Button(self.glob, "O P T I O N S", "Roboto-Light", 30, vec(0.65, 0.9), 0.15, 0.05, 0)
        self.quit_button = Button(self.glob, "Q U I T", "Roboto-Light", 30, vec(0.8, 0.9), 0.15, 0.05, 0)

        self.glob.all_virtuals.add([self])

    """
    Fonction update:
    - Fonctionnement : verifie si les differents boutons sont appuyes s'ils le sont, alors lire le code associe.
    """
    def update(self):


        if self.start_button.active == True:
            self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8])
            self.glob.game_lvl = self.glob.data["game_lvl"]
            Game_Page_Display(self.glob)
            pg.mixer.music.stop()
            pg.mixer.music.load(self.glob.game_music)
            pg.mixer.music.play(-1,0)

        if self.level_button.active == True:
            #Trans_Display(self.glob, 2)
            self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8])
            Level_Page_Display(self.glob)
        
        if self.session_button.active == True:
                self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8])
                Session_Page_Display(self.glob)
            
        if self.options_button.trigger == True:
            # start chrono
            if self.options_button.active == True:
                self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8])
                Option_Page_Display(self.glob)

        if self.quit_button.trigger == True:
            # start chrono
            if self.quit_button.active == True:
                self.glob.running = False


"""
Classe Level_Page_Display
- But : creer la page pour acceder aux differents niveaux du jeu et place toutes les icones des niveaux a selectionner.
- Fonctionnement : affiche toutes les icones des niveaux 
- Utilisation : la classe Level_Page_Display() peut-etre appelee par la page menu. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Level_Page_Display():
    def __init__(self, glob):

        self.glob = glob
        self._layer = 0
        self._type = "func"
        
        Image(self.glob, self.glob.img_poster, vec(0.5,0.5), 1, 1, 0)
        Image(self.glob, self.glob.sprite["interface"][0], vec(0.5,0.5), 0.5, 0.9, 7)

        Decorated_Text(self.glob, "L E V E L", WHITE, "Roboto-Light", 25, vec(0.5,0.1), 0.1, 0.05, 7)

        button_dim = vec(0.0391,0.0695)

        for i in range(0,10):
            for k in range(0,10):
                Level_Button(self.glob, vec(0.33+ button_dim.x * k ,0.2 + button_dim.y * i), button_dim.x, button_dim.y, i*10 + k , 7)
        
        self.Return_Button = Button(self.glob, "B A C K", "Roboto-Light", 25, vec(0.65, 0.9), 0.1, 0.05, 7)
        
        self.glob.all_virtuals.add([self])
    
    """
    Fonction update:
    - Fonctionnement : verifie si les differents boutons sont appuyes s'ils le sont, alors lire le code associe.
    """
    def update(self):

        if self.Return_Button.active:
            self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8])
            Menu_Page_Display(self.glob)



"""
Classe Option_Page_Display
- But : creer la page pour acceder aux differentes options du jeu et place tous les boutons sur l'ecran (boutons + crossfaders)
- Fonctionnement : affiche tous les boutons options
- Utilisation : la classe Option_Page_Display() peut-etre appelee par la page menu. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Option_Page_Display():
    def __init__(self, glob):

        self.glob = glob
        self._layer = 0
        self._type = "func"


        Image(self.glob, self.glob.img_poster, vec(0.5,0.5), 1, 1, 0)

        Image(self.glob, self.glob.sprite["interface"][0], vec(0.5,0.5), 0.3, 0.8, 1)

        Decorated_Text(self.glob, "O P T I O N S", WHITE, "Roboto-Light", 25, vec(0.5,0.2), 0.2, 0.05, 7)

        if self.glob.data["full_screen"] == 0:
            self.full_screen_button = Button(self.glob, "Full Screne Off", "Roboto-Light", 30, vec(0.5, 0.3), 0.2, 0.05, 7)
        else:
            self.full_screen_button = Button(self.glob, "Full Screne On", "Roboto-Light", 30, vec(0.5, 0.3), 0.2, 0.05, 7)
        
        if self.glob.data["screen_width"] == 1280:
            self.resolution_button = Button(self.glob, "Resol. 1280x720", "Roboto-Light", 30, vec(0.5, 0.35), 0.2, 0.05, 7)
        else:
            self.resolution_button = Button(self.glob, "Resol. 1920x1080", "Roboto-Light", 30, vec(0.5, 0.35), 0.2, 0.05, 7)
        
        
        Sound_Pitcher(self.glob, vec(0.5, 0.5), 0.1, "music_sound_lvl", 7)
        Sound_Pitcher(self.glob, vec(0.5, 0.6), 0.1, "fx_sound_lvl", 7)

        self.Return_Button = Button(self.glob, "B A C K", "Roboto-Light", 25, vec(0.5, 0.85), 0.1, 0.05, 7)

        self.glob.all_virtuals.add([self])
    
    """
    Fonction update:
    - Fonctionnement : verifie si les differents boutons sont appuyes s'ils le sont, alors lire le code associe.
    """
    def update(self):

        if self.Return_Button.active:
            self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8])
            Menu_Page_Display(self.glob)

        if self.full_screen_button.active:
            if self.glob.data["full_screen"] == 0:
                self.glob.data["full_screen"] = 1
                self.full_screen_button.text = "Full Screen On"
                self.full_screen_button.change()
                pg.display.quit()
                pg.display.init()
                self.glob.window = pg.display.set_mode((self.glob.data["screen_width"],self.glob.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF|pg.FULLSCREEN)
            else:
                self.glob.data["full_screen"] = 0
                self.full_screen_button.text = "Full Screen Off"
                self.full_screen_button.change()
                pg.display.quit()
                pg.display.init()
                self.glob.window = pg.display.set_mode((self.glob.data["screen_width"],self.glob.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF)
        
        
        if self.resolution_button.active == True:
            if self.glob.data["screen_width"] != 1280:
                self.glob.data["screen_width"] = 1280
                self.glob.data["screen_height"] = 720
                self.resolution_button.text = "Resol. 1280x720"
                self.resolution_button.change()

                pg.display.quit()
                pg.display.init()
                if self.glob.data["full_screen"] == 0:
                    self.glob.window = pg.display.set_mode((self.glob.data["screen_width"],self.glob.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF)
                if self.glob.data["full_screen"] == 1:
                    self.glob.window = pg.display.set_mode((self.glob.data["screen_width"],self.glob.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF|pg.FULLSCREEN)
            else:
                self.glob.data["screen_width"] = 1920
                self.glob.data["screen_height"] = 1080
                self.resolution_button.text = "Resol. 1920x1080"
                self.resolution_button.change()
                pg.display.quit()
                pg.display.init()
                if self.glob.data["full_screen"] == 0:
                    self.glob.window = pg.display.set_mode((self.glob.data["screen_width"],self.glob.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF)
                if self.glob.data["full_screen"] == 1:
                    self.glob.window = pg.display.set_mode((self.glob.data["screen_width"],self.glob.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF|pg.FULLSCREEN)

"""
Classe Session_Page_Display
- But : creer la page pour visualiser la progression du joueur ainsi que ses credits et permets de reinitialiser la session. 
- Fonctionnement : afficher les donnees du joueur ainsi que le bouton de reinitialisation
- Utilisation : la classe Session_Page_Display() peut-etre appelee par la page menu. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Session_Page_Display():
    def __init__(self, glob):

        self.glob = glob
        self._layer = 0
        self._type = "func"


        Image(self.glob, self.glob.img_poster, vec(0.5,0.5), 1, 1, 0)

        Image(self.glob, self.glob.sprite["interface"][0], vec(0.5,0.5), 0.3, 0.8, 1)

        Decorated_Text(self.glob, "S E S S I O N", WHITE, "Roboto-Light", 25, vec(0.5,0.2), 0.2, 0.05, 7)

        Decorated_Text(self.glob, "Level: {}".format(self.glob.data["game_lvl"]), WHITE, "Roboto-Light", 25, vec(0.5,0.3), 0.2, 0.05, 7)
        Decorated_Text(self.glob, "Credit: {}".format(self.glob.data["credit"]), WHITE, "Roboto-Light", 25, vec(0.5,0.35), 0.2, 0.05, 7)

        self.reset_button = Button(self.glob, "R E S E T", "Roboto-Light", 30, vec(0.5, 0.4), 0.2, 0.05, 7)

        


        self.Return_Button = Button(self.glob, "B A C K", "Roboto-Light", 25, vec(0.5, 0.85), 0.1, 0.05, 7)

        self.glob.all_virtuals.add([self])
        
    
    """
    Fonction update:
    - Fonctionnement : verifie si les differents boutons sont appuyes s'ils le sont, alors lire le code associe.
    """
    def update(self):

        if self.Return_Button.active:
            self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8])
            Menu_Page_Display(self.glob)
        
        if self.reset_button.active:
            DataBase().db_remove()
            DataBase().db_spawn()
            DataBase().db_dict_get(self.glob.data)
            self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8])
            Menu_Page_Display(self.glob)


"""
Classe Game_Page_Display
- But : ordonner le contenu de la page du jeu.
- Fonctionnement : afficher les boutons composants le jeu.
- Utilisation : la classe Game_Page_Display() peut-etre appelee par la page menu ou encore par la page de selection des niveaux. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Game_Page_Display():
    def __init__(self, glob):
        self.glob = glob
        self._layer = 7
        self._type = "func_prime"

        self.timer = Timer()
        
        self.game_frame = Game_Frame(self.glob, 7)
        self.button_pause = Button(self.glob, "", "Roboto-Light", 10, vec(0.9, 0.95), 0.0391, 0.0695, 7)
        self.equip_icon = Image(self.glob, self.glob.sprite["interface"][27], vec(0.9, 0.95), 0.03 - 0.001, 0.05 - 0.0017, 7)

        self.equip_button = Button(self.glob, "", "Roboto-Light", 10, vec(0.645, 0.95), 0.03, 0.05, 7)
        self.equip_icon = Image(self.glob, self.glob.sprite["interface"][10], vec(0.645, 0.95), 0.03 - 0.001, 0.05 - 0.0017, 7)
        self.research_button = Button(self.glob, "", "Roboto-Light", 10, vec(0.33, 0.95), 0.03, 0.05, 7)
        self.research_icon = Image(self.glob, self.glob.sprite["interface"][9], vec(0.33, 0.95), 0.03 - 0.001, 0.05 - 0.0017, 7)

        self.energy_indicator = Decorated_Text(self.glob, "energy/max_energy", YELLOW, "Roboto-Light", 15, vec(0.8,0.057), 0.065, 0.035, 7)
        self.energy_icon = Image(self.glob, self.glob.sprite["interface"][6], vec(0.8,0.02), 0.01, 0.03, 7)
        self.credit_indicator = Decorated_Text(self.glob, self.glob.data["credit"], WHITE_BLUE, "Roboto-Light", 15, vec(0.70,0.057), 0.065, 0.035, 7)
        self.energy_icon = Image(self.glob, self.glob.sprite["interface"][8], vec(0.70,0.02), 0.025, 0.03, 7)

        Decorated_Text(self.glob, "STAGE - {}".format(self.glob.game_lvl), WHITE, "Roboto-Light", 17, vec(0.92,0.05), 0.1, 0.05, 7)

        #self.build_button_0 = Build_Button(self.glob, 0)
        Map(self.glob)
        self.player = Player(self.glob)
        self.foe = Foe(self.glob)

        button_dim = vec(0.0391,0.0695)

        self.build_1 = Build_Button(self.glob, self.player, vec(0.37, 0.95), button_dim.x, button_dim.y, 1, 7)# 1 for first button
        self.build_2 = Build_Button(self.glob, self.player, vec(0.37 + button_dim.x, 0.95), button_dim.x, button_dim.y, 2, 7)
        self.build_3 = Build_Button(self.glob, self.player, vec(0.37 + 2*button_dim.x, 0.95), button_dim.x, button_dim.y, 3, 7)
        self.build_4 = Build_Button(self.glob, self.player, vec(0.37 + 3*button_dim.x, 0.95), button_dim.x, button_dim.y, 4, 7)
        self.build_5 = Build_Button(self.glob, self.player, vec(0.37 + 4*button_dim.x, 0.95), button_dim.x, button_dim.y, 5, 7)
        self.build_6 = Build_Button(self.glob, self.player, vec(0.37 + 5*button_dim.x, 0.95), button_dim.x, button_dim.y, 6, 7)
        self.build_7 = Build_Button(self.glob, self.player, vec(0.37 + 6*button_dim.x, 0.95), button_dim.x, button_dim.y, 7, 7)
        

        if self.glob.cheat:
            
            Image(self.glob, self.glob.sprite["interface"][0], vec(0.06,0.53), 0.12, 0.09, 7)
            self.unlock_tank = Button(self.glob, "TANKS", "Roboto-Light", 7, vec(0.03, 0.5), 0.03, 0.03, 7)
            self.unlock_upgrades = Button(self.glob, "UPGRADES", "Roboto-Light", 7, vec(0.06, 0.5), 0.03, 0.03, 7)
            self.unlock_lvl = Button(self.glob, "LVL", "Roboto-Light", 7, vec(0.09, 0.5), 0.03, 0.03, 7)
            self.get_500_cr = Button(self.glob, "500 CR", "Roboto-Light", 7, vec(0.03, 0.53), 0.03, 0.03, 7)
            self.get_500_en = Button(self.glob, "500 NRJ", "Roboto-Light", 7, vec(0.06, 0.53), 0.03, 0.03, 7)
            self.spawn_foe = Button(self.glob, "FOE", "Roboto-Light", 7, vec(0.09, 0.53), 0.03, 0.03, 7)
            self.spawn_ally = Button(self.glob, "ALLY", "Roboto-Light", 7, vec(0.03, 0.56), 0.03, 0.03, 7)
            self.hp_Ally = Button(self.glob, "A -500", "Roboto-Light", 7, vec(0.06, 0.56), 0.03, 0.03, 7)
            self.hp_Foe = Button(self.glob, "F -500", "Roboto-Light", 7, vec(0.09, 0.56), 0.03, 0.03, 7)


        #Add class for rover - rover action. ps: rovers are on layer 1
        Check_Master(self.glob)
        
        self.glob.all_virtuals.add([self])

    """
    Fonction check:
    - Fonctionnement : verifie les conditions de victoire (gagne/perdu) et affiche le menu de fin de niveau.
    """
    def check(self):
        if self.player.ally_base.hp <= 0:
            # LOST!
            self.glob.sound_repertoire.append(self.glob.sounds[11])
            EndGame_Frame(self.glob, False)
            
        if self.foe.foe_base.hp <= 0:
            # WON!
            self.glob.sound_repertoire.append(self.glob.sounds[13])
            EndGame_Frame(self.glob, True)
    
    """
    Fonction update:
    - Fonctionnement : verifie si les differents boutons sont appuyes s'ils le sont, alors lire le code associe. Verifie si le menu cheat est active. Appelle la fonction check().
    """
    def update(self):

        self.check()

        if self.glob.cheat:
            self.cheat_update()

        if self.timer.chrono(0.05):
            self.energy_indicator.text = "{} / {}".format(self.player.energy ,self.player.energy_max)
            self.energy_indicator.change()
            self.credit_indicator.text = self.glob.data["credit"]
            self.credit_indicator.change()
        
            

        if self.button_pause.active or "k_escape" in self.glob.key_event:
            if "k_escape" in self.glob.key_event:
                self.glob.key_event.remove("k_escape")
            Game_Pause_Frame(self.glob)

        if self.equip_button.active:
            Game_Equip_Frame(self.glob)
        
        if self.research_button.active:
            Game_Research_Frame(self.glob)

    """
    Fonction prime_update
    - Fonctionnement : sera lue quand la classe est gelee / mets a jour le conteur de credits toutes les 0.2s.
    """
    def prime_update(self):
        if self.timer.chrono(0.2):
            self.energy_indicator.text = "{} / {}".format(self.player.energy ,self.player.energy_max)
            self.energy_indicator.change()
            self.credit_indicator.text = self.glob.data["credit"]
            self.credit_indicator.change()
    

    """
    Fonction cheat_update:
    - Fonctionnement : verifie si les differents boutons cheat sont appuyes s'ils le sont, alors lire le code associe. 
    """
    def cheat_update(self):
        if self.unlock_tank.active == True:
            self.glob.data["rover_lvl"] = 5
            self.glob.data["flak_lvl"] = 5
            self.glob.data["rocket_lvl"] = 4
            self.glob.data["panther_lvl"] = 4
            self.glob.data["tanker_lvl"] = 4

        if self.unlock_upgrades.active == True:
            self.glob.data["cannon_1_lvl"] = 9
            self.glob.data["cannon_2_lvl"] = 9
            self.glob.data["cannon_3_lvl"] = 9
            self.glob.data["cannon_4_lvl"] = 9
            self.glob.data["base_shielding_lvl"] = 9
            self.glob.data["build_time_lvl"] = 9
            self.glob.data["equip_cost_lvl"] = 9
            self.glob.data["build_slots"] = 7
            self.glob.data["energy_production_lvl"] = 9
            self.glob.data["energy_storage_lvl"] = 9
            self.glob.data["credit_gain_lvl"] = 9

        if self.unlock_lvl.active == True:
            self.glob.data["game_lvl"] = 99
        
        if self.spawn_foe.active:
            Vehicle(self.glob,"E_1","Foe")
            Vehicle(self.glob,"E_2","Foe")
            Vehicle(self.glob,"E_3","Foe")
            Vehicle(self.glob,"E_4","Foe")
            Vehicle(self.glob,"E_5","Foe")
            Vehicle(self.glob,"E_6","Foe")
            Vehicle(self.glob,"E_7","Foe")
            Vehicle(self.glob,"E_8","Foe")
        
        if self.spawn_ally.active:
            Vehicle(self.glob,"Rover_1","Ally")
            Vehicle(self.glob,"Rover_2","Ally")
            Vehicle(self.glob,"Rover_3","Ally")
            Vehicle(self.glob,"Rover_4","Ally")
            Vehicle(self.glob,"Rover_5","Ally")
            Vehicle(self.glob,"Rocket_1","Ally")
            Vehicle(self.glob,"Rocket_2","Ally")
            Vehicle(self.glob,"Rocket_3","Ally")
            Vehicle(self.glob,"Rocket_4","Ally")
            Vehicle(self.glob,"Panther_1","Ally")
            Vehicle(self.glob,"Panther_2","Ally")
            Vehicle(self.glob,"Panther_3","Ally")
            Vehicle(self.glob,"Panther_4","Ally")
            Vehicle(self.glob,"Flak_1","Ally")
            Vehicle(self.glob,"Flak_2","Ally")
            Vehicle(self.glob,"Flak_3","Ally")
            Vehicle(self.glob,"Flak_4","Ally")
            Vehicle(self.glob,"Flak_5","Ally")
            Vehicle(self.glob,"Tanker_1","Ally")
            Vehicle(self.glob,"Tanker_2","Ally")
            Vehicle(self.glob,"Tanker_3","Ally")
            Vehicle(self.glob,"Tanker_4","Ally")

        
        if self.get_500_cr.active:
            self.glob.data["credit"] += 500
        
        if self.get_500_en.active:
            self.player.energy += 500

        
        if self.hp_Ally.active:
            self.player.ally_base.hp -= 500
        if self.hp_Foe.active:
            self.foe.foe_base.hp -= 500




"""
Classe EndGame_Frame
- But : affiche la page de fin de niveau et permets au joueur de changer de niveau (suivant, rejouer, precedent)
- Fonctionnement : affiche les boutons pour changer de niveau, ainsi que le texte de fin de jeu en plus du bonus de credits si le joeur a gagne la partie.
- Utilisation : la classe EndGame_Frame() peut-etre appelee par la fonction check() qui verifie la condition de victoire. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class EndGame_Frame():
    def __init__(self, glob, draft):
        self.glob = glob
        self._layer = 8
        self._type = "func"

        self.draft = draft
        
        self.fond = Image(self.glob, pg.Surface((50,50), pg.SRCALPHA), vec(0.5, 0.5) , 1, 1, 8)
        self.fond.image.fill((0,0,0,128))

        Image(self.glob, self.glob.sprite["interface"][0], vec(0.5,0.5), 0.2, 0.4, 8)

        if self.draft:
            Decorated_Text(self.glob, "YOU WON !", GREEN, "Roboto-Light", 25, vec(0.5,0.35), 0.2, 0.05, 8)
        else:
            Decorated_Text(self.glob, "YOU LOST !", RED, "Roboto-Light", 25, vec(0.5,0.35), 0.2, 0.05, 8)
        
        if self.draft:
            price = int((1 + self.glob.game_lvl) * 25 * (1 + (self.glob.data["credit_gain_lvl"])/10))
            self.glob.data["credit"] += price
            Decorated_Text(self.glob, "+{} Cr".format(price), WHITE_BLUE, "Roboto-Light", 25, vec(0.5,0.4), 0.11, 0.05, 8)
        

        self.restart_button = Button(self.glob, "R E S T A R T", "Roboto-Light", 30, vec(0.5, 0.5), 0.2, 0.05, 8)

        if self.glob.game_lvl != 0:
            self.last_button = Button(self.glob, "<<< L A S T", "Roboto-Light", 30, vec(0.5, 0.55), 0.2, 0.05, 8)
        else:
            self.last_button = Button(self.glob, "M I N", "Roboto-Light", 30, vec(0.5, 0.55), 0.2, 0.05, 8)
        
        if self.draft:
            if self.glob.game_lvl < 99:
                self.next_button = Button(self.glob, "N E X T >>>", "Roboto-Light", 30, vec(0.5, 0.45), 0.2, 0.05, 8)
            else:
                self.next_button = Button(self.glob, "M A X", "Roboto-Light", 30, vec(0.5, 0.45), 0.2, 0.05, 8)
        
        self.menu_button = Button(self.glob, "M E N U", "Roboto-Light", 30, vec(0.45, 0.65), 0.1, 0.05, 8)
        self.quit_button = Button(self.glob, "Q U I T", "Roboto-Light", 30, vec(0.55, 0.65), 0.1, 0.05, 8)

        self.glob.all_virtuals.freeze([0,1,2,3,4,5,6,7])

        if self.glob.game_lvl == self.glob.data["game_lvl"] and self.draft and self.glob.game_lvl < 99:
            self.glob.data["game_lvl"] += 1

        self.glob.all_virtuals.add([self])
    
    """
    Fonction update:
    - Fonctionnement : verifie si les differents boutons sont appuyes s'ils le sont, alors lire le code associe. 
    """
    def update(self):
        if self.restart_button.active:
            self.glob.build_phase.clear()
            self.glob.all_virtuals.unfreeze_all()
            self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8,9])

            Game_Page_Display(self.glob)


        if self.last_button.active and self.glob.game_lvl != 0:
            self.glob.game_lvl += -1
            self.glob.build_phase.clear()
            self.glob.all_virtuals.unfreeze_all()
            self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8,9])

            Game_Page_Display(self.glob)
        
        if self.draft and self.glob.game_lvl < 99:
            if self.next_button.active:
                self.glob.game_lvl += 1
                self.glob.build_phase.clear()
                self.glob.all_virtuals.unfreeze_all()
                self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8,9])

                Game_Page_Display(self.glob)


        if self.menu_button.active:
            # empty specific
            self.glob.build_phase.clear()
            self.glob.all_virtuals.unfreeze_all()
            self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8,9])

            pg.mixer.music.stop()
            pg.mixer.music.load(self.glob.menu_music)
            pg.mixer.music.play(-1,0)

            Menu_Page_Display(self.glob)

        if self.quit_button.active:
            self.glob.running = False



"""
Classe Game_Pause_Frame
- But : affiche le menu pause et mets en pause le jeu.
- Fonctionnement : affiche le menu pause et gele les layers dedies au jeu de la bibliotheque all_virtuals
- Utilisation : la classe Game_Pause_Frame() peut-etre appelee lorsque le joueur appuie sur echap ou clique sur le bouton pause. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Game_Pause_Frame():
    def __init__(self, glob):
        self.glob = glob
        self._layer = 8
        self._type = "func"
        
        self.fond = Image(self.glob, pg.Surface((50,50), pg.SRCALPHA), vec(0.5, 0.487) , 1, 1, 8)
        self.fond.image.fill((0,0,0,128))

        Image(self.glob, self.glob.sprite["interface"][0], vec(0.5,0.5), 0.3, 0.8, 8)

        Decorated_Text(self.glob, "P A U S E", WHITE, "Roboto-Light", 25, vec(0.5,0.2), 0.2, 0.05, 8)

        self.resume_button = Button(self.glob, "R E S U M E", "Roboto-Light", 30, vec(0.5, 0.3), 0.2, 0.05, 8)
        self.option_button = Button(self.glob, "O P T I O N S", "Roboto-Light", 30, vec(0.5, 0.35), 0.2, 0.05, 8)
        self.menu_button = Button(self.glob, "M E N U", "Roboto-Light", 30, vec(0.5, 0.40), 0.2, 0.05, 8)
        self.quit_button = Button(self.glob, "Q U I T", "Roboto-Light", 30, vec(0.5, 0.45), 0.2, 0.05, 8)

        self.glob.all_virtuals.freeze([0,1,2,3,4,5,6,7])

        self.glob.all_virtuals.add([self])

    """
    Fonction update:
    - Fonctionnement : verifie si les differents boutons sont appuyes s'ils le sont, alors lire le code associe. 
    """ 
    def update(self):

        if self.resume_button.active or "k_escape" in self.glob.key_event:
            if "k_escape" in self.glob.key_event:
                self.glob.key_event.remove("k_escape")
            self.glob.all_virtuals.unfreeze([0,1,2,3,4,5,6,7])
            self.glob.all_virtuals.clear_layer([8])

        if self.option_button.active:
            self.glob.all_virtuals.clear_layer([8])
            Game_Option_Frame(self.glob)

        if self.menu_button.active:
            # empty specific
            self.glob.build_phase.clear()
  
            self.glob.all_virtuals.unfreeze_all()
            self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8,9])

            pg.mixer.music.stop()
            pg.mixer.music.load(self.glob.menu_music)
            pg.mixer.music.play(-1,0)

            Menu_Page_Display(self.glob)

        if self.quit_button.active:
            self.glob.running = False


"""
Classe Game_Option_Frame
- But : creer la page pour acceder aux differentes options du jeu et place tous les boutons sur l'ecran (boutons + crossfaders).
- Fonctionnement :  affiche tous les boutons options
- Utilisation : la classe Game_Pause_Frame() peut-etre appelee lorsque le joueur appuie sur le bouton options dans le menu pause du jeu. Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Game_Option_Frame():
    def __init__(self, glob):

        self.glob = glob
        self._layer = 8
        self._type = "func"

        self.fond = Image(self.glob, pg.Surface((50,50), pg.SRCALPHA), vec(0.5, 0.487) , 1, 1, 8)
        self.fond.image.fill((0,0,0,128))

        Image(self.glob, self.glob.sprite["interface"][0], vec(0.5,0.5), 0.3, 0.8, 8)

        Decorated_Text(self.glob, "O P T I O N S", WHITE, "Roboto-Light", 25, vec(0.5,0.2), 0.2, 0.05, 8)

        if self.glob.data["full_screen"] == 0:
            self.full_screen_button = Button(self.glob, "Full Screne Off", "Roboto-Light", 30, vec(0.5, 0.3), 0.2, 0.05, 8)
        else:
            self.full_screen_button = Button(self.glob, "Full Screne On", "Roboto-Light", 30, vec(0.5, 0.3), 0.2, 0.05, 8)
        
        if self.glob.data["screen_width"] == 1280:
            self.resolution_button = Button(self.glob, "Resol. 1280x720", "Roboto-Light", 30, vec(0.5, 0.35), 0.2, 0.05, 8)
        else:
            self.resolution_button = Button(self.glob, "Resol. 1920x1080", "Roboto-Light", 30, vec(0.5, 0.35), 0.2, 0.05, 8)
        
        
        Sound_Pitcher(self.glob, vec(0.5, 0.5), 0.1, "music_sound_lvl",8)
        Sound_Pitcher(self.glob, vec(0.5, 0.6), 0.1, "fx_sound_lvl", 8)

        self.Return_Button = Button(self.glob, "B A C K", "Roboto-Light", 25, vec(0.5, 0.85), 0.1, 0.05, 8)

        self.glob.all_virtuals.add([self])
    

    """
    Fonction update:
    - Fonctionnement : verifie si les differents boutons sont appuyes s'ils le sont, alors lire le code associe. 
    """ 
    def update(self):

        if self.Return_Button.active or "k_escape" in self.glob.key_event:
            if "k_escape" in self.glob.key_event:
                self.glob.key_event.remove("k_escape")
            self.glob.all_virtuals.clear_layer([8])
            Game_Pause_Frame(self.glob)

        if self.full_screen_button.active:
            if self.glob.data["full_screen"] == 0:
                self.glob.data["full_screen"] = 1
                self.full_screen_button.text = "Full Screen On"
                self.full_screen_button.change()
                pg.display.quit()
                pg.display.init()
                self.glob.window = pg.display.set_mode((self.glob.data["screen_width"],self.glob.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF|pg.FULLSCREEN)
            else:
                self.glob.data["full_screen"] = 0
                self.full_screen_button.text = "Full Screen Off"
                self.full_screen_button.change()
                pg.display.quit()
                pg.display.init()
                self.glob.window = pg.display.set_mode((self.glob.data["screen_width"],self.glob.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF)
        
        
        if self.resolution_button.active == True:
            if self.glob.data["screen_width"] != 1280:
                self.glob.data["screen_width"] = 1280
                self.glob.data["screen_height"] = 720
                self.resolution_button.text = "Resol. 1280x720"
                self.resolution_button.change()

                pg.display.quit()
                pg.display.init()
                if self.glob.data["full_screen"] == 0:
                    self.glob.window = pg.display.set_mode((self.glob.data["screen_width"],self.glob.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF)
                if self.glob.data["full_screen"] == 1:
                    self.glob.window = pg.display.set_mode((self.glob.data["screen_width"],self.glob.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF|pg.FULLSCREEN)
            else:
                self.glob.data["screen_width"] = 1920
                self.glob.data["screen_height"] = 1080
                self.resolution_button.text = "Resol. 1920x1080"
                self.resolution_button.change()
                pg.display.quit()
                pg.display.init()
                if self.glob.data["full_screen"] == 0:
                    self.glob.window = pg.display.set_mode((self.glob.data["screen_width"],self.glob.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF)
                if self.glob.data["full_screen"] == 1:
                    self.glob.window = pg.display.set_mode((self.glob.data["screen_width"],self.glob.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF|pg.FULLSCREEN)


"""
Classe Level_Button
- But : permettre au joueur de selectionner un niveau de jeu.
- Fonctionnement : afficher une icone qui represente un niveau donnee en fonction de la variable partagee : num. Va bloquer les niveaux non debloques avec un cadenas.
- Utilisation : la classe Level_Button() peut-etre appelee par le menu de selection de niveaux (classe Level_Page_Display()). Cette classe est ajoutee aux Virtuals() sa fonction update() sera donc lue chaque boucle.
"""
class Level_Button():
    def __init__(self, glob, pos, w, h, num, layer):
        self.glob = glob
        self._layer = layer
        self._type = "func_sprite"
        
        self.num = num
        self.text = "{}".format(self.num)
        self.font = "Roboto-Light"
        self.size = 25

        self.state = "NONE"

        self.indicative_width = w
        self.indicative_height = h
        self.width = self.indicative_width * self.glob.data["screen_width"]
        self.height = self.indicative_height * self.glob.data["screen_height"]
        self.indicative_pos = pos
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
        

        if self.glob.data["game_lvl"] < self.num:
            self.state = "LOCKED"
            self.image = self.inactive_image.copy()
            icon(self, self.glob.sprite["interface"][25], vec(0,0), 0.7)
        else:
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
    - Fonctionnement : elle va verifier les differentes conditions du bouton de selection du niveau. Si le bouton est active, alors la fonction va partager son niveau avec self.glob.game_lvl et lancer le jeu (Game_Page_Display()).
    """
    def update(self):
        if self.state == "NONE":
            if self.glob.Resol_Check.change:
                self.pos = vec(self.indicative_pos.x * self.glob.data["screen_width"], self.indicative_pos.y * self.glob.data["screen_height"])
                self.rest_image = pg.transform.scale(self.rest_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
                self.hover_image = pg.transform.scale(self.hover_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
                self.active_image = pg.transform.scale(self.active_image, (int(self.indicative_width * self.glob.data["screen_width"]), int(self.indicative_height * self.glob.data["screen_height"])))
                self.image = self.rest_image.copy()
                self.rect = self.image.get_rect()
                self.rect.center = self.pos
            
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
                self.glob.sound_repertoire.append(self.glob.sounds[1])
                self.glob.game_lvl = self.num
                self.glob.all_virtuals.clear_layer([0,1,2,3,4,5,6,7,8])
                Game_Page_Display(self.glob)
                pg.mixer.music.stop()
                pg.mixer.music.load(self.glob.game_music)
                pg.mixer.music.play(-1,0)
    
    """
    Fonction change
    - Fonctionnement : valide les modifications de texte ou de position faites par une classe associee.
    """
    def change(self):
        self.caption.text = self.text
        self.caption.change()
        self.rect.center = self.pos
