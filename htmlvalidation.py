def convert_div_to_list(filepath):
    k=open(filepath,'r')
    j=k.read()
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(j, 'html.parser')
    return convert_div_to_list_1(soup)
def convert_div_to_list_1(div):
    children = div.find_all(recursive=False)
    nested_list = []
    for child in children:
        if child.name == 'div':
            nested_list.append(child.get("fig-name"))
            children1=child.find_all(recursive=False)
            if children1:
                nested_list.append(convert_div_to_list_1(child))
        else:
            continue
    return nested_list
def rule_1_validation(lists):   
    if lists[0] in ["Header","Body","Footer","Row","Container | Fluid"] or lists[0].startswith("col") or len(lists)>2:
        return False
    elif lists[0].startswith("Input") or lists[0]=="Button" or lists[0]=="RadioButton" or lists[0]=="Textarea" or lists[0]=="Checkbox":
        return False
    else:
        return True
def rule_2_validation(lists):
    if lists[0]=="Sidedraw": 
        g=0
        for i in lists[1]:
            if isinstance(i,list) == False:
                if i in ["Header","Body","Footer"]:
                    g+=1
                else:
                    return False
        if g==3:
            return True
        else:
            return False
    return False
def rule_3_validation(lists):
    for i in lists[1]:
        if i=="Body":
            if len(lists[1][lists[1].index(i)+1])==2 and lists[1][lists[1].index(i)+1][0]=="Container | Fluid":
                return True
            else:
                return False
def rule_4_validation(lists):
    for i in lists[1]:
        if isinstance(i,list):
            for j in i[1]:
                if isinstance(j,list)==False:
                    if j=="Row":
                        continue
                    else:
                        return False
    return True
def rule_5_validation(lists):
    for i in lists[1]:
        if isinstance(i,list):
            for j in i[1]:
                if isinstance(j,list):
                    for k in j:
                        if isinstance(k,list)==False:
                            if k.startswith("col"):
                                continue
                            else:
                                return False
    return True
def rule_6_validation(lists):
    for i in lists[1]:
        if isinstance(i,list):
            for j in i[1]:
                if isinstance(j,list):
                    for k in j:
                        if isinstance(k,list):
                            for l in k:
                                if isinstance(l,list)==False:
                                    if l==None:
                                        continue
                                    elif l.startswith("Input") or l=="Button" or l=="RadioButton" or l=="Textarea" or l=="Checkbox":
                                        continue
                                    else:
                                        return False
    return True
