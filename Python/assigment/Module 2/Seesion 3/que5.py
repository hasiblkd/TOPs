def video_details(titles, views):
    result = [(title, round(view / 1000) * 1000) for title, view in zip(titles, views)]
    return result

titles = ["Python Tutorial", "AI Explained", "Django Course"]
views = [125430, 287650, 512340]

print(video_details(titles, views))