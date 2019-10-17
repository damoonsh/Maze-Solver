from map import Map
import pygame
from Consts import vals

def main():
    # Initial boolean variable for the whole thing
    Run, pause = True, False
    # The function that prompts the user to enter the map properties
    def set_vals():
        # Initializing an object with it's default values
        val = vals()
        val.set_props()
        # Prompting the user, if they want to adjust the map properties
        command = input('Press any key but D/d to set your map settings: ')
        # If the aadjusting was requested then:
        if command.lower() == 'd':
            print('[MESSAGE]:You have chosen to set your map properties')
            # Get the values
            col = int(input('[INPUT]Enter the number of cols: '))
            row = int(input('[INPUT]Enter the number of rows: '))
            scale = int(input('[INPUT]:Enter the scale of your map: '))
            val.set_props(scale=scale, rows=row, cols=col)
        # Return the val object
        return val
    # Get the consts object so other objects can communicate with each other easier
    consts = set_vals()
    # Instantiate and run the map by the given consts
    map = Map(consts)
    map.run()
    # Main loop where the whole app runs
    while Run:
        # If it wasn't paused then the moving shall be proceeded
        if not pause:
            map.autoMove()
        """ Control section: """
        # Controlling the events within the app by this part
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Input
            if event.type == pygame.KEYDOWN:
                # When space is enter questions for readjusting will be asked
                if event.key == pygame.K_SPACE:
                    # Just to seperate the processes
                    print('-----------------------------------')
                    # Adjusting for the delay time, if demanded
                    command = input('Press y/Y if you want to change the delay time: ')
                    if command.lower() == 'y':
                        new_delay = int(input('New delay time: '))
                        map.delay = new_delay
                    # Ajdusting for the map properties if demanded
                    command = input('Want to change the map properties(Y): ')
                    if command.lower() == 'y':
                        consts = set_vals()
                    # Re-instantiating the map and running it
                    map = Map(consts)
                    map.run()

                # For pausing the process
                if event.key == pygame.K_x:
                    pause = not pause
                    print('Paused: ', pause)

                # Moving manually
                if event.key == pygame.K_RIGHT:
                    map.move(1, 0)
                if event.key == pygame.K_LEFT:
                    map.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    map.move(0, 1)
                if event.key == pygame.K_UP:
                    map.move(0, -1)

        # Updating the display
        pygame.display.update()

if __name__ == '__main__':
    main()