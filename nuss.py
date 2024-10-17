from pygame import*
from random import*
from threading import*
w = 1280
h = 720
x = 0
screen = display.set_mode((w, h), FULLSCREEN)
display.set_caption('NUSS')
clock = time.Clock()
done = False
background = transform.scale(image.load("nuss_images/background_day.png").convert(), (3480, 720))

class Objeto(sprite.Sprite):
	def __init__(self, x, y, ancho, largo, color, vidas):
		sprite.Sprite.__init__(self)
		self.x = x
		self.y = y
		self.ancho = ancho
		self.largo = largo
		self.color = color
		self.vidas = vidas

	def DibujarObjeto(self):
		draw.rect(screen, self.color, (self.x,self.y,self.ancho,self.largo))

class Barra(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas)


class Personaje(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas)
	
	def Movimiento(self):
		global timer, plus_timer, level
		x = self.x
		y = self.y
		keys = key.get_pressed()
		if level == 1:
			if keys[K_w]==1 and plus_timer == False:
				if y == 30:
					pass
				else:
					self.y -= 230
					plus_timer = True
			if keys[K_s]==1 and plus_timer == False:
				if y == 490:
					pass
				else:
					self.y += 230
					plus_timer = True
		if level == 2:
			if keys[K_w]==1 and plus_timer == False:
				if y == 30:
					pass
				else:
					self.y -= 140
					plus_timer = True
			if keys[K_s]==1 and plus_timer == False:
				if y == 590:
					pass
				else:
					self.y += 140
					plus_timer = True
		if level == 3:
			if keys[K_w]==1 and plus_timer == False:
				if y == 30:
					pass
				else:
					self.y -= 230
					plus_timer = True
			if keys[K_s]==1 and plus_timer == False:
				if y == 490:
					pass
				else:
					self.y += 230
					plus_timer = True
			if keys[K_a]==1 and plus_timer == False:
				if x == 50:
					pass
				else:
					self.x -= 200
					plus_timer = True
			if keys[K_d]==1 and plus_timer == False:
				if x == 450:
					pass
				else:
					self.x += 200
					plus_timer = True
		if level == 4:
			if keys[K_w]==1 and plus_timer == False:
				if y == 30:
					pass
				else:
					self.y -= 140
					plus_timer = True
			if keys[K_s]==1 and plus_timer == False:
				if y == 590:
					pass
				else:
					self.y += 140
					plus_timer = True
			if keys[K_a]==1 and plus_timer == False:
				if x == 50:
					pass
				else:
					self.x -= 150
					plus_timer = True
			if keys[K_d]==1 and plus_timer == False:
				if x == 650:
					pass
				else:
					self.x += 150
					plus_timer = True
		if plus_timer == True:
			timer += 1
			if timer == 20:
				timer = 0
				plus_timer = False
		#self.DibujarObjeto()

	def check_colisiones(sprite1, sprite2):
		xsprite1 = sprite1.x
		ysprite1 = sprite1.y
		anchosprite1 = sprite1.ancho
		largosprite1 = sprite1.largo
		xsprite2 = sprite2.x
		ysprite2 = sprite2.y
		anchosprite2 = sprite2.ancho
		largosprite2 = sprite2.largo
		if (ysprite1 + largosprite1) > ysprite2 and ysprite1 < (ysprite2 + largosprite2) and (xsprite1 + anchosprite1) > xsprite2 and xsprite1 < (xsprite2 + anchosprite2):
			return True

