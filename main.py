import Birds_Module as BI

flag=1
while flag==1:
    select=input("Choose Bird:\n (Eagle\Pigeon\Owl)\n(Exit) to Exit")
    if select=="Eagle":
        BI.eagle_obj.My_name("Eagle")
        BI.eagle_obj.My_age(1)
        BI.eagle_obj.My_class("Birds")
        BI.eagle_obj.Life_Cycle(10)
        BI.eagle_obj.My_color("red")
        BI.eagle_obj.Food("animals and fishes")
    elif select== "Pigeon":
        BI.pigeon_obj.My_name("Pigeon")
        BI.pigeon_obj.My_age(3)
        BI.pigeon_obj.My_class("Birds")
        BI.pigeon_obj.Life_Cycle(7)
        BI.pigeon_obj.My_color("white")
        BI.pigeon_obj.Food("plants")
    elif select== "Owl":
        BI.owl_obj.My_name("Owl")
        BI.owl_obj.My_age(2)
        BI.owl_obj.My_class("Birds")
        BI.owl_obj.Life_Cycle(5)
        BI.owl_obj.My_color("blue")
        BI.owl_obj.food("plants")
    elif select =="Exit" :
        print("Thank you , God bye")
        flag=0
    else:
        print("Invalid input")