def rule_7_validation(lists):
    snf=["1","2","3","4","5","6","7","8","9","10","11","12"]
    snl=[4,5,7,8]
    smf=["xl","lg","md","sm","offxl","offlg","offmd","offsm"]
    for i in lists[1]:
        if isinstance(i,list):
            for j in i[1]:
                if isinstance(j,list):
                    for k in j:
                        if isinstance(k,list)==False:
                            if len(k.split("|")[1].split(","))==1:
                                if len(k.split("|")[1].split(",")[0]) in snl:
                                    if k.split("|")[1].split(",")[0][1:3] in smf:
                                        if k.split("|")[1].split(",")[0].split(k.split("|")[1].split(",")[0][1:3])[1] in snf:
                                            continue
                                        else:
                                            return False
                                    return False
                                return False
                            elif len(k.split("|")[1].split(","))==2:
                                if len(k.split("|")[1].split(",")[0]) in snl and len(k.split("|")[1].split(",")[1]) in snl :
                                    if k.split("|")[1].split(",")[0][1:3] in smf and k.split("|")[1].split(",")[1][1:3] in smf and k.split("|")[1].split(",")[0][1:3]!= k.split("|")[1].split(",")[1][1:3] :
                                        if k.split("|")[1].split(",")[0].split(k.split("|")[1].split(",")[0][1:3])[1] in snf and k.split("|")[1].split(",")[1].split(k.split("|")[1].split(",")[1][1:3])[1] in snf:
                                            continue
                                        else:
                                            return False
                                    elif k.split("|")[1].split(",")[0][1:3] in smf and k.split("|")[1].split(",")[1][1:6] in smf and k.split("|")[1].split(",")[0][1:3] == k.split("|")[1].split(",")[1][4:6] :
                                        if k.split("|")[1].split(",")[0].split(k.split("|")[1].split(",")[0][1:3])[1] in snf and k.split("|")[1].split(",")[1].split(k.split("|")[1].split(",")[1][1:6])[1] in snf:
                                            continue
                                        else:
                                            return False
                                    return False
                                return False
                            elif len(k.split("|")[1].split(","))==3:
                                if len(k.split("|")[1].split(",")[0]) in snl and len(k.split("|")[1].split(",")[1]) in snl and len(k.split("|")[1].split(",")[2]) in snl:
                                    if k.split("|")[1].split(",")[0][1:3] in smf and k.split("|")[1].split(",")[1][1:3] in smf and k.split("|")[1].split(",")[2][1:3] in smf and k.split("|")[1].split(",")[0][1:3]!=k.split("|")[1].split(",")[1][1:3] and k.split("|")[1].split(",")[1][1:3]!=k.split("|")[1].split(",")[2][1:3] and k.split("|")[1].split(",")[2][1:3]!=k.split("|")[1].split(",")[0][1:3]:
                                        if k.split("|")[1].split(",")[0].split(k.split("|")[1].split(",")[0][1:3])[1] in snf and k.split("|")[1].split(",")[1].split(k.split("|")[1].split(",")[1][1:3])[1] in snf and k.split("|")[1].split(",")[2].split(k.split("|")[1].split(",")[2][1:3])[1] in snf:
                                            continue
                                        else:
                                            return False
                                    return False
                                return False
                            elif len(k.split("|")[1].split(","))==4:
                                if len(k.split("|")[1].split(",")[0]) in snl and len(k.split("|")[1].split(",")[1]) in snl and len(k.split("|")[1].split(",")[2]) in snl and len(k.split("|")[1].split(",")[3]) in snl:
                                    if k.split("|")[1].split(",")[0][1:3] in smf and k.split("|")[1].split(",")[1][1:3] in smf and k.split("|")[1].split(",")[2][1:3] in smf and k.split("|")[1].split(",")[3][1:3] in smf and k.split("|")[1].split(",")[0][1:3]!=k.split("|")[1].split(",")[1][1:3] and k.split("|")[1].split(",")[1][1:3]!=k.split("|")[1].split(",")[2][1:3]and k.split("|")[1].split(",")[2][1:3]!=k.split("|")[1].split(",")[3][1:3]:
                                        if k.split("|")[1].split(",")[0].split(k.split("|")[1].split(",")[0][1:3])[1] in snf and k.split("|")[1].split(",")[1].split(k.split("|")[1].split(",")[1][1:3])[1] in snf and k.split("|")[1].split(",")[2].split(k.split("|")[1].split(",")[2][1:3])[1] in snf and k.split("|")[1].split(",")[3].split(k.split("|")[1].split(",")[3][1:3])[1] in snf:
                                            continue
                                        else:
                                            return False
                                    elif k.split("|")[1].split(",")[0][1:3] in smf and k.split("|")[1].split(",")[1][1:3] in smf and k.split("|")[1].split(",")[2][1:6] in smf and k.split("|")[1].split(",")[3][1:6] in smf and k.split("|")[1].split(",")[0][1:3]!=k.split("|")[1].split(",")[1][1:3] and k.split("|")[1].split(",")[0][1:3]==k.split("|")[1].split(",")[2][4:6] and k.split("|")[1].split(",")[1][1:3]==k.split("|")[1].split(",")[3][4:6]:
                                        if k.split("|")[1].split(",")[0].split(k.split("|")[1].split(",")[0][1:3])[1] in snf and k.split("|")[1].split(",")[1].split(k.split("|")[1].split(",")[1][1:3])[1] in snf and k.split("|")[1].split(",")[2].split(k.split("|")[1].split(",")[2][1:6])[1] in snf and k.split("|")[1].split(",")[3].split(k.split("|")[1].split(",")[3][1:6])[1] in snf:
                                            continue
                                        else:
                                            return False
                                    return False
                                return False
                            elif len(k.split("|")[1].split(","))==6:
                                if len(k.split("|")[1].split(",")[0]) in snl and len(k.split("|")[1].split(",")[1]) in snl and len(k.split("|")[1].split(",")[2]) in snl and len(k.split("|")[1].split(",")[3]) in snl and len(k.split("|")[1].split(",")[4]) in snl and len(k.split("|")[1].split(",")[5]) in snl:
                                    if k.split("|")[1].split(",")[0][1:3] in smf and k.split("|")[1].split(",")[1][1:3] in smf and k.split("|")[1].split(",")[2][1:3] in smf and k.split("|")[1].split(",")[3][1:6] in smf and k.split("|")[1].split(",")[4][1:6] in smf and k.split("|")[1].split(",")[5][1:6] in smf and k.split("|")[1].split(",")[0][1:3]!=k.split("|")[1].split(",")[1][1:3] and k.split("|")[1].split(",")[1][1:3]!=k.split("|")[1].split(",")[2][1:3] and k.split("|")[1].split(",")[2][1:3]!= k.split("|")[1].split(",")[0][1:3] and k.split("|")[1].split(",")[0][1:3]==k.split("|")[1].split(",")[3][4:6] and k.split("|")[1].split(",")[1][1:3]==k.split("|")[1].split(",")[4][4:6] and k.split("|")[1].split(",")[2][1:3]==k.split("|")[1].split(",")[5][4:6]:
                                        if k.split("|")[1].split(",")[0].split(k.split("|")[1].split(",")[0][1:3])[1] in snf and k.split("|")[1].split(",")[1].split(k.split("|")[1].split(",")[1][1:3])[1] in snf and k.split("|")[1].split(",")[2].split(k.split("|")[1].split(",")[2][1:3])[1] in snf and k.split("|")[1].split(",")[3].split(k.split("|")[1].split(",")[3][1:6])[1] in snf and k.split("|")[1].split(",")[4].split(k.split("|")[1].split(",")[4][1:6])[1] in snf and k.split("|")[1].split(",")[5].split(k.split("|")[1].split(",")[5][1:6])[1] in snf:
                                            continue
                                        else:
                                            return False
                                    return False
                                return False
                            elif len(k.split("|")[1].split(","))==8:
                                if len(k.split("|")[1].split(",")[0]) in snl and len(k.split("|")[1].split(",")[1]) in snl and len(k.split("|")[1].split(",")[2]) in snl and len(k.split("|")[1].split(",")[3]) in snl and len(k.split("|")[1].split(",")[4]) in snl and len(k.split("|")[1].split(",")[5]) in snl and len(k.split("|")[1].split(",")[6]) in snl and len(k.split("|")[1].split(",")[7]) in snl:
                                    if k.split("|")[1].split(",")[0][1:3] in smf and k.split("|")[1].split(",")[1][1:3] in smf and k.split("|")[1].split(",")[2][1:3] in smf and k.split("|")[1].split(",")[3][1:3] in smf and k.split("|")[1].split(",")[4][1:6] in smf and k.split("|")[1].split(",")[5][1:6] in smf and k.split("|")[1].split(",")[6][1:6] in smf and k.split("|")[1].split(",")[7][1:6] in smf and k.split("|")[1].split(",")[0][1:3]!=k.split("|")[1].split(",")[1][1:3] and k.split("|")[1].split(",")[0][1:3]!=k.split("|")[1].split(",")[2][1:3] and k.split("|")[1].split(",")[0][1:3]!=k.split("|")[1].split(",")[3][1:3] and k.split("|")[1].split(",")[1][1:3]!=k.split("|")[1].split(",")[2][1:3] and k.split("|")[1].split(",")[1][1:3]!=k.split("|")[1].split(",")[3][1:3] and k.split("|")[1].split(",")[2][1:3]!=k.split("|")[1].split(",")[3][1:3] and k.split("|")[1].split(",")[0][1:3]==k.split("|")[1].split(",")[4][4:6] and k.split("|")[1].split(",")[1][1:3]==k.split("|")[1].split(",")[5][4:6] and k.split("|")[1].split(",")[2][1:3]==k.split("|")[1].split(",")[6][4:6] and k.split("|")[1].split(",")[3][1:3]==k.split("|")[1].split(",")[7][4:6]:
                                        if k.split("|")[1].split(",")[0].split(k.split("|")[1].split(",")[0][1:3])[1] in snf and k.split("|")[1].split(",")[1].split(k.split("|")[1].split(",")[1][1:3])[1] in snf and k.split("|")[1].split(",")[2].split(k.split("|")[1].split(",")[2][1:3])[1] in snf and k.split("|")[1].split(",")[3].split(k.split("|")[1].split(",")[3][1:3])[1] in snf and k.split("|")[1].split(",")[4].split(k.split("|")[1].split(",")[4][1:6])[1] in snf and k.split("|")[1].split(",")[5].split(k.split("|")[1].split(",")[5][1:6])[1] in snf and k.split("|")[1].split(",")[6].split(k.split("|")[1].split(",")[6][1:6])[1] in snf and k.split("|")[1].split(",")[7].split(k.split("|")[1].split(",")[7][1:6])[1] in snf:
                                            continue
                                        else:
                                            return False
                                    return False
                                return False
                            return False
    return True