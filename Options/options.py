class Options:

    def __init__(self):
        self.__options_dict = {
            'area_size': 5,
            'difficulty': 'NONE'
        }
        self.__diff_list = [
            'easy', 'medium', 'hard'
        ]

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

    def something(self):
        pass
