# Generative art with Turtle, based on user input
# Eindopdracht Programmeren, Blok 1, 2021, HvA, Mark Westerweel     versie: 1.0

##############################################
# TO DO:
# Collect all answers and store in list / tuple and build the artpiece from the list. == Edits and shows information from minimal 1 list
# Use FLOAT datatype to determin starting point pen.
# Refactor for coding conventions.
# Defensive coding to ensure quality data input && 
# format data as final string (
#    final_string = "Looks like {} came together quite nicely! You used a {} background with {} outling and {} fillings."
#   print(final_string.format(name_artpiece, background, outline, filling)))   


# DONE:
# Uses Integers and Bool (if/else))
# Read and edit user input
# Writes information to the output.
# Uses functions (TO DO: each block in a function)
# Uses modules (Turtle, random, time)
# 
###############################################

import turtle, random, time # at least 2 modules imported

from turtle import *

# Ask how user wants to name the art piece. 
print("   _____ ___________________________________.___.   __  .__             _______________ ________________________.____     ___________")
print("  /  _  \\______   \__    ___/   _____/\__  |   | _/  |_|  |__   ____   \__    ___/    |   \______   \__    ___/|    |    \_   _____/")
print(" /  /_\  \|       _/ |    |  \_____  \  /   |   | \   __\  |  \_/ __ \    |    |  |    |   /|       _/ |    |   |    |     |    __)_ ")
print("/    |    \    |   \ |    |  /        \ \____   |  |  | |   Y  \  ___/    |    |  |    |  / |    |   \ |    |   |    |___  |        \ ")
print("\____|__  /____|_  / |____| /_______  / / ______|  |__| |___|  /\___  >   |____|  |______/  |____|_  / |____|   |_______ \/_______  /")
print("        \/       \/                 \/  \/                   \/     \/                             \/                   \/        \/ ")
time.sleep(1.5)
print('                         Hello! My name is Artoise, I am your little artist turtle for today.')
time.sleep(1.5)
print("                         Today YOU and I are going to draw something together! ")
time.sleep(1.5)
print("                         Mind if I ask you some questions before we make an artpiece together?")



def art_name ():
    
    # print('\n First we need a name, have you thought about any? (pls provide a name for now)')
    # will do yes/no boolean and use input or go with a standard one like ... and Artoise . 
    name_artpiece = input('                         First we need a name for the project, have you thought about any? (pls provide a name for now)')
    
    if name_artpiece.isalpha() == True:
        turtle.title(name_artpiece)
        print('                 Splendid! I think', name_artpiece, 'is a wonderful name...')
        print("                 Some more questions and let's check out the canvas in the other window and let's rock!")
         
    else : 
        print("                 Ehr... Unless you're Elon Musk, we name our produce with letters only... you know, with words...")
        print('                 So you got a name?')
        name_artpiece = input()
        if name_artpiece.isalpha() :
            turtle.title(name_artpiece)
            print('             Thank you for getting along with the program!')
        else : 
            print("             Yeah, when you're not in THAT mood, start the program again...")
            exit()
            # CAN USE WHILE LOOP INSTEAD OF EXIT
    return name_artpiece

name_artpiece = art_name()

   
# coloring options
def colors () :
    background = input('                What colour do you want to the background to be? ') #add random 
    outline = input('               What colour would you use for the outlining?') 
    fill = input('What about the filling?')
    
    return background, outline, fill

background, outline, fill = colors()   


#list with sets for size and starting point.

canvasSizes = [[600, 400, 90.5, 0.5], [800, 600, 100, 0.5],[1200, 800, 100, 0.5]]

## IF USER WANTS TO CHANGE THE POSITION OF THE PEN, alter list with float canvas[3]
# starting_point = input('Do you want to start the drawing NOT from the middle, if so, provide floats for X and Y')

# arguments are canvassize and starting point
size = input('What canvas size would you like? We got "small", "medium" or "large"...')
# refactor for limited cognitive complexity
if size == "small" :
    canvas = turtle.Screen()
    canvas.setup(width=canvasSizes[0][0], height=canvasSizes[0][1], startx=canvasSizes[0][2], starty=canvasSizes[0][3])
elif size == "medium" :
    canvas = turtle.Screen() 
    canvas.setup(width=canvasSizes[1][0], height=canvasSizes[1][1], startx=canvasSizes[1][2], starty=canvasSizes[1][3])
elif size == "large" :
    canvas = turtle.Screen() 
    canvas.setup(width=canvasSizes[2][0], height=canvasSizes[2][1], startx=canvasSizes[2][2], starty=canvasSizes[2][3])



# pen = turtle.Turtle() 
# pen.shape("turtle")
# # options for pen skin and / or size

# pen.shapesize(1)
# pen.fillcolor('red') # change color of pen
# pen.pencolor('blue') # change color of outline 
# bruch.color('red', 'blue') # change color of both pen and gives it an outline

# scale of artwork compared to canvas
# scale = 10
# # pen up is like lifting the pen in real life
# pen.penup()
# #putting th pen left side of the screen, in the middle.
# pen.setpos(-300, 0)
# # is like putting the pen down and draw.
# pen.pendown()

# 
# pen.color('red', 'yellow')
# pen.begin_fill()
# pen.end_fill()

#########################################################################
# CIRCLES
#########################################################################

circles = input("How many circles would you like?")
print("Check out the canvas in the other window")
time.sleep(3)

end_range = int(circles) 
seen = set()

turtle.color(outline, fill) #input
turtle.bgcolor(background)
turtle.begin_fill()

for steps in range(1, end_range):
    print('Drawing...')
    turtle.circle(random.randint(0,100))
    turtle.left(random.randint(25,90))
    
turtle.end_fill()
    
    # if end_range == end_range : save_drawing()
    # add time delay


#########################################################################
# HALF CIRCLE DRAWING // Need to customize it 
#########################################################################


# current = 0  
# seen = set()
# #loop over sequence
# for step_size in range(1, 100):
#     backwards = current - step_size
    
#     # makes increasingly bigger half circles to the left. 
#     if backwards > 0 and backwards not in seen:
#         #set heading = 
#         pen.setheading(90)
#         pen.circle(scale * step_size/2, 180)
#         current = backwards 
#         seen.add(current)
#     # Makes a right bottom circle if backward is not in sequence 
#     else:
#         pen.setheading(270) 
#         pen.circle(scale * step_size/2, 180)
#         current += step_size
#         seen.add(current)

#########################################################################
# SAVE TO FILE 
#########################################################################

ts = turtle.getscreen()
filename = name_artpiece +'.eps'
ts.getcanvas().postscript(file=filename)
print('Your file is stored under ' + filename)
time.sleep(1.5)
print('Well, see you around for the next piece!')
time.sleep(2.5) 
exit = input("exit?")
if exit == True : turtle.bye()


# TRYING TO SAVE TO .png (to no avail without CLI  -- Imagemagick)

# from PIL import EpsImagePlugin, Image
# EpsImagePlugin.gs_windows_binary =  r'X:\...\gs\gs9.52\bin\gswin64c'
# im = Image.open('test.eps')
# im.save('test.png')








# import convertapi

# convertapi.api_secret = 'zkNv7WQH38gG8Ek5'
# convertapi.convert('jpg', {
#     'File': '/path/to/my_file.eps'
# }, from_format = 'eps').save_files('/path/to/dir')

# eps_image.save('a.jpg')

# eps_image = Image.open('example.eps')
# # Rasterise onto 4x higher resolution grid
# eps_image.load(scale=4)   
# eps_image.save('a.jpg') 


# turtle.done()


