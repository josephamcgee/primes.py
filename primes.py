import sys

# Playing with the recursion limit due to printed primes maxing out on default at a little over 100 due to nested recursion

limitStart = sys.getrecursionlimit()
# Set initial (default) recursion limit

def nats(n):
    yield n
    yield from nats(n+1)

def sieve(s):
    n = next(s)
    yield n
    yield from sieve(i for i in s if i%n!=0)

sInt = 2
print("How many primes?")
iterate = int(input())

result = sieve(nats(sInt))

sys.setrecursionlimit(limitStart + iterate)
# Set recursion limit prior to while loop

while(iterate>=0):
    prime = next(result)
    print(prime)
    iterate = iterate - 1

sys.setrecursionlimit(limitStart)
# Reset recursion limit
