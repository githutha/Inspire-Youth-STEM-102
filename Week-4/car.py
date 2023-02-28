class car:
    def _init_(self,model,make,year_of_manufacture,engine):
        self.model = model
        self.make = make
        self.year_of_manufacture = year_of_manufacture
        self.engine = engine

#getters
    def get_model(self):
        return self.model
    
    def get_make(self):
        return self.make
    
    def get_year(self):
        return self.year_of_manufacture

    def get_engine(self):
        return self.engine
    
#setters-set the attributes
    def set_model(self,model):
        set.model = model

    def set_make(self,make):
        set.make = make

    def set_engine(self,engine):
        set.engine = engine 

    def set_year_of_manufacture(self,year_of_manufacture):
        set.year_of_manufacture = year_of_manufacture        

        

car1 = ("demio","nissan",2003,1300)        
car2  = ("hilux","toyota",2020,1500) 
car3 = ("passat","vw",2011,1900) 

print(car1.get_model())
print(car1.get_year())

print(car2.get_model())
print(car2.get_year())

print(car3.get_model())
print(car3.get_year())


