class Email:
    def __init__(self, sender, reciever, content):
        self.sender = sender
        self.reciever = reciever
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.reciever}: {self.content}. Sent: {self.is_sent}"


email_list = []
information= input()
while information != "Stop":
    sender, receiver, content = information.split(" ")
    email = Email(sender, receiver, content)
    email_list.append(email)
    information = input()

indices_lst = [int(i) for i in input().split(", ")]
for indx in indices_lst:
    email = email_list[indx]
    email.send()

for email in email_list:
    print(email.get_info())