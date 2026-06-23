Base_Salary0 = float(input("Please enter the base salary: "))

while True:
    if Base_Salary0 <= 0:
        Base_Salary1 = float(input("Base salary can't be less than zero.Please try again: "))
        if 0 < Base_Salary1 < 1000000:
            Insurance = (Base_Salary1 * 7) / 100
            Final_Salary = Base_Salary1 - Insurance
            print("Your salary, being below ane million toman, is tax-exempt.")
            print("Insurance withheld:", Insurance)
            print("Your salary, after deducting insurance premiums is", Final_Salary, "Toman.")
            break
        elif Base_Salary1 >= 1000000:
            Tax = Base_Salary1 * 0.1
            Insurance = (Base_Salary1 * 7) / 100
            Final_Salary = Base_Salary1 - (Insurance + Tax)
            print("Tax withheld:", Tax)
            print("Insurance withheld:", Insurance)
            print("Total withheld:", Insurance + Tax)
            print("Your salary, after deducting tax and insurance premiums is", Final_Salary, "Toman.")
            break
    elif 0 < Base_Salary0 < 1000000:
        Insurance = (Base_Salary0 * 7) / 100
        Final_Salary = Base_Salary0 - Insurance
        print("Your salary, being below ane million toman, is tax-exempt.")
        print("Insurance withheld:", Insurance)
        print("Your salary, after deducting insurance premiums is", Final_Salary, "Toman.")
        break
    else:
        Tax = Base_Salary0 * 0.1
        Insurance = (Base_Salary0 * 7) / 100
        Final_Salary = Base_Salary0 - (Insurance + Tax)
        print("Tax withheld:", Tax)
        print("Insurance withheld:", Insurance)
        print("Total withheld:", Insurance + Tax)
        print("Your salary, after deducting tax and insurance premiums is", Final_Salary, "Toman.")
        break
