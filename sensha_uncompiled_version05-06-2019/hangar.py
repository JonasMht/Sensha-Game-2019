# hangar.py

"""
Importe le code du fichier <<sprites.py>>
"""
from sprites import *

"""
Fonction constructor
- Fonctionnement : utilise dans la classe Vehicle et Base, elle permet de definir la struture des differents tanks en ajoutant des composants a la bibliotheque frame
"""
def constructor(self, name):
	# Turret: glob, image_file, fire_range, fire_rate, rot_speed, pos_adj, layer, projectile_image, projectile_speed, projectile_damage, fire_sound, trail_anim, explosion_anim, explosion_sound

		if name == "Rover_1":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][2], 3))
			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][41], 3))
			self.frame['turret'][0].fire_range = 0.3 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2.3
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 3
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(-0.002,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 10
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			self.hp = 150
			self.max_acc = (0.25)
			self.detection_range = (0.5) * self.glob.data["screen_width"]
			self.hold_range = (0.2) * self.glob.data["screen_width"]
			self.rot_speed = 1

		if name == "Rover_2":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][3], 3))
			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][42], 3))
			self.frame['turret'][0].fire_range = 0.35 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 6
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(-0.004,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 15
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			self.hp = 200
			self.max_acc = (0.27)
			self.detection_range = (0.5) * self.glob.data["screen_width"]
			self.hold_range = (0.25) * self.glob.data["screen_width"]
			self.rot_speed = 1

		if name == "Rover_3":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][4], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][43], 3))
			self.frame['turret'][0].fire_range = 0.4 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2.2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 4
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(-0.004,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 20
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			self.hp = 400
			self.max_acc = (0.29)
			self.detection_range = (0.5) * self.glob.data["screen_width"]
			self.hold_range = (0.3) * self.glob.data["screen_width"]
			self.rot_speed = 1

		if name == "Rover_4":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][5], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][0].fire_range = 0.4 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 8
			self.frame['turret'][0].salvo_interval = 0.1
			self.frame['turret'][0].pos_adj = vec(0.015,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][60]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 10
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][44], 3))
			self.frame['turret'][1].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][1].fire_rate = 2
			self.frame['turret'][1].rot_speed = 3
			self.frame['turret'][1].salvo = 6
			self.frame['turret'][1].salvo_interval = 0.2
			self.frame['turret'][1].pos_adj = vec(-0.005,0) * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][1].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_damage = 25
			self.frame['turret'][1].fire_sound = self.glob.sounds[2]
			self.frame['turret'][1].trail_anim = "None"
			self.frame['turret'][1].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][1].explosion_sound = self.glob.sounds[1]

			self.hp = 750
			self.max_acc = (0.31)
			self.detection_range = (0.6) * self.glob.data["screen_width"]
			self.hold_range = (0.4) * self.glob.data["screen_width"]
			self.rot_speed = 1
			
		if name == "Rover_5":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][6], 3))
			
			self.frame['turret'].append(Launcher(self, self.glob.sprite["obj"][40], 3))
			self.frame['turret'][0].fire_range = 0.4 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2.5
			self.frame['turret'][0].salvo = 1
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].pos_adj = vec(0.01,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][68]
			self.frame['turret'][0].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][0].missile_rot_speed = 4
			self.frame['turret'][0].projectile_damage = 15
			self.frame['turret'][0].fire_sound = self.glob.sounds[3]
			self.frame['turret'][0].trail_anim = self.glob.sprite['anim_vapour_trail']
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_yellow_exp']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][45], 3))
			self.frame['turret'][1].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][1].fire_rate = 3
			self.frame['turret'][1].rot_speed = 3
			self.frame['turret'][1].salvo = 6
			self.frame['turret'][1].salvo_interval = 0.2
			self.frame['turret'][1].pos_adj = vec(-0.01,0) * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][1].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_damage = 30
			self.frame['turret'][1].fire_sound = self.glob.sounds[2]
			self.frame['turret'][1].trail_anim = "None"
			self.frame['turret'][1].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][1].explosion_sound = self.glob.sounds[1]

			

			self.hp = 1000
			self.max_acc = (0.33)
			self.detection_range = (0.6) * self.glob.data["screen_width"]
			self.hold_range = (0.4) * self.glob.data["screen_width"]
			self.rot_speed = 2

		if name == "Rocket_1":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][7], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][0].fire_range = 0.4 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 3
			self.frame['turret'][0].salvo_interval = 0.4
			self.frame['turret'][0].pos_adj = vec(0.003,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][60]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 15
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]
			
			self.frame['turret'].append(Launcher(self, self.glob.sprite["obj"][46], 3))
			self.frame['turret'][1].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][1].fire_rate = 3.5
			self.frame['turret'][1].salvo = 2
			self.frame['turret'][1].salvo_interval = 0.2
			self.frame['turret'][1].rot_speed = 2
			self.frame['turret'][1].pos_adj = vec(-0.0085,0) * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_image = self.glob.sprite["obj"][68]
			self.frame['turret'][1].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][1].missile_rot_speed = 2.5
			self.frame['turret'][1].projectile_damage = 35
			self.frame['turret'][1].fire_sound = self.glob.sounds[3]
			self.frame['turret'][1].trail_anim = self.glob.sprite['anim_vapour_trail']
			self.frame['turret'][1].explosion_anim = self.glob.sprite['anim_yellow_exp']
			self.frame['turret'][1].explosion_sound = self.glob.sounds[1]

			

			self.hp = 100
			self.max_acc = (0.2)
			self.detection_range = (0.6) * self.glob.data["screen_width"]
			self.hold_range = (0.4) * self.glob.data["screen_width"]
			self.rot_speed = 2
		
		if name == "Rocket_2":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][8], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][0].fire_range = 0.4 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 3
			self.frame['turret'][0].salvo_interval = 0.3
			self.frame['turret'][0].pos_adj = vec(0.003,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][60]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 25
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]
			
			self.frame['turret'].append(Launcher(self, self.glob.sprite["obj"][47], 3))
			self.frame['turret'][1].fire_range = 0.6 * self.glob.data["screen_width"]
			self.frame['turret'][1].fire_rate = 4.0
			self.frame['turret'][1].salvo = 3
			self.frame['turret'][1].salvo_interval = 0.2
			self.frame['turret'][1].rot_speed = 2
			self.frame['turret'][1].pos_adj = vec(-0.0085,0) * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_image = self.glob.sprite["obj"][68]
			self.frame['turret'][1].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][1].missile_rot_speed = 3
			self.frame['turret'][1].projectile_damage = 45
			self.frame['turret'][1].fire_sound = self.glob.sounds[3]
			self.frame['turret'][1].trail_anim = self.glob.sprite['anim_vapour_trail']
			self.frame['turret'][1].explosion_anim = self.glob.sprite['anim_yellow_exp']
			self.frame['turret'][1].explosion_sound = self.glob.sounds[1]

			self.hp = 150
			self.max_acc = (0.2)
			self.detection_range = (0.7) * self.glob.data["screen_width"]
			self.hold_range = (0.5) * self.glob.data["screen_width"]
			self.rot_speed = 2
		
		if name == "Rocket_3":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][9], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][0].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 3
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.003,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][60]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 30
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]
			
			self.frame['turret'].append(Launcher(self, self.glob.sprite["obj"][48], 3))
			self.frame['turret'][1].fire_range = 0.7 * self.glob.data["screen_width"]
			self.frame['turret'][1].fire_rate = 5.0
			self.frame['turret'][1].salvo = 4
			self.frame['turret'][1].salvo_interval = 0.2
			self.frame['turret'][1].rot_speed = 2
			self.frame['turret'][1].pos_adj = vec(-0.0085,0) * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_image = self.glob.sprite["obj"][68]
			self.frame['turret'][1].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][1].missile_rot_speed = 3.5
			self.frame['turret'][1].projectile_damage = 50
			self.frame['turret'][1].fire_sound = self.glob.sounds[3]
			self.frame['turret'][1].trail_anim = self.glob.sprite['anim_vapour_trail']
			self.frame['turret'][1].explosion_anim = self.glob.sprite['anim_yellow_exp']
			self.frame['turret'][1].explosion_sound = self.glob.sounds[1]

			self.hp = 200
			self.max_acc = (0.2)
			self.detection_range = (0.8) * self.glob.data["screen_width"]
			self.hold_range = (0.65) * self.glob.data["screen_width"]
			self.rot_speed = 2
		
		if name == "Rocket_4":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][10], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][0].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 4
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.003,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][60]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 35
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]
			
			self.frame['turret'].append(Launcher(self, self.glob.sprite["obj"][49], 3))
			self.frame['turret'][1].fire_range = 0.75 * self.glob.data["screen_width"]
			self.frame['turret'][1].fire_rate = 6.0
			self.frame['turret'][1].salvo = 5
			self.frame['turret'][1].salvo_interval = 0.2
			self.frame['turret'][1].rot_speed = 2
			self.frame['turret'][1].pos_adj = vec(-0.0085,0) * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_image = self.glob.sprite["obj"][68]
			self.frame['turret'][1].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][1].missile_rot_speed = 4
			self.frame['turret'][1].projectile_damage = 50
			self.frame['turret'][1].fire_sound = self.glob.sounds[3]
			self.frame['turret'][1].trail_anim = self.glob.sprite['anim_vapour_trail']
			self.frame['turret'][1].explosion_anim = self.glob.sprite['anim_yellow_exp']
			self.frame['turret'][1].explosion_sound = self.glob.sounds[1]

			

			self.hp = 250
			self.max_acc = (0.2)
			self.detection_range = (0.8) * self.glob.data["screen_width"]
			self.hold_range = (0.7) * self.glob.data["screen_width"]
			self.rot_speed = 2

		if name == "Panther_1":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][11], 3))

			
			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][50], 3))
			self.frame['turret'][0].fire_range = 0.3 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 1
			self.frame['turret'][0].salvo_interval = 0.4
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][61]
			self.frame['turret'][0].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 30
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = self.glob.sprite['anim_bullet_flame']
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_energy_leak_exp']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			

			self.hp = 350
			self.max_acc = (0.2)
			self.detection_range = (0.5) * self.glob.data["screen_width"]
			self.hold_range = (0.25) * self.glob.data["screen_width"]
			self.rot_speed = 2
		
		if name == "Panther_2":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][12], 3))

			
			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][51], 3))
			self.frame['turret'][0].fire_range = 0.35 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 1
			self.frame['turret'][0].salvo_interval = 0.4
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][61]
			self.frame['turret'][0].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 45
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = self.glob.sprite['anim_bullet_flame']
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_energy_leak_exp']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			

			self.hp = 500
			self.max_acc = (0.21)
			self.detection_range = (0.5) * self.glob.data["screen_width"]
			self.hold_range = (0.3) * self.glob.data["screen_width"]
			self.rot_speed = 2

		if name == "Panther_3":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][13], 3))

			
			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][52], 3))
			self.frame['turret'][0].fire_range = 0.4 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 1
			self.frame['turret'][0].salvo_interval = 0.4
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][61]
			self.frame['turret'][0].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 65
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = self.glob.sprite['anim_bullet_flame']
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_energy_leak_exp']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			

			self.hp = 750
			self.max_acc = (0.22)
			self.detection_range = (0.6) * self.glob.data["screen_width"]
			self.hold_range = (0.35) * self.glob.data["screen_width"]
			self.rot_speed = 2

		if name == "Panther_4":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][14], 3))

			
			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][53], 3))
			self.frame['turret'][0].fire_range = 0.45 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 2
			self.frame['turret'][0].salvo_interval = 0.4
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][61]
			self.frame['turret'][0].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 85
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = self.glob.sprite['anim_bullet_flame']
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_energy_leak_exp']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			

			self.hp = 1500
			self.max_acc = (0.23)
			self.detection_range = (0.6) * self.glob.data["screen_width"]
			self.hold_range = (0.4) * self.glob.data["screen_width"]
			self.rot_speed = 2
		
		if name == "Flak_1":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][11], 3))

			
			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][54], 3))
			self.frame['turret'][0].fire_range = 0.3 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 2
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][61]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 10
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = self.glob.sprite['anim_bullet_flame']
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			

			self.hp = 300
			self.max_acc = (0.22)
			self.detection_range = (0.5) * self.glob.data["screen_width"]
			self.hold_range = (0.25) * self.glob.data["screen_width"]
			self.rot_speed = 2
		
		if name == "Flak_2":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][12], 3))

			
			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][55], 3))
			self.frame['turret'][0].fire_range = 0.35 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 3
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][61]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 15
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = self.glob.sprite['anim_bullet_flame']
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			

			self.hp = 400
			self.max_acc = (0.24)
			self.detection_range = (0.5) * self.glob.data["screen_width"]
			self.hold_range = (0.3) * self.glob.data["screen_width"]
			self.rot_speed = 2

		if name == "Flak_3":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][13], 3))

			
			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][56], 3))
			self.frame['turret'][0].fire_range = 0.4 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 3
			self.frame['turret'][0].salvo_interval = 0.1
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][61]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 20
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = self.glob.sprite['anim_bullet_flame']
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			

			self.hp = 600
			self.max_acc = (0.26)
			self.detection_range = (0.5) * self.glob.data["screen_width"]
			self.hold_range = (0.35) * self.glob.data["screen_width"]
			self.rot_speed = 2

		if name == "Flak_4":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][14], 3))

			
			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][57], 3))
			self.frame['turret'][0].fire_range = 0.45 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 4
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][61]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 30
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = self.glob.sprite['anim_bullet_flame']
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			

			self.hp = 900
			self.max_acc = (0.28)
			self.detection_range = (0.6) * self.glob.data["screen_width"]
			self.hold_range = (0.4) * self.glob.data["screen_width"]
			self.rot_speed = 2
		
		if name == "Flak_5":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][14], 3))

			
			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][58], 3))
			self.frame['turret'][0].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 3
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 5
			self.frame['turret'][0].salvo_interval = 0.4
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][61]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 40
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = self.glob.sprite['anim_bullet_flame']
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			

			self.hp = 1250
			self.max_acc = (0.30)
			self.detection_range = (0.6) * self.glob.data["screen_width"]
			self.hold_range = (0.45) * self.glob.data["screen_width"]
			self.rot_speed = 2
		
		if name == "Tanker_1":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][15], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][0].fire_range = 0.2 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 4
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 3
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][60]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 10
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			

			self.hp = 600
			self.max_acc = (0.35)
			self.detection_range = (0.5) * self.glob.data["screen_width"]
			self.hold_range = (0.1) * self.glob.data["screen_width"]
			self.rot_speed = 2
		
		if name == "Tanker_2":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][16], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][0].fire_range = 0.2 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 4
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 3
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][60]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 15
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			

			self.hp = 1000
			self.max_acc = (0.35)
			self.detection_range = (0.5) * self.glob.data["screen_width"]
			self.hold_range = (0.1) * self.glob.data["screen_width"]
			self.rot_speed = 2

		if name == "Tanker_3":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][17], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][0].fire_range = 0.2 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 4
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 3
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][60]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 20
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			

			self.hp = 1500
			self.max_acc = (0.35)
			self.detection_range = (0.5) * self.glob.data["screen_width"]
			self.hold_range = (0.1) * self.glob.data["screen_width"]
			self.rot_speed = 2
		
		if name == "Tanker_4":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][18], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][0].fire_range = 0.2 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 4
			self.frame['turret'][0].rot_speed = 2
			self.frame['turret'][0].salvo = 3
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][60]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 30
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			

			self.hp = 2200
			self.max_acc = (0.35)
			self.detection_range = (0.5) * self.glob.data["screen_width"]
			self.hold_range = (0.1) * self.glob.data["screen_width"]
			self.rot_speed = 2

		if name == "E_1":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][19], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][33], 3))
			self.frame['turret'][0].fire_range = 0.3 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 4 - int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].rot_speed = 1 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo = 3 + int(3 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.008,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 10 + int(10 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			self.hp = 100 + int(100 * (self.glob.game_lvl / 99))
			self.max_acc = (0.2) + (0.1 * (self.glob.game_lvl / 99))
			self.detection_range = (0.5) * self.glob.data["screen_width"]
			self.hold_range = (0.2) * self.glob.data["screen_width"]
			self.rot_speed = 3

		if name == "E_2":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][20], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][34], 3))
			self.frame['turret'][0].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 5 - int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].rot_speed = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo = 1 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo_interval = 0.4
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][67]
			self.frame['turret'][0].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 85 + int(100 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = self.glob.sprite['anim_bullet_flame']
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_energy_leak_exp']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			self.hp = 200 + int(100 * (self.glob.game_lvl / 99))
			self.max_acc = (0.15) + (0.1 * (self.glob.game_lvl / 99))
			self.detection_range = (0.7) * self.glob.data["screen_width"]
			self.hold_range = (0.5) * self.glob.data["screen_width"]
			self.rot_speed = 3

		if name == "E_3":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][21], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][32], 3))
			self.frame['turret'][0].fire_range = 0.4 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].rot_speed = 1
			self.frame['turret'][0].salvo = 2 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo_interval = 0.5
			self.frame['turret'][0].pos_adj = vec(0.01,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][61]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 15 + int(25 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_energy_leak_exp']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Launcher(self, self.glob.sprite["obj"][30], 3))
			self.frame['turret'][1].fire_range = (0.9) * self.glob.data["screen_width"]
			self.frame['turret'][1].fire_rate = 10 - int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].salvo = 3 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].salvo_interval = 0.2
			self.frame['turret'][1].rot_speed = 1 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].pos_adj = vec(-0.02,0) * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_image = self.glob.sprite["obj"][68]
			self.frame['turret'][1].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][1].missile_rot_speed = 4
			self.frame['turret'][1].projectile_damage = 45 + int(150 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].fire_sound = self.glob.sounds[3]
			self.frame['turret'][1].trail_anim = self.glob.sprite['anim_vapour_trail']
			self.frame['turret'][1].explosion_anim = self.glob.sprite['anim_yellow_exp']
			self.frame['turret'][1].explosion_sound = self.glob.sounds[1]

			self.hp = 75 + int(100 * (self.glob.game_lvl / 99))
			self.max_acc = (0.1)
			self.detection_range = (1.1) * self.glob.data["screen_width"]
			self.hold_range = (0.9) * self.glob.data["screen_width"]
			self.rot_speed = 3
		
		if name == "E_4":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][22], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][57], 3))
			self.frame['turret'][0].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 4 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo = 5 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.0,0) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][60]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 25 + int(10 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]


			self.hp = 200 + int(100 * (self.glob.game_lvl / 99))
			self.max_acc = (0.17)
			self.detection_range = (0.7) * self.glob.data["screen_width"]
			self.hold_range = (0.5) * self.glob.data["screen_width"]
			self.rot_speed = 3
		
		if name == "E_5":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][23], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][33], 3))
			self.frame['turret'][0].fire_range = 0.3 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.012,0.019) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 10 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][33], 3))
			self.frame['turret'][1].fire_range = 0.3 * self.glob.data["screen_width"]
			self.frame['turret'][1].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].salvo_interval = 0.2
			self.frame['turret'][1].pos_adj = vec(0.012,-0.019) * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][1].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_damage = 15 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].fire_sound = self.glob.sounds[2]
			self.frame['turret'][1].trail_anim = "None"
			self.frame['turret'][1].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][1].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][38], 3))
			self.frame['turret'][2].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][2].fire_rate = 5 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].rot_speed = 1 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].salvo = 1 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].salvo_interval = 0.4
			self.frame['turret'][2].pos_adj = vec(-0.01,0) * self.glob.data["screen_width"]
			self.frame['turret'][2].projectile_image = self.glob.sprite["obj"][67]
			self.frame['turret'][2].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][2].projectile_damage = 85 + int(100 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].fire_sound = self.glob.sounds[2]
			self.frame['turret'][2].trail_anim = self.glob.sprite['anim_bullet_flame']
			self.frame['turret'][2].explosion_anim = self.glob.sprite['anim_energy_leak_exp']
			self.frame['turret'][2].explosion_sound = self.glob.sounds[1]

			self.hp = 250 + int(100 * (self.glob.game_lvl / 99))
			self.max_acc = (0.15)
			self.detection_range = (0.7) * self.glob.data["screen_width"]
			self.hold_range = (0.5) * self.glob.data["screen_width"]
			self.rot_speed = 3
		
		if name == "E_6":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][24], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][31], 3))
			self.frame['turret'][0].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.013,0.0175) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 10 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][31], 3))
			self.frame['turret'][1].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][1].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].salvo_interval = 0.2
			self.frame['turret'][1].pos_adj = vec(0.013,-0.0175) * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][1].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_damage = 10 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].fire_sound = self.glob.sounds[2]
			self.frame['turret'][1].trail_anim = "None"
			self.frame['turret'][1].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][1].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][56], 3))
			self.frame['turret'][2].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][2].fire_rate = 4 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].rot_speed = 2
			self.frame['turret'][2].salvo = 4 + int(4 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].salvo_interval = 0.2
			self.frame['turret'][2].pos_adj = vec(-0.005,0) * self.glob.data["screen_width"]
			self.frame['turret'][2].projectile_image = self.glob.sprite["obj"][67]
			self.frame['turret'][2].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][2].projectile_damage = 25 + int(25 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].fire_sound = self.glob.sounds[2]
			self.frame['turret'][2].trail_anim = "None"
			self.frame['turret'][2].explosion_anim = self.glob.sprite['anim_energy_leak_exp']
			self.frame['turret'][2].explosion_sound = self.glob.sounds[1]

			self.hp = 250 + int(100 * (self.glob.game_lvl / 99))
			self.max_acc = (0.14)
			self.detection_range = (0.7) * self.glob.data["screen_width"]
			self.hold_range = (0.5) * self.glob.data["screen_width"]
			self.rot_speed = 3
		
		if name == "E_7":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][25], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][0].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.014,0.019) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 10 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][1].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][1].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].salvo_interval = 0.2
			self.frame['turret'][1].pos_adj = vec(0.014,-0.019) * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][1].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_damage = 10 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].fire_sound = self.glob.sounds[2]
			self.frame['turret'][1].trail_anim = "None"
			self.frame['turret'][1].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][1].explosion_sound = self.glob.sounds[1]
			
			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][2].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][2].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].salvo_interval = 0.2
			self.frame['turret'][2].pos_adj = vec(-0.022,0.0185) * self.glob.data["screen_width"]
			self.frame['turret'][2].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][2].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][2].projectile_damage = 10 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].fire_sound = self.glob.sounds[2]
			self.frame['turret'][2].trail_anim = "None"
			self.frame['turret'][2].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][2].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][3].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][3].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][3].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][3].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][3].salvo_interval = 0.2
			self.frame['turret'][3].pos_adj = vec(-0.022,-0.0185) * self.glob.data["screen_width"]
			self.frame['turret'][3].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][3].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][3].projectile_damage = 10 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][3].fire_sound = self.glob.sounds[2]
			self.frame['turret'][3].trail_anim = "None"
			self.frame['turret'][3].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][3].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][51], 3))
			self.frame['turret'][4].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][4].fire_rate = 5 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][4].rot_speed = 1 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][4].salvo = 1 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][4].salvo_interval = 0.4
			self.frame['turret'][4].pos_adj = vec(0,0) * self.glob.data["screen_width"]
			self.frame['turret'][4].projectile_image = self.glob.sprite["obj"][67]
			self.frame['turret'][4].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][4].projectile_damage = 85 + int(100 * (self.glob.game_lvl / 99))
			self.frame['turret'][4].fire_sound = self.glob.sounds[2]
			self.frame['turret'][4].trail_anim = "None"
			self.frame['turret'][4].explosion_anim = self.glob.sprite['anim_energy_leak_exp']
			self.frame['turret'][4].explosion_sound = self.glob.sounds[1]

			self.hp = 300 + int(100 * (self.glob.game_lvl / 99))
			self.max_acc = (0.12)
			self.detection_range = (0.7) * self.glob.data["screen_width"]
			self.hold_range = (0.5) * self.glob.data["screen_width"]
			self.rot_speed = 3
		
		if name == "E_8":
			self.frame['body'].append(Body(self, self.glob.sprite["obj"][26], 3))

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][0].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][0].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].salvo_interval = 0.2
			self.frame['turret'][0].pos_adj = vec(0.04,0.01) * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][0].projectile_damage = 10 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][0].fire_sound = self.glob.sounds[2]
			self.frame['turret'][0].trail_anim = "None"
			self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][0].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][1].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][1].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].salvo_interval = 0.2
			self.frame['turret'][1].pos_adj = vec(0.04,-0.01) * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][1].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][1].projectile_damage = 10 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][1].fire_sound = self.glob.sounds[2]
			self.frame['turret'][1].trail_anim = "None"
			self.frame['turret'][1].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][1].explosion_sound = self.glob.sounds[1]
			
			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][33], 3))
			self.frame['turret'][2].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][2].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].salvo_interval = 0.2
			self.frame['turret'][2].pos_adj = vec(0.0135,0.0185) * self.glob.data["screen_width"]
			self.frame['turret'][2].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][2].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][2].projectile_damage = 10 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][2].fire_sound = self.glob.sounds[2]
			self.frame['turret'][2].trail_anim = "None"
			self.frame['turret'][2].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][2].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][33], 3))
			self.frame['turret'][3].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][3].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][3].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][3].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][3].salvo_interval = 0.2
			self.frame['turret'][3].pos_adj = vec(0.0135,-0.0185) * self.glob.data["screen_width"]
			self.frame['turret'][3].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][3].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][3].projectile_damage = 10 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][3].fire_sound = self.glob.sounds[2]
			self.frame['turret'][3].trail_anim = "None"
			self.frame['turret'][3].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][3].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][4].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][4].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][4].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][4].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][4].salvo_interval = 0.2
			self.frame['turret'][4].pos_adj = vec(-0.0225,0.0185) * self.glob.data["screen_width"]
			self.frame['turret'][4].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][4].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][4].projectile_damage = 10 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][4].fire_sound = self.glob.sounds[2]
			self.frame['turret'][4].trail_anim = "None"
			self.frame['turret'][4].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][4].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][39], 3))
			self.frame['turret'][5].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][5].fire_rate = 3 - int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][5].rot_speed = 2 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][5].salvo = 3 + int(2 * (self.glob.game_lvl / 99))
			self.frame['turret'][5].salvo_interval = 0.2
			self.frame['turret'][5].pos_adj = vec(-0.0225,-0.0185) * self.glob.data["screen_width"]
			self.frame['turret'][5].projectile_image = self.glob.sprite["obj"][59]
			self.frame['turret'][5].projectile_speed = 0.01 * self.glob.data["screen_width"]
			self.frame['turret'][5].projectile_damage = 10 + int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][5].fire_sound = self.glob.sounds[2]
			self.frame['turret'][5].trail_anim = "None"
			self.frame['turret'][5].explosion_anim = self.glob.sprite['anim_spark']
			self.frame['turret'][5].explosion_sound = self.glob.sounds[1]

			self.frame['turret'].append(Turret(self, self.glob.sprite["obj"][53], 3))
			self.frame['turret'][6].fire_range = 0.5 * self.glob.data["screen_width"]
			self.frame['turret'][6].fire_rate = 10 - int(5 * (self.glob.game_lvl / 99))
			self.frame['turret'][6].rot_speed = 1 + int(1 * (self.glob.game_lvl / 99))
			self.frame['turret'][6].salvo = 2
			self.frame['turret'][6].salvo_interval = 0.4
			self.frame['turret'][6].pos_adj = vec(-0.002,0) * self.glob.data["screen_width"]
			self.frame['turret'][6].projectile_image = self.glob.sprite["obj"][67]
			self.frame['turret'][6].projectile_speed = 0.005 * self.glob.data["screen_width"]
			self.frame['turret'][6].projectile_damage = 85 + int(100 * (self.glob.game_lvl / 99))
			self.frame['turret'][6].fire_sound = self.glob.sounds[2]
			self.frame['turret'][6].trail_anim = self.glob.sprite['anim_bullet_flame']
			self.frame['turret'][6].explosion_anim = self.glob.sprite['anim_energy_leak_exp']
			self.frame['turret'][6].explosion_sound = self.glob.sounds[1]

			self.hp = 400 + int(100 * (self.glob.game_lvl / 99))
			self.max_acc = (0.11)
			self.detection_range = (0.7) * self.glob.data["screen_width"]
			self.hold_range = (0.5) * self.glob.data["screen_width"]
			self.rot_speed = 3

		if name == "Base":
			self.frame['body'][0] = Body(self, self.glob.sprite["obj"][0], 4)
			
			if self.glob.data["cannon_1_lvl"] > 0:
				self.frame['turret'][0] = Turret(self, self.glob.sprite["obj"][29], 4)
				self.frame['turret'][0].fire_range = (0.6 + (0.4 * (self.glob.data["cannon_1_lvl"] / 9)) ) * self.glob.data["screen_width"]
				self.frame['turret'][0].fire_rate = 5 - int(1 * (self.glob.data["cannon_1_lvl"] / 9))
				self.frame['turret'][0].salvo = 5 + int(3 * (self.glob.data["cannon_1_lvl"] / 9))
				self.frame['turret'][0].salvo_interval = 0.2
				self.frame['turret'][0].rot_speed = 2 + int(1 * (self.glob.data["cannon_1_lvl"] / 9))
				self.frame['turret'][0].pos_adj = vec(0.01,-0.19) * self.glob.data["screen_width"]
				self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][61]
				self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
				self.frame['turret'][0].projectile_damage = 5 + int(25 * (self.glob.data["cannon_1_lvl"] / 9))
				self.frame['turret'][0].fire_sound = self.glob.sounds[2]
				self.frame['turret'][0].trail_anim = "None"
				self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
				self.frame['turret'][0].explosion_sound = self.glob.sounds[1]
			
			if self.glob.data["cannon_2_lvl"] > 0:
				self.frame['turret'][1] = Turret(self, self.glob.sprite["obj"][29], 4)
				self.frame['turret'][1].fire_range = (0.6 + (0.4 * (self.glob.data["cannon_2_lvl"] / 9)) ) * self.glob.data["screen_width"]
				self.frame['turret'][1].fire_rate = 5 - int(1 * (self.glob.data["cannon_2_lvl"] / 9))
				self.frame['turret'][1].salvo = 5 + int(3 * (self.glob.data["cannon_2_lvl"] / 9))
				self.frame['turret'][1].salvo_interval = 0.2
				self.frame['turret'][1].rot_speed = 2 + int(1 * (self.glob.data["cannon_2_lvl"] / 9))
				self.frame['turret'][1].pos_adj = vec(0.01,-0.105) * self.glob.data["screen_width"]
				self.frame['turret'][1].projectile_image = self.glob.sprite["obj"][61]
				self.frame['turret'][1].projectile_speed = 0.01 * self.glob.data["screen_width"]
				self.frame['turret'][1].projectile_damage = 5 + int(25 * (self.glob.data["cannon_2_lvl"] / 9))
				self.frame['turret'][1].fire_sound = self.glob.sounds[2]
				self.frame['turret'][1].trail_anim = "None"
				self.frame['turret'][1].explosion_anim = self.glob.sprite['anim_spark']
				self.frame['turret'][1].explosion_sound = self.glob.sounds[1]
			
			if self.glob.data["cannon_3_lvl"] > 0:
				self.frame['turret'][2] = Turret(self, self.glob.sprite["obj"][28], 4)
				self.frame['turret'][2].fire_range = (0.6 + (0.4 * (self.glob.data["cannon_3_lvl"] / 9)) ) * self.glob.data["screen_width"]
				self.frame['turret'][2].fire_rate = 10 - int(5 * (self.glob.data["cannon_3_lvl"] / 9))
				self.frame['turret'][2].salvo = 1 + int(1 * (self.glob.data["cannon_3_lvl"] / 9))
				self.frame['turret'][2].salvo_interval = 2
				self.frame['turret'][2].rot_speed = 1 + int(1 * (self.glob.data["cannon_3_lvl"] / 9))
				self.frame['turret'][2].pos_adj = vec(0.01,0.105) * self.glob.data["screen_width"]
				self.frame['turret'][2].projectile_image = self.glob.sprite["obj"][67]
				self.frame['turret'][2].projectile_speed = 0.005 * self.glob.data["screen_width"]
				self.frame['turret'][2].projectile_damage = 100 + int(500 * (self.glob.data["cannon_3_lvl"] / 9))
				self.frame['turret'][2].fire_sound = self.glob.sounds[0]
				self.frame['turret'][2].trail_anim = self.glob.sprite['anim_bullet_flame']
				self.frame['turret'][2].explosion_anim = self.glob.sprite['anim_energy_leak_exp']
				self.frame['turret'][2].explosion_sound = self.glob.sounds[1]

			if self.glob.data["cannon_4_lvl"] > 0:
				self.frame['turret'][3] = Launcher(self, self.glob.sprite["obj"][30], 4)
				self.frame['turret'][3].fire_range = (0.6 + (0.4 * (self.glob.data["cannon_4_lvl"] / 9)) ) * self.glob.data["screen_width"]
				self.frame['turret'][3].fire_rate = 10 - int(5 * (self.glob.data["cannon_4_lvl"] / 9))
				self.frame['turret'][3].salvo = 3 + int(5 * (self.glob.data["cannon_4_lvl"] / 9))
				self.frame['turret'][3].salvo_interval = 0.2
				self.frame['turret'][3].rot_speed = 1 + int(1 * (self.glob.data["cannon_4_lvl"] / 9))
				self.frame['turret'][3].pos_adj = vec(0.01,0.19) * self.glob.data["screen_width"]
				self.frame['turret'][3].projectile_image = self.glob.sprite["obj"][69]
				self.frame['turret'][3].projectile_speed = 0.005 * self.glob.data["screen_width"]
				self.frame['turret'][3].missile_rot_speed = 2 + int(0.3 * self.glob.data["cannon_4_lvl"])
				self.frame['turret'][3].projectile_damage = 25 + int(100 * (self.glob.data["cannon_4_lvl"] / 9))
				self.frame['turret'][3].fire_sound = self.glob.sounds[3]
				self.frame['turret'][3].trail_anim = self.glob.sprite['anim_vapour_trail']
				self.frame['turret'][3].explosion_anim = self.glob.sprite['anim_yellow_exp']
				self.frame['turret'][3].explosion_sound = self.glob.sounds[1]
			
			self.hp = 2000 + 500 * self.glob.data["base_shielding_lvl"]
			self.hp_max = self.hp
				
			self.detection_range = (1.1) * self.glob.data["screen_width"]

			
		if name == "E_Base":
			self.frame['body'][0] = Body(self, self.glob.sprite["obj"][1], 4)
			
			if self.glob.game_lvl > 5:
				self.frame['turret'][0] = Turret(self, self.glob.sprite["obj"][29], 4)
				self.frame['turret'][0].fire_range = 0.9 * self.glob.data["screen_width"]
				self.frame['turret'][0].fire_rate = 7 - int(2 * (self.glob.game_lvl / 99))
				self.frame['turret'][0].salvo = 3 + int(6 * (self.glob.game_lvl / 99))
				self.frame['turret'][0].salvo_interval = 0.2
				self.frame['turret'][0].rot_speed = 1 + int(2 * (self.glob.game_lvl / 99))
				self.frame['turret'][0].pos_adj = vec(0.01,-0.105) * self.glob.data["screen_width"]
				self.frame['turret'][0].projectile_image = self.glob.sprite["obj"][61]
				self.frame['turret'][0].projectile_speed = 0.01 * self.glob.data["screen_width"]
				self.frame['turret'][0].projectile_damage = 5 + int(20 * (self.glob.game_lvl / 99))
				self.frame['turret'][0].fire_sound = self.glob.sounds[2]
				self.frame['turret'][0].trail_anim = "None"
				self.frame['turret'][0].explosion_anim = self.glob.sprite['anim_spark']
				self.frame['turret'][0].explosion_sound = self.glob.sounds[1]
			
			if self.glob.game_lvl > 20:
				self.frame['turret'][1] = Turret(self, self.glob.sprite["obj"][29], 4)
				self.frame['turret'][1].fire_range = 0.9 * self.glob.data["screen_width"]
				self.frame['turret'][1].fire_rate = 7 - int(2 * (self.glob.game_lvl / 99))
				self.frame['turret'][1].salvo = 3 + int(6 * (self.glob.game_lvl / 99))
				self.frame['turret'][1].salvo_interval = 0.2
				self.frame['turret'][1].rot_speed = 1 + int(2 * (self.glob.game_lvl / 99))
				self.frame['turret'][1].pos_adj = vec(0.01,0.105) * self.glob.data["screen_width"]
				self.frame['turret'][1].projectile_image = self.glob.sprite["obj"][61]
				self.frame['turret'][1].projectile_speed = 0.01 * self.glob.data["screen_width"]
				self.frame['turret'][1].projectile_damage = 5 + int(20 * (self.glob.game_lvl / 99))
				self.frame['turret'][1].fire_sound = self.glob.sounds[2]
				self.frame['turret'][1].trail_anim = "None"
				self.frame['turret'][1].explosion_anim = self.glob.sprite['anim_spark']
				self.frame['turret'][1].explosion_sound = self.glob.sounds[1]
			
			if self.glob.game_lvl > 40:
				self.frame['turret'][2] = Turret(self, self.glob.sprite["obj"][28], 4)
				self.frame['turret'][2].fire_range = 0.9 * self.glob.data["screen_width"]
				self.frame['turret'][2].fire_rate = 10 - int(5 * (self.glob.game_lvl / 99))
				self.frame['turret'][2].salvo = 1
				self.frame['turret'][2].salvo_interval = 0.2
				self.frame['turret'][2].rot_speed = 1 + int(1 * (self.glob.game_lvl / 99))
				self.frame['turret'][2].pos_adj = vec(0.01,0.19) * self.glob.data["screen_width"]
				self.frame['turret'][2].projectile_image = self.glob.sprite["obj"][67]
				self.frame['turret'][2].projectile_speed = 0.005 * self.glob.data["screen_width"]
				self.frame['turret'][2].projectile_damage = 100 + int(150 * (self.glob.game_lvl / 99))
				self.frame['turret'][2].fire_sound = self.glob.sounds[0]
				self.frame['turret'][2].trail_anim = self.glob.sprite['anim_bullet_flame']
				self.frame['turret'][2].explosion_anim = self.glob.sprite['anim_energy_leak_exp']
				self.frame['turret'][2].explosion_sound = self.glob.sounds[1]

			if self.glob.game_lvl > 60:
				self.frame['turret'][3] = Launcher(self, self.glob.sprite["obj"][30], 4)
				self.frame['turret'][3].fire_range = 0.9 * self.glob.data["screen_width"]
				self.frame['turret'][3].fire_rate = 5 - int(2 * (self.glob.game_lvl / 99))
				self.frame['turret'][3].salvo = 2 + int(3 * (self.glob.game_lvl / 99))
				self.frame['turret'][3].salvo_interval = 0.2
				self.frame['turret'][3].rot_speed = 1 + int(1 * (self.glob.game_lvl / 99))
				self.frame['turret'][3].pos_adj = vec(0.01,-0.19) * self.glob.data["screen_width"]
				self.frame['turret'][3].projectile_image = self.glob.sprite["obj"][69]
				self.frame['turret'][3].projectile_speed = 0.005 * self.glob.data["screen_width"]
				self.frame['turret'][3].missile_rot_speed = 2 + int(5 * (self.glob.game_lvl / 99))
				self.frame['turret'][3].projectile_damage = 10 + int(100 * (self.glob.game_lvl / 99))
				self.frame['turret'][3].fire_sound = self.glob.sounds[3]
				self.frame['turret'][3].trail_anim = self.glob.sprite['anim_vapour_trail']
				self.frame['turret'][3].explosion_anim = self.glob.sprite['anim_yellow_exp']
				self.frame['turret'][3].explosion_sound = self.glob.sounds[1]

			self.hp = 2000 + int(5500 * (self.glob.game_lvl / 99))
			self.hp_max = self.hp

			self.detection_range = (1.1) * self.glob.data["screen_width"]



