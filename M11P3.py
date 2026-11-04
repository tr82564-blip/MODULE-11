
# function section

def calculate_sales(sales_amount):

    if sales_amount > 100000:
        commission_rate = 0.10

    else:
        commission_rate = 0.05

    commission_amount = sales_amount * commission_rate

    next_year_target = sales_amount * 0.05

    return commission_amount, next_year_target


# input section

last_name = input("Enter salesperson last name: ")
sales_amount = float(input("Enter sales amount: "))


# processing section

commission_amount, next_year_target = calculate_sales(sales_amount)


# output section

print(f"Salesperson Last Name: {last_name}")
print(f"Commission: ${commission_amount:,.2f}")
print(f"Next Year Target: ${next_year_target:,.2f}")
