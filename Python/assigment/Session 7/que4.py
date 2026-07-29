messages = ['Hi', 'Spam', 'Hello', 'Spam', 'How are you?']
for i in messages:
    if i=='Spam':
        continue

    if i=='How are you?':
        break
    print(i)