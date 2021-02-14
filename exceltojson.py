import pandas as pd
import json

#input details here:
#-----------------------------------------------------
separator='_'
excelfile="exampleExcel.xlsx"
#-----------------------------------------------------

def listremover(thedict,sep):
    """removes list in the values of dict file if the list contains only one element
    Also return a list of keys in dictionary with a separator, to get removed later"""
    remove=[]
    for key,value in thedict.items():
        if key[-1]==sep:
            remove.append(key)
        if type(value)!=list or key[-1]==sep:
            continue
        if not len(value):
            thedict[key]=''
        elif len(value)==1:
            thedict[key]=value[0]
    return thedict,remove

def createjson(file,sep):
    """file = excel file encoded in json format
       sep  = separator used
       Returns a dictionary in json format"""
    res={}
    data=pd.read_excel(file)
    data=pd.read_excel(file,names=[i for i in range(data.shape[1])])
    # print(data.to_string())
    # print(data.shape)
    tempDict,tempDict2,tempList={},{},[]
    j=0
    for key_ in data[0]:
        res[key_] = [data[i][j] for i in range(1,data.shape[1]) if not isinstance(data[i][j], float)]
        j+=1

    [res,deleteLater] = listremover(res,sep)

    for key,values in res.items():
        if sep in key:
            if key[-1]!=sep:
                tempList.append(key.split(sep))
            tempDict[key]=values

    for i in tempList:
        tempDict2[i[0]] = [dict.fromkeys({x[1] for x in tempList if x[0]==i[0]}, '')]

    for key,values in tempDict2.items():
        for value in values[0]:
            x=sep.join([key,value])
            tempDict2[key][0][value] = tempDict[x]
            del res[x]
    res.update(tempDict2)

    for delete in deleteLater:
        res[delete[:-1]] = res[delete]
        del res[delete]

    return res

convertedJSON = createjson(excelfile,separator)
print(convertedJSON)

#dumps dictionary into json file

with open("result.json", 'w') as result:
    json.dump(convertedJSON, result, indent=4, sort_keys=True)