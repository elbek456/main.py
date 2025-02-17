# 1-misoll
# class Ishchi:
#     def __init__(self, id: int, ism: str, familiya: str, maosh: int):
#         self.id = id
#         self.ism = ism
#         self.familiya = familiya
#         self.maosh = maosh
#
#     def id_olish(self) -> int:
#         return self.id
#
#     def ism_olish(self) -> str:
#         return self.ism
#
#     def familiya_olish(self) -> str:
#         return self.familiya
#
#     def toliq_ism_olish(self) -> str:
#         return f"{self.ism} {self.familiya}"
#
#     def maosh_olish(self) -> int:
#         return self.maosh
#
#     def maosh_ozgartirish(self, yangi_maosh: int):
#         if yangi_maosh <= 0:
#             raise ValueError("Maosh musbat son bo'lishi kerak!")
#         self.maosh = yangi_maosh
#
#     def yillik_maosh(self) -> int:
#         return self.maosh * 12
#
#     def maosh_oshirish(self, foiz: int) -> int:
#         if foiz < 0:
#             raise ValueError("Foiz manfiy bo'lishi mumkin emas!")
#         self.maosh += self.maosh * foiz // 100
#         return self.maosh
#
#     def malumot(self) -> str:
#         return f"Ishchi[id={self.id}, ism={self.toliq_ism_olish()}, maosh={self.maosh}]"
#
#
# if __name__ == "__main__":
#     ishchi = Ishchi(id=632322, ism="Elbek", familiya="Umaraliyev", maosh=5000)
#
#     print("ID:", ishchi.id_olish())
#     print("Ism:", ishchi.ism_olish())
#     print("Familiya:", ishchi.familiya_olish())
#     print("To'liq ism:", ishchi.toliq_ism_olish())
#     print("Hozirgi maosh:", ishchi.maosh_olish())
#
#     ishchi.maosh_ozgartirish(6000)
#     print("Yangi maosh:", ishchi.maosh_olish())
#
#     print("Yillik maosh:", ishchi.yillik_maosh())
#
#     ishchi.maosh_oshirish(10)
#     print("10% oshgandan keyin maosh:", ishchi.maosh_olish())
#
#     print("Ishchi haqida:", ishchi.malumot())
#
#
# 2-misoll
# class Circle:
#     def __init__(self, radius, color):
#         self.radius = radius
#         self.color = color
#
#     def get_radius(self):
#         return self.radius
#
#     def set_radius(self, radius):
#         self.radius = radius
#
#     def get_color(self):
#         return self.color
#
#     def set_color(self, color):
#         self.color = color
#
#     def get_area(self):
#         return 3.14 * self.radius * self.radius
#
#     def get_circumference(self):
#         return 2 * 3.14 * self.radius
#
#     def get_info(self):
#         return f"Radius: {self.radius}, Rang: {self.color}, Yuzasi: {self.get_area()}, Aylana uzunligi: {self.get_circumference()}"
#
#
# doira = Circle(5, "ko'k")
# print(doira.get_info())
#
# doira.set_radius(10)
# doira.set_color("ko'k")
# print(doira.get_info())
#

# 3-misoll
# class Rectangle:
#     def __init__(self, height, width):
#         self.height = height
#         self.width = width
#
#     def get_height(self):
#         return self.height
#
#     def set_height(self, height):
#         self.height = height
#
#     def get_width(self):
#         return self.width
#
#     def set_width(self, width):
#         self.width = width
#
#     def get_area(self):
#         return self.height * self.width
#
#     def get_perimeter(self):
#         return 2 * (self.height + self.width)
#
#     def get_info(self):
#         return f"Bo'yi: {self.height}, Enni: {self.width}, Yuzasi: {self.get_area()}, Perimetr: {self.get_perimeter()}"
#
#
# tortburchak = Rectangle(5, 10)
# print(tortburchak.get_info())
#
# tortburchak.set_height(8)
# tortburchak.set_width(12)
# print(tortburchak.get_info())


