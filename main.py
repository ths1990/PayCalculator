import decimal


def main():
    def calc_hours(hours_worked, minutes_worked):
        """Function to convert hours and minutes worked into a number that can be used in pay calculation"""
        hours_minutes = decimal.Decimal(hours_worked + minutes_worked / 60)
        return hours_minutes

    def calc_pay(time, hourly_rate):
        """Function to calculate total pay"""
        total_pay = decimal.Decimal(time * hourly_rate).quantize(decimal.Decimal('0.00'))
        return total_pay

    invoices = {}  # Dictionary to store projects and invoice totals
    project_id = 0
    num_projects = int(input("How many projects are you invoicing for?"))

    for i in range(num_projects):
        project_id = project_id + 1
        invoices[project_id] = {}
        project_name = input("What is the name of your project?")
        rate = decimal.Decimal(input("What is the hourly rate for the project?")).quantize(decimal.Decimal('0.00'))
        hours = int(input("How many hours did you work?"))
        minutes = int(input("How many minutes did you work (0-59)?"))

        if 0 < minutes > 59:
            print("Minutes must be between 0 and 59. Try again.")
            minutes = int(input("How many minutes did you work (0-59)?"))
        else:
            total_time = calc_hours(hours, minutes)

        pay = calc_pay(total_time, rate)

        # Assigns key pair values for rate, total hours, and total pay
        invoices[project_id]["Project Name"] = project_name
        invoices[project_id]["Rate"] = rate
        invoices[project_id]["Total Hours"] = total_time
        invoices[project_id]["Total Pay"] = pay

    for i, v in invoices.items():
        print("\n")
        print("Invoice --", i, "--\n")

        for j, k in invoices[i].items():
            print(j, ":", k)


if __name__ == '__main__':
    main()
