class car:
    def __init__(self,model,color,manufacturer,yof,):
        self.model = model
        self.color = color
        self.manufacturer = manufacturer
        self.yop = yof

    def speed(self):
        print("The manufacturer",self.model,"is",self.manufacturer)

car1 = car("B12","white","BMW")

car2 = car("M360","Red","BMW")
car3 = car("M200","Mate black","BMW")
car4 = car("M300","Black","BMW")
