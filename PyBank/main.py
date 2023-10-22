#Import modules
import csv
import os

#Setting file path to csv file
budget_path= os.path.join("Resources/budget_data.csv")

#Open/Read csv 

with open(budget_path) as budget_data:
    budget_reader = csv.reader(budget_data, delimiter=",")

    #skip header
    budget_header = next(budget_reader)

    #list for profits and months
    profits=[]
    months=[]

    i=0
    revenue_total=0

    #list for revenue changes and initialize variable for previous row data
    revenue_changes=[]
    previous_row=[]

    #iterate through csv rows, add change to list and update

    for row in budget_reader:
        revenue_change=0
        
        if i !=0:
            revenue_change=int(row[1])-int(previous_row[1])

            revenue_changes.append(revenue_change)

        profits.append(int(row[1]))
        months.append(row[0])

        previous_row=row

        i =+ 1
    #actual calculations
    revenue_avg=sum(revenue_changes)/len(revenue_changes)
    total_months=len(months)
    greatest_inc=max(revenue_changes)
    greatest_dec=min(revenue_changes)

    #print results to console
    print("Analysis")
    print("------------------------")
    print(f'Total Months:{total_months}')
    print(f'Total: ${sum(profits)}')
    print(f'Average Change: ${revenue_avg:.2f}')
    print(f'Greatest Increase in Profits: ${greatest_inc}')
    print(f'Greatest Decrease in Profits: ${greatest_dec}')

    #write results to text file in separate analysis file
    file=open("Analysis/analysis.txt", "w")

    file.write("Analysis\n")
    file.write("----------------------------\n")
    file.write(f'Total Months:{total_months}\n')
    file.write(f'Total: ${sum(profits)}\n')
    file.write(f'Average Change: ${revenue_avg:.2f}\n')
    file.write(f'Greatest Increase in Profits: ${greatest_inc}\n')
    file.write(f'Greatest Decrease in Profits: ${greatest_dec}\n')


