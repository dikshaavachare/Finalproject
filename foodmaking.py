class FoodItem:
    def __init__(self, name, quantity, price, discount, stock):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock


class Admin:
    def __init__(self):
        self.food_items = []
        self.food_id_counter = 1

    def add_food_item(self, name, quantity, price, discount, stock):
        food_item = FoodItem(name, quantity, price, discount, stock)
        food_item.food_id = self.food_id_counter
        self.food_id_counter += 1
        self.food_items.append(food_item)
        print("Food item added successfully!")

    def edit_food_item(self, food_id, name, quantity, price, discount, stock):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                food_item.name = name
                food_item.quantity = quantity
                food_item.price = price
                food_item.discount = discount
                food_item.stock = stock
                print("Food item updated successfully!")
                return
        print("Food item not found!")

    def view_food_items(self):
        if len(self.food_items) == 0:
            print("No food items available.")
        else:
            for food_item in self.food_items:
                print("Food ID:", food_item.food_id)
                print("Name:", food_item.name)
                print("Quantity:", food_item.quantity)
                print("Price:", food_item.price)
                print("Discount:", food_item.discount)
                print("Stock:", food_item.stock)
                print("--------------------------")

    def remove_food_item(self, food_id):
        for food_item in self.food_items:
            if food_item.food_id == food_id:
                self.food_items.remove(food_item)
                print("Food item removed successfully!")
                return
        print("Food item not found!")


class User:
    def __init__(self, name, phone_number, email, address, password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password
        self.order_history = []

    def place_new_order(self, food_items):
        order = []
        total_price = 0
        for food_id in food_items:
            for food_item in admin.food_items:
                if food_item.food_id == food_id:
                    order.append(food_item)
                    total_price += food_item.price
                    break

        if len(order) == 0:
            print("No food items selected.")
            return

        print("Selected Food Items:")
        for food_item in order:
            print(food_item.name, food_item.quantity, "[INR", food_item.price, "]")

        place_order = input("Do you want to place this order? (yes/no): ")
        if place_order.lower() == "yes":
            self.order_history.append(order)
            print("Order placed successfully!")
        else:
            print("Order canceled.")

    def view_order_history(self):
        if len(self.order_history) == 0:
            print("No order history available.")
        else:
            for order in self.order_history:
                print("Order:")
                for food_item in order:
                    print(food_item.name, food_item.quantity, "[INR", food_item.price, "]")
                print("--------------------------")

    def update_profile(self, name, phone_number, email, address, password):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.password = password


admin = Admin()

# Sample food items for testing
admin.add_food_item("Tandoori Chicken", "4 pieces", 240, 0, 50)
admin.add_food_item("Vegan Burger", "1 piece", 320, 0, 100)
admin.add_food_item("Truffle Cake", "500gm", 900, 0, 20)

user = None


def register_user():
    full_name = input("Full Name: ")
    phone_number = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    password = input("Password: ")

    global user
    user = User(full_name, phone_number, email, address, password)
    print("User registered successfully!")


def login():
    global user
    email = input("Email: ")
    password = input("Password: ")

    if user is None or user.email != email or user.password != password:
        print("Invalid email or password.")
        return

    print("Login successful!")


def display_food_items():
    admin.view_food_items()


def place_new_order():
    if user is None:
        print("Please log in to place an order.")
        return

    print("Food Items:")
    admin.view_food_items()

    food_items = input("Enter the numbers of the food items you want to order (comma-separated): ")
    food_items = list(map(int, food_items.split(",")))

    user.place_new_order(food_items)


def view_order_history():
    if user is None:
        print("Please log in to view the order history.")
        return

    user.view_order_history()


def update_profile():
    if user is None:
        print("Please log in to update your profile.")
        return

    full_name = input("Full Name: ")
    phone_number = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    password = input("Password: ")

    user.update_profile(full_name, phone_number, email, address, password)
    print("Profile updated successfully!")


while True:
    print("---------------")
    print("Food Ordering App")
    print("---------------")
    print("1. Register")
    print("2. Log in")
    print("3. Place New Order")
    print("4. Order History")
    print("5. Update Profile")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        register_user()
    elif choice == "2":
        login()
    elif choice == "3":
        place_new_order()
    elif choice == "4":
        view_order_history()
    elif choice == "5":
        update_profile()
    elif choice == "6":
        print("Thank you for using the Food Ordering App!")
        break
    else:
        print("Invalid choice. Please try again.")