class Boss(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas)
		self.disparo1 = Disparo(self.x, 100, 50, 50, (255,0,0), 1)
		self.disparo2 = Disparo(self.x, 350, 50, 50, (255,0,0), 1)
		self.disparo3 = Disparo(self.x, 600, 50, 50, (255,0,0), 1)
		self.disparo4 = Disparo(self.x, 225, 25, 25, (255,0,0), 1)
		self.disparo5 = Disparo(self.x, 475, 25, 25, (255,0,0), 1)
		self.disparo6 = Disparo(150, 0, 50, 50, (255,0,0), 1)
		self.disparo7 = Disparo(350, 0, 50, 50, (255,0,0), 1)
		self.disparo8 = Disparo(550, 0, 50, 50, (255,0,0), 1)
		self.disparo9 = Disparo(225, 225, 25, 25, (255,0,0), 1)
		self.disparo10 = Disparo(525, 475, 25, 25, (255,0,0), 1)

	def Movimiento(self):
		self.DibujarObjeto()

	def Disparar(self):
		global level, aleatorio1, aleatorio2, aleatorio3, aleatorio4, aleatorio5, aleatorio6, recharge
		if level == 1:
			if recharge == True:
				aleatorio1 = randrange(1,4)
				aleatorio2 = randrange(1,4)
				self.disparo1.y = 100
				self.disparo2.y = 350
				self.disparo3.y = 600
				recharge = False
			if aleatorio1 != aleatorio2:
				if (aleatorio1 == 1 and aleatorio2 == 2) or (aleatorio1 == 2 and aleatorio2 == 1):
					self.disparo1.Movimiento()
					self.disparo2.Movimiento()
					self.disparo2.x = self.disparo1.x
				if (aleatorio1 == 1 and aleatorio2 == 3) or (aleatorio1 == 3 and aleatorio2 == 1):
					self.disparo1.Movimiento()
					self.disparo3.Movimiento()
					self.disparo3.x = self.disparo1.x
				if (aleatorio1 == 2 and aleatorio2 == 3) or (aleatorio1 == 3 and aleatorio2 == 2):
					self.disparo2.Movimiento()
					self.disparo3.Movimiento()
					self.disparo3.x = self.disparo2.x
			if aleatorio1 == aleatorio2:
				recharge = True
		if level == 2:
			if recharge == True: #randrange(1,6)
				aleatorio1 = randrange(1,6)
				aleatorio2 = randrange(1,6)
				aleatorio3 = randrange(1,6)
				self.disparo1.y = 100
				self.disparo2.y = 350
				self.disparo3.y = 600
				self.disparo4.y = 225
				self.disparo5.y = 475
				recharge = False
			if aleatorio1 != aleatorio2 and aleatorio1 != aleatorio3 and aleatorio2 != aleatorio3:
				if aleatorio1 == 1 or aleatorio2 == 1 or aleatorio3 == 1:
					self.disparo2.x = self.disparo1.x
					self.disparo3.x = self.disparo1.x
					self.disparo4.x = self.disparo1.x
					self.disparo5.x = self.disparo1.x
				elif aleatorio1 == 2 or aleatorio2 == 2 or aleatorio3 == 2:
					self.disparo3.x = self.disparo2.x
					self.disparo4.x = self.disparo2.x
					self.disparo5.x = self.disparo2.x
				elif aleatorio1 == 3 or aleatorio2 == 3 or aleatorio3 == 3:
					self.disparo4.x = self.disparo3.x
					self.disparo5.x = self.disparo3.x				 
				if aleatorio1 == 1 or aleatorio2 == 1 or aleatorio3 == 1:
					self.disparo1.Movimiento2_1()
				if aleatorio1 == 2 or aleatorio2 == 2 or aleatorio3 == 2:
					self.disparo2.Movimiento()
				if aleatorio1 == 3 or aleatorio2 == 3 or aleatorio3 == 3:
					self.disparo3.Movimiento2_3()
				if aleatorio1 == 4 or aleatorio2 == 4 or aleatorio3 == 4:
					self.disparo4.Movimiento2_4()
				if aleatorio1 == 5 or aleatorio2 == 5 or aleatorio3 == 5:
					self.disparo5.Movimiento2_5()
			if aleatorio1 == aleatorio2 or aleatorio1 == aleatorio3 or aleatorio2 == aleatorio3:
				recharge = True
		if level == 3:
			if recharge == True:
				aleatorio1 = randrange(1,4)
				aleatorio2 = randrange(1,4)
				aleatorio4 = randrange(1,4)
				aleatorio5 = randrange(1,4)
				self.disparo1.y = 100
				self.disparo2.y = 350
				self.disparo3.y = 600
				recharge = False
			if aleatorio1 != aleatorio2 and aleatorio4 != aleatorio5:
				if (aleatorio1 == 1 and aleatorio2 == 2) or (aleatorio1 == 2 and aleatorio2 == 1):
					self.disparo1.Movimiento()
					self.disparo2.Movimiento()
					self.disparo2.x = self.disparo1.x
				if (aleatorio1 == 1 and aleatorio2 == 3) or (aleatorio1 == 3 and aleatorio2 == 1):
					self.disparo1.Movimiento()
					self.disparo3.Movimiento()
					self.disparo3.x = self.disparo1.x
				if (aleatorio1 == 2 and aleatorio2 == 3) or (aleatorio1 == 3 and aleatorio2 == 2):
					self.disparo2.Movimiento()
					self.disparo3.Movimiento()
					self.disparo3.x = self.disparo2.x
				if (aleatorio4 == 1 and aleatorio5 == 2) or (aleatorio4 == 2 and aleatorio5 == 1):
					self.disparo6.Movimiento3()
					self.disparo7.Movimiento3()
					if self.disparo6.y < 1000:
						self.disparo7.y = self.disparo6.y
				if (aleatorio4 == 1 and aleatorio5 == 3) or (aleatorio4 == 3 and aleatorio5 == 1):
					self.disparo6.Movimiento3()
					self.disparo8.Movimiento3()
					if self.disparo6.y < 1000:
						self.disparo8.y = self.disparo6.y
				if (aleatorio4 == 2 and aleatorio5 == 3) or (aleatorio4 == 3 and aleatorio5 == 2):
					self.disparo7.Movimiento3()
					self.disparo8.Movimiento3()
					if self.disparo7.y < 1000:
						self.disparo8.y = self.disparo7.y
			if aleatorio1 == aleatorio2 or aleatorio4 == aleatorio5:
				self.disparo6.y = 0
				self.disparo7.y = 0
				self.disparo8.y = 0
				recharge = True
		if level == 4:
			if recharge == True: #randrange(1,6)
				aleatorio1 = randrange(1,6)
				aleatorio2 = randrange(1,6)
				aleatorio3 = randrange(1,6)
				aleatorio4 = randrange(1,6)
				aleatorio5 = randrange(1,6)
				aleatorio6 = randrange(1,6)
				self.disparo1.y = 100
				self.disparo2.y = 350
				self.disparo3.y = 600
				self.disparo4.y = 225
				self.disparo5.y = 475
				recharge = False
			if aleatorio1 != aleatorio2 and aleatorio1 != aleatorio3 and aleatorio2 != aleatorio3:
				if aleatorio1 == 1 or aleatorio2 == 1 or aleatorio3 == 1:
					self.disparo2.x = self.disparo1.x
					self.disparo3.x = self.disparo1.x
					self.disparo4.x = self.disparo1.x
					self.disparo5.x = self.disparo1.x
				elif aleatorio1 == 2 or aleatorio2 == 2 or aleatorio3 == 2:
					self.disparo3.x = self.disparo2.x
					self.disparo4.x = self.disparo2.x
					self.disparo5.x = self.disparo2.x
				elif aleatorio1 == 3 or aleatorio2 == 3 or aleatorio3 == 3:
					self.disparo4.x = self.disparo3.x
					self.disparo5.x = self.disparo3.x
				if aleatorio4 == 1 or aleatorio5 == 1 or aleatorio6 == 1:
					if self.disparo6.y < 1000:
						self.disparo7.y = self.disparo6.y
						self.disparo8.y = self.disparo6.y
						self.disparo9.y = self.disparo6.y
						self.disparo10.y = self.disparo6.y
				elif aleatorio4 == 2 or aleatorio5 == 2 or aleatorio6 == 2:
					if self.disparo7.y < 1000:
						self.disparo8.y = self.disparo7.y
						self.disparo9.y = self.disparo7.y
						self.disparo10.y = self.disparo7.y
				elif aleatorio4 == 3 or aleatorio5 == 3 or aleatorio6 == 3:
					if self.disparo8.y < 1000:
						self.disparo9.y = self.disparo8.y
						self.disparo10.y = self.disparo8.y			 
				if aleatorio1 == 1 or aleatorio2 == 1 or aleatorio3 == 1:
					self.disparo1.Movimiento()
				if aleatorio1 == 2 or aleatorio2 == 2 or aleatorio3 == 2:
					self.disparo2.Movimiento()
				if aleatorio1 == 3 or aleatorio2 == 3 or aleatorio3 == 3:
					self.disparo3.Movimiento()
				if aleatorio1 == 4 or aleatorio2 == 4 or aleatorio3 == 4:
					self.disparo4.Movimiento()
				if aleatorio1 == 5 or aleatorio2 == 5 or aleatorio3 == 5:
					self.disparo5.Movimiento()
				if aleatorio4 == 1 or aleatorio5 == 1 or aleatorio6 == 1:
					self.disparo6.Movimiento3()
				if aleatorio4 == 2 or aleatorio5 == 2 or aleatorio6 == 2:
					self.disparo7.Movimiento3()
				if aleatorio4 == 3 or aleatorio5 == 3 or aleatorio6 == 3:
					self.disparo8.Movimiento3()
				if aleatorio4 == 4 or aleatorio5 == 4 or aleatorio6 == 4:
					self.disparo9.Movimiento3()
				if aleatorio4 == 5 or aleatorio5 == 5 or aleatorio6 == 5:
					self.disparo10.Movimiento3()
			if aleatorio1 == aleatorio2 or aleatorio1 == aleatorio3 or aleatorio2 == aleatorio3 or aleatorio4 == aleatorio5 or aleatorio4 == aleatorio6 or aleatorio5 == aleatorio6:
				self.disparo6.y = 0
				self.disparo7.y = 0
				self.disparo8.y = 0
				self.disparo9.y = 0
				self.disparo10.y = 0
				recharge = True	

