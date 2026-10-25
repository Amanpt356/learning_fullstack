class Product:
    def __init__(self,name,price):
        self.name = name
        self._price = price
    @property
    def price(self):
        return self._price
    @price.setter
    def price(self,new_price):
        if new_price < 0 :
            raise ValueError("Price Cant be negative")
        self._price = new_price

prd1 = Product("Keyboard",1500)
print(prd1.price)
prd1.price = 1200
print(prd1.price)


