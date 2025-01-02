from Block import Block
from Transaction import Transaction


class BlockChain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 3
        self.pending_transactions = []
        self.mining_reward = 50

    def create_genesis_block(self):
        return Block(0,"0",[])

    def mine_pending_transactions(self,miner_address):
        block = Block(len(self.chain),self.pending_transactions,self.get_last_block().hash)
        block.mine_block(self.difficulty)

        print(f"Mined block {block}")
        self.chain.append(block)
        self.pending_transactions = [Transaction("System",miner_address,self.mining_reward)]

    def add_transaction(self,transaction):
        if not transaction.sender or not transaction.receiver or transaction.amount <= 0:
            raise ValueError("Transaction must be greater than 0")
        self.pending_transactions.append(transaction)

    def get_last_block(self):
        return self.chain[-1]

    # def add_block(self, data):
    #     latest_block = self.get_last_block()
    #     new_block = Block(len(self.chain),data,latest_block.hash,[])
    #     self.chain.append(new_block)
    #     # return new_block
    #     # self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1,len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.calculatehash():
                return False

            if current.previous_hash != previous.hash:
                return False


        return True