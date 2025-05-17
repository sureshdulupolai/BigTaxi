DMS = [
    {'CouponCode' : 'DRIVERBIGTAXI10001', 'DriverName' : 'suresh'},
    {'CouponCode' : 'DRIVERBIGTAXI10002', 'DriverName' : 'akash'},
    {'CouponCode' : 'BIGTAXICUSTOMER', 'DriverName' : 'ashish'},
    {'CouponCode' : 'BIGTAXIDEVELOPER10001', 'DriverName' : 'santosh'}
]

# DMS = []

requestUsername = 'pritam'.lower()
CodeName = 'DRIVERBIGTAXI'
NotCouponNameOne = 'BIGTAXIDEVELOPER'
NotCouponNameTwo = 'BIGTAXICUSTOMER'

if len(DMS) > 0:

    # DMS.last()
    codeLst, lstOfUsername = [DataCode['CouponCode'] for DataCode in DMS if (DataCode['CouponCode'] != NotCouponNameTwo) and (NotCouponNameOne not in DataCode['CouponCode'])], [DataIn['DriverName'].lower() for DataIn in DMS if (DataIn['CouponCode'] != NotCouponNameTwo) and (NotCouponNameOne not in DataIn['CouponCode'])]
    # print(len(codeLst))
    lastCode = codeLst[len(codeLst) - 1]


    if requestUsername in lstOfUsername:
        # message - you can't create two coupon for one id
        pass

    else:
        oldCode = ''
        for LC in lastCode:
            if LC.isdigit():
                oldCode += LC
        newCode = CodeName + str((int(oldCode) + 1))
        # print(oldCode)
        # print(lastCode)
        # print(newCode)

else:
    Number = 10001; newCodeFirst = CodeName + str(Number); DMS.append(newCodeFirst)

# print(DMS)