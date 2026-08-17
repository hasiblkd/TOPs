import math as m

price=[199.1,349.8,599.3]
round_price=[]
for i in price:
    round_price.append(m.ceil(i))

print(round_price)