#from bin_random import rand_bin
#from logicop import xor
from pq_tables import *
from f_fun import f_fun
from transf import *

#raw_key= rand_bin(64)
#print(raw_key)

def key_gen(raw_key):
    key_4bit= []
    for i in range(16):
        key_4bit.append([raw_key[4*i:4*i+4]])

    #print(key_4bit)

    kbf_dict={}
    for i in range(4):
        temp=''
        for j in range(4):
            temp= temp+str(key_4bit[4*(j)+i][0])        #kbif=(j=0 to 4)concat(key_4bit[4(j-1)_i])
        kbf_dict["kb"+str(i+1)+"f"]= temp

    #print(kbf_dict)

    kaf_dict={}
    for i in range(4):
        kaf_dict["ka"+str(i+1)+"f"]= f_fun(kbf_dict["kb"+str(i+1)+"f"])   

    #print(kaf_dict)

    for i in range(4):
        if i==1:
            K1=transf1(kaf_dict["ka"+str(i+1)+"f"])
        if i==2:
            K2=transf2(kaf_dict["ka"+str(i+1)+"f"])
        if i==3:
            K3=transf3(kaf_dict["ka"+str(i+1)+"f"])
        if i==0:
            K4=transf4(kaf_dict["ka"+str(i+1)+"f"])


   # K12=xor(K1,K2)
    #K34=xor(K3,K4)
   #K5=xor(K12,K34)

    return K1,K2,K3,K4