# 4-misoll
# class Account:
#     def __init__(self, id, name, balance=0):
#         self.id = id
#         self.name = name
#         self.balance = balance
#
#     def get_id(self):
#         return self.id
#
#     def get_name(self):
#         return self.name
#
#     def get_balance(self):
#         return self.balance
#
#     def credit(self, amount):
#         self.balance += amount
#         return self.balance
#
#     def debit(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Amount exceeded balance")
#         return self.balance
#
#     def transfer(self, another_account, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             another_account.credit(amount)
#         else:
#             print("Amount exceeded balance")
#         return self.balance
#
#
# account1 = Account("001", "Elbek", 500)
# account2 = Account("002", "Raxmatilo", 300)
#
# print(f"Account[id={account1.id}, name={account1.name}, balance={account1.balance}]")
# print(f"Account[id={account2.id}, name={account2.name}, balance={account2.balance}]")
#
# account1.credit(200)
# print(f"Account[id={account1.id}, name={account1.name}, balance={account1.balance}]")
#
# account1.debit(100)
# print(f"Account[id={account1.id}, name={account1.name}, balance={account1.balance}]")
#
# account1.transfer(account2, 300)
# print(f"Account[id={account1.id}, name={account1.name}, balance={account1.balance}]")
# print(f"Account[id={account2.id}, name={account2.name}, balance={account2.balance}]")


# 5-misoll
# class Date:
#     def __init__(self, day: int, month: int, year: int):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def getDay(self) -> int:
#         return self.day
#
#     def getMonth(self) -> int:
#         return self.month
#
#     def getYear(self) -> int:
#         return self.year
#
#     def setDay(self, day: int):
#         self.day = day
#
#     def setMonth(self, month: int):
#         self.month = month
#
#     def setYear(self, year: int):
#         self.year = year
#
#     def setDate(self, day: int, month: int, year: int):
#         self.day = day
#         self.month = month
#         self.year = year
#
#     def toString(self) -> str:
#         return f"{self.day:02}/{self.month:02}/{self.year}"
#
# date = Date(31, 12, 2025)
# print("Hozirgi sana:", date.toString())
#
# date.setDay(1)
# date.setMonth(1)
# date.setYear(2026)
# print("Yangi sana:", date.toString())
#
# date.setDate(15, 7, 2023)
# print("O‘zgartirilgan sana:", date.toString())
#
#
# 6-misoll
# class Time:
#     def __init__(self, hour: int, minute: int, second: int):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     def getHour(self) -> int:
#         return self.hour
#
#     def getMinute(self) -> int:
#         return self.minute
#
#     def getSecond(self) -> int:
#         return self.second
#
#     def setHour(self, hour: int):
#         self.hour = hour
#
#     def setMinute(self, minute: int):
#         self.minute = minute
#
#     def setSecond(self, second: int):
#         self.second = second
#
#     def setTime(self, hour: int, minute: int, second: int):
#         self.hour = hour
#         self.minute = minute
#         self.second = second
#
#     def toString(self) -> str:
#         return f"{self.hour:02}:{self.minute:02}:{self.second:02}"
#
#     def nextSecond(self):
#         self.second += 1
#         if self.second == 60:
#             self.second = 0
#             self.minute += 1
#             if self.minute == 60:
#                 self.minute = 0
#                 self.hour += 1
#                 if self.hour == 24:
#                     self.hour = 0
#         return self
#
#     def previousSecond(self):
#         self.second -= 1
#         if self.second == -1:
#             self.second = 59
#             self.minute -= 1
#             if self.minute == -1:
#                 self.minute = 59
#                 self.hour -= 1
#                 if self.hour == -1:
#                     self.hour = 23
#         return self
#
#
# # Sinov uchun kod
# time = Time(23, 59, 59)
# print("Hozirgi vaqt:", time.toString())
# time.nextSecond()
# print("Keyingi soniya:", time.toString())
# time.previousSecond()
# time.previousSecond()
# print("Oldingi soniya:", time.toString())


