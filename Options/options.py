import random


class Options:

    def __init__(self):
        self.__options_dict = {
            'area_size': 5,
            'difficulty': 'NONE'
        }
        self.__diff_list = [
            'easy', 'medium', 'hard'
        ]
        self.__coefficient = 0

    def set_options(self):
        area_size = int(input('Enter area size: '))
        difficulty = input('Enter difficulty: ')

        self.__options_dict['area_size'] = area_size
        if difficulty not in self.__diff_list:
            self.__options_dict['difficulty'] = self.__diff_list[0]
        else:
            self.__options_dict['difficulty'] = difficulty

    def get_options(self) -> dict:
        return self.__options_dict

    def __get_coefficient(self) -> int:
        if self.__options_dict.get('difficulty') == self.__diff_list[0]:
            return int(pow(self.__options_dict.get('area_size'), 2) / 6)
        elif self.__options_dict.get('difficulty') == self.__diff_list[1]:
            return int(pow(self.__options_dict.get('area_size'), 2) / 4)
        else:
            return int(pow(self.__options_dict.get('area_size'), 2) / 2)

    def get_indexes(self):
        return random.sample(range(0, pow(self.__options_dict.get('area_size'), 2)), self.__get_coefficient())

    def get_area_size(self):
        return self.__options_dict.get('area_size')
