def squre(a):
    for i in range(1,a):
        yield i*i

k=squre(5)

print(next(k))
print(next(k))
print(next(k))