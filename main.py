import funcs
import dealerships

if __name__ == '__main__':

    print("Use this program to determine what your car lease options are at local dealers."
          "\nPresumably, you're looking for a RAV4 Hybrid LE in New Hampshire.")

    dealer_list = []
    user_choice = funcs.menu()
    while user_choice != "7":
        if user_choice == "1":  # Prints lease terms
            print("\nHere are the terms of your lease:"
                  "\nLease term: 36 months"
                  "\nMiles allowed per year: 10k")
            user_choice = funcs.menu()
        elif user_choice == "2":  # Stores a local dealer's pricing
            while True:
                try:
                    new_city = input("What city is the dealer in? ")
                    new_MSRP = int(input("What is the MSRP of the car? "))
                    new_sale = int(input("What is the dealer's sale price? "))
                    new_down = int(input("What is the required down payment? "))
                    new_monthly = int(input("What is the monthly payment? "))
                    new_fees_included = input("Are all dealer fees included in the down payment? (Y/N) ")
                    new_buyout = int(input("What is the lease buy-out price? "))
                    break
                except:
                    print("Enter a number.")
            new_dealer = dealerships.Dealers(new_city, new_MSRP, new_sale, new_down, new_monthly, new_fees_included, new_buyout)
            dealer_list.append(new_dealer)
            print("\nDealer added.")
            print(new_dealer)
            user_choice = funcs.menu()
        elif user_choice == "3":  # Removes a stored dealer
            remove_city = input("Which dealer would you like to remove? Enter city: ")
            found = False
            for i in dealer_list:
                if i.city == remove_city:
                    found = True
                    dealer_list.remove(i)
                    print("Dealer successfully removed.")
            if found == False:
                print("Dealer not found.")
            user_choice = funcs.menu()
        elif user_choice == "4":  # Searches for a stored dealer
            found = False
            dealer = input("Which dealer are you looking for? Enter the city: ")
            for i in dealer_list:
                if i.city == dealer:
                    found = True
                    search_dealer = i
                    print("Dealer found:\n", search_dealer)
            if found == False:
                print("Dealer not found.")
            user_choice = funcs.menu()
        elif user_choice == "5":  # Compares dealer pricing to ideal pricing
            user_ideal = funcs.ideal_price()
            found = False
            dealer = input("Which dealer are you looking for? Enter the city: ")
            for i in dealer_list:
                if i.city == dealer:
                    found = True
                    compare_dealer = i
                    compare_dealer.compare_ideal(user_ideal)
            if found == False:
                print("Dealer not found.")
            user_choice = funcs.menu()
        elif user_choice == "6":  # Prints all dealer options
            for i in dealer_list:
                print(i)
            user_choice = funcs.menu()
        else:
            print("Good luck getting your dream car!")

    f = open('stored_dealers.txt', 'w')
    for object in dealer_list:
       object = str(object)
       f.write(object + '\n')
    f.close()