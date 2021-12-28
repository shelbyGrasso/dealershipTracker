class Dealers:
    def __init__(self, city, MSRP, sale, down, monthly, fees_included, buyout):
        self.city = city  # Location of dealer
        self.MSRP = MSRP  # MSRP value of car
        self.sale = sale  # Price dealer is selling car
        self.down = down  # Amount down for lease
        self.monthly = monthly  # Monthly payments for 36 months
        self.fees_included = fees_included  # Does the down payment include dealer fees?
        self.buyout = buyout  # Residual value if car is purchased at lease-end


    def __str__(self):
        return "\nLocation: " + str(self.city) + \
               "\nMSRP: $" + str(self.MSRP) + \
               "\nSales Price: $" + str(self.sale) + \
               "\nDown Payment: $" + str(self.down) + \
               "\nMonthly payment: $" + str(self.monthly) + \
               "\nFees included in down payment: " + str(self.fees_included) + \
               "\nLease buy-out: $" + str(self.buyout)


    def college_rebate(self):  # Takes $1000 off of monthly payments
        total_monthly = self.monthly * 36
        self.monthly = (total_monthly - 1000) / 36
        return self.monthly


    def compare_ideal(self, ideal_set): # Compares a dealer's price to ideal price
        ideal_down = ideal_set[0]  # Store ideal values as local variables
        ideal_monthly = ideal_set[1]
        ideal_lease = ideal_down + (ideal_monthly * 36)  # Calculate total cost of ideal lease
        dealer_lease = self.down + (self.monthly * 36)  # Calculate total cost of dealer lease

        compare_lease = ideal_lease - dealer_lease  # Store difference between leases in local variables

        print("In your ideal lease, you would spend ${:.2f} total, "
              "including down payment and all monthly installments.".format(ideal_lease))
        print("With the dealer in {}, you would spend ${:.2f} total.".format(self.city, dealer_lease))
        if compare_lease > 0:
            print("You are getting a good deal!")
        else:
            print("You can do better.")
        return

