import csv


def main():
    infile = open('EmployeePay.csv', 'r')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)       #Skips over first row

    for record in csvfile:
        
        ID = record[0]
        FName = record[1]
        LName = record[2]
        Salary = float(record[3])
        SalaryRound = round(Salary, 2)
        Bonus =float(record[4])
        BonusRound = round(Bonus, 2)
        BonusAmt = Bonus*Salary
        BonusAmtRound=round(BonusAmt, 2)
    

        print("ID:        ", ID)
        print("FirstName: ", FName)
        print("LastName:  ", LName)
        print("Salary:    ", "${:0,.2f}".format(SalaryRound))
        print("Bonus:     ", "${:0,.2f}".format(BonusAmtRound))
        print("Total Pay: ", "${:0,.2f}".format(SalaryRound+BonusAmtRound))
        enter = input()
    

main()