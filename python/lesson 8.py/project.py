class robot:
    def __init__(self , name , model , year):
        self.name = name
        self.model = model
        self.year = year

rubo = robot("rubo","Astra-9X" , 2025)
Zentra = robot("Zentra","ZT-5000",2024)

print("{} was made in the year {} and its model is{}".format(rubo.name, rubo.year, rubo.model))
print("{} was made in the year {} and its model is{}".format(Zentra.name, Zentra.year, Zentra.model))