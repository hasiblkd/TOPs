lists=[[210, 180, 240], [150, 200], [300, 120, 90]]

ans=[i for j in lists for i in j if i>200]
print(ans)