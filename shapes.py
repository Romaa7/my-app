class ReadValues:
    def  __init__(self):
        self.redius=0
        self.base=0
        self.hight=0
        self.length=0
        self.width=0
        self.pi=3.14
        self.side1_length=0
        self.side2_length = 0
        self.side3_length = 0
        self.area=0
        self.perimter=0

    def read_redius(self):
        self.redius=int(input("please Enter the redius value :"))
    def read_base(self):
        self.base=int(input("please Enter the base value :"))
    def read_hight(self):
        self.hight=int(input("please Enter the hight value :"))
    def read_width(self):
        self.width=int(input("please Enter the width value :"))
    def read_length(self):
        self.redius=int(input("please Enter the length value :"))
    def read_dimantion(self):
        self.side1_length==int(input("please Enter the side1_length= value :"))
        self.side2_length==int(input("please Enter the side2_length= value :"))
        self.side3_length==int(input("please Enter the side3_length= value :"))
class Circle(ReadValues):
   def circle_Area(self):
       self.read_redius()
       Area_C=self.pi*(self.redius)**2
       return Area_C
   def circle_perimeter(self):
       self.read_redius()
       perimeter_C=2*self.pi*self.redius
       return perimeter_C


class Triangle(ReadValues):
    def triangle_Area(self):
        self.read_base()
        self.read_hight()
        Area_T = 0.5* self.base * self.hight
        return Area_T
    def triangle_perimeter(self):
        self.read_dimantion()
        perimeter_T = (self.side1_length+self.side2_length+self.side3_length)
        return perimeter_T


class Square(ReadValues):
   def square_area(self):
       self.read_length()
       Area_S=self.length**2
       return Area_S
   def square_perimeter(self):
       self.read_length()
       perimeter_S=4*self.length
       return perimeter_S



class Rectangle(ReadValues):
    def rectangle_area(self):
        self.read_length()
        self.read_width()
        Area_R = self.length*self.width
        return Area_R
    def rectangle_perimeter(self):
        self.read_length()
        self.read_width()
        perimeter_R= 2 *(self.width+self.length)
        return perimeter_R

read_value_object=ReadValues()
circle_object=Circle()
triangle_object=Triangle()
square_object=Square()
rectangle_object=Rectangle()

flag=1
while flag:
    print("\t\tChoose which operation you need to preform :")
    print("\t\tFor preform a Circle calculations :press 1 ")
    print("\t\tFor  preform a Triangle calculations:press 2 ")
    print("\t\tFor  preform a Square calculations:press 3 ")
    print("\t\tFor  preform a Rectangle calculations:press 4 ")
    print("\t\tpress o to exit")
    user_input=int(input())
    if user_input==1:
        cicle_area=circle_object.circle_Area()
        cicle_per=circle_object.circle_perimeter()
        print("\n Circle Area :",cicle_area)
        print("\n Circle perimeter:",cicle_per)

    elif user_input==2:
        triangle_area = triangle_object.triangle_Area()
        triangle_per = triangle_object.triangle_perimeter()
        print("\n Triangle Area:", triangle_area)
        print("\n Triangle perimeter:", triangle_per)
    elif user_input==3:
        square_area =square_object.square_area()
        square_per =square_object.square_perimeter()
        print("\n Square Area:", square_area)
        print("\n Square perimeter:", square_per)
    elif user_input==4:
        rectangle_area=rectangle_object.rectangle_area()
        rectangle_per=rectangle_object.rectangle_perimeter()
        print("\n Rectangle Area:", rectangle_area)
        print("\n Rectangle perimeter:", rectangle_per)
    elif user_input==0:
        check_user_answare=input("Do You What Exit From This Process Yes/No")
        if check_user_answare == "YES" or check_user_answare=="yes"or check_user_answare=="Yes":
            print(" Thanks , Good bye")
            flag=0
        else:
            pass
    else:
        print("Invalid User Input ,Please Try Again")