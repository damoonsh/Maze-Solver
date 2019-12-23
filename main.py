"""
    This module runs the different parts of the objects at the same
    time based on the input by the user.
"""
# Pygame is imported so the initial stuff can be instantiated
import pygame
# Importing the wirtten modules
from map import Map
from utilities.Consts import vals
from utilities.loggings import *
# Main function
def main():
    # Initial boolean variable for the whole thing
    Run, pause, userMode = True, False, False

    def declare_mode():
        """Ask the user to see if the user's moves should be tracked or not"""
        if input(mode_selection).lower() == 'c':
            userMode = False
        else:
            userMode = True
            print('Running on user mode.')

    def ask_adjustion():
        """Asks if the user wants to adjust the map"""
        # Initializing an object with it's default values
        val = vals()
        # Prompting the user, if they want to adjust the map properties
        comm = input(map_settings)
        # Adjusting for the map properties if demanded
        if comm.lower() == 'd':
            val = set_val(val)
        else:
            val.set_props()
        declare_mode()
        return val

    def set_val(val):
        """The function that prompts the user to enter the map properties"""
        # Get the values
        col = int(input(col_input))
        row = int(input(row_input))
        scale = int(input(scale_input))
        # Setting the attributes
        val.set_props(scale=scale, rows=row, cols=col)
        # Return the val object
        return val

    # Get the consts object so other objects can communicate with each other
    consts = ask_adjustion()

    # Instantiate and run the map by the given consts
    maze = Map(consts)
    maze.run()
    # Main loop where the whole app runs
    while Run:
        """ Control section: """
        # Controlling the events within the app by this part
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(quit_message)
                pygame.quit()
                quit()
            # Input
            if event.type == pygame.KEYDOWN:
                # When space is enter questions for readjusting will be asked
                if event.key == pygame.K_SPACE:
                    # Just to separate the processes
                    print(seperator)
                    # Adjusting for the delay time, if demanded
                    command = input(delay_adjusment)
                    if command.lower() == 'y':
                        new_delay = int(input('New delay time: '))
                        maze.delay = new_delay
                        # Check to see if the user wants to adjust the map
                        ask_adjustion()
                    # Re-instantiating the map and running it
                    maze = Map(consts)
                    maze.run()
                # Quick reset with no questions asked
                if event.key == pygame.K_r:
                    # Re-instantiating the map and running it
                    maze = Map(consts)
                    print(map_reset)
                    pause = False
                    maze.run()

                # For pausing the process
                if event.key == pygame.K_x:
                    pause = not pause
                    print(paused_msg, pause)

                # Moving manually
                if event.key == pygame.K_RIGHT:
                    print("\U0001F923")
                    maze.move(1, 0)
                if event.key == pygame.K_LEFT:
                    maze.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    maze.move(0, 1)
                if event.key == pygame.K_UP:
                    maze.move(0, -1)

        # If it wasn't paused and not in the user mode then the moving
        # shall be proceeded
        if not pause and not userMode:
            maze.autoMove()
        # Updating the display
        pygame.display.update()


if __name__ == '__main__':
    main()
