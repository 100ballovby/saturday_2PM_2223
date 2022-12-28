import pygame as pg
import game_functions as gf
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
        gf.check_events(ship)  # трекаем события в игре
        ship.update()
        gf.update_screen(game_config, screen, ship)  # обновление экрана игры


run()



