def format_follower_count(number):
    if number>1000000:
        return str(number/1000000)+" M"
    elif number>1000 or number<999999:
        return str(number/1000)+" K"
    else:
        return str(number)


follower=int(input("Enter No. of Follower's:-"))
print(format_follower_count(follower))