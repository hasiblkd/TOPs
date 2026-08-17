def format_likes(count):
    if count >= 1000000:
        return str(count / 1000000) + "M"
    elif count >= 1000:
        return str(count / 1000) + "K"
    else:
        return count
    
