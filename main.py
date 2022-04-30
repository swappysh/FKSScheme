# 26-adic FKS schemes
from collections import defaultdict

# 40 common words
K = {"A", "ABOUT", "AN", "AND", "ARE", "AS", "AT", "BE", "BOY", "BUT", "BY", "FOR", "FROM", "HAD", "HAVE", "HE", "HER", "HIS", "HIM", "I", "IN", "IS", "IT", "NOT", "OF", "ON", "OR", "SHE", "THAT", "THE", "THEY", "THIS", "TO", "WAS", "WHAT", "WHERE", "WHICH", "WHY", "WITH", "YOU"}

# 26-adic scheme
def computeValue(x):
  res = 0
  A_unicode = ord('A')
  for c in reversed(x):
    # print(c)
    res = res * 26 + (ord(c) - A_unicode + 1)
  
  return res

def computeHk(k, x):
  return (((k*x) % 12356633) % 40)

def isGood(k):
  n = 40
  b = defaultdict(int)
  for x in K:
    # print(x, computeValue(x), computeHk(k, computeValue(x)))
    b[computeHk(k, computeValue(x))] += 1

  # print(b)
  # Check if constraint is satisfied
  cons = 0
  for k, v in b.items():
    cons += (v*(v-1))/2

  return cons < n

for i in range(1, 41):
  print(i, ":", isGood(i))
# isGood(1)