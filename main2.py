
from player import *
from pygame import *



WIN_WIDTH = 800  # Ширина создаваемого окна
WIN_HEIGHT = 640  # Высота
hero = Player(70, 300) # создаем героя по (x,y) координатам
BACKGROUND_COLOR = "#1E90FF"
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)  # Группируем ширину и высоту в одну переменную
block = pygame.image.load("block.jpg")
PLATFORM_WIDTH = 20
PLATFORM_HEIGHT = 20
timer = pygame.time.Clock()
level_tex = []
level = [
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    " " * 15 + "-" * 10 + " " * 15,
    " " * 15 + "-" * 10 + " " * 15,
    " " * 15 + "-" * 10 + " " * 15,
    " " * 15 + "-" * 10 + " " * 15,
    " " * 15 + "-" * 10 + " " * 15,
    " " * 15 + "-" * 10 + " " * 15,
    " " * 15 + "-" * 10 + " " * 15,
    " " * 15 + "-" * 10 + " " * 15,
    " " * 15 + "-" * 10 + " " * 15,
    " " * 15 + "-" * 10 + " " * 15,
    " " * 15 + "-" * 10 + " " * 15,
    " " * 15 + "-" * 10 + " " * 15,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40,
    "-" * 40]


def main():
    left = right = up = down = False
    pygame.init()  # Инициация PyGame, обязательная строчка
    screen = pygame.display.set_mode(DISPLAY)  # Создаем окошко
    pygame.display.set_caption("igor")  # Пишем в шапку
    run = True

    while run:  # Основной цикл программы
        timer.tick(100)
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                run = False
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True

            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False

            if e.type == KEYDOWN and e.key == K_UP:
                up = True
            if e.type == KEYDOWN and e.key == K_DOWN:
                down = True

            if e.type == KEYUP and e.key == K_UP:
                up = False
            if e.type == KEYUP and e.key == K_DOWN:
                down = False
        if hero.rect.y % 20 == 0:
            if level[(hero.rect.y - 20) // 20][hero.rect.x // 20] == '-':
                up = False
            elif level[(hero.rect.y + 40) // 20][hero.rect.x // 20] == '-':
                down = False
        if hero.rect.x % 20 == 0:
            if level[hero.rect.y // 20][hero.rect.x // 20] == '-':
                left = False
            elif level[hero.rect.y // 20][(hero.rect.x + 40) // 20] == '-':
                right = False
        screen.fill(BACKGROUND_COLOR)
        x = y = 0  # координаты
        for row in level:
            for col in row:
                if col == "-":
                    screen.blit(block, (x, y))
                    quad = pygame.Rect(x, y, 20, 20)
                    level_tex.append(quad)
                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0
        hero.update(left, right, up, down)  # передвижение
        hero.draw(screen)
        pygame.display.update()



if __name__ == "__main__":
    main()
