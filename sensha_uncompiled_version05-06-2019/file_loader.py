# file_loader.py

"""
Importe les bibliotheques "XML", "SQLite" et "Pygame"
"""
import xml.etree.ElementTree as ET
import sqlite3
import pygame as pg

vec = pg.math.Vector2

"""
Classe SpriteSheet
- But : decouper les sprites en fonction des donnees XML fournies.
- Fonctionnement : decoupe l'image associee grace aux coordonnes et dimensions lues dans le fichier XML et renvoyer (return) le decoupage.
- Utilisation : dans une boucle for, va decouper une image et sauvegarder le decoupage dans une liste. Ceci est fait au debut du jeu, pour eviter d'avoir a charger les images pendant le jeu.
"""
class SpriteSheet():
    # load an atlas image and cut a specific piece out of it
    # can also pass an associated XML file
    def __init__(self, img_file, data_file=None):
        self.spritesheet = img_file
        if data_file:
            tree = ET.parse(data_file)
            self.map = {}
            for node in tree.iter():
                if node.attrib.get('name'):
                    name = node.attrib.get('name')
                    self.map[name] = {}
                    self.map[name]['x'] = int(node.attrib.get('x'))
                    self.map[name]['y'] = int(node.attrib.get('y'))
                    self.map[name]['width'] = int(node.attrib.get('width'))
                    self.map[name]['height'] = int(node.attrib.get('height'))
                if node.attrib.get('num'):
                    num = node.attrib.get('num')
                    self.map[num] = {}
                    self.map[num]['x'] = int(node.attrib.get('x'))
                    self.map[num]['y'] = int(node.attrib.get('y'))
                    self.map[num]['width'] = int(node.attrib.get('width'))
                    self.map[num]['height'] = int(node.attrib.get('height'))

    """
    Fonction get_image_rect
    - Fonctionnement : renvoie l'image en fonction des dimensions et des coordonees
    """
    def get_image_rect(self, x, y, w, h):
        return self.spritesheet.subsurface(pg.Rect(x, y, w, h))

    """
    Fonction get_image_name
    - Fonctionnement : renvoie l'image en fonction de son nom dans le fichier XML associe a des coordonnees et des dimensions.
    """
    def get_image_name(self, name):
        rect = pg.Rect(self.map[name]['x'], self.map[name]['y'],
                       self.map[name]['width'], self.map[name]['height'])
        return self.spritesheet.subsurface(rect)
    
    """
    Fonction get_image_num
    - Fonctionnement : renvoie l'image en fonction du numro dans la liste XML associee a des coordonnees et des dimensions.
    """
    def get_image_num(self, num):
        rect = pg.Rect(self.map[num]['x'], self.map[num]['y'],
                       self.map[num]['width'], self.map[num]['height'])
        return self.spritesheet.subsurface(rect)


