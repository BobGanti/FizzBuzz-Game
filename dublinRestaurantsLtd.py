
# --- Setup --------------------------------------------- #
def validate_input(num, min_limit, max_limit):
    int_num = is_integer(num)
    if int_num is not None:
        if in_range(int_num, min_limit, max_limit):
            return int_num
        print("Error! Input is out of range")
    else:
        print("Error! Input is not an integer!")
        return None


# Verify that user input is a +ve integer
def is_integer(num):
    try:
        int_num = int(num)
        return int_num
    except ValueError:
        return None


def is_float(num):
    try:
        float_num = float(num)
        return float_num
    except ValueError:
        return None


# Verify that user input is not out of range
def in_range(num, min_limit, max_limit):
    if min_limit <= num <= max_limit:
        return True
    else:
        return False


def setup(num, min_limit, max_limit):
    valid_num = validate_input(num, min_limit, max_limit)
    while valid_num is None:
        valid_num = validate_input(input(f"\nEnter number again from {min_limit} to {max_limit} inclusive!: "),
                                   min_limit, max_limit)
    return valid_num

# --- Main --------------------------------------------- #
def run_app():
    weekly_earning_list = []
    min_restaurant = 1
    max_restaurant = 4
    min_days = 1
    max_days = 7
    num_restaurant = setup(
        input(f"Enter number of Opened Restaurants ({min_restaurant} to {max_restaurant} inclusive) : "),
        min_restaurant, max_restaurant
    )

    for i in range(1, num_restaurant + 1):
        daily_earnings = []
        weekly_earning = 0
        days_open = setup(
            input(f"\nEnter days open ({min_days} to {max_days} inclusive) for Restaurant {i}: "),
            min_days, max_days
        )

        print(f"\n\nTALLY FOR RESTAURANT {i}")
        print("*" * 25)
        for j in range(1, days_open + 1):
            day_earning = is_float(input(f"Enter the earnings for day {j}: "))
            while day_earning is None:
                print("Input is not a number!")
                day_earning = is_float(input(f"\nEnter the earning for day {j} again: "))
            daily_earnings.append(day_earning)
            weekly_earning += day_earning

        weekly_earning_list.append(weekly_earning)

    max_earning = max(weekly_earning_list)
    index = weekly_earning_list.index(max_earning)
    all_weekly = sum(weekly_earning_list)
    av_income = all_weekly/num_restaurant

    print()
    print(f"Weekly Earnings: {weekly_earning_list}")
    print(f"\nRestaurant {index + 1} has Max Weekly Earning of €{max_earning}")
    print(f"\nOVERALL INCOME:\nOverall Income = €{all_weekly}")
    print(f"\nAVERAGE REVENUE:\nAverage Revenue = €{av_income}")
    print(f"\nRESTAURANTS EXCEEDING AV. REVENUE:")
    for i in range(len(weekly_earning_list)):
        if weekly_earning_list[i] > av_income:
            print(f"Restaurant {i+1} earned €{weekly_earning_list[i]}")
        print(f"\nWeekly Earning for Restaurant {i+1} = €{weekly_earning_list[i]}")

    res = input("\n\nQuery Data (Y/N)?: ").upper()
    while res == "Y":
        num = setup(
            input(f"\nEnter the Restaurant Number for query ({min_restaurant} to {num_restaurant} inclusive): "),
            min_restaurant, num_restaurant
        )
        print(f"\nWeekly Income for Restaurant {num} is {weekly_earning_list[num - 1]}")
        res = input("\nQuery Data again (Y/N)?: ").upper()

run_app()
