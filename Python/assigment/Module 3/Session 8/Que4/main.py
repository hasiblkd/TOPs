import likes, comments

current_likes = int(input("Enter Current Likes: "))
new_likes = int(input("Enter New Likes: "))

current_comments=input("Enter Current Comments: ")
new_comments=input("Enter New Comments: ")

likes_result=likes.like_count(current_likes, new_likes)
comments_result=comments.comment_count(current_comments, new_comments)

print("Updated Likes:", likes_result)
print("Updated Comments:", comments_result)