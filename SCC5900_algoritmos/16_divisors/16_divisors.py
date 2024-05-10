max_n = 1000001
max_div = 1001

spf = []
primes = []
def sieve():
    global spf, primes
    spf = [i for i in range(max_n)]
    spf[0] = spf[1] = 1
    for i in range(2, max_div):
        if spf[i] == i:
            primes.append(i)
            for j in range(i * i, max_n, i):
                if spf[j] == j:
                    spf[j] = i

def get_divisors(n):
    global spf, primes
    divisors = {}
    while n != 1:
        divisors[spf[n]] = divisors.get(spf[n], 0) + 1
        n //= spf[n]
    return divisors

def get_divisor_amount(n):
    divisors = get_divisors(n)
    amount = 1
    for key in divisors:
        amount *= (divisors[key] + 1)
    return amount

if __name__ == '__main__':
    n = int(input())
    sieve()
    for i in range(n):
        num = int(input())
        amount = get_divisor_amount(num)
        print(amount)
        