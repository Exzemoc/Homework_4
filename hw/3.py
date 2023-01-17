x = [12, 12, 32, 42, 124, 35, 43, 623, 423, 3, 57, 47, 54, 67, 568, 56, 4, 56, 35, 34, 5, 2436, 35, 7, 457, 45, 3, 3245,
     23, 53, 476, 45, 74, 7, ]


def count_ident_elements(a):
    k = 0
    y = set(a)
    for i in y:
        for j in a:
            if j == i:
                k += 1
        print(i, '=', k)
        k = 0


count_ident_elements(x)
