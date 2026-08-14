instagram=[('raj', 800), ('simran', 1500), ('veer', 1200), ('ananya', 950)]
user=list(filter(lambda l:l[1]>1000,instagram))
for i in user:
    print(i[0]+" K Badge")