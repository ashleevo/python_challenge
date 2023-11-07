#import os module
import os
#module for reading files
import csv


#set path for file
csv_path = os.path.join("budget_data.csv")
os.chdir(os.path.dirname(os.path.realpath(__file__)))


#using method 2: improved reading using CSV module
with open (csv_path, encoding = 'UTF-8') as csvfile:
    #create variable that holds contents and specify delimiter
    csvreader = csv.reader(csvfile, delimiter = ",")
    #read headers
    header = next(csvreader)


#create empty lists for month count, profit, and the change in profit
    month_count = []
    profit = []
    change_profit = []


#iterate through values and add to created lists
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        change_profit.append(profit[i+1]-profit[i])
#find the greatest increase and greatest decrease in the change of profits
increase = max(change_profit)
decrease = min(change_profit)


month_increase = change_profit.index(max(change_profit))+1
month_decrease = change_profit.index(min(change_profit))+1


#print the financial analysis in terminal
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")

#export onto txt file
output = open("printedresults.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months:{len(month_count)}")
line4 = str(f"Total:{sum(profit)}")
line5 = str(f"Average Change:{round(sum(change_profit)/len(change_profit),2)}")
line6 = str(f"Greatest Increase in Profits:{month_count[month_increase]} ({(str(increase))})")
line7 = str(f"Greatest Decrease in Profits:{month_count[month_decrease]} (${(str(decrease))})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))