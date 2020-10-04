class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.mydict = {}
        self.big = big
        self.medium = medium
        self.small = small
        self.mydict[1] = big
        self.mydict[2] = medium
        self.mydict[3] = small


    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        if self.mydict[carType]>0:
            self.mydict[carType] -= 1
            return True
        else:
            return False




if __name__ == '__main__':
    obj = ParkingSystem(1, 1, 0)
    param_1 = obj.addCar(1)
    print(param_1)
