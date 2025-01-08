import hashlib
import time
from operator import index


class Block:
    def __init__(self, ind, transactions,previous_hash):
        self.ind = ind
        self.timestamp = time.time()
        # self.data = data
        self.nonce = 0
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.hash = self.calculatehash()
        # self.previousHash = ""



    def calculatehash(self):
        block_data = f"{self.ind}{self.timestamp}{[str(tx) for tx in self.transactions]}{self.nonce}"
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine_block(self,difficulty):
        target = "0" * difficulty
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculatehash()