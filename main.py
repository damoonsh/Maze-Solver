from map import Map
import pygame

# cols = int(input("Enter the number of columns: "))
# rows = int(input("Enter the number of rows: "))
# scale = int(input("Enter the scale: ")

def main():
    Run = True
    map = Map()

    map.run()
    while Run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            # Input
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    map = Map()
                    map.run()
                if event.key == pygame.K_PAGEUP:
                    pass
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