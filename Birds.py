class Birds:
  def __init__(self):
    self.name=""
    self.age=0
    self.my_class=""
    self.life_cycle=0
    self.food=""
  def My_name(self,name):
      self.name=name
      print("My Name Is :",self.name)
  def My_age(self,age):
      self.age=age
      print("My Age Is :",self.age)

  def My_class(self, my_class):
      self.my_class= my_class
      print("My Class Is :", self.my_class)

  def Life_Cycle(self, life_cycle):
      self.life_cycle = life_cycle
      print("I Live  About :", self.life_cycle,"years")
class Eagle (Birds):
    def My_color(self,color):
        self.color=color
        print("My Color Is :",color)
    def Food(self,food):
        self.food=food
        print("And I`m eating :",food)

class Pigeon (Birds):
    def My_color(self,color):
        self.color=color
        print("My Color Is :",color)
    def Food(self,food):
        self.food=food
        print("And I`m eating :",food)

class Owl (Birds):
    def My_color(self,color):
        self.color=color
        print("My Color Is :",color)
    def Food(self,food):
        self.food=food
        print("And I`m eating :",food)

birds_obj=Birds()
eagle_obj=Eagle()
pigeon_obj=Pigeon()
owl_obj=Owl()



flag=1
while flag==1:
    select=input("Choose Bird:\n (Eagle\Pigeon\Owl)\n(Exit) to Exit")
    if select=="Eagle":
        eagle_obj.My_name("Eagle")
        eagle_obj.My_age(1)
        eagle_obj.My_class("Birds")
        eagle_obj.Life_Cycle(10)
        eagle_obj.My_color("red")
        eagle_obj.Food("animals and fishes")
    elif select== "Pigeon":
        pigeon_obj.My_name("Pigeon")
        pigeon_obj.My_age(3)
        pigeon_obj.My_class("Birds")
        pigeon_obj.Life_Cycle(7)
        pigeon_obj.My_color("white")
        pigeon_obj.Food("plants")
    elif select== "Owl":
        pigeon_obj.My_name("Owl")
        pigeon_obj.My_age(2)
        pigeon_obj.My_class("Birds")
        pigeon_obj.Life_Cycle(5)
        pigeon_obj.My_color("blue")
        pigeon_obj.food("plants")
    elif select=="Exit" :
        print("Thank you , God bye")
        flag=0
    else:
        print("Invalid input")


