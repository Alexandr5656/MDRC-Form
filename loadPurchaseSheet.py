# importing pandas as pd
import pandas as pd


# read an excel file and convert
# into a dataframe object


# show the dataframe


#   0:TimeStamp

class PartOrdered:

    def __init__(self, name, team, part, price, quantity, company, ordered):
        self.name = name
        self.team = team
        self.part = part
        self.price = price
        self.quantity = quantity
        self.company = company
        self.ordered = ordered


#   1:Name
#   2:Team
#   3:Part
#   4:Price
#   5:Quantity
#   6:Company
#   7:Link
#   8:Total Amount
#   9:Additional Notes
#   10:Account
#   11:Ordered
#   12:Date Ordered
#   13:Date Recieved
# name,team,part,price,quantity,company,ordered
def loadSheet(fileName):
    df = pd.DataFrame(pd.read_excel(fileName))
    purchaseList = dict()
    for partOrdered in df.values:
        newPart = PartOrdered(partOrdered[1], partOrdered[2], partOrdered[3], partOrdered[4], partOrdered[5],
                              partOrdered[6], partOrdered[11])

        if newPart.ordered == "y":
            continue
        if "TUX" in newPart.team or "Battle" in newPart.team:
            if 'BattleBots' not in purchaseList.keys():
                purchaseList["BattleBots"] = dict()
                purchaseList["BattleBots"][newPart.company] = []
                purchaseList["BattleBots"][newPart.company].append(newPart)
                continue
            if newPart.company not in purchaseList["BattleBots"]:
                purchaseList["BattleBots"][newPart.company] = []
            purchaseList["BattleBots"][newPart.company].append(newPart)
            continue

        if not newPart.team in purchaseList.keys():
            purchaseList[newPart.team] = dict()
            purchaseList[newPart.team][newPart.company] = []
            purchaseList[newPart.team][newPart.company].append(newPart)
            continue
        if not newPart.company in purchaseList[newPart.team].keys():
            purchaseList[newPart.team][newPart.company] = []
            purchaseList[newPart.team][newPart.company].append(newPart)
            continue
        purchaseList[newPart.team][newPart.company].append(newPart)
    return purchaseList
