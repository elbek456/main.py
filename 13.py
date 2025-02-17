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
