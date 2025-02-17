ls1 = [10, 20, 30, 40, 50, 60, 70]

print("Oldingi list:", ls1)

if len(ls1) >= 2:
    ls1[0], ls1[-1] = ls1[-1], ls1[0]

print("Keyingi list:", ls1)