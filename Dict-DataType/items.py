car = {1:"Mahindra",2:"Tata",3:"Suzuki",4:"Tesala",5:"Nisan",6:"Toyoto"}
for k,v in car.items():
    print(k,"----",v)

car[7]="Lamborgini"
print(car)
car.pop(6)
print(car)
car.popitem()
print(car)
electric_car = car.copy()
print(electric_car)