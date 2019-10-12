from map import Map
import pygame

# cols = int(input("Enter the number of columns: "))
# rows = int(input("Enter the number of rows: "))
# scale = int(input("Enter the scale: ")

def main():
    Run = True
    already = False
    while Run:
        if not already:
            map = Map()
            already = True
            map.run()

        if pygame.event.get(): print(pygame.event.get())

        for event in pygame.event.get():
            if event.type == pygame.K_x:
                pygame.quit()
                quit()
            # Input
            if event.type == pygame.KEYDOWN:

                # In order to observe the process
                if event.key == pygame.K_SPACE:
                    Run = False
                if event.key == pygame.K_PAGEUP:
                    pass
                if event.key == pygame.K_PAGEDOWN:
                    pass

                # Moving manually
                if event.key == pygame.K_RIGHT:
                    pass
                if event.key == pygame.K_LEFT:
                    pass
                if event.key == pygame.K_DOWN:
                    pass
                if event.key == pygame.K_UP:
                    pass

if __name__ == '__main__':
    main()