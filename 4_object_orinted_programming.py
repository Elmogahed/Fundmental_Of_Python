class Product: 
    type = 'mobile'
    def __init__(self, id, name, price, count):
        self.id = id
        self.name = name 
        self.price = price
        self.count = count
    def discount(self, ratio): 
        self.price = self.price - self.price * ratio


iphone_14 = Product(id=1, name='Iphone 14', price=999, count=10)
samsung_s23 = Product(id=2, name='Samsung Galaxy S23', price=985, count=8)

print(iphone_14.type)
print(samsung_s23.type)
 
print(iphone_14)
print(iphone_14.name)
print(iphone_14.price)
iphone_14.discount(0.1)
print(iphone_14.price)

class Car: 
    # النوع الخاص بالسيارت وهي عبارة عن مركبات 
    type = 'Vehical'
    # تهيئة خصائص السيارة 
    def __init__(self, color,  engine_displacement, distance):
        self.color = color
        self.engine_displacemnt = engine_displacement 
        self.distance = distance 

    def reset_counter(self): 
        # تصفير العداد
        self.distance = 0
    def increase_counter(self, icreacement):
        # زيادة العداد للمسافة 
        self.distance += icreacement 
