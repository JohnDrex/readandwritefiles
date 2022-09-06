import csv


def main():
    infile = open('customers.csv', 'r')

    csvfile = csv.reader(infile, delimiter=',')

    next(csvfile)       #Skips over first row

    for record in csvfile:
        
        ID = record[0]
        FName = record[1]
        LName = record[2]
        City = record[3]
        Country = record[4]
        Phone = record[5]

        print("ID: ", ID)
        print("FirstName: ", FName)
        print("LastName: ", LName)
        print("City: ", City)
        print("Country: ", Country)
        print("Phone:", Phone)
        enter = input()

main()