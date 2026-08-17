names  = ['Shoes', 'Bag', 'Watch', 'Headphones']
prices = [999, 1500, 700, 2200]

product=list(zip(names,prices))

lists=[i for i in product if i[1]>1000]
print(lists)