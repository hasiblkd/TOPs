# 1. Globel Scope
# 2. Local Scope

a=10
def test():
    # Access Globel Variable Value
    global a
    a=20
    print(a)

print(a)
test()
print(a)