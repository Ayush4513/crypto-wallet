from hashlib import sha256
MAX_NoNCE = 100000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_no,transactions, prev_hash, prefix_zeroes):
    pref_str='0'*prefix_zeroes
    for nonce in range(MAX_NoNCE):
        text=str(block_no) + transactions+prev_hash+str(nonce)
        new_hash=SHA256(text)
        if new_hash.startswith(pref_str):
            print(f"{nonce}")
            return new_hash
        
        if __name__=='__main__':
            transactions=''
            difficulty = 6
            import time
            start=time.time()
            print("start mining")
            new_hash=mine(5,transactions,'0000vfdgshh00s6',difficulty)
            total_time=str((time.time()-start))
            print(f"{total_time}")
            print(new_hash)