# 7-misol
# class Kitob:
#     def __init__(self, muallif, nomi, betlar, narx, nashr_yili):
#
#         if not muallif:
#             raise ValueError("Muallif maydoni bo'sh bo'lishi mumkin emas.")
#         muallif_sozlar = muallif.split()
#
#         if len(muallif_sozlar) < 2 or len(muallif_sozlar) > 4:
#             raise ValueError("Muallif 2-4 so'zdan iborat bo'lishi kerak.")
#
#         if not all(soz.istitle() for soz in muallif_sozlar):
#             raise ValueError("Muallifning har bir so'zi bosh harf bilan boshlanishi kerak.")
#
#         self.muallif = muallif
#
#
#         if len(nomi) < 5:
#             raise ValueError("Kitob nomi kamida 5 ta harfdan iborat bo'lishi kerak.")
#
#         if not nomi[0].isupper():
#             raise ValueError("Kitob nomi bosh harf bilan boshlanishi kerak.")
#
#         if len(nomi) > 128:
#             raise ValueError("Kitob nomining uzunligi 128 ta belgidan oshmasligi kerak.")
#
#         self.nomi = nomi
#
#         if betlar < 5:
#             raise ValueError("Kitob kamida 5 betdan iborat bo'lishi kerak.")
#
#         self.betlar = betlar
#
#         if narx < 0:
#             raise ValueError("Kitob narxi manfiy bo'lishi mumkin emas.")
#
#         self.narx = narx
#
#         if not isinstance(nashr_yili, int) or nashr_yili <= 0:
#             raise ValueError("Nashr yili musbat butun son bo'lishi kerak.")
#
#         self.nashr_yili = nashr_yili
#
#     def malumot_korsat(self):
#         # Kitob haqida ma'lumot chiqarish
#         print("Muallif:", self.muallif)
#         print("Nomi:", self.nomi)
#         print("Betlar soni:", self.betlar)
#         print("Narxi: $", self.narx)
#         print("Nashr yili:", self.nashr_yili)
#
#     def qalinmi(self):
#         return self.betlar >= 500
#
#
# try:
#     yangi_kitob = Kitob(
#         muallif="Umaraliyev Elbek",
#         nomi="Python dasturi",
#         betlar=550,
#         narx=45.67,
#         nashr_yili=2020
#     )
#
#
#     yangi_kitob.malumot_korsat()
#
#
#     if yangi_kitob.qalinmi():
#         print("Kitob juda qalin:")
#     else:
#         print("Kitob qalin emas:")
#
# except ValueError as xato:
#     print("Xatolik:", xato)


# 1-misoll
# class kitob:
#     def __init__(self, nomi, muallif, nashr_yili):
#         self.nomi = nomi
#         self.muallif = muallif
#         self.nashr_yili = nashr_yili
#
#     def malumot(self):
#         return f"Nomi:{self.nomi},Muallif:{self.muallif},Nashr_yili:{self.nashr_yili}"
#
#
# class BadiiyKitob(kitob):
#     def __init__(self, nomi, muallif, nashr_yili, janr):
#         super().__init__(nomi, muallif, nashr_yili)
#         self.janr = janr
#
#     def malumot(self):
#         return super().malumot() + f"janr:{self.janr}"
#
#
# class IlmiyKitob(kitob):
#     def __init__(self, nomi, muallif, nashr_yili, yonalish):
#         super().__init__(nomi,muallif,nashr_yili)
#         self.yonalish=yonalish
#     def malumot(self):
#         return super().malumot() + f"Yo'nalish:{self.yonalish}"
#
# kitob1 = BadiiyKitob("Sherlar", "Alisher Navoiy", 1492, "She'riyat")
# kitob2 = IlmiyKitob("Fizika asoslari", "Umaraliyev Elbek", 1687, "Fizika")
#
# # Ma'lumot chiqarish
# print(kitob1.malumot())
# print(kitob2.malumot())


