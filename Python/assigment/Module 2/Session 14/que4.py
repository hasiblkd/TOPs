orders = {
    101: {
        "restaurant": "Pizza Point",
        "items": ["Pizza", "Fries"],
        "total": 450
    },
    102: {
        "restaurant": "Burger Hub",
        "items": ["Burger", "Coke"],
        "total": 350
    }
}
# print(orders)
def add_new_order(id,restaurant,item,total):
   order=orders.setdefault(id,{})

   order["Resturent"]=restaurant
   order["Item"]=item
   order["Total"]=total

def update_total(id,new_total):
   if id in orders:
      orders[id]["Total"]=new_total
    
add_new_order(103,"Silver Nest",["Panner Tikka","Panner Kaju"],700)

update_total(103,750)

print(orders)

