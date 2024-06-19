def factorize(n):
    factors = []
    divisor = 2
    while n > 1:
        if n % divisor == 0:
            count = 0
            while n % divisor == 0:
                count += 1
                n //= divisor
            factors.append(' ' + str(divisor) + ('^' + str(count) if count > 1 else ''))
        else:
            divisor += 1
    return ' *'.join(factors)[1:]  
while True:
    try:
        num = int(input())
        print(factorize(num))
    except EOFError:
        break
