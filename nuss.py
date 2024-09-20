from pygame import*
from random import*
w = 1280
h = 720
x = 0
screen = display.set_mode((w, h), FULLSCREEN)
clock = time.Clock()
done = False
background = transform.scale(image.load("nuss_images/background_day.png").convert(), (3480, 720))
background = transform.scale(image.load("nuss_images/background_sunset.png").convert(), (3480, 720))
#background = transform.scale(image.load("nuss_images/background_day.png").convert(), (3480, 720))

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
		if plus_timer == True:
			timer += 1
			if timer == 20:
				timer = 0
				plus_timer = False
		self.DibujarObjeto()

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

	def Movimiento(self):
		self.DibujarObjeto()

	def Disparar(self):
		global level, aleatorio1, aleatorio2, aleatorio3, recharge
		if level == 1:
			if recharge == True:
				aleatorio1 = randrange(1,4)
				aleatorio2 = randrange(1,4)
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
			if recharge == True:
				aleatorio1 = randrange(1,6)
				aleatorio2 = 2
				aleatorio3 = randrange(1,6)
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
					self.disparo1.Movimiento()
				if aleatorio1 == 2 or aleatorio2 == 2 or aleatorio3 == 2:
					self.disparo2.Movimiento()
				if aleatorio1 == 3 or aleatorio2 == 3 or aleatorio3 == 3:
					self.disparo3.Movimiento()
				if aleatorio1 == 4 or aleatorio2 == 4 or aleatorio3 == 4:
					self.disparo4.Movimiento()
				if aleatorio1 == 5 or aleatorio2 == 5 or aleatorio3 == 5:
					self.disparo5.Movimiento()
			if aleatorio1 == aleatorio2 or aleatorio1 == aleatorio3 or aleatorio2 == aleatorio3:
				recharge = True
				

class Disparo(Objeto):
	def __init__(self, x, y, ancho, largo, color , vidas):
		Objeto.__init__(self, x, y, ancho, largo, color, vidas)
	
	def Movimiento(self):
		global aleatorio1, aleatorio2, recharge, level
		if level == 1:
			self.x -= 10
			if self.x + self.ancho <= 50:
				aleatorio1 = randrange(1,4)
				aleatorio2 = randrange(1,4)
				if aleatorio1 != aleatorio2:
					self.x = 1280
					recharge = True
		if level == 2:
			if self.x == 1280:
				if self.y == 100:
					self.y = 600
				if self.y == 225:
					self.y = 475
				if self.y == 225:
					self.y = 475
				if self.y == 600:
					self.y = 100
			self.x -= 10
			self.y += 2.1
			if self.x + self.ancho <= 50:
				aleatorio1 = randrange(1,4)
				aleatorio2 = randrange(1,4)
				if aleatorio1 != aleatorio2:
					self.x = 1280
					recharge = True
		self.DibujarObjeto()

plataforma = Personaje(50, 260, 200, 200,(0,0,0), 3)
fantasma = transform.scale(image.load("nuss_images/fantasma.png"), (200, 200))
nube = transform.scale(image.load("nuss_images/nube.png"), (600, 600))
rayo = transform.scale(image.load("nuss_images/rayo.png"), (300, 300))
sol = transform.scale(image.load("nuss_images/sol.png"), (600, 600))
fuego = transform.scale(image.load("nuss_images/fuego.png"), (150, 150))
boss = Boss(1000, 30, 250, 600, (255,255,255), 1)
z = 0

while not done:
	global timer, plus_timer, aleatorio1, aleatorio2, level, recharge
	for evento in event.get():
		if evento.type == QUIT:
			done = True
		elif evento.type == KEYDOWN:
			if evento.key == K_ESCAPE:
				done = True
	if z == 0:
		timer = 0
		plus_timer = False
		aleatorio1 = randrange(1,4)
		aleatorio2 = randrange(1,4)
		level = 2
		recharge = True
		if aleatorio1 != aleatorio2:
			z = 1
	if level == 2 and z == 1:
		fantasma = transform.scale(image.load("nuss_images/fantasma.png"), (100, 100))
		plataforma.y = 310
		plataforma.ancho = 100
		plataforma.largo = 100
		boss.disparo1.ancho = 25
		boss.disparo1.largo = 25
		boss.disparo2.ancho = 25
		boss.disparo2.largo = 25
		boss.disparo3.ancho = 25
		boss.disparo3.largo = 25
		aleatorio3 = randrange(1,6)
		z = 2
	x_relativa = x % 3480
	plataforma.Movimiento()
	screen.blit(background, [x_relativa - 3480, 0])
	screen.blit(background, [x_relativa, 0])
	x -= 1
	boss.Disparar()
	if level == 1:
		if aleatorio1 == 1 or aleatorio2 == 1:
			screen.blit(fuego, [boss.disparo1.x-125, boss.disparo1.x-125])
		if aleatorio1 == 2 or aleatorio2 == 2:
			screen.blit(rayo, [boss.disparo2.x-125, boss.disparo2.y-125])
		if aleatorio1 == 3 or aleatorio2 == 3:
			screen.blit(rayo, [boss.disparo3.x-125, boss.disparo3.y-125])
	if level == 2:
		if aleatorio1 == 1 or aleatorio2 == 1 or aleatorio3 == 1:
			screen.blit(fuego, [boss.disparo1.x-62.5, boss.disparo1.x-75])
		if aleatorio1 == 2 or aleatorio2 == 2 or aleatorio3 == 2:
			screen.blit(fuego, [boss.disparo2.x-62.5, boss.disparo2.x-75])
		if aleatorio1 == 3 or aleatorio2 == 3 or aleatorio3 == 3:
			screen.blit(fuego, [boss.disparo3.x-62.5, boss.disparo3.y-75])
		if aleatorio1 == 4 or aleatorio2 == 4 or aleatorio3 == 4:
			screen.blit(fuego, [boss.disparo4.x-62.5, boss.disparo4.y-75])
		if aleatorio1 == 5 or aleatorio2 == 5 or aleatorio3 == 5:
			screen.blit(fuego, [boss.disparo5.x-62.5, boss.disparo5.y-75])
	screen.blit(fantasma, [plataforma.x, plataforma.y])
	screen.blit(sol, [700, boss.y])
	display.flip()
	clock.tick(60)
quit()