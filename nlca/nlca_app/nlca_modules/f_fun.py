import random
from pq_tables import * 

#raw_key= rand_bin(16)
#print(raw_key)
def f_fun(raw_key):
    r1_1= P(raw_key[0:4])
    r1_2= Q(raw_key[4:8])
    r1_3= P(raw_key[8:12])
    r1_4= Q(raw_key[12:16])

    r2_1= Q(r1_1[0:2]+r1_2[0:2])
    r2_2= P(r1_1[2:4]+r1_3[0:2])
    r2_3= Q(r1_2[2:4]+r1_4[0:2])
    r2_4= P(r1_3[2:4]+r1_4[2:4])

    #print(r1_1)
    #print(r1_2)
    #print(r2_1)
    #print(r2_2)

    r3_1= P(r2_1[0:2]+r2_2[0:2])
    r3_2= Q(r2_1[2:4]+r2_3[0:2])
    r3_3= P(r2_2[2:4]+r2_4[0:2])
    r3_4= Q(r2_3[2:4]+r2_4[2:4])

    #print(r3_1)
    #print(r3_2)
    #print(r3_3)
    #print(r3_4)
    return [r3_1,r3_2,r3_3,r3_4]
