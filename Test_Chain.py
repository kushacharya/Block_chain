from Block_chain import BlockChain

my_blockchain = BlockChain()

my_blockchain.add_block("Transaction 1 : Hello fro u 1")
my_blockchain.add_block("Transaction 2 : Hello fro u 2")
my_blockchain.add_block("Transaction 3 : Hello fro u 3")

for block in my_blockchain.chain:
    print(f"Index: {block.ind}")
    print(f"Time stamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"previous_hash: {block.previous_hash}")
    print(f"hash: {block.hash}")
    print("-" * 40) #prints the 40 times for visual saperation like -----

print("Is the blockchain valid?",my_blockchain.is_chain_valid())