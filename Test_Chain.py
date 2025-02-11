from Block_chain import BlockChain

my_blockchain = BlockChain()

while True:
    user_input = input("Enter transaction data (or type 'exit' to stop): ")
    if user_input.lower() == 'exit':
        break
    my_blockchain.add_block(user_input)
    print("Block added successfully!\n")

print("\nBlockchain Data:")
for block in my_blockchain.chain:
    print(f"Index: {block.ind}")
    print(f"Time stamp: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Previous Hash: {block.previous_hash}")
    print(f"Hash: {block.hash}")
    print("-" * 50)

print("Is the blockchain valid?", my_blockchain.is_chain_valid())
