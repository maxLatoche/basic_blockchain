from genesis import create_genesis_block
from new_block import next_block


blockchain = [create_genesis_block()]

blocks_to_add = 20

for i in range(0, blocks_to_add):
    previous_block = blockchain[-1]
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    print("Block #{}".format(block_to_add.index))
    print("Hash: {}\n".format(block_to_add.hash))
