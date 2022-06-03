#####################################

# Title: Christmastime Is Here 
# Date: November 5, 2021
# Programmer: Anika Sharma
# Description: Indoor Christmas scene 

#####################################


# Imports
from tkinter import *
from time import sleep
from random import randint, choice
from math import sin
from decimaltohex import getColour

# Screen setup
s = Canvas(Tk(), width = 600, height = 400, background = "white")
s.pack()



###############
# BACKGROUND #
###############

# The wall #

# Starting colour 
r1 = 255
g1 = 250
b1 = 230

# Ending colour 
r2 = 210
g2 = 180
b2 = 255

# Figuring out the changing rates of the colours
dr = (r2-r1)/350
dg = (g2-g1)/350
db = (b2-b1)/350

for line in range(350):
	r = round(r1 + line*dr) 
	g = round(g1 + line*dg)
	b = round(b1 + line*db)
	c = getColour(r, g, b)

	s.create_rectangle(0,line, 600,line+1, fill = c, outline = "")


# Painting on the wall
painting = PhotoImage(file = "img.ppm")
s.create_image(100,105, image = painting)


# Lining of the wall
s.create_rectangle(0,330, 600,350, fill = "grey99", outline = "grey93")
s.create_line(0,338, 600,338, fill = "grey93")
s.create_line(0,342, 600,342, fill = "grey93")


# Floor
s.create_rectangle(0,350, 600,400, fill = "brown4", outline = "")
xl = 50
for floorline in range(12):
  s.create_line(xl,350, xl-25,400, fill = "brown")
  xl += 50


# Power outlet and plug+wire for Christmas Lights
s.create_rectangle(50,300, 70,325, fill = "grey97", outline = "grey93")
s.create_oval(53,305, 67,315, fill = "black")
s.create_line(60,310, 60,360, 175,360, fill = "black", width = 3, smooth = True)



# WINDOW #

# Main window
s.create_rectangle(325,0, 575,150, fill = "grey90", outline = "brown", width = 10)
s.create_rectangle(330,125, 570,145, fill = "snow", outline = "")

# Window lines
def windowLines():
  s.create_line(450,0, 450,150, fill = "brown", width = 5)
  s.create_line(325,75, 575,75, fill = "brown", width = 5)



# SNOWMAN #
def snowman():
  # Head
  s.create_oval(475,50, 500,75, fill = "white", outline = "")

  # Eyes
  s.create_oval(480,55, 482,57, fill = "black")
  s.create_oval(487,55, 489,57, fill = "black")

  # Nose
  s.create_polygon(487,60, 487,65, 475,63, fill = "orange")

  # Mouth
  s.create_line(477,67, 480,70, 490,70, 495,67)

  # Hands
  s.create_line(475,85, 460,75, fill = "brown", width = 2)
  s.create_line(500,85, 515,75, fill = "brown", width = 2)

  # Body
  s.create_oval(473,75, 502,102, fill = "white", outline = "")

  # Buttons
  s.create_oval(485,80, 487,82, fill = "black")
  s.create_oval(485,85, 487,87, fill = "black")
  s.create_oval(485,90, 487,92, fill = "black")

  # Bottom
  s.create_oval(472,100, 503,127, fill = "white", outline = "")

  # Hat 
  s.create_polygon(475,50, 500,50, 500,47, 497,47, 497,35, 478,35, 478,47, 475,47, fill = "black")

snowman()
windowLines()



# SOCKS #

# Ledge
s.create_line(365,200, 540,200, fill = "coral4", width = 10)

# 3 Socks
sockx = 390
for sock in range(3):
	s.create_rectangle(sockx,205, sockx+25,250, fill = "red", outline = "")
	s.create_oval(sockx-20,225, sockx+15,250, fill = "red", outline = "")
	s.create_rectangle(sockx,200, sockx+25,210, fill = "white", outline = "")
	s.create_oval(sockx+10,198, sockx+15,203, outline = "red")

	sockx += 50



# TABLE #
s.create_rectangle(350,325, 500,340, fill = "sienna4", outline = "")
s.create_rectangle(350,325, 365,400, fill = "sienna4", outline = "")
s.create_rectangle(485,325, 500,400, fill = "sienna4", outline = "")
s.create_rectangle(510,300, 525,375, fill = "sienna4", outline = "")
s.create_rectangle(375,300, 390,375, fill = "sienna4", outline = "")
s.create_polygon(500,335, 525,310, 525,300, 375,300, 350,325, fill = "sienna4", outline = "")



# HOT CHOCOLATE #

# Mug with hot chocolate and handle
s.create_rectangle(455,275, 490,325, fill = "azure2", outline = "")
s.create_oval(455,265, 490,280, fill = "azure2", outline = "azure")
s.create_oval(455,320, 490,330, fill = "azure2", outline = "")

s.create_arc(455,265, 490,280, start = 0, extent = -180, fill = "chocolate", outline = "")

s.create_oval(470,290, 500,310, fill = "", outline = "azure2", width = 5)



# PLATE WITH COOKIES #
s.create_oval(375,310, 445,330, fill = "mint cream", outline = "")
s.create_oval(378,315, 440,325, outline = "azure2")
for cookie in range(5):
	cx = randint(390,420)
	cy = randint(310,320)
	s.create_oval(cx,cy, cx+20,cy+10, fill = "sienna1", outline = "sienna4")



