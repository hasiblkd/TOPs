rating=[
    [4, 5, 3, 2],
    [5, 4, 4, 3],
    [3, 2, 5, 5]
]

ans=[i for j in rating for i in j if i>4]

print(ans)