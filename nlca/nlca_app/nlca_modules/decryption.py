import time
from nlca_app.nlca_modules.ascii import atoh, btoa
from nlca_app.nlca_modules.hex_to_bin import hex_to_bin
from nlca_app.nlca_modules.key_generation import key_gen
from nlca_app.nlca_modules.decryption_round import decr_round
from nlca_app.nlca_modules.bin_to_hex import b2h
from nlca_app.nlca_modules.logicop import xor


#This function Swaps and returns the blocks
def swap(b1, b2, b3, b4):
    return b2,b1,b4,b3

def decryption_128(plaintext, KK1, KK2, KK3, KK4, KKK):
    p1=plaintext[:32]
    p2=plaintext[32:64]
    p3=plaintext[64:96]
    p4=plaintext[96:128]

     #round1
    d1_1,d1_2,d1_3,d1_4= decr_round(KKK,p1,p2,p3,p4)
    d1_1,d1_2,d1_3,d1_4= swap(d1_1,d1_2,d1_3,d1_4)

    #round2
    d2_1,d2_2,d2_3,d2_4=decr_round(KK4,d1_1,d1_2,d1_3,d1_4)
    d2_1,d2_2,d2_3,d2_4=swap(d2_1,d2_2,d2_3,d2_4)

    #round3
    d3_1,d3_2,d3_3,d3_4= decr_round(KK3,d2_1,d2_2,d2_3,d2_4)
    d3_1,d3_2,d3_3,d3_4=swap(d3_1,d3_2,d3_3,d3_4)

    #round4
    d4_1,d4_2,d4_3,d4_4= decr_round(KK2,d3_1,d3_2,d3_3,d3_4)
    d4_1,d4_2,d4_3,d4_4=swap(d4_1,d4_2,d4_3,d4_4)

    #round5
    d5_1,d5_2,d5_3,d5_4= decr_round(KK1,d4_1,d4_2,d4_3,d4_4)

    decrpttext=d5_1+d5_2+d5_3+d5_4
    return b2h(decrpttext, False), '0'

def decryption(pt, key):
    
    raw_key= hex_to_bin(key)
    plaintext= hex_to_bin(pt)

    K1,K2,K3,K4= key_gen(raw_key[:64])
    K5,K6,K7,K8= key_gen(raw_key[64:])

    KK1= K1+K2
    KK2= K3+K4
    KK3= K5+K6
    KK4= K7+K8

    KKK=xor(xor(KK1,KK2),xor(KK3,KK4))

    decrpttext=''
    decrypt_hex=''
    if len(plaintext)%128!=0:
        for i in range(128-len(plaintext)%128):
            plaintext='0'+plaintext
    print("from decr",len(plaintext))
    if len(plaintext)>128:
        for i in range(len(plaintext)//128):
            print('in for loop ',len(plaintext[128*i:128*(i+1)]))
            plaintext_temp= plaintext[128*i:128*(i+1)]
            decrypt_hex, zero=decryption_128(plaintext_temp,KK1,KK2,KK3,KK4,KKK)
            decrpttext+=decrypt_hex

    else:
        decrypt_hex, zero=decryption_128(plaintext,KK1,KK2,KK3,KK4,KKK)
        decrpttext+=decrypt_hex

        print("from decr",decrypt_hex)
    print('decrtextc',decrpttext)
    if decrpttext[-1] in '0123456789ABCDEF':
        pad_bit= int(decrpttext[-1],16)
        check_str=''
        for i in range(pad_bit):
            check_str+='0'+decrpttext[-1]

        print('padding',decrpttext[-2*pad_bit:])
        if check_str==decrpttext[-2*pad_bit:]:
            print(decrpttext[0:-2*pad_bit])
            decrpttext=decrpttext[0:-2*pad_bit]


        print(pad_bit)

    return b2h(KK1,True), b2h(KK2,True), b2h(KK3,True), b2h(KK4,True), b2h(KKK,True), decrpttext, btoa(hex_to_bin(decrpttext)), zero

    


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