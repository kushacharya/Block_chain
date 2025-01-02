class Transaction:
    def __init__(self, sender, receiver,amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
    # print(f"Sender: {self.sender} -> Receiver: {self.receiver}, Amount: {self.amount}")
    def __str__(self):
        return f"Sender: {self.sender} -> Receiver: {self.receiver}, Amount: {self.amount}"
    #     # will try if print works or not
    #     print