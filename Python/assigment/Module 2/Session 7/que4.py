def word_dict_frequncy(text):
    stopwords = ["the", "and", "in", "of", "a", "to", "is"]

    word=text.lower().split()
    count={}

    for i in word:
        if i in stopwords:
            continue

        if i in count:
            count[i]+=1
        else:
            count[i]=1
    return count

text =input("Enter a String:-")

print(word_dict_frequncy(text))