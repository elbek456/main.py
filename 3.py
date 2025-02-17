def juft_son(n):
    n1 = 0
    for i in range(n, -1, -1):
        if i % 2 == 0:
            n1 += i
    print(f"Juft sonlarning yig'indisi: {n1}")


def toq_son(n):
    n1 = 0
    for i in range(n, -1, -1):
        if i % 2 != 0:
            n1 += i
    print(f"Toq sonlarning yig'indisi: {n1}")


def natija():
    n = int(input("Sonni kiriting: "))
    if n % 2 == 0:
        juft_son(n)
    else:
        toq_son(n)


natija()
