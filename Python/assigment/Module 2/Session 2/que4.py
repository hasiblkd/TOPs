unread_counts = [2, 0, 15, 120, 5]
for i in range(len(unread_counts)):
    if unread_counts[i]>99:
        print("99+")
    else:
        print(unread_counts[i])