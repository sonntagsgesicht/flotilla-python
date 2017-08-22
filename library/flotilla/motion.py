from .module import Module


class Motion(Module):
    name = 'motion'

    @property
    def x(self):
        if len(self.data) > 0:
            return int(self.data[0])
        return 0

    @property
    def y(self):
        if len(self.data) > 1:
            return int(self.data[1])
        return 0

    @property
    def z(self):
        if len(self.data) > 2:
            return int(self.data[2])
        return 0

    @property
    def magnetometer_x(self):
        if len(self.data) > 3:
            return int(self.data[3])
        return 0

    @property
    def magnetometer_y(self):
        if len(self.data) > 4:
            return int(self.data[4])
        return 0

    @property
    def magnetometer_z(self):
        if len(self.data) > 5:
            return int(self.data[5])
        return 0