"""
Fonction File_Loader
- Fonctionnement : charge tout le contenu du jeu et le sauvegarde sous la classe Prgm().
"""
def File_Loader(self):

    # cannon sounds
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/shoot/DryFire.ogg")) #0
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/shoot/WetFire.ogg")) #1
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/shoot/canon.ogg")) #2
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/missile/Missle_Launch.ogg")) #3
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/explosion/Cracking.ogg")) #4
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/explosion/doing.ogg")) #5
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/activation/pen_click.ogg")) #6
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/activation/drop_click.ogg")) #7
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/activation/Construction.ogg")) #8
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/activation/Construction_quick.ogg")) #9
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/activation/Swing.ogg")) #10
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/activation/Swing_lox.ogg")) #11
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/activation/Tzwing.ogg")) #12
    self.sounds.append(pg.mixer.Sound("files/sound/audio_fx/activation/Ka_Tching.ogg")) #13

    self.game_music = "files/sound/music/Game_music.ogg"
    self.menu_music = "files/sound/music/Menu_music.ogg"
    #self.game_music = "files\sound\music\Machinimasound.com_-_Gold_Coast.ogg"
    #self.menu_music = "files\sound\music\Bit_Coast.ogg"
    
    # Fill sprite library with ready to use sprites
    self.img_interface = pg.image.load("files/img/sprites/tile_maps/interface_design.png").convert_alpha()
    self.img_trans = pg.image.load("files/img/sprites/tile_maps/trans_display_tilemap.png").convert_alpha()
    self.img_all_obj = pg.image.load("files/img/sprites/tile_maps/all_obj.png").convert_alpha()
    self.img_all_windows = pg.image.load("files/img/sprites/tile_maps/all_windows.png").convert_alpha()
    self.img_exp1 = pg.image.load("files/img/sprites/visual fx/exp1_200x200px.png").convert_alpha()
    self.img_exp2 = pg.image.load("files/img/sprites/visual fx/exp2_200x200px.png").convert_alpha()
    self.img_poster = pg.image.load("files/img/sprites/poster.png").convert_alpha()
    self.img_title = pg.image.load("files/img/sprites/title.png").convert_alpha()
    self.img_rb = pg.image.load("files/img/sprites/shallow_wave/sprite_0.png").convert_alpha()
    
    self.sprite['interface'] = []
    self.sprite['obj'] = []
    self.sprite['windows'] = []
    self.sprite['trans_doors'] = []
    self.sprite['map'] = []
    self.sprite['exp1'] = []
    self.sprite['exp2'] = []
    self.sprite['anim_energy_leak_exp'] = []
    self.sprite['anim_vapour_trail'] = []
    self.sprite['anim_bullet_flame'] = []
    self.sprite['anim_yellow_exp'] = []
    self.sprite['anim_fire'] = []
    self.sprite['anim_spark'] = []

    # When creating list add name for easier finding

    for i in range(0, 27 + 1, 1):
        self.sprite['interface'].append(SpriteSheet(self.img_interface, "files/img/sprites/tile_maps/xml/interface_tiles.xml").get_image_num("{}".format(i)).convert_alpha())
    for i in range(0, 1 + 1, 1):
        self.sprite['trans_doors'].append(SpriteSheet(self.img_trans, "files/img/sprites/tile_maps/xml/trans_display_tilemap.xml").get_image_num("{}".format(i)).convert_alpha())
    for i in range(0, 69 + 1, 1):
        self.sprite['obj'].append(SpriteSheet(self.img_all_obj, "files/img/sprites/tile_maps/xml/all_obj.xml").get_image_num("{}".format(i)).convert_alpha())
    for i in range(0, 0 + 1, 1):
        self.sprite['windows'].append(SpriteSheet(self.img_all_windows, "files/img/sprites/tile_maps/xml/all_windows.xml").get_image_num("{}".format(i)).convert_alpha())
    for i in range(0, 15 + 1, 1):
        self.sprite['map'].append(pg.image.load("files/img/sprites/maps/map{}.png".format(i)).convert_alpha())
    for i in range(0, 21 + 1, 1):
        self.sprite['exp1'].append(SpriteSheet(self.img_exp1, "files/img/sprites/visual fx/anim_xml/exp1_200x200px.xml").get_image_num("{}".format(i)).convert_alpha())
    for i in range(0, 16 + 1, 1):
        self.sprite['exp2'].append(SpriteSheet(self.img_exp2, "files/img/sprites/visual fx/anim_xml/exp2_200x200px.xml").get_image_num("{}".format(i)).convert_alpha())
    for i in range(0, 15 + 1, 1):
        self.sprite['anim_energy_leak_exp'].append(pg.image.load("files/img/sprites/visual fx/anim_energy_leak_explosion/sprite_{}.png".format(i)).convert_alpha())
    for i in range(0, 9 + 1, 1):
        self.sprite['anim_vapour_trail'].append(pg.image.load("files/img/sprites/visual fx/anim_vapour_trail/sprite_{}.png".format(i)).convert_alpha())
    for i in range(0, 2 + 1, 1):
        self.sprite['anim_bullet_flame'].append(pg.image.load("files/img/sprites/visual fx/anim_bullet_flame/sprite_{}.png".format(i)).convert_alpha())
    for i in range(0, 20 + 1, 1):
        self.sprite['anim_yellow_exp'].append(pg.image.load("files/img/sprites/visual fx/anim_yellow_exp/sprite_{}.png".format(i)).convert_alpha())
    for i in range(0, 98 + 1, 1):
        self.sprite['anim_fire'].append(pg.image.load("files/img/sprites/visual fx/anim_fire/sprite_{}.png".format(i)).convert_alpha())
    for i in range(0, 13 + 1, 1):
        self.sprite['anim_spark'].append(pg.image.load("files/img/sprites/visual fx/anim_spark/sprite_{}.png".format(i)).convert_alpha())



