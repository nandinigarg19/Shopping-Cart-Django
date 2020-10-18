import json
allprods = ''

def printit(fl):
    print(json.dumps(fl,indent=4))


with open('Products.json','r') as fp:
    allprods = json.load(fp)
    printit(allprods)
fp.close()

allprods = [prod for prod in allprods if prod["ancestors"] == []]
printit(allprods)