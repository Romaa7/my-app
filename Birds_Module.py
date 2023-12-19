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
