import random
from Display import display
from Options import options


def get_item_event(pos: list, area: list) -> bool:
    if area[pos[0]][pos[1]] == 'M':
        return True
    else:
        return False


def find_player_pos(area: list) -> list:
    for line in area:
        for column in line:
            if column == 'P':
                return [line, column]


def check_position_on_correct(area_size: int, current_pos: int, movement_action: str) -> bool:
    if movement_action == 'w' or movement_action == 'a':
        if current_pos - 1 < area_size - 1:
            return False
    elif movement_action == 's' or movement_action == 'd':
        if current_pos + 1 > area_size - 1:
            return False
    else:
        return True


class Player:

    def __init__(self):
        self.__player_info = {
            'HP': 100,
            'items': []
        }
        self.event_type = [
            'fight', 'use_item'
        ]
        self.__player_position = find_player_pos(display.Display().get_area())
        self.__field_size = options.Options().get_area_size()

    def update_hp(self, event: str) -> str:
        if event == self.event_type[0]:
            self.__player_info.get('HP') - random.randint(10, 20)

            if self.__player_info.get('HP') <= 0:
                return 'death'
            else:
                return 'continue'

        if event == self.event_type[1]:
            pass

    def move_player(self):
        movement_way = input('Enter which way u wanna go: ')

        # Insert check_position_on_correct method there somehow

        if movement_way == 'w':
            self.__player_position[0] -= 1
        elif movement_way == 'a':
            self.__player_position[1] -= 1
        elif movement_way == 's':
            self.__player_position[0] += 1
        else:
            self.__player_position[1] += 1

    def get_player_info(self) -> dict:
        if len(self.__player_info.get('items')) == 0:
            self.__player_info['items'].append('empty')
        else:
            pass

        # Do something like add items check in this method

        return self.__player_info
