from functools import reduce

swiggy_order=[120, 80, 150, 60]
ans=reduce(lambda x,y:x+y,swiggy_order)
print(ans)