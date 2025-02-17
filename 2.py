def numbers(n):
    if n < 1:
        print("son 1 dan kichik bolishi mumkin emas:")
    else:
        for i in range(1, n + 1):
            if (i % 2 == 0):
                print(i)


number=int(input("istalgan son kiriting:"))

numbers(number)