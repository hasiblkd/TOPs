class Notification:

    def send(self):
        print("Sending Notification")


class EmailNotification(Notification):

    def send(self):
        print("Sending Notification through Email")


class SMSNotification(Notification):

    def send(self):
        print("Sending Notification through SMS")


n1 = Notification()
e1 = EmailNotification()
s1 = SMSNotification()

n1.send()
e1.send()
s1.send()

# Method overriding means the child classes (EmailNotification and SMSNotification) 
# provide their own implementation of the send() method inherited from Notification.