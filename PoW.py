import hashlib
import time

class ProofOfWork:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def mine_block(self, block_data):
        nonce = 0
        start_time = time.time()
        while True:
            block_content = f"{block_data}{nonce}".encode()
            block_hash = hashlib.sha256(block_content).hexdigest()
            if block_hash[:self.difficulty] == "0" * self.difficulty:
                end_time = time.time()
                print(f"Block Mined! \nNonce: {nonce}\nHash: {block_hash}")
                print(f"Time Taken: {end_time - start_time:.2f} seconds")
                return nonce, block_hash
            nonce += 1

difficulty_level = int(input("Enter difficulty level: "))
num_blocks = int(input("Enter number of blocks to mine: "))

pow_system = ProofOfWork(difficulty=difficulty_level)

for i in range(num_blocks):
    print(f"Mining Block {i + 1}...")
    pow_system.mine_block(f"Block {i + 1} Data")
