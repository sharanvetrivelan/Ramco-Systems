import time
start=time.time()
import jsonvalidation 
import htmlvalidation
import os
import json
import csv
from datetime import datetime
a=datetime.now()
b="D://automation//output//Validation_"+a.strftime("%Y-%m-%d_%H-%M-%S")
if os.path.exists("D://automation//output"):
    os.mkdir(b)
else:
    os.mkdir("D://automation//output")
    os.mkdir(b)
dic= jsonvalidation.convert_json_to_dictionary('D://automation//1655-29168 1.json')
li=htmlvalidation.convert_div_to_list('D://automation//test1.html')
r=open('D://automation//Rules.json','r')
rule=r.read()
rules=json.loads(rule)
r.close()
fields=["Rule.No","Description","JSON Key Assessed","HTML Key Assessed","Validation Status"]
csvfile=open(f'{b}//rulesvalidationreport1.csv','w',newline='')
csvwriter = csv.writer(csvfile)
csvwriter.writerow(fields)
for key in rules.keys():
    if key=="RULE 1":
        if jsonvalidation.rule_1_validation(dic) and htmlvalidation.rule_1_validation(li):
            csvwriter.writerow([1,rules[key],"Name,Type","Fig-Name","Pass"])
        else:
            csvwriter.writerow([1,rules[key],"Name,Type","Fig-Name","Fail"])
    elif key=="RULE 2":
        if jsonvalidation.rule_2_validation(dic) and htmlvalidation.rule_2_validation(li):
            csvwriter.writerow([2,rules[key],"Name","Fig-Name","Pass"])
        else:
            csvwriter.writerow([2,rules[key],"Name","Fig-Name","Fail"])
    elif key=="RULE 3":
        if jsonvalidation.rule_3_validation(dic) and htmlvalidation.rule_3_validation(li):
            csvwriter.writerow([3,rules[key],"Name","Fig-Name","Pass"])
        else:
            csvwriter.writerow([3,rules[key],"Name","Fig-Name","Fail"])
    elif key=="RULE 4":
        if jsonvalidation.rule_4_validation(dic) and htmlvalidation.rule_4_validation(li):
            csvwriter.writerow([4,rules[key],"Name","Fig-Name","Pass"])
        else:
            csvwriter.writerow([4,rules[key],"Name","Fig-Name","Fail"])
    elif key=="RULE 5":
        if jsonvalidation.rule_5_validation(dic) and htmlvalidation.rule_5_validation(li):
            csvwriter.writerow([5,rules[key],"Name","Fig-Name","Pass"])
        else:
            csvwriter.writerow([5,rules[key],"Name","Fig-Name","Fail"])
    elif key=="RULE 6":
        if jsonvalidation.rule_6_validation(dic) and htmlvalidation.rule_6_validation(li):
            csvwriter.writerow([6,rules[key],"Type","Fig-Name","Pass"])
        else:
            csvwriter.writerow([6,rules[key],"Type","Fig-Name","Fail"])
    elif key=="RULE 7":
        if jsonvalidation.rule_7_validation(dic) and htmlvalidation.rule_7_validation(li):
            csvwriter.writerow([7,rules[key],"Name","Fig-Name","Pass"])
        else:
            csvwriter.writerow([7,rules[key],"Name","Fig-Name","Fail"])
    else:
        print("error")
        break
csvfile.close()
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
wb = Workbook()
ws = wb.active
csvfile1=open(f'{b}//rulesvalidationreport1.csv','r')
csvreader=csv.reader(csvfile1)
for row in csvreader:
    ws.append(row)
csvfile1.close()
for col in ws.columns:
    max_length = 0
    column = col[0].column_letter
    for cell in col:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(cell.value)
        except:
            pass
    adjusted_width = (max_length + 2)
    ws.column_dimensions[column].width = adjusted_width
excel=open(f'{b}//rulesvalidationreport.xlsx','w')
wb.save(f'{b}//rulesvalidationreport.xlsx')
os.remove(f'{b}//rulesvalidationreport1.csv')
end=time.time()
print(end-start)