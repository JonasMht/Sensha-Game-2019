# main.py

"""
Importe le code du fichier <<display.py>>
"""
from display import *

"""
Programme
- But : la base des operations du programme
- Fonctionnement : contient le jeu, les variables, etc... / permet de demarrer et de fermer le jeu correctement (avec sauvegarde base de donnee) / partage ses variables a toutes les fonctions liees
- Utilisation : /
"""
class Prgm:
    """
    Fonction d'initialisation:
    - Fonctionnement : Initialise toutes les valeurs/listes/bibliotheques 
    """
    def __init__(self):
        # One ruler
        self.Data_Check()
        self.data = {}
        self.Data_Assign()
        # ex print(self.data["sound_lvl"])

        pg.init()
        pg.mixer.init()
        pg.mixer.set_num_channels(50)
        pg.font.init()

        if self.data["full_screen"] == 0:
            self.window = pg.display.set_mode((self.data["screen_width"],self.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF)
        if self.data["full_screen"] == 1:
            self.window = pg.display.set_mode((self.data["screen_width"],self.data["screen_height"]),pg.HWSURFACE|pg.DOUBLEBUF|pg.FULLSCREEN)
        
        icon = pg.image.load("files/img/sprites/icone.png").convert_alpha()
        icon = pg.transform.scale(icon, (32, 32))
        
        pg.display.set_icon(icon)
        pg.display.set_caption(TITLE)

        self.running = True

        self.clock = pg.time.Clock()
        # FPS stabilizer factor
        self.fps_stab = 1

        # Get Own virtual class here
        self.all_virtuals = Virtuals(self, 10)

        # def sprite library to be filled ["..."]
        self.sprite = {}
        self.sounds = []

        self.build_phase = []

        self.sound_repertoire = []
        MusicPlayer(self)


        self.map_instance = 0
        self.mouse_select_holder = "None"
        self.key_event = []

        self.game_lvl = self.data["game_lvl"]

        self.cheat = False

        self.Resol_Check = Resolution_Check(self)

        Load_Page_Display(self)
        
        
    """
    Fonction boucle principale:
    - Fonctionnement : s'execute toute les 1/60s (en boucle)
    """
    def main_loop(self):
        
        self.clock.tick(FPS)
        
        if self.clock.get_fps() != 0:
            self.fps_stab = FPS/self.clock.get_fps()
            if self.fps_stab < 1 or self.clock.get_fps() < 20:
                self.fps_stab = 1
        else:
            self.fps_stab = 1
            
        self.window.fill(BLACK)

        self.event()
        
        self.Parametrics()

        self.all_virtuals.update()

        #print(self.glob.all_sprites,"\n" ,self.glob.all_virtuals)

        self.run_check()
        pg.display.flip()

# User functions
    """
    Fonction Parametrics:
    - Fonctionnement : sauvegarde la position vectorielle du curseur dans la variable self.mouse_pos
    """
    def Parametrics(self):

        mouse_pos = pg.mouse.get_pos()
        self.mouse_pos = vec(mouse_pos[0], mouse_pos[1])
    
    """
    Fonction event:
    - Fonctionnement : attends un evenement donné (touche du clavier ou croix pour quitter) / ajoute le nom de la touche pressee a la liste key_event (qui est videe a chaque boucle), cette liste pourra etre lu par d'autres fonctions de classes virtuelles
    """
    def event(self):
        if len(self.key_event) > 0:
            self.key_event.clear()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

            if event.type == pg.KEYUP:
                if event.key == pg.K_ESCAPE:
                    self.key_event.append("k_escape")
            if event.type == pg.MOUSEBUTTONUP:
                self.key_event.append("mouse_press")
# Technical functions

    """
    Fonction Data_Assign:
    - Fonctionnement : transfert les donnees de la base de donnees <<session.db>> vers la bibliotheque self.data
    """
    def Data_Assign(self):

        DataBase().db_dict_get(self.data)

    """
    Fonction Data_Save:
    - Fonctionnement : transfert une donnee precise de la bibliotheque self.data vers la base de donnees <<session.db>>
    """
    def Data_Save(self, name):

        DataBase().db_update(name,self.data[name])

    """
    Fonction Data_Save_All:
    - Fonctionnement : transfert toutes les donnees de la bibliotheque self.data vers la base de donnees <<session.db>>
    """
    def Data_Save_All(self):

        DataBase().db_dict_update(self.data)

    """
    Fonction Data_Check:
    - Fonctionnement : verifie si la base de donnees <<session.db>> existe, si non alors elle la cree
    """
    def Data_Check(self):

        if DataBase().db_check() is False:
            DataBase().db_spawn()
        # DataBase().db_update("full_screen", 0)

    """
    Fonction run_check:
    - Fonctionnement : verifie si la variable self.running est toujours vrai, si non elle appelle la fonction Data_Save_All()
    """
    def run_check(self):

        if self.running is False:
            print("QUIT")
            self.Data_Save_All()
            # apply data lift/save


p = Prgm()

"""
Boucle principale:
- Fonctionnement : tant que p.running vraie, lit moi la fonction p.main_loop(), si non quitte le programme
"""
while p.running:
    p.main_loop()

pg.quit()