def main() -> object:
    invoices = []  # Array list to store invoice totals


def calc_hours(hours_worked, minutes_worked):
    """Function to convert hours and minutes worked into a number that can be used in pay calculation"""
    hours_minutes = hours_worked + minutes_worked / 60
    return hours_minutes


def calc_pay(time, hourly_rate):
    """Function to calculate total pay"""
    total_pay = time * hourly_rate
    return total_pay


# TODO: Add while loop to allow user to keep adding projects to create invoices for

hours = int(input("How many hours did you work?"))
minutes = int(input("How many minutes did you work (0-59)?"))
rate = float(input("What is your hourly rate?"))

if 0 < minutes > 59:
    print("Minutes must be between 0 and 59. Try again.")
    minutes = int(input("How many minutes did you work (0-59)?"))
else:
    total_time = calc_hours(hours, minutes)

pay = calc_pay(total_time, rate)

# TODO: Replace with function to add invoices to list/dictionary and print

# print(pay) *Test Line to confirm calculation works

if __name__ == '__main__':
    main()
