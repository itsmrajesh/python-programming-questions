def binary_to_octal(n):
    n=int(n)
    a = 1
    octal = 0
    while n > 0:
        octal += (n % 10) * a
        a *= 2
        n //= 10
    return octal


print(binary_to_octal(input()))
