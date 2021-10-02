# importing pandas as pd
import pandas as pd


class PartOrdered:

    def __init__(self, name, team, partNum, part, price, quantity, company, ordered,link,stock,account):
        self.name = name
        self.team = team
        self.partNum = partNum
        self.part = part
        self.price = price
        self.quantity = quantity
        self.company = str(company).replace(" ", "")
        if company == "McMaster":
            self.company = "McMaster-Carr"

        self.ordered = ordered
        self.link = link
        self.stock = stock
        self.account= account


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
                              partOrdered[6], partOrdered[7], partOrdered[12],partOrdered[8],partOrdered[13],partOrdered[11])

        if newPart.ordered == "Y" or  newPart.stock == "Y" or newPart.account != "KGCOE":
            continue

        #BattleBots Sorter
        #if "TUX" in newPart.team or "Battle" in newPart.team:
#
        #    if 'BattleBots' not in purchaseList.keys():
        #        purchaseList["BattleBots"] = dict()
        #        purchaseList["BattleBots"][newPart.company]=[]
        #        purchaseList["BattleBots"][newPart.company].append(list())
        #        purchaseList["BattleBots"][newPart.company][0]=[]
        #        purchaseList["BattleBots"][newPart.company][0].append(newPart)
        #        continue
        #    if newPart.company not in purchaseList["BattleBots"]:
        #        purchaseList["BattleBots"][newPart.company]=list()
        #        purchaseList["BattleBots"][newPart.company].append(list())
        #        purchaseList["BattleBots"][newPart.company][0]=[]
        #        purchaseList["BattleBots"][newPart.company][0].append(newPart)
        #        continue
        #    ########
        #    if len(purchaseList["BattleBots"][newPart.company][len(purchaseList["BattleBots"][newPart.company])-1])>4:
        #        purchaseList["BattleBots"][newPart.company].append(list())
        #        purchaseList["BattleBots"][newPart.company][len(purchaseList["BattleBots"][newPart.company])-1].append(newPart)
        #        continue
        #    else:
        #        purchaseList["BattleBots"][newPart.company][len(purchaseList["BattleBots"][newPart.company])-1].append(newPart)
        #        continue
#
        ##Check to see if theres a team
        #if not newPart.team in purchaseList.keys():
        #    purchaseList[newPart.team] = dict()
        #    purchaseList[newPart.team][newPart.company] = []
        #    purchaseList[newPart.team][newPart.company].append([newPart])
        #    continue
        ##Check to see if theres a company
        if not newPart.company in purchaseList.keys():
            purchaseList[newPart.company] = []
            purchaseList[newPart.company].append([newPart])
            continue
        #Sorting through list
        if len(purchaseList[newPart.company][len(purchaseList[newPart.company])-1]) > 4:
            purchaseList[newPart.company].append([])
            purchaseList[newPart.company][len(purchaseList[newPart.company])-1].append(newPart)
        else:

            purchaseList[newPart.company][len(purchaseList[newPart.company])-1].append(newPart)

    return purchaseList
