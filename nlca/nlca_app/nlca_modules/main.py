from key_generation import key_gen
from bin_random import rand_bin
from encryption import encr_round
from bin_to_hex import b2h
from logicop import xor


#This function Swaps and returns the blocks
def swap(b1, b2, b3, b4):
    return b2,b1,b4,b3

raw_key= rand_bin(128)
plaintext= rand_bin(128)                             

p1=plaintext[:32]
p2=plaintext[32:64]
p3=plaintext[64:96]
p4=plaintext[96:128]

K1,K2,K3,K4= key_gen(raw_key[:64])
K5,K6,K7,K8= key_gen(raw_key[64:])

KK1= K1+K2
KK2= K3+K4
KK3= K5+K6
KK4= K7+K8

KKK=xor(xor(KK1,KK2),xor(KK3,KK4))

#round1
r1_1,r1_2,r1_3,r1_4= encr_round(KK1,p1,p2,p3,p4)
r1_1,r1_2,r1_3,r1_4= swap(r1_1,r1_2,r1_3,r1_4)

#round2
r2_1,r2_2,r2_3,r2_4= encr_round(KK2,r1_1,r1_2,r1_3,r1_4)
r2_1,r2_2,r2_3,r2_4= swap(r2_1,r2_2,r2_3,r2_4)

#round3
r3_1,r3_2,r3_3,r3_4= encr_round(KK3,r2_1,r2_2,r2_3,r2_4)
r3_1,r3_2,r3_3,r3_4= swap(r3_1,r3_2,r3_3,r3_4)

#round4
r4_1,r4_2,r4_3,r4_4= encr_round(KK4,r3_1,r3_2,r3_3,r3_4)
r4_1,r4_2,r4_3,r4_4= swap(r4_1,r4_2,r4_3,r4_4)

#round5
r5_1,r5_2,r5_3,r5_4= encr_round(KKK,r4_1,r4_2,r4_3,r4_4)

print("\nPlainText (128-Bit) =",b2h(plaintext))
print("\nKey 1 (32-Bit)=",b2h(KK1))
print("Key 2 (32-Bit)=",b2h(KK2))
print("Key 3 (32-Bit)=",b2h(KK3))
print("Key 4 (32-Bit)=",b2h(KK4))
print("Key 5 (32-Bit)=",b2h(KKK))
print("\nCipherText (128-Bit)=",b2h(r5_1+r5_2+r5_3+r5_4)+"\n")
