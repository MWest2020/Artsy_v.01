import turtle

def exit() : 
        choice = input("exit program?? Y/N ?").lower()
        if choice in ('yes', 'y'): 
            print('See you next time!')
            turtle.bye()            
        elif choice in ('no', 'n'): 
            print('all right! Launching again')
            
        else : 
            print('all right! Launching again')
            exit()
    
exit()