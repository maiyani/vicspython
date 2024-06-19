class devices:
    def __init__(self,model,yom):
        self.model = model
        self.yom = yom

    def crash(self):
        print(self.model,"has crsshed")

computer = devices("hp",1999)
computer.crash()

laptop = devices("Dell",2005)
laptop.crash()