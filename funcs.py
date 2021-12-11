
def menu():
    print("\nWhat would you like to do?"
          "\n1 - View lease terms"
          "\n2 - Add a local dealer's pricing"
          "\n3 - Remove a local dealer's pricing"
          "\n4 - Search for a previously stored dealer"
          "\n5 - Compare specific dealer prices to your ideal pricing"
          "\n6 - Print all dealer options"
          "\n7 - Quit")
    user_choice = input("What would you like to do (1-6)? ").strip()
    return user_choice


def ideal_price():  # Stores user's ideal pricing for lease
    while True:
        try:
            ideal_down = float(input("How much would you like to put down for your lease? "))
            ideal_monthly = float(input("How much would you like to pay per month? "))
            break
        except:
            print("Enter a number value.")
    return ideal_down, ideal_monthly
