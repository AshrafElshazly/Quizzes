import random

def generate():
    return random.randint(1, 200)

n = generate()

def is_prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False
        
print(is_prime(2))