"""
Classe Vehicle
- But : assembler des composants frame du tank
- Fonctionnement : partage des variables et des vecteurs avec les classes contenues dans self.frame
- Utilisation : lorsqu'elle est appellee, la classe fait apparaitre le vehicule souhaite
"""
class Vehicle():
	def __init__(self, glob, vehicle, allegiance):
		self.glob = glob
		self._layer = 2
		self._type = "func_prime"

		self.banner = allegiance
		self.vehicle = vehicle

		self.hp = 0

		self.frame = {}
		self.frame['body'] = []
		self.frame['turret'] = []
		self.pos = vec(0,0)
		self.spd = vec(0, 0)
		self.acc = vec(0, 0)

		self.death_timer = Timer()
		self.remove_turret = False


		self.rot_target = 0
		self.rot_tracker = 0
		self.target = False
		self.traget_dist = 0
		self.pin = vec(0,0)

		if self.banner == "Ally":
			self.rot = 0
		else:
			self.rot = 180

		# Different vehivles function:
		constructor(self, self.vehicle)

		# Collision radius
		self.radius = int(self.frame['body'][0].rect.w/2)

		#Position spawn
		if self.banner == "Ally":
			self.pos.x = self.glob.map_instance.pos.x - self.radius * 2
		else:
			self.pos.x = self.glob.map_instance.pos.x + self.radius * 2 + self.glob.map_instance.rect.w
		
		self.pos.y = random.randint(self.glob.map_instance.pos.y, self.glob.map_instance.pos.y + 0.825 * self.glob.data["screen_height"])
		
		self.glob.all_virtuals.add(Framer(self))
		
	"""
	Fonction update
	- Fonctionnement : mets a jour la position du vehicule a chaque boucle et verifie son etat (toujours en vie?) / IA (conduit le tank, gestion de la collision, detection ennemi)
	"""
	def update(self):
		self.pos.x += self.glob.map_instance.map_offset
		self.acc = vec(0, 0)
		Troop_AI(self)

		if self.hp <= 0:
			
			if self.remove_turret == False:
				
				pos = vec(self.pos.x/self.glob.data["screen_width"], self.pos.y/self.glob.data["screen_height"])
				Animation_Player(self.glob, self.glob.sprite['anim_fire'], 0.01, pos, self.rot, 0.002 * self.radius, 0.00355 * self.radius, 6)
				
				self.glob.all_virtuals.remove(self.frame["turret"])
				self.remove_turret = True

			if self.death_timer.chrono(2):
				
				self.glob.all_virtuals.remove(self.frame["body"])
				self.glob.all_virtuals.remove([self])


		self.acc += (self.spd * -0.2)
		self.spd += self.acc
		self.pos += self.spd.rotate(-self.rot) * self.glob.fps_stab * (self.glob.data["screen_height"]/720)

	"""
	Fonction prime_update
	- Fonctionnement : sera lue quand la classe est gelee / change la position du tank si la resolution de l'ecran est modifiee
	"""
	def prime_update(self):
        
		if self.glob.Resol_Check.change:
			if self.glob.data["screen_height"] == 720:
				self.pos.x = self.pos.x * (2/3)
				self.pos.y = self.pos.y * (2/3)
			else:
				self.pos.x = self.pos.x * (3/2)
				self.pos.y = self.pos.y * (3/2)
				
				

            

