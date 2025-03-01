class Vehicle():
    def __init__(self,model):
        self.model = model
                
    def start(self):
        print("Araç çalıştırılıyor..")

#super -> kalıtım aldığım üst class
#sub,self -> bulunduğum class
class Car(Vehicle):
    def __init__(self,model):
        super().__init__(model)
    # override -> üzerine yazma    
    def start(self):
        super().start()
        print("Araba çalıştırılıyor..")


class Truck(Vehicle):
    def __init__(self,model):
        super().__init__(model) 


car1 = Car("Toyota")
car1.start()

truck1 = Truck("Scania")
truck1.start()