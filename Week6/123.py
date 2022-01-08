TRADING_PACK_PRICE = 4.25
MIN_PACKS_NUMBER = 36
MIN_PACKS_COST = 125
DICE_SET_PRICE = 11
BOARD_GAME_PRICE = 50


def print_summary_per_customer(customer_number, total_trading_cost,
                               total_dice_cost,
                               total_games_cost, total_single_paid):
    print(
        f'Customer {customer_number} spent ${dollar_format(total_single_paid)}')
    print(f'>>> ${dollar_format(total_trading_cost)} for trading card packs') #improve readibility, otherwise messy
    print(f'>>> ${dollar_format(total_dice_cost)} for dice sets')
    print(f'>>> ${dollar_format(total_games_cost)} for board games')
    print()


def print_additional_info(total_paid, all_non_trading_paid, max_single_paid,
                          max_paid_customers):
    print(f'Combined all customers paid ${dollar_format(total_paid)} total')
    print(
        f'Non-trading card products (dice + board games) were ${dollar_format(all_non_trading_paid)} total')
    print("")
    print(
        f'${dollar_format(max_single_paid)} was the most paid by any single customer')
    print("The customer(s) that paid the most were: " + ', '.join(
        max_paid_customers))
    print()


def dollar_format(amount):
    dollars = "{:.2f}".format(amount) #rounds fractional part up to 2 digits
    return dollars


def sales_summary(data):
    """
    Parameters:
      packs_per_customer: How many packs of trading cards each customer purchased.
      dice_purchased: How many sets of dice were each customer purchased.
      board_games_purchased: How many board games each customer purchased.
    """
    # number_of_customers = min(len(packs_purchased), len(dice_purchased), len(board_games_purchased))


    print("Welcome to the Ada's Game Emporium Sales Tracker!")
    print()

    max_single_paid = 0  # most paid by a single customer

    all_non_trading_paid = 0  # total earnings from dice+board games
    all_dice_paid = 0  # total earnings from dice
    all_games_paid = 0  # total earnings from board games

    total_paid = 0  # total earnings by all customers
    max_paid_customers = []  # list of the most profitable customers
    for cat in data:
        for i in range(len(cat)):
            customer_number = i + 1  # range() indexes start at 0, not 1
            # adding +1 gives us a correct customer number

            packs_per_customer = packs_purchased[i]
            dice_per_customer = dice_purchased[i]
            games_per_customer = board_games_purchased[i]

            sale_packs = packs_per_customer // MIN_PACKS_NUMBER  # calculates packs purchased at discount
            non_sale_packs = packs_per_customer % MIN_PACKS_NUMBER  # calculates packs purchased at a regular price

            total_trading_cost = sale_packs * MIN_PACKS_COST + non_sale_packs * TRADING_PACK_PRICE  # total spent on trading cards per customer
            total_dice_cost = dice_per_customer * DICE_SET_PRICE
            total_games_cost = games_per_customer * BOARD_GAME_PRICE
            total_single_paid = total_trading_cost + total_dice_cost + total_games_cost  # total spent on trading cards, dice and board games per customer

            if total_single_paid >= max_single_paid:  # at every iteration total_single paid is compared to the current maximum paid by a customer
                if total_single_paid > max_single_paid:
                    max_paid_customers.clear()  # if total_single_paid is greater than the current max_single_paid,
                    # no need to store this customer number any more
                max_single_paid = total_single_paid
                max_paid_customers.append("#" + str(customer_number))

            total_paid += total_single_paid
            all_dice_paid += total_dice_cost
            all_games_paid += total_games_cost
            all_non_trading_paid = all_dice_paid + all_games_paid

            print_summary_per_customer(customer_number, total_trading_cost,
                                       total_dice_cost,
                                       total_games_cost,
                                       total_single_paid)
    print_additional_info(total_paid, all_non_trading_paid, max_single_paid,
                          max_paid_customers)


# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# c = list(map(int, input().split()))
packs = [60, 0, 4]
dice = [0, 7, 8]
board_games = [1, 4, 3]

sales_summary(a, b, c)

'''
Welcome to the Ada's Game Emporium Sales Tracker!

Customer 1 spent $215.05
>>> $43.10 for trading card packs
>>> $21.98 for dice sets
>>> $149.97 for board games

Customer 2 spent $125.84
>>> $25.86 for trading card packs
>>> $0.00 for dice sets
>>> $99.98 for board games

Customer 3 spent $161.84
>>> $150.85 for trading card packs
>>> $10.99 for dice sets
>>> $0.00 for board games

Combined all customers paid $502.73 total
Non-trading card products (dice + board games) were $282.92 total

$215.05 was the most paid by any single customer
The customer(s) that paid the most were: #1

'''
