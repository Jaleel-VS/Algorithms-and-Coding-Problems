def primeFactors(n):
    count = {}

    while n != 1:
        for i in range(2, int(n**0.5)+1):
            if not n % i:
                count[i] = count.get(i, 0) + 1
                n //= i
                break
        else:
            count[n] = count.get(n, 0) + 1
            break
    items = sorted(count.items(), key=lambda x: x[0])
    print(items)
    return ''.join(['({}**{})'.format(k, v) if v > 1 else '({})'.format(k) for k, v in items])