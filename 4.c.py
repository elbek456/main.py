
numbers_tuple = tuple(range(10, 31))

tson = []
json = []

index = 0
while index < len(numbers_tuple):
    number = numbers_tuple[index]
    if number % 2 == 0:
        json.append(number)
    else:
        tson.append(number)
    index += 1

toq_son = len(tson)
juft_son = len(json)

if toq_son > juft_son:
    comparison = "Toq sonlar ko'proq"
else:
    comparison = ("Juft sonlar ko'proq")

print("Tuple:", numbers_tuple)
print("Toq sonlar listi:", tson)
print("Juft sonlar listi:", json)
print("Toq sonlar soni:", toq_son)
print("Juft sonlar soni:", juft_son)
print("Natija:", comparison)