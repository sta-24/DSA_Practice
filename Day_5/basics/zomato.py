class User:
    def __init__(self,name,phone_number):
        self.name=name
        self.phone_number=phone_number

    def display_info(self):
        print (f"Name: {self.name}  Phone no: {self.phone_number}")

class Customer(User):
    def __init__(self,name,phone,address):
        super().__init__(name,phone)
        self.address=address
        self.orders=[]

    def place_order(self,orders):
        self.orders.append(orders)
        print("your order is successfully placed")

class FoodItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def display(self):
        print(f"{self.name} - Rs.{self.price}")

class Restaurant:
    def __init__(self,name):
        self.name=name
        self.menu:list[FoodItem]=[]

    def add_food(self,food):
        self.menu.append(food)

    def show_menu(self):
        for item in self.menu:
            item.display()

class Order:
    def __init__(self,order_id:str,
        customer:Customer,
        restaurant:Restaurant,
        order_items:list[FoodItem],status="Placed"):
            self.order_id=order_id
            self.customer=customer
            self.restaurant=restaurant
            self.order_items=order_items
            self.status=status

    def add_item(self,item:FoodItem):
        self.order_items.append(item)

    def calculate_total(self):
        total=0
        for item in self.order_items:
            total+=item.price
        return total
    
    def update_status (self,status):
        self.status=status

    def show_order(self):
        print(f"Oder id : {self.order_id}")
        print(f"Customer Name: {self.customer.name}")
        print(f"Restaurant Name: {self.restaurant.name}")
        for item in self.order_items:
            item.display()
        print(f"Order status {self.status}")
        print(f"Bill Total :{self.calculate_total()}")

class DeliveryPartner(User):
    def __init__(self,name,phone_number):
        super().__init__(name,phone_number)

    def delivery_order(self,order:Order):
        order.update_status("Preparing")
        order.update_status("Out for Delivery")
        order.update_status("Delivered")


# Demo

res=Restaurant("KFC")
food_item1=FoodItem("Masala Dosa",150)
food_item2=FoodItem("Paneer Butter Masala",100)
food_item3=FoodItem("Rasgula",70)

res.add_food(food_item1)
res.add_food(food_item2)
res.add_food(food_item3)

res.show_menu()

cust1=Customer("Dr.Radhakrishna","9867894320","CCE")

order=Order("123",cust1,res,[food_item1, food_item2])

order.show_order()

del_p=DeliveryPartner("ABC","123456787")





    



