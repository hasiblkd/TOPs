product=['Mobile', 'Mouse', 'Laptop', 'Monitor', 'Keyboard']

k = filter(lambda r:r.startswith("M"),product)
print(list(k))