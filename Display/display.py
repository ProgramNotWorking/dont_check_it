from Options import options
from Player import player


def paint_field(area: list):
    for item in area:
        print(item)


def paint_info(current_info: dict):
    print(f'\nHP: {current_info.get("HP")}\nItems:\n{current_info.get("items")}')


def set_player_in_area(area: list):
    if len(area) % 2 == 0:
        area[len(area) - 1][int((len(area) - 2) / 2)] = 'P'
    else:
        area[len(area) - 1][int((len(area) - 1) / 2)] = 'P'


def set_monsters(area: list, indexes_to_change: any, area_size: int):
    for index in indexes_to_change:
        if index < area_size:
            area[0][index] = 'M'
        else:
            area[int(index / area_size)][area_size - int(index / area_size)] = 'M'


class Display:

    def __init__(self):
        self.__options = options.Options()
        self.__options_dict = {}
        self.__player = player.Player()
        self.__field = [[]]

    def display_init(self):
        self.options_init()
        paint_field(self.create_field())
        paint_info(self.__player.get_player_info())

    def create_field(self) -> list:
        self.__field = [
            ['0' for _ in range(self.__options_dict.get('area_size'))]
            for _ in range(self.__options_dict.get('area_size'))
        ]
        set_monsters(self.__field, self.__options.get_indexes(), self.__options_dict.get('area_size'))
        set_player_in_area(self.__field)

        return self.__field

    def options_init(self):
        self.__options.set_options()
        self.__options_dict = self.__options.get_options()

    def get_area(self) -> list:
        return self.__field
