class FoodOrder:
    def __init__(self,rest_name,items,total):
        self.rest_name=rest_name
        self.items=items
        self.total=total

    def show_Order(self):
        print("Resturent Name:-",self.rest_name)
        print("Items:-",self.items)
        print("Total:-",self.total)

r_name=input("Enter a Resturant name:-")
item=input("Enter Food Item:-")
item=item.split(",")
total=float(input("Enter a Total:-"))

f1=FoodOrder(r_name,item,total)

f1.show_Order()
