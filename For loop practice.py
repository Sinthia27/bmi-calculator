ice_cream_sales = [120, 135, 150, 90, 80, 140, 160, 170, 180, 110, 105, 95, 130, 125]


def sales_on(day):
    return ice_cream_sales[day-1]

print(sales_on(1))

def max_sales():
    print (max(ice_cream_sales))

def average_sales():
    return sum(ice_cream_sales)/len(ice_cream_sales)

print (average_sales())