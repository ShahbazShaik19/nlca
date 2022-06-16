def hex_to_bin(h):
    b=bin(int(h, base=16))
    b=str(b)[2:]
    diff=128-len(b)
    for i in range(diff):
        b='0'+b
    return b

#print(hex_to_bin('2A1'))