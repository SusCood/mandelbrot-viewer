import pygame
pygame.init()


C = complex(-0.6,0.4)
POWER = 2
ITERATIONS = 200 
MAX_ITERS  = 50
GRAY  = (100,100,100)
DISPLAY = WIDTH,HEIGHT = 800,600
SCALED_WIDTH  = 4
SCALE_RATIO   = WIDTH/SCALED_WIDTH
SCALED_HEIGHT = HEIGHT/SCALE_RATIO 

current_colour = pygame.Color(0,0,0)	# initialised as black
current_colour.hsla = (0,100,50,100)

screen = pygame.display.set_mode(DISPLAY)
pygame.display.set_caption("The Julia Set")
screen.fill(GRAY)


for pygame_original_x in range(WIDTH):
	# convert pygame_x to a graphical_x
	original_x = pygame_original_x - WIDTH//2
	scaled_x = original_x/SCALE_RATIO

	for pygame_original_y in range(HEIGHT):
		# convert pygame_y to a graphical_y
		original_y = (HEIGHT//2) - pygame_original_y
		scaled_y = original_y/SCALE_RATIO

		z = complex(scaled_x,scaled_y)

		for i in range(ITERATIONS):
			z = pow(z, POWER) + C

			if abs(z.real) > 2 or abs(z.imag) > 2:
				exited_at = i
				# now, map iterations exited at to a number in the range 0-255 for a hue value
				# let's assume > MAX_ITERS iters corresponds to blue colour

				if i > MAX_ITERS: 
					current_colour.hsla = (255,100,50,100)	# BLUE
				else: 
					hue_value = (1 - (i/MAX_ITERS)) * 255	# only the hue differs, changing the entire colour scale
					# 1 - fraction for bluish background, fraction only for reddish background (cooler imo :/)
					current_colour.hsla = (hue_value, 100, 50, 100)

				break
		else:
			current_colour.hsla = (0,100,0,100)				# BLACK

		screen.set_at((pygame_original_x, pygame_original_y), current_colour)

	pygame.display.flip()

pygame.image.save(screen,f"julia_{C.real}+{C.imag}_{POWER}_{MAX_ITERS}_{ITERATIONS}.png")
