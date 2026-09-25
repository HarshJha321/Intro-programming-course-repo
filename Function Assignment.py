def circle_area(radius):
    pi = 3.14159
    area = pi * (radius ** 2)
    return area

def calculate_taxes(money, tax_rate):
    total_due = money + (money * tax_rate)
    return total_due

def convert_temperature(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

# 1. Area of a Circle
radius = float(input("Enter radius: "))
area = circle_area(radius)
print(f"{area:.2f}")

# 2. Taxes
money = float(input("Enter money: "))
tax_input = input("Enter tax rate: ")

# Remove the % sign and convert to a decimal for the math
tax_rate = float(tax_input.replace("%", "")) / 100

total = calculate_taxes(money, tax_rate)
print(f"{total:.2f}")

# 3. Temperature
fahrenheit = float(input("Enter Fahrenheit: "))
celsius = convert_temperature(fahrenheit)
print(celsius)