# 2-misoll
# class Talaba:
#     def __init__(self, ism, yosh, id_raqam):
#         if yosh < 18:
#             raise ValueError("Talaba yoshi 18 dan kichik bo‘lishi mumkin emas!")
#         if not id_raqam.isdigit():
#             raise ValueError("ID raqam faqat sonlardan iborat bo‘lishi kerak!")
#         if len(id_raqam) < 8:
#             raise ValueError("ID raqam kamida 8 ta raqamdan iborat bo‘lishi kerak!")
#
#         self.ism = ism
#         self.yosh = yosh
#         self.id_raqam = id_raqam
#
#     def malumot(self):
#         return f"Ism: {self.ism}, Yosh: {self.yosh}, ID: {self.id_raqam}"
#
#
# class Bakalavr(Talaba):
#     def __init__(self, ism, yosh, id_raqam, yonalish):
#         super().__init__(ism, yosh, id_raqam)
#         self.yonalish = yonalish
#
#     def malumot(self):
#         return super().malumot() + f", Yo'nalish: {self.yonalish}"
#
#
# class Magistr(Talaba):
#     def __init__(self, ism, yosh, id_raqam, ilmiy_ish):
#         super().__init__(ism, yosh, id_raqam)
#         self.ilmiy_ish = ilmiy_ish
#
#     def malumot(self):
#         return super().malumot() + f", Ilmiy ish: {self.ilmiy_ish}"
## try:
#     talaba1 = Bakalavr("Olim", 20, "12345678", "Dasturlash")
#     talaba2 = Magistr("Anvar", 24, "87654321", "Sun'iy intellekt")
#
#     print(talaba1.malumot())
#     print(talaba2.malumot())
#
# except ValueError as xato:
#     print("Xatolik:", xato)

# 3-misoll
# class Vehicle:
#     def __init__(self, brand, model, year, mileage, price):
#         if not isinstance(brand, str) or not isinstance(model, str):
#             raise ValueError("Brand va model faqat matn (String) bo‘lishi kerak!")
#         if year < 1990:
#             raise ValueError("Yil 1990 dan katta bo‘lishi kerak!")
#         if mileage < 0 or price < 0:
#             raise ValueError("Yurgan masofa va narx 0 dan katta bo‘lishi kerak!")
#
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.mileage = mileage
#         self.price = price
#
#     def get_vehicle_info(self):
#         return f"{self.brand} {self.model}, Yil: {self.year}, Yurgan: {self.mileage} km, Narx: {self.price}$"
#
#
# class ElectricCar(Vehicle):
#     def __init__(self, brand, model, year, mileage, price, battery_capacity):
#         super().__init__(brand, model, year, mileage, price)
#         if battery_capacity < 0:
#             raise ValueError("Batareya hajmi 0 dan katta bo‘lishi kerak!")
#         self.battery_capacity = battery_capacity
#
#     def calculate_range(self):
#         return self.battery_capacity * 5
#
#
# class GasolineCar(Vehicle):
#     def __init__(self, brand, model, year, mileage, price, tank_capacity):
#         super().__init__(brand, model, year, mileage, price)
#         if tank_capacity < 0:
#             raise ValueError("Yoqilg‘i baki hajmi 0 dan katta bo‘lishi kerak!")
#         self.tank_capacity = tank_capacity
#
#     def calculate_range(self):
#         return self.tank_capacity * 10
#
#
# try:
#     tesla = ElectricCar("Tesla", "Model S", 2022, 15000, 70000, 100)
#     bmw = GasolineCar("BMW", "X5", 2019, 50000, 40000, 60)
#
#     print(tesla.get_vehicle_info(), f"Yurish masofasi: {tesla.calculate_range()} km")
#     print(bmw.get_vehicle_info(), f"Yurish masofasi: {bmw.calculate_range()} km")
#
# except ValueError as xato:
#     print("Xatolik:", xato)

