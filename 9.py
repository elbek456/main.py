# 1-misol
# matn = input("matin kiriting:")
#
# with open("input.txt", "w") as file:
#     file.write(matn)
#
# print("malumot fayilga mofaqiyatli joylandi:")


# 2-misol
# with open("input.txt", "r") as file:
#     matn = file.read()
#
# sozlar = matn.split()
# for soz in sozlar:
#     print(soz)


# 3-misol
# import json
#
# kompyuter = {
#     "ism": "Elbek",
#     "Familiya": "Umaraliyev",
#     "yosh": 20,
#     "viloyati": "Toshkent",
#     "tumani": "Ohangaron",
#     "Kasbi": "dasturchi"
# }
#
# with open("string.txt", "w") as txt_fayl:
#     txt_fayl.write(str(kompyuter))
#
# print("Ma'lumotlar string.txt fayliga saqlandi.")
#
# with open("json.json", "w") as json_fayl:
#     json.dump(kompyuter, json_fayl, indent=0)
# print("Ma'lumotlar json.json fayliga JSON shaklida saqlandi.")


# 4-misol
# import json
#
# with open('string.txt', 'r') as file:
#     string_data = file.read()
#
# with open('json.json', 'w') as json_file:
#     json.dump({"data": string_data}, json_file)
#
# with open('json.json', 'r') as json_file:
#     json_data = json.load(json_file)
#
# print(json.dumps(json_data))
