# character_creation_module/main.py

from random import randint

# Новый импорт.
# Из модуля start_game_banner, который расположен в папке graphic_arts,
# импортируем функцию run_screensaver().
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    if char_class == 'Warrior':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(3, 5)}')
    if char_class == 'Mage':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'Healer':
        return (f'{char_name} нанёс урон противнику равный '
                f'{5 + randint(-3, -1)}')


def defence(char_name: str, char_class: str) -> str:
    if char_class == 'Warrior':
        return f'{char_name} блокировал {10 + randint(5, 10)} ед. урона'
    if char_class == 'Mage':
        return f'{char_name} блокировал {10 + randint(-2, 2)} ед. урона'
    if char_class == 'Healer':
        return f'{char_name} блокировал {10 + randint(2, 5)} ед. урона'


def special(char_name: str, char_class: str) -> str:
    if char_class == 'Warrior':
        return (f'{char_name} применил специальное умение '
                f'«Выносливость {80 + 25}»')
    if char_class == 'Mage':
        return (f'{char_name} применил специальное умение '
                f'«Атака {5 + 40}»')
    if char_class == 'Healer':
        return (f'{char_name} применил специальное умение '
                f'«Защита {10 + 30}»')


def start_training(char_name: str, char_class: str) -> str:
    if char_class == 'Warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'Mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'Healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: '
          'Attack — чтобы атаковать противника, '
          'Defence — чтобы блокировать атаку противника, '
          'Special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду Skip.')
    cmd: str = None
    while cmd != 'Skip':
        cmd = input('Введи команду: ')
        if cmd == 'Attack':
            print(attack(char_name, char_class))
        if cmd == 'Defence':
            print(defence(char_name, char_class))
        if cmd == 'Special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        char_class = input('Введи название класса, за который хочешь играть: '
                           'Воитель — Warrior, '
                           'Маг — Mage, '
                           'Лекарь — Healer: ')
        if char_class == 'Warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'Mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'Healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, чтобы выбрать '
                               'другого персонажа ').lower()
    return char_class


def main():
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))

main()