"""
Classe Base
- But : assembler des composants frame de la base
- Fonctionnement : partage des variables et des vecteurs avec les classes contenues dans self.frame
- Utilisation : lorsqu'elle est appellee, la classe fait apparaitre la souhaitee (base ennemie ou alliee)
"""
class Base():
	def __init__(self, glob, base, allegiance):
		self.glob = glob
		self._layer = 1
		self._type = "func_prime"

		self.banner = allegiance
		self.base = base

		self.hp = 0
		self.hp_max = 0

		self.frame = {}
		self.frame['body'] = ["None"]
		self.frame['turret'] = ["None","None","None","None"]

		self.death_timer = Timer()
		self.timer = Timer()

		self.pos = vec(0,0)
		self.target = False
		self.traget_dist = 0
		self.pin = vec(0,0)

		if self.banner == "Ally":
			self.rot = 0
		else:
			self.rot = 180

		# Different bases function:
		constructor(self, self.base)

		if self.banner == "Ally":
			self.turrets = []
			for i in range(1,4+1):
				self.turrets.append(self.glob.data["cannon_{}_lvl".format(i)])

		# Collision radius
		self.radius = int(self.frame['body'][0].rect.w/2)
		
		#Position spawn
		if self.banner == "Ally":
			self.pos.x = self.glob.map_instance.pos.x + self.radius
		else:
			self.pos.x = self.glob.map_instance.pos.x + self.glob.map_instance.rect.w - self.radius
	
		self.pos.y = self.glob.map_instance.pos.y + ( 0.825 * self.glob.data["screen_height"]/2)

		if self.banner == "Ally":
			self.life_bar = Progression_Bar(self.glob, vec(0.25 ,0.085), 0.5, 0.01, GREEN, "Left", 7)
		else:
			self.life_bar = Progression_Bar(self.glob, vec(0.75 ,0.085), 0.5, 0.01, RED, "Right", 7)
		
		self.glob.all_virtuals.add(Framer(self))

	
	"""
	Fonction update
	- Fonctionnement : sera lue a chaque boucle et change la position de la base si la carte bouge / gere la barre de vie des bases
	"""
	def update(self):
		self.pos.x += self.glob.map_instance.map_offset

		Base_AI(self)

		if self.hp/self.hp_max <= 0.25:
			if self.timer.chrono(1):
				Animation_Player(self.glob, self.glob.sprite['anim_fire'], 0.01, vec(random.uniform(self.pos.x/self.glob.data["screen_width"]- 0.01 ,self.pos.x/self.glob.data["screen_width"] + 0.01) ,random.uniform(0.075,0.9)), self.rot, 0.002 * self.radius, 0.00355 * self.radius, 6)

		self.life_bar.progression = self.hp/self.hp_max
		self.life_bar.change()

	
	"""
	Fonction prime_update
	- Fonctionnement : sera lue quand la classe est gelee / change la position de la base si la carte bouge et gere l'apparition de nouvelles tourelles si la base est amelioree.
	"""
	def prime_update(self):
		
		if self.glob.Resol_Check.change:
			if self.glob.data["screen_height"] == 720:
				self.pos.x = int(self.pos.x * (2/3))
				self.pos.y = int(self.pos.y * (2/3))
			else:
				self.pos.x = int(self.pos.x * (3/2))
				self.pos.y = int(self.pos.y * (3/2))
		

		if self.banner == "Ally":
			if self.hp_max != 2000 + 500 * self.glob.data["base_shielding_lvl"]:
				self.hp_max = 2000 + 500 * self.glob.data["base_shielding_lvl"]
			for i in range(1,4 + 1):
				if self.glob.data["cannon_{}_lvl".format(i)] != self.turrets[i - 1]:
					ls = []
					for k in self.frame:
						for j in self.frame[k]:
							if j != "None":
								ls.append(j)
								j = "None"
					print("Bin: ",ls)
					self.glob.all_virtuals.remove(ls)

					constructor(self, self.base)
					
					self.glob.all_virtuals.add(Framer2(self))

					all_frames = Framer2(self)

					for frame in all_frames:
						frame.update()

					self.turrets[i - 1] = self.glob.data["cannon_{}_lvl".format(i)]