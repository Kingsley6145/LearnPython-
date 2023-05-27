purchase = float(input("Enter the purchase amount in ksh: "))
if purchase > 1000:
    discount = 0.05*purchase 
    discount_amount =purchase-discount 
    print("Discount applied! discount_amount is: ksh",discount_amount)
else:
    print("No discount applied. Total amount is: ksh",purchase)
    