from map import Map
import pygame
from Consts import vals

# cols = int(input("Enter the number of columns: "))
# rows = int(input("Enter the number of rows: "))
# scale = int(input("Enter the scale: ")

def main():
    Run, pause = True, False

    def set_vals():
        val = vals()
        val.set_props()
        command = input('Press any key but D/d to set your map settings: ')
        if command.lower() == 'd':
            print('You have chosen to set your map properties')
            col = int(input('Enter the number of cols: '))
            row = int(input('Enter the number of rows: '))
            scale = int(input('Enter the scale of your map: '))
            val.set_props(scale=scale, rows=row, cols=col)
        return val


    consts = set_vals()
    map = Map(consts)
    map.run()

    while Run:

        if not pause:
            map.autoMove()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Input
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    print('-----------------------------------')
                    command = input('Press y/Y if you want to change the delay time: ')
                    if command.lower() == 'y':
                        new_delay = int(input('New delay time: '))
                        map.delay = new_delay
                        consts = set_vals()
                    map = Map(consts)
                    map.run()
                if event.key == pygame.K_x:
                    pause = not pause
                    print('Paused: ', pause)
                if event.key == pygame.K_PAGEDOWN:
                    pass

                # Moving manually
                if event.key == pygame.K_RIGHT:
                    map.move(1, 0)
                if event.key == pygame.K_LEFT:
                    map.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    map.move(0, 1)
                if event.key == pygame.K_UP:
                    map.move(0, -1)

        pygame.display.update()

if __name__ == '__main__':
    main()