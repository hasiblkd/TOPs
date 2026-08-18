def word_dict_frequncy(text):
    count={}

    for i in text:
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count

text =input("Enter a String:-")

ans=word_dict_frequncy(text.lower())

sort_ans=dict(sorted(ans.items()))

print(sort_ans)