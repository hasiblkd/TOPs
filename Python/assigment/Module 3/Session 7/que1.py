class InstaStory:
    def share(self):
        print("Instagram Story is Sharing")

class WhatsappStory(InstaStory):
    def share(self):
        print("Whatsapp Story is Sharing")

i1=InstaStory()
w1=WhatsappStory()

i1.share()
w1.share()