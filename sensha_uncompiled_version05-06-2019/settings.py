# settings.py

"""
Importe des bibliotheques externes et le code du fichier <<file_loader.py>>
"""
import math
import random
from file_loader import *

"""
Definition des variables fixes
"""

TITLE = "Sensha"
WIDTH = 1920 #1280 # largeur
HEIGHT = 1080 #720 # hauteur
FPS = 60 # rafraichissement


# Level property
DIVIDENT = 3
EXP_DIVIDENT = 2
SCROLL_ACC = 10 # acc ecran
SCROLL_FRICT = -0.2 # limitateur de vitesse

# makeup (colors)
WHITE = (255,255,255)
WHITE_BLUE = (140,150,255)
BLACK = (0,0,0)
RED = (255,0,0)
ORANGE = (241, 160, 42, 255)
DARKRED = (100,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
STELLAR_DUST = (221,150,37)

# Global timer
"""
Classe Timer
- But : chronometrer le temps
- Fonctionnement : chronmetre un temps donne t et delivre un signal positif si le temps est ecoule
- Utilisation : utilise dans une condition if (par exemple : l'economie du jeu)
"""
class Timer():
	def __init__(self):
		self.start_time = 0
		self.top = True
		self.progress = 0
	
	"""
	Fonction chrono
	- Fonctionnement : calcul la difference de temps entre start_time et le temps actuel, si end_time est atteint, renvoyer vrais
	"""
	def chrono(self, end_time):
		if self.top:
			self.top = False
			self.start_time = pg.time.get_ticks()

		self.progress = (pg.time.get_ticks() - self.start_time) / (end_time * 1000)

		if self.progress >= 1:
			self.top = True

		return self.top


#Check if screne change has accured
"""
Classe Resolution_Check
- But : verifier si la resolution de l'ecran n'a pas changee
- Fonctionnement : verifie si la resolution precedente (de la base de donnee) est differente de la nouvelle resolution
- Utilisation : par toutes les classes et fonctions associees
"""
class Resolution_Check():
	def __init__(self, glob):
		self.glob = glob
		self._layer = 10
		self._type = "func"

		self.former_resolution_w = self.glob.data["screen_width"]
		self.change = False

		self.glob.all_virtuals.add([self])
	"""
	Fonction update
	- Fonctionnement : est lue a chaque boucle et verifie si la resolution a changee
	"""
	def update(self):

		if self.former_resolution_w != self.glob.data["screen_width"]:
			self.former_resolution_w = self.glob.data["screen_width"]
			self.change = True

		elif self.change == True:
			self.change = False

"""
Classe Virtuals
- But : simplifier la gestion des classes du programme, permet de creer un programme complexe
- Fonctionnement : regrouper toutes les classes pour lire leurs fonctions 'update' a chaque boucle selon un ordre definit par les layers / si la fonction est de type 'sprite', dessiner sa variable image
- Utilisation : peut ajouter/supprimer des classes ou mettre en pause la lecture des classes
"""
class Virtuals():
	def __init__(self, glob, max_layer):
		self.glob = glob

		self.all_virtuals = {}
		# there are different layers:
		self.max_layer = max_layer
		for i in range(0, self.max_layer + 1):
			self.all_virtuals[i] = []
		
		self.frozen = []
		self.bin = []
	
	"""
	Fonction update
	- Fonctionnement : permet de lire toutes les fonctions update de toutes les classes contenues dans la bibliotheque all_virtuals[] et cela a chaque boucle / dessine sur l'ecran les images de fonctions 'sprites'
	"""
	def update(self):
		# Do .update() for all objects in all lists
		for layer in self.all_virtuals:
			# loop initialisation
			
			# run all .update() function of the classes contained in virtuals group
			# len(list) returns the number of elements in list ex: x = [1,5,3,10]; len(x) = 4
			# self.frist and self.second in while loop check for changes in number of elements in list, ex one has been removed
			for element in self.all_virtuals[layer]:

				if layer not in self.frozen:
					
					if element._type is "func" or element._type is "func_prime":
						element.update()

					elif element._type is "func_sprite" or element._type is "func_sprite_prime":
						element.update()
						self.draw(element)
					elif element._type is "func_sprite_shadow" or element._type is "func_sprite_shadow_prime":
						element.update()
						self.draw_shadow(element)
						self.draw(element)
				else:

					if element._type is "sprite" or element._type is "func_sprite":
						self.draw(element)
					
					elif element._type is "func_sprite_shadow":
						self.draw_shadow(element)
						self.draw(element)
						
					elif element._type is "func_prime":
						element.prime_update()

					elif element._type is "func_sprite_prime":
						element.prime_update()
						self.draw(element)
					
					elif element._type is "func_sprite_shadow_prime":
						element.prime_update()
						self.draw_shadow(element)
						self.draw(element)


		for element in self.bin:
			self.all_virtuals[element._layer].remove(element)
		if len(self.bin) > 0:
			self.bin.clear()

	"""
	Fonction add
	- Fonctionnement : permet d'ajouter une ou plusieurs classes a la bibliotheque all_virtuals[] 
	"""
	def add(self, obj):
		# add specific object to list
		for i in obj:
			self.all_virtuals[i._layer].append(i)

	"""
	Fonction remove
	- Fonctionnement : permet de supprimer une classe donnee de la bibliotheque all_virtuals[] en l'ajoutant a la liste self.bin
	"""
	def remove(self, obj):
			# Remove specific object in list
			for i in obj:
				if i not in self.bin:
					self.bin.append(i)

	"""
	Fonction clear
	- Fonctionnement : supprimer toutes les classes de la bibliotheque all_virtuals[] 
	"""
	def clear(self):
		# remove all elements in all lists
		for layer in range(0, self.max_layer + 1):
			self.all_virtuals[layer].clear()

	"""
	Fonction clear_layer
	- Fonctionnement : supprimer toutes les classes d'un ou de plusieurs layer de la bibliotheque all_virtuals[] en ajoutant toute classe de ce ou ces layer a la liste self.bin
	"""
	def clear_layer(self, layer):
			# Remove one or a list of layers
			for i in layer:
				for x in self.all_virtuals[i]:
					if x not in self.bin and i in self.all_virtuals:
						self.bin.append(x)

	"""
	Fonction freeze
	- Fonctionnement : ajoute un ou plusieurs layer a la bibliotheque self.freeze
	"""
	def freeze(self, layer):
		# Freeze one or multiple layers
		for i in layer:
			if i not in self.frozen:
				self.frozen.append(i)
		
	"""
	Fonction unfreeze
	- Fonctionnement : enleve un ou plusieurs layer de la bibliotheque self.freeze
	"""
	def unfreeze(self, layer):
		for i in layer:
			if i in self.frozen:
				self.frozen.remove(i)
	
	"""
	Fonction unfreeze_all
	- Fonctionnement : enleve tous les layers de la bibliotheque self.freeze
	"""	
	def unfreeze_all(self):
			self.frozen.clear()
	
	"""
	Fonction draw
	- Fonctionnement : dessine une image contenue dans une classe donnee
	"""
	def draw(self, obj):

		self.glob.window.blit(obj.image, obj.rect)
	
	"""
	Fonction draw_shadow
	- Fonctionnement : dessine une image de type ombre dans une classe donnee
	"""
	def draw_shadow(self, obj):

		self.glob.window.blit(obj.shadow, obj.shadow_rect)
	

# Utilities

"""
Fonction Framer
- Fonctionnement : permet de creer une liste avec toutes les classes 'sprites' liees a une classe mere ainsi que cette derniere
"""	
def Framer(self):
	frame_list = []
	frame_list.append(self)
	for name in self.frame:
			for i in self.frame[name]:
				if i != "None":
					frame_list.append(i)
	return frame_list

"""
Fonction Framer2
- Fonctionnement : permet de creer une liste avec toutes les classes 'sprites' liees a une classe mere
"""	
def Framer2(self):
	frame_list = []
	for name in self.frame:
			for i in self.frame[name]:
				if i != "None":
					frame_list.append(i)
	return frame_list

	frame_list = [self,self.frame['body'][0], self.frame['turret'][0],self.frame['turret'][1]]


"""
Classe MusicPlayer
- But : gerer le son dans le jeu (pistes audio, volume sonore, musique)
- Fonctionnement : classe virtuelle qui sera lue chaque boucle, elle lira tout sons contenu dans la liste self.glob.sound_repertoire
- Utilisation : est ajoutee aux virtuals des l'initialisation du programme
"""
class MusicPlayer():
	def __init__(self, glob):
		self.glob = glob
		self._layer = 10
		self._type = "func"

		pg.mixer.music.set_volume(self.glob.data["music_sound_lvl"])
		
		#for i in self.glob.sounds:
        #            i.set_volume(self.glob.data["fx_sound_lvl"])

		self.glob.all_virtuals.add([self])

	"""
	Fonction update
	- Fonctionnement : lira tout sons contenu dans la liste self.glob.sound_repertoire en les placant sur des pistes sons librent et en adaptant leurs volume sonore
	"""
	def update(self):
		# no ndeed for #*
		#*pg.mixer.music.set_volume(self.glob.data["music_sound_lvl"])
		
		for i in self.glob.sound_repertoire:
			for k in range(pg.mixer.get_num_channels()):
				if pg.mixer.Channel(k).get_busy() == 0:

					i.set_volume(self.glob.data["fx_sound_lvl"])
					pg.mixer.Channel(k).play(i)
					# Could create an error
					# FPS are good?
					try:
						self.glob.sound_repertoire.remove(i)
						break
					except:
						break
					
				if k == pg.mixer.get_num_channels()-1:
					self.glob.sound_repertoire = []