def xnor(plaintext,key):
    ciphertext=''
    for i in range(32):
         if plaintext[i]==key[i]:
             ciphertext +="1"
         else:
             ciphertext +="0"
    return ciphertext 

def xor(plaintext,key):
    ciphertext=""
    for i in range(32):
         if plaintext[i]!=key[i]:
             ciphertext +="1"
         else:
             ciphertext +="0"
    return ciphertext 