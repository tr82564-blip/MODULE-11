
total_amount = 0.0
sales_tax = 0.0


# function section

def calculate_total(quantity, unit_price):

    global total_amount
    global sales_tax

    total_amount = quantity * unit_price

    sales_tax = total_amount * 0.07


# input section

quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))


# processing section

calculate_total(quantity, unit_price)


# output section

print(f"Total: ${total_amount:,.2f}")
print(f"Tax: ${sales_tax:,.2f}")

