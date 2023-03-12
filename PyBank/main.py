import csv
import os

csv_path = os.path.join ("Resource","budget_data.csv")

total_months = 0
total_net=0
GreatestIncrease=0
GreatestIncrease_month=''
GreatestDecrease=0
GreatestDecrease_month=''
net_change=0
month_of_change=[]
net_change_list=[]



with open(csv_path) as csv_file:
    csvreader= csv.reader(csv_file, delimiter=",")
    csv_header=next(csvreader)
    
    first_row=next(csvreader)
    total_months=total_months+1
    total_net=total_net+int(first_row[1])
    prev_net=int(first_row[1])

    for row in csvreader:
        total_months=total_months+1
        total_net=total_net+int(row[1])
    
        net_change=int(row[1])-prev_net
        prev_net=int(row[1])
        net_change_list=net_change_list+[net_change]
        month_of_change=month_of_change+[row[0]]
        AverageChange=sum(net_change_list)/len(net_change_list) 

      
       
        if net_change>GreatestIncrease:
                GreatestIncrease_month=row[0]
                GreatestIncrease=net_change
        

        if net_change<GreatestDecrease:
            GreatestDecrease_month=row[0]
            GreatestDecrease=net_change
    
    
    print ("total months:",total_months)
    print("Total:$",total_net)
    print("Average Change:$",AverageChange)
    print("Greatest Increase in Profits:",GreatestIncrease_month,"($",str(GreatestIncrease),")")
    print("Greatest Decrease in Profits:",GreatestDecrease_month,"($",str(GreatestDecrease),")")

    f=open ("Analysis/txt_file.write", "w")
    f.write("Financial Analysis")
    f.write('\n')
    f.write("..............................")
    f.write('\n')
    f.write("total:$"+str(total_net))
    f.write('\n')
    f.write("Average Change:$"+str(AverageChange))
    f.write('\n')
    f.write("Greatest Increase in profits:"+"\t"+GreatestIncrease_month+"\t"+"($"+"\t"+str(GreatestIncrease)+"\t"+")")
    f.write('\n')
    f.write("Greatest Decrease in profits:"+"\t"+GreatestDecrease_month+"\t"+"($"+"\t"+str(GreatestDecrease)+"\t"+")")


