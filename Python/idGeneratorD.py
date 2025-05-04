lst = [
    'DRIVER1234', 'DRIVER12353'
]

lastUserId = lst[len(lst) - 1]

Data = ''; Number = ''

for LUI in lastUserId:

    if LUI.isdigit():
        Number += LUI
        
    else:
        Data += LUI

NewUserId = Data + str(int(Number) + 1)

print(NewUserId)