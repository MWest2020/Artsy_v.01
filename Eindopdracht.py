# Generative art with Turtle
# Eindopdracht Programmeren, Blok 1, 2021, HvA, Mark Westerweel     versie: 1.0
#
# This is a simple program that asks the user for input and based on that input draws random circles on a canvas. The program is written
# as an experiment to later work with more complex input and / or other modules.
# The output is generated in a second window and stored in an .eps file. These files can be viewed with Adobe photoshop or numerous other programs
# Saving it to a jpeg file is possible, but beyond the scope of this experiment as it requires /Path configurations or gaining API keys.  


##############################################
# TO DO:
# Collect all answers and store in list / tuple and build the artpiece from the list. == Edits and shows information from minimal 1 list
# Refactor for coding conventions.
# Defensive coding to ensure quality data input && 
# format data as final string (



# DONE:
# Uses Integers and Bool (if/else))
# Read and edit user input
# Writes information to the output.
# Uses functions (TO DO: each block in a function)
# Uses modules (Turtle, random, time)
# 
###############################################



# de gebruikers input die wordt gevraagd moet je duidelijker aangeven. wat zijn de mogelijke keuzes?



# This imports required modules for the profram to run correctly
import turtle, random, time 

from turtle import *

# # This will run the into. The time module create the delay effect.
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

def main () :
    # The art_name function asks user input for a name. The name must be of the "string" datatype 
    def art_name ():
        
        # ask user for input to store in a variable. 
        name_artpiece = input('                         First we need a name for the project, have you thought about any? (pls provide a name for now --letters only)')
        
        # Verifies user input for a string datatype
        if name_artpiece.isalpha() == True:
            turtle.title(name_artpiece)
            print('                 Splendid! I think', name_artpiece, 'is a wonderful name...')
            print("                 Some more questions and let's check out the canvas in the other window and let's rock!")

        # Defensively excludes all other user inputs. The program will ask again or exit.     
        else : 
            print("                 Ehr... Unless you're Elon Musk, we name our produce with letters only... you know, with words...")
            print('                 So you got a name? ')
            name_artpiece = input()
            # verifies again for the string datatype
            if name_artpiece.isalpha() :
                turtle.title(name_artpiece)
                print('             Thank you for getting along with the program!')
            # else exits the program
            else : 
                print("             Yeah, when you're not in THAT mood, start the program again...")
                exit()
                # CAN USE WHILE LOOP INSTEAD OF EXIT
        return name_artpiece

    name_artpiece = art_name()
    

    
    # The colors function asks user input for a name. The input must be of the "string" datatype and a known colour in English or a hexidecimal value.
    def colors () :

        
        background = input('                What colour do you want to the background to be? (I will take English names for colours or even hex values) ').lower()
        outline = input('               What colour would you use for the outlining? ').lower() 
        fill = input('What colours would you use for the filling? ').lower()
        
        return background, outline, fill

    # destructured variables
    background, outline, fill = colors()   


    # list with set values for size and starting point. These values corresspond to a small, medium or large canvas.
    # canvasSizes[0:1:2][0] = width.                                                --Screen size modifications require a integer datatype.
    # canvasSizes[0:1:2][1] = height                                                --Screen size modifications require a integer datatype.
    # canvasSizes[0:1:2][2] = starting point x , a little to the left.              --Coordinates take a float datatype.
    # canvasSizes[0:1:2][3] = starting point y , sligthly up from the center.       --Coordinates take a float datatype. 

    canvasSizes = [[600, 400, 90.5, 0.5], [800, 600, 100, 0.5],[1200, 800, 100, 0.5]]

    # arguments are canvassize and starting points
    size = input('What canvas size would you like? We got "small", "medium" or "large"... ')
    if size != "small" or "medium " or "large" : size == "medium"

    # Determines the canvas size, based on use input.
    if size == "small" :
        canvas = turtle.Screen()
        canvas.setup(width=canvasSizes[0][0], height=canvasSizes[0][1], startx=canvasSizes[0][2], starty=canvasSizes[0][3])
    elif size == "medium" :
        canvas = turtle.Screen() 
        canvas.setup(width=canvasSizes[1][0], height=canvasSizes[1][1], startx=canvasSizes[1][2], starty=canvasSizes[1][3])
    elif size == "large" :
        canvas = turtle.Screen() 
        canvas.setup(width=canvasSizes[2][0], height=canvasSizes[2][1], startx=canvasSizes[2][2], starty=canvasSizes[2][3])


    #########################################################################
    # CIRCLES // 
    #########################################################################

    # This function draws the generative circle art. Based on the user input (x), an integer (x) is used as x steps in an range( to draw x circles).
    # conditional logic is derived from the steps counter.  

    def draw_circle_art():
        circles = input("How many circles would you like to draw? Pick an integer ")
        print("Check out the canvas in the other window")
        time.sleep(3)

        # user input is converted to an integer and used for x amount of iterations.
        end_range = int(circles) 
        seen = set()

        # each iteration draws a different circle
        for steps in range(1, end_range):
            # unaltered circle based on user input 
            turtle.color(outline, fill) 
            turtle.bgcolor(background)
            turtle.begin_fill()
            print('Drawing...')
            
            # randomized circle based on even number iterations
            if int(steps) % 2 == 0 :
                turtle.begin_fill()
                print("... a circle...")
                turtle.circle(random.randint(0,100))
                turtle.left(random.randint(25,90))
                # circle filling based on iteration / 3 = 0 
                if steps % 3 == 0 or 1 : turtle.end_fill()
            else :
                # skips the first step and based on iteration / 3 = 0
                if steps != 0 and steps % 3 == 0:
                    print('changing the brush size! A dash here... ')
                    # changes brush outline size
                    pensize(random.randint(1, 8))
                    # occasionally draw a dash to either left or right
                    if steps % 2 == 0 : turtle.forward(random.randint(25, 250))
                    else : turtle.backward(random.randint(25, 250))
                elif steps % 3 == 1 or 2:
                    # draws and occasional random coloured circle
                    # lamba is an unnamed function 
                    r = lambda: random.randint(0, 255)
                    random_color = '#{:02x}{:02x}{:02x}'.format(r(), r(), r())
            
                    print('Maybe a different circle')
                    turtle.color(random_color, random_color) 
                    turtle.begin_fill()
                    turtle.circle(random.randint(0,100))
                    turtle.left(random.randint(25,90))
                    turtle.end_fill()
            
        turtle.end_fill()
        
        final_string = "Looks like {} came together quite nicely! You used a {} background with {} outling and {} fillings. \n \n I added some randomness to spice it up!"
        print(final_string.format(name_artpiece, background, outline, fill))
    

    draw_circle_art()


    #########################################################################
    # SAVE TO FILE 
    #########################################################################

    
    # this function take care of saving the artpiece 
    def save_art() : 
        # Takes a screenshot
        ts = turtle.getscreen()
        # Save the screenshot to a .eps file 
        filename = name_artpiece +'.eps'
        ts.getcanvas().postscript(file=filename)
        
        # User interaction
        print('\n Your file is stored under ' + filename)
        time.sleep(2.5)
        
        print('\n See you around for the next piece!')
        time.sleep(2.5) 

    save_art()

    # The exit function check for user input and closes the program and continues for another art session.
    def exit() : 
        choice = input("Continue working on the same piece?? Y/N ?").lower()
        if choice in ('yes', 'y'): 
            print('all right! Launching again')
            main()
        elif choice in ('no', 'n'): 
            print('See you next time!')
            turtle.bye()            
        else : 
            exit()
    
    exit()

# Function call to run the program after the intro
main()
