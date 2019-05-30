import re


# 1
N = 90000
GC = 0.6
string = 'ACGGTCGGG'

count_GC = string.count('G') + string.count('C')
count_AT = string.count('A') + string.count('T')
prob = ((0.5 * GC) ** count_GC) * ((0.5 * (1 - GC)) ** count_AT)

probability = 1 - (1 - prob) ** N


# 2

dict = {'A':71.03711, 'C':103.00919, 'D':115.02694, 'E':129.04259, 'F':147.06841, 'G':57.02146, 'H':137.05891, 'I':113.08406, 'K':128.09496, 'L':113.08406, 'M':131.04049, 'N':114.04293, 'P':97.05276, 'Q':128.05858, 'R':156.10111, 'S':87.03203, 'T':101.04768, 'V':99.06841, 'W':186.07931, 'Y':163.06333}

weights = (3524.8542,3710.9335,3841.974,3970.0326,4057.0646)

weights = weights[::-1]
amino = []

for i in range(1,len(weights)):
    amino.append(round(weights[i-1]-weights[i],2))

for key,val in dict.items():
    for j in amino:
        if j == round(val,2):
            print(key)

# 3





