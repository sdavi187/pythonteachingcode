# [ ] create, call and test 
max_order = 200.00
min_order = 2.00
price = 5.75

order_amt = float(input("How much would you like to order?"))

if order_amt > max_order:
    print (order_amt, "exceeds available stock only", max_order, "available")
elif order_amt < min_order:
    print (order_amt, "is below the minimum order threshold of", min_order)
else:
    print (order_amt, "costs $", order_amt*price)
