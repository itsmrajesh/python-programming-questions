import math as m


def is_prime(n):
    """Checks wheather given number is prime or not  """
    n=int(n)
    if n <= 1:
        return False
    else:
        val = round(m.sqrt(n))
        for i in range(2, val + 1):
            if n % i == 0:
                return False
        return True
