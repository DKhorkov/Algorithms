def alg_of_Evklid(num_1, num_2):
    a = num_1
    b = num_2
    while not a == b:
        if a % b == 0:
            return b
        else:
            c = a % b
            a = b
            b = c


res = alg_of_Evklid(15, 10)
print(res)
