def pre_sell_tickets():
    total_tickets = 20
    total_buyers = 0

    while total_tickets > 0:
        try:
            tickets_requested = int(input("Enter the number of tickets you want to buy (up to 4): "))
            if tickets_requested < 1 or tickets_requested > 4:
                print("You can only buy between 1 and 4 tickets.")
                continue
            if tickets_requested > total_tickets:
                print(f"Only {total_tickets} tickets remaining. Please enter a valid number.")
                continue
            total_tickets -= tickets_requested
            total_buyers += 1
            print(f"Tickets purchased: {tickets_requested}. Tickets remaining: {total_tickets}.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"All tickets sold! Total number of buyers: {total_buyers}")

# Run the function
pre_sell_tickets()