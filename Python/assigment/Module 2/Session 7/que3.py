def word_freq_dict(text):
    count={}

    word=text.split(" ")

    for i in word:
        if count.get(i) is None:
            count.update({i:1})
        else:
            c=count.get(i)
            c+=1
            count.update({i:c})
    return count
    
ans=word_freq_dict("Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match")
print(ans)