class Disparo(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas)
	
	def Movimiento(self):
		global aleatorio1, aleatorio2, recharge, level
		self.x -= 10
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 1
			self.y = 1000
		if self.x + self.ancho <= 50:
			aleatorio1 = randrange(1,4)
			aleatorio2 = randrange(1,4)
			if aleatorio1 != aleatorio2:
				self.x = 1280
				recharge = True
	
	def Movimiento2_1(self):
		global aleatorio1, aleatorio2, recharge
		self.x -= 10
		self.y += 4.5
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 1
			self.y = 1000
		if self.x + self.ancho <= 50:
			aleatorio1 = randrange(1,4)
			aleatorio2 = randrange(1,4)
			if aleatorio1 != aleatorio2:
				self.x = 1280
				recharge = True
		self.DibujarObjeto()
	
	def Movimiento2_4(self):
		global aleatorio1, aleatorio2, recharge
		self.x -= 10
		self.y += 2.25
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 1
			self.y = 1000
		if self.x + self.ancho <= 50:
			aleatorio1 = randrange(1,4)
			aleatorio2 = randrange(1,4)
			if aleatorio1 != aleatorio2:
				self.x = 1280
				recharge = True
		self.DibujarObjeto()

	def Movimiento2_3(self):
		global aleatorio1, aleatorio2, recharge
		self.x -= 10
		self.y -= 4.5
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 1
			self.y = 1000
		if self.x + self.ancho <= 50:
			aleatorio1 = randrange(1,4)
			aleatorio2 = randrange(1,4)
			if aleatorio1 != aleatorio2:
				self.x = 1280
				recharge = True
		self.DibujarObjeto()
	
	def Movimiento2_5(self):
		global aleatorio1, aleatorio2, recharge
		self.x -= 10
		self.y -= 2.25
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 1
			self.y = 1000
		if self.x + self.ancho <= 50:
			aleatorio1 = randrange(1,4)
			aleatorio2 = randrange(1,4)
			if aleatorio1 != aleatorio2:
				self.x = 1280
				recharge = True
		self.DibujarObjeto()
	
	def Movimiento3(self):
		global aleatorio1, aleatorio2, recharge, level
		self.y += 5.6
		if Personaje.check_colisiones(self, plataforma) == True:
			plataforma.vidas -= 1
			self.y = 1000
		self.DibujarObjeto()

