
# function section

def calculate_discount(quantity, unit_price, discount_rate):

    total_price = quantity * unit_price

    discount_amount = total_price * discount_rate

    discounted_price = total_price - discount_amount

    return discount_amount, discounted_price


# input section

quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter price: "))
discount_rate = float(input("Enter discount rate: "))


# processing section

discount_amount, discounted_price = calculate_discount(quantity, unit_price, discount_rate)


# output section

print(f"Quantity: {quantity}")
print(f"Price: ${unit_price:.2f}")
print(f"Discount Amount: ${discount_amount:.2f}")
print(f"Discounted Price: ${discounted_price:.2f}")
