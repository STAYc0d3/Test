

class Building:
    def __init__(self, height, year) -> None:
        self.height = height
        self.year = year
    
    def change_height(self, height):
        self.height = height

    def get_attr(self):
        print(f'Висота - {self.height}\nРік - {self.year}\n******')

School = Building('100m', 1982)
School.get_attr()
School.change_height('50m')
School.get_attr()