plataforma = Personaje(50, 260, 200, 200,(0,0,0), 3)
fantasma = transform.scale(image.load("nuss_images/fantasma.png"), (200, 200))
fantasma2 = transform.scale(image.load("nuss_images/fantasma2.png"), (200, 200))
fantasma3 = transform.scale(image.load("nuss_images/fantasma3.png"), (200, 200))
nube = transform.scale(image.load("nuss_images/nube.png"), (600, 600))
rayo = transform.scale(image.load("nuss_images/rayo.png"), (300, 300))
sol = transform.scale(image.load("nuss_images/sol.png"), (600, 600))
fuego = transform.scale(image.load("nuss_images/fuego.png"), (150, 150))
luna = transform.scale(image.load("nuss_images/luna.png"), (600, 600))
meteorito1 = transform.scale(image.load("nuss_images/meteorito1.png"), (300, 300))
meteorito2 = transform.scale(image.load("nuss_images/meteorito2.png"), (300, 300))
alien = transform.scale(image.load("nuss_images/alien.png"), (600, 600))
ovni = transform.scale(image.load("nuss_images/ovni.png"), (150, 150))
boss = Boss(1000, 30, 250, 600, (255,255,255), 1)
barra = Barra(340, 25, 0, 25,(166, 215, 255), 3)
barra_bg = transform.scale(image.load("nuss_images/barra_bg.png"), (625, 25))
nube_icon = transform.scale(image.load("nuss_images/nube_icon.png"), (40, 40))
sol_icon = transform.scale(image.load("nuss_images/sol_icon.png"), (40, 40))
luna_icon = transform.scale(image.load("nuss_images/luna_icon.png"), (40, 40))
ovni_icon = transform.scale(image.load("nuss_images/ovni_icon.png"), (40, 40))
victoria = transform.scale(image.load("nuss_images/victoria.png"), (1000, 540))
z = 0
animacion_boss = 0

