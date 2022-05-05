# 26-adic FKS schemes
from collections import defaultdict

# 40 common words
K = {"A", "ABOUT", "AN", "AND", "ARE", "AS", "AT", "BE", "BOY", "BUT", "BY", "FOR", "FROM", "HAD", "HAVE", "HE", "HER", "HIS", "HIM", "I", "IN", "IS", "IT", "NOT", "OF", "ON", "OR", "SHE", "THAT", "THE", "THEY", "THIS", "TO", "WAS", "WHAT", "WHERE", "WHICH", "WHY", "WITH", "YOU"}

# 26-adic scheme
def computeValue(x):
  res = 0
  A_unicode = ord('A')
  for c in x:
    # print(c)
    res = res * 26 + (ord(c) - A_unicode + 1)
  
  return res

def computeHk(k, x):
  return (((k*x) % 12356633) % 40)

b = defaultdict(int)

def isGood(k):
  n = 40
  b.clear()
  for x in K:
    # print(x, computeValue(x), computeHk(k, computeValue(x)))
    # print(x, computeValue(x))
    b[computeHk(k, computeValue(x))] += 1

  # print(b)
  # Check if constraint is satisfied
  cons = 0
  for k, v in b.items():
    cons += (v*(v-1))/2

  return b, cons < n

def isPerfect(k, i):
  if b[i] == 0:
    return False

  count = 0
  for x in K:
    if (((k*computeValue(x)) % 12356633) % (b[i]*b[i])) == i:
      count += 1

  return count == 1

# for k in range(1, 41):
#   b, isGoodK = isGood(k)
#   if isGoodK:
#     print(k, ":", isGoodK)
#   for i in range(40):
#     if isPerfect(k, i):
#       print("isPerfect -> k:", k, " i:", i, " ", isPerfect(k, i))

b, isGoodK = isGood(1)
print(isGoodK, b)

# for k0 in range(1, 41):
#   b, isGoodK = isGood(k0)
#   for i in range(40):
#     k = 1
#     while not isPerfect(k, i) and k < 100:
#       k += 1
#     print("isPerfect -> k:", k, " i:", i, " ", isPerfect(k, i))