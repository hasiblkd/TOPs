call_duration=(12, 5, 0, 20, 7, 3, 15)
l=list(call_duration)
new_list=[]
for i in l:
    if i>=5:
        new_list.append(i)
call_duration=tuple(new_list)
print(new_list)