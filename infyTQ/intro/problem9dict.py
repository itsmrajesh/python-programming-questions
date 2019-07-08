# PF-Prac-9
def generate_dict(number):
    new_dict = {k: k * k for k in range(1, number + 1)}

    return new_dict


number = 20
print(generate_dict(number))
