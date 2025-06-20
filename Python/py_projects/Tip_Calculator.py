lstOfItems = [
    {'prdId': '101', 'prdName': 'Plane Rice', 'price': 99},
    {'prdId': '102', 'prdName': 'Dal Tadka', 'price': 120},
    {'prdId': '103', 'prdName': 'Paneer Butter Masala', 'price': 180},
    {'prdId': '104', 'prdName': 'Chicken Biryani', 'price': 210},
    {'prdId': '105', 'prdName': 'Masala Dosa', 'price': 90},
    {'prdId': '106', 'prdName': 'Veg Pulao', 'price': 110},
    {'prdId': '107', 'prdName': 'Fish Curry', 'price': 250},
    {'prdId': '108', 'prdName': 'Chole Bhature', 'price': 95},
    {'prdId': '109', 'prdName': 'Mutton Rogan Josh', 'price': 320},
    {'prdId': '110', 'prdName': 'Idli Sambhar', 'price': 80}
]

lstOfOrders = [
    {'id': 1, 'barcode': 'A102', 'prdCode': ['101', '102'], 'Tip': 20},
    {'id': 2, 'barcode': 'A103', 'prdCode': ['103'], 'Tip': 15},
    {'id': 3, 'barcode': 'A104', 'prdCode': ['104', '105'], 'Tip': 10},
    {'id': 4, 'barcode': 'A105', 'prdCode': ['106'], 'Tip': 25},
    {'id': 5, 'barcode': 'A106', 'prdCode': ['107', '108'], 'Tip': 5},
    {'id': 6, 'barcode': 'A107', 'prdCode': ['109'], 'Tip': 18},
    {'id': 7, 'barcode': 'A108', 'prdCode': ['110', '101'], 'Tip': 12},
    {'id': 8, 'barcode': 'A109', 'prdCode': ['102'], 'Tip': 8},
    {'id': 9, 'barcode': 'A110', 'prdCode': ['103', '104'], 'Tip': 30},
    {'id': 10, 'barcode': 'A111', 'prdCode': ['105'], 'Tip': 22}
]

def Bill():
    lstOfPrdId = []; Cont = True; PresentIn = 0
    newId = int(lstOfOrders[len(lstOfOrders) - 1]['id']) + 1
    newBarCode = int(lstOfOrders[len(lstOfOrders) - 1]['barcode'][1:]) + 1
    
    while Cont:
        barCodeInter = input('Enter Code: ')
        for i in lstOfItems:
            if barCodeInter == i['prdId']:
                PresentIn += 1; lstOfPrdId.append(i['prdId']); userCheck = int(input('\n1. yes\n2. No\nAdded More Items? : '))
                if userCheck == 2: Cont = False; break

        if PresentIn == 0:
            Cont = False
            print(f'{barCodeInter} is Not Present In System!')

    if PresentIn != 0:
        tip = int(input('Tip : ')) or 0
        lstOfOrders.append({'id' : newId, 'barcode' : newBarCode, 'prdCode' : lstOfPrdId, 'Tip' : tip})
        print(lstOfOrders)

def ReturnPrd():
    ...

def Inquery():
    ...

def checkPrice():
    ...

def TipCount():
    ...

def profit():
    ...

def Restro():
    print("1. Bill\n2. Return\n3. Inquery\n4. Check Price\n5. Tips Count\n6. Total")
    userInput = int(input('Select Option : '))
    if userInput == 1: Bill()
    elif userInput == 2: ReturnPrd()
    elif userInput == 4: checkPrice()
    elif userInput == 5: TipCount()
    elif userInput == 6: profit()
    else: Inquery()


# -------------------------------------------------------------------------------------
Restro()
