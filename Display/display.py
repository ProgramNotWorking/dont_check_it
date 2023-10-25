from Options import options


def paint_field(area: list):
    for item in area:
        print(item)


class Display:

    def __init__(self):
        self.__options = options.Options()
        self.__options_dict = {}

    def display_init(self):
        self.options_init()
        paint_field(self.create_field())

    def create_field(self) -> list:
        field = [
            ['0' for _ in range(self.__options_dict.get('area_size'))]
            for _ in range(self.__options_dict.get('area_size'))
        ]
        
        # Something like player display at center bottom of this shit
        # field[self.__options_dict.get('area_size') - 1][::-1] = 'p'

        return field

    def options_init(self):
        self.__options.set_options()
        self.__options_dict = self.__options.get_options()
