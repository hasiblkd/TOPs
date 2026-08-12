score=int(input("Enter your Favorite team Score:-"))
if score>=200:
    print("High Score...")
elif score>=150 and score<=199:
    print("Good Score...")
elif score>=100 and score<=149:
    print("Average Score...")
else:
    print("Needs Improvement...")