def ax_0s(a: str):
    a = a.lstrip("0")
    if len(a) == 0:
        a = "0"
    return a

def sum(a: str, b: str):
    a = ax_0s(a)
    b = ax_0s(b)
    n = max(len(a), len(b))
    ra = a.rjust(n,"0")[::-1]
    rb = b.rjust(n,"0")[::-1]
    rc = ""
    carry = 0
    for i in range(n):
        s = int(ra[i]) + int(rb[i]) + carry
        rc += str(s%2)
        carry = s // 2
    rc += str(carry)
    return rc[::-1]

def sum3(a: str, b: str, c: str):
    a = ax_0s(a)
    b = ax_0s(b)
    c = ax_0s(c)
    n = max(len(a), len(b), len(c))
    ra = a.rjust(n,"0")[::-1]
    rb = b.rjust(n,"0")[::-1]
    rc = c.rjust(n,"0")[::-1]
    rd = ""
    carry = 0
    for i in range(n):
        s = int(ra[i]) + int(rb[i]) + int(rc[i]) + carry
        rd += str(s%2)
        carry = s // 2
    if carry == 0:
        rd += "00"
    elif carry == 1:
        rd += "10"
    elif carry == 2:
        rd += "01"
    return rd[::-1]

def sub(a: str, b: str):
    a = ax_0s(a)
    b = ax_0s(b)
    n = max(len(a), len(b))
    ra = a.rjust(n,"0")[::-1]
    rb = b.rjust(n,"0")[::-1]
    rc = ""
    carry = 0
    for i in range(n):
        s = int(ra[i]) - int(rb[i]) - carry
        rc += str(s%2)
        carry = 1 if s < 0 else 0
    return rc[::-1]


def mul3(a: str, b: str):
    a = a.rjust(3,"0")
    b = b.rjust(3,"0")
    if a == "000":
        return "0"
    if a == "001":
        return b
    if a == "010":
        return b + "0"
    if a == "011":
        return sum(b, b+"0")
    if a == "100":
        return b + "00"
    if a == "101":
        return sum(b, b+"00")
    if a == "110":
        return sum(b+"00", b+"0")
    if a == "111":
        return sum3(b, b+"0", b+"00")
    raise Exception(f"Wrong size of {a}: {len(a)}")

def mul(a: str, b: str):
    a = ax_0s(a)
    b = ax_0s(b)

    n = max(len(a), len(b))
    if n <= 3:
        return mul3(a,b)

    if n % 2 == 1:
        n += 1

    mid = n//2
    a = a.rjust(n,"0")
    b = b.rjust(n,"0")

    a1 = a[:mid]
    a2 = a[mid:]
    b1 = b[:mid]
    b2 = b[mid:]

    # m1 = a1*b1
    # m2 = a2*b2
    # m3 = (a1+a2)*(b1+b2) = m1 + a1*b2 + a2*b1 + m2
    # m4 = m3 - (m1 + m2)
    # a*b = m = m1*2^n + m4*2^mid + m2
    
    m1 = mul(a1, b1)
    m2 = mul(a2, b2)
    p1 = sum(a1,a2)
    p2 = sum(b1,b2)
    m3 = mul(p1, p2)
    m4 = sub(m3, sum(m1, m2))

    m1 = m1 + "0"*n
    m4 = m4 + "0"*mid

    return sum3(m4,m2,m1)


if __name__ == "__main__":
    n_dig = int(input())
    x = input().strip()
    y = input().strip()
    xy = mul(x,y)
    xy = ax_0s(xy)
    print(xy)