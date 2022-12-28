import sys
import pygame as pg


def check_keydown_events(event, obj):
    if event.key == pg.K_RIGHT:
        obj.moving_right = True  # разрешаем кораблю двигаться вправо
    elif event.key == pg.K_LEFT:
        obj.moving_left = True


def check_keyup_events(event, obj):
    if event.key == pg.K_RIGHT:
        obj.moving_right = False  # запрещаем движение
    elif event.key == pg.K_LEFT:
        obj.moving_left = False


def check_events(obj):
    for event in pg.event.get():  # обрабатываю события
        if event.type == pg.QUIT:  # если нажали на крестик
            sys.exit()  # закрыть окно
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event, obj)
        elif event.type == pg.KEYUP:
            check_keyup_events(event, obj)


def update_screen(settings, screen, obj):
    screen.fill(settings.bg_color)
    obj.blit()
    pg.display.flip()  # отображение последнего прорисованного кадра