# 4-misoll
# class Employee:
#     def __init__(self, name, employee_id, salary, position, department):
#         if not name or not position or not department:
#             raise ValueError("Ism, lavozim va bo‘lim bo‘sh bo‘lmasligi kerak!")
#         if not employee_id.isdigit() or len(employee_id) < 8:
#             raise ValueError("ID faqat raqamlardan iborat va uzunligi kamida 8 bo‘lishi kerak!")
#         if salary < 0:
#             raise ValueError("Maosh 0 dan katta bo‘lishi kerak!")
#
#         self.name = name
#         self.employee_id = employee_id
#         self.salary = salary
#         self.position = position
#         self.department = department
#
#     def get_employee_info(self):
#         return f"Xodim: {self.name}, ID: {self.employee_id}, Lavozim: {self.position}, Bo‘lim: {self.department}, Maosh: {self.salary}$"
#
#
# class Manager(Employee):
#     def __init__(self, name, employee_id, salary, position, department, team_size):
#         super().__init__(name, employee_id, salary, position, department)
#         if team_size < 1:
#             raise ValueError("Jamoa hajmi 1 dan katta bo‘lishi kerak!")
#         self.team_size = team_size
#
#     def can_lead(self):
#         return self.team_size > 5
#
#
# class Intern(Employee):
#     def __init__(self, name, employee_id, salary, position, department, duration):
#         super().__init__(name, employee_id, salary, position, department)
#         if duration < 1 or duration > 12:
#             raise ValueError("Amaliyot muddati 1 dan 12 oy orasida bo‘lishi kerak!")
#         self.duration = duration
#
#     def is_full_time(self):
#         return self.duration >= 6
#
#
# try:
#     manager = Manager("Alisher", "12345678", 5000, "Team Lead", "Dasturlash", 10)
#     intern = Intern("Bobur", "87654321", 1000, "Intern", "Marketing", 6)
#
#     print(manager.get_employee_info(), f"Jamoani boshqara oladi: {manager.can_lead()}")
#     print(intern.get_employee_info(), f"To‘liq stavkada ishlaydi: {intern.is_full_time()}")
#
# except ValueError as xato:
#     print("Xatolik:", xato)

# 5 - misoll
# class Animal:
#     def __init__(self, name: str, species: str, age: int, weight: float, habitat: str):
#         if not name or not species or not habitat:
#             raise ValueError("name, species va habitat bo'sh bo'lmasligi kerak.")
#         if age <= 0:
#             raise ValueError("age 0 dan katta bo'lishi kerak.")
#         if weight <= 0:
#             raise ValueError("weight 0 dan katta bo'lishi kerak.")
#
#         self.name = name
#         self.species = species
#         self.age = age
#         self.weight = weight
#         self.habitat = habitat
#
#     def get_info(self) -> str:
#         return (f"Hayvon: {self.name}, Turi: {self.species}, Yoshi: {self.age}, "
#                 f"O'g'irligi: {self.weight} kg, Yashash joyi: {self.habitat}")
#
# class Bird(Animal):
#     def __init__(self, name: str, species: str, age: int, weight: float, habitat: str, wing_span: float):
#         super().__init__(name, species, age, weight, habitat)
#         if wing_span <= 0:
#             raise ValueError("wing_span 0 dan katta bo'lishi kerak.")
#         self.wing_span = wing_span
#
#     def can_fly(self) -> bool:
#         return self.wing_span > 0.5
#
# class Mammal(Animal):
#     def __init__(self, name: str, species: str, age: int, weight: float, habitat: str, fur_color: str):
#         super().__init__(name, species, age, weight, habitat)
#         if not fur_color:
#             raise ValueError("fur_color bo'sh bo'lmasligi kerak.")
#         self.fur_color = fur_color
#
#     def is_domestic(self) -> bool:
#         return self.species.lower() in ["cat", "dog", "cow"]
#
# sparrow = Bird(name="Chumchuq", species="sparrow", age=2, weight=0.3, habitat="o‘rmon", wing_span=0.6)
# print(sparrow.get_info())
# print("Ucha oladimi:", sparrow.can_fly())
#
# cat = Mammal(name="Mushuk", species="cat", age=3, weight=4.2, habitat="uy", fur_color="qora")
# print(cat.get_info())
# print("Uy hayvonimi:", cat.is_domestic())
#
