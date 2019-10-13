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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Input
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    pass
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
        pygame.display.update()

if __name__ == '__main__':
    main()