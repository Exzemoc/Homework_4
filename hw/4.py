def timenow(n):
    from datetime import datetime
    from time import sleep
    a = (i for i in range(1, n + 1))
    for i in a:
        print(datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
        sleep(i / i)


timenow(int(input()))
