import json
def convert_json_to_dictionary(filepath):
    z=open(filepath,'r')
    y=z.read()
    js=json.loads(y)
    z.close()
    return js
def rule_1_validation(dictionary):
    l1=list(dictionary["nodes"].keys())[0]
    if len(dictionary["nodes"][l1]["document"]["children"])==1:
        l=dictionary["nodes"][l1]["document"]["children"][0]
        if l["name"] in ["Header","Body","Footer","Row","Container | Fluid"] or l["name"].startswith("col"):
            return False
        elif l["type"]=="INSTANCE":
            return False
        else:
            return True
    return False
def rule_2_validation(dictionary):
    l1=list(dictionary["nodes"].keys())[0]
    if dictionary["nodes"][l1]["document"]["children"][0]["name"]=="Sidedraw": 
        l=dictionary["nodes"][l1]["document"]["children"][0]["children"]
        g=0
        for i in range(len(l)):
            if l[i]["name"] in ["Header","Body","Footer"]:
                g+=1
            else:
                return False
        if g==3:
            return True
        else:
            return False
    return False
def rule_3_validation(dictionary):
    l1=list(dictionary["nodes"].keys())[0]
    l=dictionary["nodes"][l1]["document"]["children"][0]["children"]
    for i in range(len(l)):
        if l[i]["name"]=="Body":
           if len(l[i]["children"])==1 and l[i]["children"][0]["name"]=="Container | Fluid":
               return True
           else:
               return False
def rule_4_validation(dictionary):
    l1=list(dictionary["nodes"].keys())[0]
    l=dictionary["nodes"][l1]["document"]["children"][0]["children"]
    for i in range(len(l)):
        if l[i]["name"]=="Body":
            for j in range(len(l[i]["children"][0]["children"])):
                if l[i]["children"][0]["children"][j]["name"]=="Row":
                    continue
                else:
                    return False
    return True
def rule_5_validation(dictionary):
    l1=list(dictionary["nodes"].keys())[0]
    l=dictionary["nodes"][l1]["document"]["children"][0]["children"]
    for i in range(len(l)):
        if l[i]["name"]=="Body":
            for j in range(len(l[i]["children"][0]["children"])):
                for k in range(len(l[i]["children"][0]["children"][j]["children"])):
                    if l[i]["children"][0]["children"][j]["children"][k]["name"].startswith("col"):
                        continue
                    else:
                        return False
    return True
def rule_6_validation(dictionary):
    l1=list(dictionary["nodes"].keys())[0]
    l=dictionary["nodes"][l1]["document"]["children"][0]["children"]
    for i in range(len(l)):
        if l[i]["name"]=="Body":
            for j in range(len(l[i]["children"][0]["children"])):
                for k in range(len(l[i]["children"][0]["children"][j]["children"])):
                    for m in range(len(l[i]["children"][0]["children"][j]["children"][k]["children"])):
                        if l[i]["children"][0]["children"][j]["children"][k]["children"][m]["type"]=="INSTANCE" or l[i]["children"][0]["children"][j]["children"][k]["children"][m]["type"]=="GROUP":
                            continue
                        else:
                            return False
    return True    
def rule_7_validation(dictionary):
    snf=["1","2","3","4","5","6","7","8","9","10","11","12"]
    snl=[4,5,7,8]
    smf=["xl","lg","md","sm","offxl","offlg","offmd","offsm"]
    l1=list(dictionary["nodes"].keys())[0]
    l=dictionary["nodes"][l1]["document"]["children"][0]["children"]
    for i in range(len(l)):
        if l[i]["name"]=="Body":
            for j in range(len(l[i]["children"][0]["children"])):
                for k1 in range(len(l[i]["children"][0]["children"][j]["children"])):
                    k=l[i]["children"][0]["children"][j]["children"][k1]["name"]        
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