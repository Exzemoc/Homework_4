x = {'one': 1, 'two': 2, 'three': 3}
print(x)


def reverse_dict(a):
    i = {v: k for k, v in a.items()}
    print(i)


reverse_dict(x)
