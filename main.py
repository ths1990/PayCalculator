def main() -> object:
    def calc_hours(hours_worked, minutes_worked):
        """Function to convert hours and minutes worked into a number that can be used in pay calculation"""
        hours_minutes = hours_worked + minutes_worked / 60
        return hours_minutes

    def calc_pay(time, hourly_rate):
        """Function to calculate total pay"""
        total_pay = time * hourly_rate
        return total_pay

    invoices = {}  # Dictionary to store projects and invoice totals
    num_projects = int(input("How many projects are you invoicing for?"))

    for i in range(num_projects):
        project_name = input("What is the name of your project?")
        rate = float(input("What is the hourly rate for the project?"))
        hours = int(input("How many hours did you work?"))
        minutes = int(input("How many minutes did you work (0-59)?"))

        if 0 < minutes > 59:
            print("Minutes must be between 0 and 59. Try again.")
            minutes = int(input("How many minutes did you work (0-59)?"))
        else:
            total_time = calc_hours(hours, minutes)

        pay = calc_pay(total_time, rate)
        invoices[project_name] = pay
    # TODO: Fix pay format to print out as $x.xx
    print(invoices)


if __name__ == '__main__':
    main()
