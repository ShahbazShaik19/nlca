from nlca_app.nlca_modules.ascii import atoh
from nlca_app.nlca_modules.decryption import decryption
from nlca_app.nlca_modules.hex_to_bin import hex_to_bin
from nlca_app.nlca_modules.key_generation import key_gen
from nlca_app.nlca_modules.encryption_round import encr_round
from nlca_app.nlca_modules.bin_to_hex import b2h
from nlca_app.nlca_modules.logicop import xor


#This function Swaps and returns the blocks
def swap(b1, b2, b3, b4):
    return b2,b1,b4,b3 

def encryption_128(plaintext, KK1, KK2, KK3, KK4, KKK):
    p1=plaintext[:32]
    p2=plaintext[32:64]
    p3=plaintext[64:96]
    p4=plaintext[96:128]

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

    return b2h(r5_1+r5_2+r5_3+r5_4,False)

def padd(pt):
    pt2=''
    pad_bits=bin((32-len(pt))//2)[2:]
    for i in range(4-len(pad_bits)):
        pad_bits='0'+pad_bits
    #print(b2h("0110", False))
    for i in range((32-len(pt))//2):
        pt2+= '0'+b2h(pad_bits, False)

    return pt2

def encryption(pt, key):          
    raw_key= hex_to_bin(key)
    K1,K2,K3,K4= key_gen(raw_key[:64])
    K5,K6,K7,K8= key_gen(raw_key[64:])

    KK1= K1+K2
    KK2= K3+K4
    KK3= K5+K6
    KK4= K7+K8

    KKK=xor(xor(KK1,KK2),xor(KK3,KK4))

    pt=atoh(pt)
    pt2=''
    ct=''
    if len(pt)<32:
        pt2=padd(pt)
        print(pt+' '+pt2)
        ct=encryption_128(hex_to_bin(pt+pt2),KK1,KK2,KK3,KK4,KKK)

    elif len(pt)>32:
        for i in range(len(pt)//32):
            print(pt[32*i:32*(i+1)])
            plaintext= hex_to_bin(pt[32*i:32*(i+1)])
            ct+=encryption_128(plaintext,KK1,KK2,KK3,KK4,KKK)


        left_out=pt[len(pt)-len(pt)%32:]
        pt2= padd(left_out)

        print(left_out,len(pt2))
        ct+=encryption_128(hex_to_bin(left_out+pt2),KK1,KK2,KK3,KK4,KKK)

    else:
        print(pt)
        ct=encryption_128(hex_to_bin(pt),KK1,KK2,KK3,KK4,KKK)
    print(ct)

    return b2h(KK1,True), b2h(KK2,True), b2h(KK3,True), b2h(KK4,True), b2h(KKK,True), ct


# print("\nPlainText (128-Bit) =",b2h(plaintext))
# print("\nKey 1 (32-Bit)=",b2h(KK1))
# print("Key 2 (32-Bit)=",b2h(KK2))
# print("Key 3 (32-Bit)=",b2h(KK3))
# print("Key 4 (32-Bit)=",b2h(KK4))
# print("Key 5 (32-Bit)=",b2h(KKK))
# print("\nCipherText (128-Bit)=",b2h(r5_1+r5_2+r5_3+r5_4)+"\n")
# pt="A"
# key="5EB351B66418A817978D5E2D8DE2CAC5"
# print(encryption(pt,key))