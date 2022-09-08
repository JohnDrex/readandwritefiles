import csv
infile = open('steps.csv', 'r')
outfile = open('avg_steps.csv', 'w')
csvfile = csv.reader(infile, delimiter=',')
next(csvfile)






MonthList = ['January', 'February', 'March', 'April', 'May', 'June', 'August', 'September', 'October', 'November', 'December']

total = 0
count = 0

month=1

outfile.write('Month, Avg Steps\n')
for record in csvfile:
    if float(record[0])!=month:
        month-=1
        average = (total/count)
        print(MonthList[month]+','+str(average))
        outfile.write(MonthList[month]+','+str(average)+'\n')
        month+=2
        count = 0
        total = 0
    if float(record[0]) == month:
        total+=float(record[1])
        count+=1


outfile.close()



