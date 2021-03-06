import os
import csv


csvpath=os.path.join('/Users/neethaabraham/Documents/ashwin_data/budget_data.csv')

months=0
net_amount=0
amount_before=0
net_change_data=[]
highest_date=[]
lowest_date=[]


with open(csvpath, newline="") as csvfile:
    csvreader=csv.reader(csvfile,delimiter=",")
    csv_header=next(csvfile)

    for bank_data in csvreader:
        profit_loss=int(bank_data[1])
        months=months+1
        net_amount=net_amount+profit_loss
        net_change=profit_loss-amount_before
        net_change_data.append(net_change)
        amount_before=int(bank_data[1])
        highest_change=max(net_change_data)
        lowest_change=min(net_change_data)
        if (net_change==highest_change):
            highest_date=bank_data[0]
        if(net_change==lowest_change):
            lowest_date=bank_data[0]
        
    mean_net_change=sum(net_change_data)/len(net_change_data)
    mean_net_change=round(mean_net_change,2)
result=(
    'Financial Analysis\n'
    '______________________\n'
    f'Total Months: {months} months\n'
    f'Total: ${net_amount}\n'
    f'Average Change: ${mean_net_change}\n'
    f'The greatest increase in profits: {highest_date} $({highest_change})\n'
    f'The greatest decrease in profits: {lowest_date} $({lowest_change})\n'
    )

print(result)

output_path=os.path.join('/Users/neethaabraham/Documents/ashwin_data/PythonChallenge/PyBank/PyBank_Result.txt')

with open(output_path,'w',newline='') as text:
    text.write(result)