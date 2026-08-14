def word_freq_dict(text):
    word={}
    for i in text:
        if i in word:
            text[i]+=1
        else:
            text[i]=1
    print(word_freq_dict(text[i]))
    
word_freq_dict("Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match")
