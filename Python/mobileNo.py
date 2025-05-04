mobileNo = '9820646838'

if len(mobileNo) == 10:

    CheckMobileNo = ''
    for MN in mobileNo:
        if MN.isdigit(): CheckMobileNo += MN
        else:break

    if len(CheckMobileNo) == 10: print('Pass')
    else: print('Fail')