class ZomatoOrder:
    def add_item(self,item,quntity=1):
        print("Item:-",item)
        print("Quntity:-",quntity)


z1=ZomatoOrder()

z1.add_item("Pizza")
z1.add_item("Burger",3)