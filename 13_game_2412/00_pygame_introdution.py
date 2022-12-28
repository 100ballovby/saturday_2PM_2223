import pygame as pg
import sys  # работа с функциями ОС
from settings import Config
from ship import Ship


def run():
    pg.init()  # инициализация PyGame
    game_config = Config((1200, 800), (230, 230, 230))  # создаю экземпляр класса настроек
    screen = pg.display.set_mode((game_config.screen_width,
                                 game_config.screen_height))  # окно игры и размер
    ship = Ship(screen)

    # цвет фона игры
    pg.display.set_caption('Battle Ship!')  # название игры в окошке
    while True:
        for event in pg.event.get():  # обрабатываю события
            if event.type == pg.QUIT:  # если нажали на крестик
                sys.exit()  # закрыть окно
            screen.fill(game_config.bg_color)
            ship.blit()
        pg.display.flip()  # отображение последнего прорисованного кадра


run()