# TREE #

# Carpet
s.create_oval(75,350, 275,400, fill = "red", outline = "gold", width = 3)

# Leaves
tip = 50
x1 = 125
x2 = 225
y = 125
for leaves in range(5):
  s.create_polygon(175,tip, x1,y, x2,y, fill = "dark green")
  tip += 15 
  x1 -= 15
  y += 50
  x2 += 15 


# Trunk
s.create_rectangle(150,325, 200,375, fill = "saddle brown", outline = "")


# Star
s.create_polygon(175,25, 175,50, 195,65, fill = "gold")
s.create_polygon(175,25, 175,50, 155,65, fill = "gold")
s.create_polygon(150,40, 175,50, 200,40, fill = "gold")



# Decor on tree

# Tree ribbons and ornaments
tip = 50
x1 = 125
x2 = 225
y = 125
colours = ["red", "gold", "silver"]
for line in range(5): 
	
	# Ribbons
	xpoint = x1 + ((175-x1)/2) - 10*line
	ypoint = tip + ((y-tip)/2) + 20*line
	s.create_line(xpoint,ypoint, 175,y-20, x2,y, fill = "gold", width = 3)

	# Ornaments
	s.create_oval(x1-5,y-10, x1+15,y+10, fill = choice(colours), outline = "")
	s.create_oval(x2-15,y-10, x2+5,y+10, fill = choice(colours), outline = "")

	# Increments
	tip += 15 
	x1 -= 15
	y += 50
	x2 += 15 



# PRESENTS #
presentcols = ["orange", "yellow", "lightgreen", "blue", "purple"]

for present in range(4):
  # Present coords and vals
  xp = randint(80,265)
  yp = randint(350,375)

  size = randint(25,50)
  ribbonc = choice(["lightpink", "ivory2", "plum"])
  
  halfxp = xp+(size/2)
  halfyp = yp+(size/2)

  # Creating present box with 2 ribbons
  s.create_rectangle(xp,yp, xp+size, yp+size, fill = choice(presentcols), outline = "")
  s.create_line(halfxp,yp, halfxp,yp+size, fill = ribbonc, width = 3)
  s.create_line(xp,halfyp, xp+size,halfyp, fill = ribbonc, width = 3)

  # Ribbon top
  s.create_polygon(halfxp,yp, xp,yp-10, xp+(size/4),yp-15, halfxp,yp-10, fill = "", outline = ribbonc, width = 3, smooth = True)
  s.create_polygon(halfxp,yp, xp+size,yp-10, (xp+size)-(size/4),yp-15, halfxp,yp-10, fill = "", outline = ribbonc, width = 3, smooth = True)






#####################
# ANIMATION #
#####################

# ARRAYS #

# Snow
snowx = []
snowy = []
sizes = []
speeds = []
snow = []

# Lights
xvals = []
yvals = []
colors = []
lights = []
lightspeed = 0

# Steam from hot chocolate
xsteam = 460
ysteam = 260
steam = []
f = 0


# FILLING ARRAYS #
for filling in range(300):

	# Snow
	snowx.append(randint(330,560))
	snowy.append(randint(10,125))
	sizes.append(randint(2,5))
	speeds.append(randint(2,7))  
	snow.append(0)

	# Lights
	xvals.append(randint(90,250))
	yvals.append(randint(55,315))
	colors.append(choice(["red", "yellow", "blue", "green2"]))
	lights.append(0)



# MAIN LOOP #
while True:

	# For snow and lights
	for i in range(300):

		# SNOW #
		snow[i] = s.create_oval(snowx[i],snowy[i], snowx[i]+sizes[i], snowy[i]+sizes[i], fill = "snow", outline = "")

		# Creating the window over the snow
		windowLines()

		# Making each snow fall at a different speed
		snowy[i] += speeds[i]

		# Resetting the snow to stay in the window
		if snowy[i] >= 135:
			snowy[i] = 10



		# LIGHTS #
		# If the light y value is greater than two lines of the tree, create the light
		if yvals[i] > (2.6*xvals[i]-400) and yvals[i] > (-2.6*xvals[i]+500):
			s.create_oval(xvals[i],yvals[i], xvals[i]+5,yvals[i]+5, fill = colors[i], outline = "")


	# STEAM #

	# Coordinates
	x = xsteam + 5*sin(0.2*f)
	y = ysteam - f

	# Making the 3 lines
	ball1 = s.create_oval(x,y, x+3,y+3, fill = "grey90", outline = "")
	ball2 = s.create_oval(x+10,y, x+13,y+3, fill = "grey90", outline = "")
	ball3 = s.create_oval(x+20,y, x+23,y+3, fill = "grey90", outline = "")

	# Putting all steam into the array
	steam.append(ball1)
	steam.append(ball2)
	steam.append(ball3)

	# Resetting the steam
	if y <= 210:
		y = 260
		f = 0
		for thing in steam:
			s.delete(thing)

	# Not resetting the steam
	else:
		f += 1



	# For the lights changing colours at a different time from snow
	if lightspeed % 10 == 0:
		colors = []
		for colour in range(300):
			colors.append(choice(["red", "yellow", "blue", "green2"]))
	lightspeed += 1



	# Update, sleep, delete
	s.update()
	sleep(0.03)
	for item in range(300):
		s.delete(snow[item], lights[item]) 