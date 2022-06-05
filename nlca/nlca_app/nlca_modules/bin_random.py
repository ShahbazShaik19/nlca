import random
def rand_bin(n):
    bin_str = ""
    for i in range(n):
        x = one_or_zero()
        bin_str += str(x)

    return bin_str

def one_or_zero():
    num = random.randint(0,1)
    return num
