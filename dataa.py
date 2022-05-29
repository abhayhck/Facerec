import csv
'''
with open('data.csv', 'w') as file:
    fld_names = ['id', 'name', 'designation', 'email']
    csv_writer = csv.DictWriter(file, fieldnames=fld_names, delimiter='\t')
    csv_writer.writeheader()
'''
with open('data.csv','r') as f:
    fread=csv.DictReader(f)
    print(fread)
    for i in fread:
        if i['id']=='101':
            print(f"\nPerson identified as : {i[' name']} \n Their ID is : {i['id']} \n Designation : {i[' designation']} \n Email : {i[' email']}")
        #





   # csv_writer.writerow(201, 'Abhay', 'Student', 'abhayp1334@gmail.com')
