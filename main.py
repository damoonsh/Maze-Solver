"""
    This module runs the different parts of the objects at the same
    time based on the input by the user.
"""
# Pygame is imported so the initial stuff can be instantiated
import pygame
# Importing the wirtten modules
from map import Map
from Consts import vals
# Main function
def main():
    # Initial boolean variable for the whole thing
    Run, pause = True, False

    # The function that prompts the user to enter the map properties
    def set_val():
        # Initializing an object with it's default values
        val = vals()
        val.set_props()
        # Prompting the user, if they want to adjust the map properties
        comm = input('Press any key but D/d to set your map settings: ')
        # If the adjusting was requested then:
        if comm.lower() == 'd':
            print('[MESSAGE]:You have chosen to set your map properties')
            # Get the values
            col = int(input('[INPUT]Enter the number of cols: '))
            row = int(input('[INPUT]Enter the number of rows: '))
            scale = int(input('[INPUT]Enter the scale of your map: '))
            val.set_props(scale=scale, rows=row, cols=col)
        # Return the val object
        return val

    # Get the consts object so other objects can communicate with each other easier
    consts = set_val()
    # Instantiate and run the map by the given consts
    maze = Map(consts)
    maze.run()
    # Main loop where the whole app runs
    while Run:
        # If it wasn't paused then the moving shall be proceeded
        if not pause:
            maze.autoMove()
        """ Control section: """
        # Controlling the events within the app by this part
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Quiting the trial as demanded.')
                pygame.quit()
                quit()
            # Input
            if event.type == pygame.KEYDOWN:
                # When space is enter questions for readjusting will be asked
                if event.key == pygame.K_SPACE:
                    # Just to separate the processes
                    print('-----------------------------------')
                    # Adjusting for the delay time, if demanded
                    command = input('Press y/Y if you want to change the delay time: ')
                    if command.lower() == 'y':
                        new_delay = int(input('New delay time: '))
                        maze.delay = new_delay
                        # Adjusting for the map properties if demanded
                        consts = set_val()
                    # Re-instantiating the map and running it
                    maze = Map(consts)
                    maze.run()
                # Quick reset with no questions asked
                if event.key == pygame.K_r:
                    # Re-instantiating the map and running it
                    maze = Map(consts)
                    print('Map is resetted===========================')
                    pause = False
                    maze.run()

                # For pausing the process
                if event.key == pygame.K_x:
                    pause = not pause
                    print('Paused: ', pause)

                # Moving manually
                if event.key == pygame.K_RIGHT:
                    maze.move(1, 0)
                if event.key == pygame.K_LEFT:
                    maze.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    maze.move(0, 1)
                if event.key == pygame.K_UP:
                    maze.move(0, -1)

        # Updating the display
        pygame.display.update()


if __name__ == '__main__':
    main()