while not done:
	global timer, plus_timer, aleatorio1, aleatorio2, aleatorio3, aleatorio4, aleatorio5, aleatorio6, level, recharge
	for evento in event.get():
		if evento.type == QUIT:
			done = True
		elif evento.type == KEYDOWN:
			if evento.key == K_ESCAPE:
				done = True
			if evento.key == K_DOWN:
				level = 2
			if evento.key == K_UP:
				level = 3
			if evento.key == K_RIGHT:
				level = 4
			if evento.key == K_LEFT:
				level = 5
	if z == 0:
		timer = 0
		plus_timer = False
		aleatorio1 = randrange(1,4)
		aleatorio2 = randrange(1,4)
		level = 1
		recharge = True
		if aleatorio1 != aleatorio2:
			z = 1
	if level == 2 and z == 1:
		fantasma = transform.scale(image.load("nuss_images/fantasma.png"), (100, 100))
		fantasma2 = transform.scale(image.load("nuss_images/fantasma2.png"), (100, 100))
		fantasma3 = transform.scale(image.load("nuss_images/fantasma3.png"), (100, 100))
		background = transform.scale(image.load("nuss_images/background_sunset.png").convert(), (3480, 720))
		plataforma.y = 310
		plataforma.ancho = 100
		plataforma.largo = 100
		boss.disparo1.ancho = 25
		boss.disparo1.largo = 25
		boss.disparo2.ancho = 25
		boss.disparo2.largo = 25
		boss.disparo3.ancho = 25
		boss.disparo3.largo = 25
		barra.color = (249,192,49)
		aleatorio3 = randrange(1,6)
		z = 2
	if level == 3 and z == 2:
		fantasma = transform.scale(image.load("nuss_images/fantasma.png"), (200, 200))
		fantasma2 = transform.scale(image.load("nuss_images/fantasma2.png"), (200, 200))
		fantasma3 = transform.scale(image.load("nuss_images/fantasma3.png"), (200, 200))
		background = transform.scale(image.load("nuss_images/background_night.png").convert(), (3480, 720))
		plataforma.y = 260
		plataforma.x = 250
		plataforma.ancho = 200
		plataforma.largo = 200
		boss.disparo1.ancho = 50
		boss.disparo1.largo = 50
		boss.disparo2.ancho = 50
		boss.disparo2.largo = 50
		boss.disparo3.ancho = 50
		boss.disparo3.largo = 50
		boss.disparo1.y = 100
		boss.disparo2.y = 350
		boss.disparo3.y = 600
		aleatorio1 = 1
		aleatorio2 = 3
		aleatorio4 = 1
		aleatorio5 = 3
		recharge = True
		barra.color = (110,1,219)
		if aleatorio4 != aleatorio5:
			z = 3
	if level == 4 and z == 3:
		fantasma = transform.scale(image.load("nuss_images/fantasma.png"), (100, 100))
		fantasma2 = transform.scale(image.load("nuss_images/fantasma2.png"), (100, 100))
		fantasma3 = transform.scale(image.load("nuss_images/fantasma3.png"), (100, 100))
		background = transform.scale(image.load("nuss_images/background_space.png").convert(), (3480, 720))
		plataforma.y = 310
		plataforma.x = 50
		plataforma.ancho = 100
		plataforma.largo = 100
		boss.disparo1.ancho = 25
		boss.disparo1.largo = 25
		boss.disparo2.ancho = 25
		boss.disparo2.largo = 25
		boss.disparo3.ancho = 25
		boss.disparo3.largo = 25
		boss.disparo6.ancho = 25
		boss.disparo6.largo = 25
		boss.disparo6.x = 75
		boss.disparo7.ancho = 25
		boss.disparo7.largo = 25
		boss.disparo7.x = 375
		boss.disparo8.ancho = 25
		boss.disparo8.largo = 25
		boss.disparo8.x = 675
		aleatorio3 = randrange(1,6)
		aleatorio6 = randrange(1,6)
		recharge = True
		barra.color = (0,228,55)
		z = 4
	if level == 5 and z == 4:
		fantasma = transform.scale(image.load("nuss_images/fantasma.png"), (200, 200))
		fantasma2 = transform.scale(image.load("nuss_images/fantasma2.png"), (200, 200))
		fantasma3 = transform.scale(image.load("nuss_images/fantasma3.png"), (200, 200))
		plataforma.x = 50
		plataforma.y = 260
		z = 5
	x_relativa = x % 3480
	screen.blit(background, [x_relativa - 3480, 0])
	screen.blit(background, [x_relativa, 0])
	x -= 1
	animacion_boss += 1
	plataforma.Movimiento()
	if barra.ancho >= 20:
		boss.Disparar()
	barra.ancho += 0.125
	if level != 5:
		barra.DibujarObjeto()
		screen.blit(barra_bg, [340, 25])
	if level == 1:
		if aleatorio1 == 1 or aleatorio2 == 1:
			screen.blit(rayo, [boss.disparo1.x-125, boss.disparo1.y-125])
		if aleatorio1 == 2 or aleatorio2 == 2:
			screen.blit(rayo, [boss.disparo2.x-125, boss.disparo2.y-125])
		if aleatorio1 == 3 or aleatorio2 == 3:
			screen.blit(rayo, [boss.disparo3.x-125, boss.disparo3.y-125])
		screen.blit(nube, [700, boss.y])
		screen.blit(nube_icon, [barra.x + barra.ancho - 40, barra.y-10])
	if level == 2:
		if aleatorio1 == 1 or aleatorio2 == 1 or aleatorio3 == 1:
			screen.blit(fuego, [boss.disparo1.x-62.5, boss.disparo1.y-75])
		if aleatorio1 == 2 or aleatorio2 == 2 or aleatorio3 == 2:
			screen.blit(fuego, [boss.disparo2.x-62.5, boss.disparo2.y-75])
		if aleatorio1 == 3 or aleatorio2 == 3 or aleatorio3 == 3:
			screen.blit(fuego, [boss.disparo3.x-62.5, boss.disparo3.y-75])
		if aleatorio1 == 4 or aleatorio2 == 4 or aleatorio3 == 4:
			screen.blit(fuego, [boss.disparo4.x-62.5, boss.disparo4.y-75])
		if aleatorio1 == 5 or aleatorio2 == 5 or aleatorio3 == 5:
			screen.blit(fuego, [boss.disparo5.x-62.5, boss.disparo5.y-75])
		screen.blit(sol, [700, boss.y])
		screen.blit(sol_icon, [barra.x + barra.ancho - 40, barra.y-10])
	if level == 3:
		if aleatorio1 == 1 or aleatorio2 == 1:
			screen.blit(meteorito1, [boss.disparo1.x-125, boss.disparo1.y-125])
		if aleatorio1 == 2 or aleatorio2 == 2:
			screen.blit(meteorito2, [boss.disparo2.x-125, boss.disparo2.y-125])
		if aleatorio1 == 3 or aleatorio2 == 3:
			screen.blit(meteorito1, [boss.disparo3.x-125, boss.disparo3.y-125])
		if aleatorio4 == 1 or aleatorio5 == 1:
			screen.blit(meteorito2, [boss.disparo6.x-125, boss.disparo6.y-125])
		if aleatorio4 == 2 or aleatorio5 == 2:
			screen.blit(meteorito1, [boss.disparo7.x-125, boss.disparo7.y-125])
		if aleatorio4 == 3 or aleatorio5 == 3:
			screen.blit(meteorito2, [boss.disparo8.x-125, boss.disparo8.y-125])
		screen.blit(luna, [700, boss.y])
		screen.blit(luna_icon, [barra.x + barra.ancho - 40, barra.y-10])
	if level == 4:
		if aleatorio1 == 1 or aleatorio2 == 1 or aleatorio3 == 1:
			screen.blit(ovni, [boss.disparo1.x-62.5, boss.disparo1.y-75])
		if aleatorio1 == 2 or aleatorio2 == 2 or aleatorio3 == 2:
			screen.blit(ovni, [boss.disparo2.x-62.5, boss.disparo2.y-75])
		if aleatorio1 == 3 or aleatorio2 == 3 or aleatorio3 == 3:
			screen.blit(ovni, [boss.disparo3.x-62.5, boss.disparo3.y-75])
		if aleatorio1 == 4 or aleatorio2 == 4 or aleatorio3 == 4:
			screen.blit(ovni, [boss.disparo4.x-62.5, boss.disparo4.y-75])
		if aleatorio1 == 5 or aleatorio2 == 5 or aleatorio3 == 5:
			screen.blit(ovni, [boss.disparo5.x-62.5, boss.disparo5.y-75])
		if aleatorio4 == 1 or aleatorio5 == 1 or aleatorio6 == 1:
			screen.blit(ovni, [boss.disparo6.x-62.5, boss.disparo6.y-75])
		if aleatorio4 == 2 or aleatorio5 == 2 or aleatorio6 == 2:
			screen.blit(ovni, [boss.disparo7.x-62.5, boss.disparo7.y-75])
		if aleatorio4 == 3 or aleatorio5 == 3 or aleatorio6 == 3:
			screen.blit(ovni, [boss.disparo8.x-62.5, boss.disparo8.y-75])
		if aleatorio4 == 4 or aleatorio5 == 4 or aleatorio6 == 4:
			screen.blit(ovni, [boss.disparo9.x-62.5, boss.disparo9.y-75])
		if aleatorio4 == 5 or aleatorio5 == 5 or aleatorio6 == 5:
			screen.blit(ovni, [boss.disparo10.x-62.5, boss.disparo10.y-75])
		screen.blit(alien, [700, boss.y])
		screen.blit(ovni_icon, [barra.x + barra.ancho - 40, barra.y-10])
	if level == 5:
		screen.blit(victoria, [250, 100])
		barra.ancho = 0
	if plataforma.vidas == 3:
		screen.blit(fantasma, [plataforma.x, plataforma.y])
	if plataforma.vidas == 2:
		screen.blit(fantasma2, [plataforma.x, plataforma.y])
	if plataforma.vidas == 1:
		screen.blit(fantasma3, [plataforma.x, plataforma.y])
	if barra.ancho >= 600:
		level += 1
		barra.ancho = 0
	if plataforma.vidas <= 0:
		done = True
	display.flip()
	clock.tick(60)
quit()