"""
Classe DataBase
- But : sauvegarder les donnees du joueur
- Fonctionnement : lors de son initialisation, va creer une base de donnees avec des latices predefinies pour contenir les donnees du joueur.
- Utilisation : la classe DataBase() est appelee dans la classe Prgm() quand le programme est lance pour charger toutes les donnes dans une bibliotheque. Lors de la fermeture du programme, DataBase().db_dict_update() va sauvegarder les donnees de la bibliotheque dans la base .db.
"""
class DataBase:
    
    """
    Fonction __init__
    - Fonctionnement : se connecte a la base de donnees session.db et sauvegarde les noms des latices dans self.db_name_list.
    """
    def __init__(self):
        self.conn = sqlite3.connect('files/session/session.db')

        self.c = self.conn.cursor()

        self.db_name_list = [
        "game_lvl",
        "credit",
        "credit_gain_lvl",
        "cannon_1_lvl",
        "cannon_2_lvl",
        "cannon_3_lvl",
        "cannon_4_lvl",
        "base_shielding_lvl",
        "energy_production_lvl",
        "energy_storage_lvl",
        "build_time_lvl",
        "equip_cost_lvl",
        "build_slots",
        "rover_lvl",
        "rocket_lvl",
        "panther_lvl",
        "flak_lvl",
        "tanker_lvl",
        "build_b1",
        "build_b2",
        "build_b3",
        "build_b4",
        "build_b5",
        "build_b6",
        "build_b7",
        "music_sound_lvl",
        "fx_sound_lvl",
        "screen_width",
        "screen_height",
        "full_screen"
        ]
    
    """
    Fonction db_spawn
    - Fonctionnement : va creer la base de donnee et va inserer des donnees par defaut
    """
    def db_spawn(self):
        # Create table
        self.c.execute("""CREATE TABLE session (
                game_lvl integer,
                credit integer,
                credit_gain_lvl integer,

                cannon_1_lvl integer,
                cannon_2_lvl integer,
                cannon_3_lvl integer,
                cannon_4_lvl integer,

                
                base_shielding_lvl integer, 
                energy_production_lvl integer,
                energy_storage_lvl integer,
                build_time_lvl integer,
                equip_cost_lvl integer,
                build_slots integer,

                rover_lvl integer,

                rocket_lvl integer,

                panther_lvl integer,
                
                flak_lvl integer,
               
                tanker_lvl integer,
                
                build_b1 TEXT,
                build_b2 TEXT,
                build_b3 TEXT,
                build_b4 TEXT,
                build_b5 TEXT,
                build_b6 TEXT,
                build_b7 TEXT,

                music_sound_lvl integer,
                fx_sound_lvl integer,
                screen_width integer,
                screen_height integer,
                full_screen integer
                )""")
        # Insert a row of data
        self.c.execute("""INSERT INTO session VALUES (
            0,  --game_lvl
            0,  --credit
            0,  --credit_gain_lvl
            0,  --cannon_1_lvl
            0,  --cannon_2_lvl
            0,  --cannon_3_lvl
            0,  --cannon_4_lvl
            0,  --base_shielding_lvl
            0,  --energy_production_lvl
            0,  --energy_storage_lvl
            0,  --build_time_lvl
            0,  --equip_cost_lvl
            1,  --build_slots (1 at start)
            1,  --rover_lvl #
            0,  --rocket_lvl #
            0,  --panther_lvl #
            0,  --flak_lvl #
            0,  --tanker_lvl #
            'Rover_1', --build_b1 TEXT
            'None',    --build_b2 TEXT
            'None',    --build_b3 TEXT
            'None',    --build_b4 TEXT
            'None',    --build_b5 TEXT
            'None',    --build_b6 TEXT
            'None',    --build_b7 TEXT
            0.5,  --music_sound_lvl
            0.5,  --fx_sound_lvl
            1280,--screen_width
            720,--screen_height
            0   --full_screen
            )""")
        self.conn.commit()
        self.conn.close()

    """
    Fonction db_update
    - Fonctionnement : sauvegarde une donnee precise designe par data_name dans la base .db.
    """
    def db_update(self, data_name, data_input):
        # Change a specific value in db
        self.c.execute("UPDATE session SET {} = {}".format(data_name, data_input))

        self.conn.commit()
        self.conn.close()

    """
    Fonction db_dict_update
    - Fonctionnement : sauvegarde toutes les donnee contenues dans data_dict_input dans la base .db.
    """
    def db_dict_update(self, data_dict_input):

        for i in range(0, len(self.db_name_list)):
            data_name = self.db_name_list[i]
            data_input = data_dict_input[self.db_name_list[i]]
            print(data_input, data_name)
            self.c.execute("UPDATE session SET {} = '{}'".format(data_name, data_input))
            
        self.conn.commit()
        self.conn.close()


    """
    Fonction db_get
    - Fonctionnement : va chercher une donnee precise et retourner sa valeur
    """
    def db_get(self, data_name):
        # Return a specific value from db
        self.c.execute("SELECT {} FROM session".format(data_name))
        val = self.c.fetchone()[0]
        self.conn.close()

        return val
    
    """
    Fonction db_dict_get
    - Fonctionnement : va chercher toutes les donnees et les sauvegarde dans data_dict_input (bibliotheque).
    """
    def db_dict_get(self, data_dict_input):
        data_dict_input.clear()

        for i in range(0, len(self.db_name_list)):

            data_name = self.db_name_list[i]
            self.c.execute("SELECT {} FROM session".format(data_name))
            data_dict_input[self.db_name_list[i]] = self.c.fetchone()[0]
            
        self.conn.close()
        
    """
    Fonction db_check
    - Fonctionnement : verifie si la base de donnees existe et renvoie un bool qui verifie cette condition.
    """
    def db_check(self):
        # Check if db has some table if not return False if true return True
        self.c.execute("""SELECT name FROM sqlite_master WHERE type='table';""")
        result = self.c.fetchone()
        if result:
            self.conn.close()
            return True
            
        else:
            self.conn.close()
            return False

    """
    Fonction db_remove
    - Fonctionnement : va suppr toutes les donnes de la base de donnnees
    """ 
    def db_remove(self):
        # Clear the entire db
        self.c.execute("DROP TABLE session")
        self.conn.commit()
        self.conn.close()