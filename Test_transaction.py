# from Test_Chain import my_blockchain
from Wallet import createWallet
from Block_chain import BlockChain
from Transaction import Transaction

niggo = createWallet()
yeti = createWallet()
miner = createWallet()

my_blockchain = BlockChain()

my_blockchain.add_transaction(Transaction(yeti,niggo,10))
my_blockchain.add_transaction(Transaction(niggo,yeti,1))

print(f"Mine pending transaction")
my_blockchain.mine_pending_transactions(miner)

my_blockchain.mine_pending_transactions(miner)

for block in my_blockchain.chain:
    print(f"Index: {block.ind}")
    print(f"Time stamp: {block.timestamp}")
    # print(f"Data: {block.data}")
    print(f"Transactions: {[str(tx) for tx in block.transactions]}")
    print(f"previous_hash: {block.previous_hash}")
    print(f"hash: {block.hash}")
    print("-" * 40)

print(f"Miner's balance: {sum(tx.amount for tx in my_blockchain.pending_transactions if tx.receiver == miner)}")