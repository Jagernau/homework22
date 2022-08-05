# Вам не кажется, что CubeVolumeCalculator 
# чаще дергает методы класса Cube? Исправьте так, 
# чтобы избавиться от лишних обращений к классу Cube


class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_compos_nums(self):
        compos = self.x * self.y * self.z
        return compos



class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube: Cube):
        return cube.get_compos_nums()

cube = Cube(1,2,3)
volume = CubeVolumeCalculator.calc_cube_volume(cube)
print(volume)
