import math

# x = 400
# kv = 2
# kb = 3
# sqrt = int(math.sqrt(x))
# power = int(math.pow(5,kb))
# print(power)
# x=6
# print(math.ceil(x))
# math.ceil(x) x dan kotta yoki teng soni qataradi
# print(math.fabs(x))
# print(math.exp(x))
import random as r

# sonlar = r.sample(range(100),10)
# print(sonlar)
# def  juftmi(x):
#     return x%2==0

# juft_sonlar = list(filter(juftmi,sonlar))
# print(juft_sonlar)
# juft_sonlar = list(filter(lambda son:son%2==0,sonlar))
# print(juft_sonlar)
mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

a_r = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')),mevalar ))
print(a_r)