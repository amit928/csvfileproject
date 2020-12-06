import csv
file=open('csvfile2.csv','r')
read=csv.reader(file)
x=input("Enter your Event ID : ")
for row in read:
    if(row[3]==x):
        print(row)
file.close()

    
