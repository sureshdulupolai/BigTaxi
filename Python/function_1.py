# return string + int dynamic
def CheckFunction(types, value, DataInText):
    NewObj = ''
    if types == '/':  NewObj += str(value[DataInText] / value[DataInText + 1])
    elif types == '-': NewObj += str(value[DataInText] - value[DataInText + 1])
    elif types == '*': NewObj += str(value[DataInText] * value[DataInText + 1])
    elif types == '%': NewObj += str(value[DataInText] % value[DataInText + 1])
    else: NewObj += str(value[DataInText] + value[DataInText + 1])
    return NewObj

def CheckOverTypes(count, value, DataInText, listOfTypes):
    NewObj = ''
    if listOfTypes[count] == '+': NewObj += str(value[DataInText] + value[DataInText + 1])
    elif listOfTypes[count] == '-': NewObj += str(value[DataInText] - value[DataInText + 1])
    elif listOfTypes[count] == '*': NewObj += str(value[DataInText] * value[DataInText + 1])
    elif listOfTypes[count] == '/': NewObj += str(value[DataInText] / value[DataInText + 1])
    elif listOfTypes[count] == '%': NewObj += str(value[DataInText] % value[DataInText + 1])
    return NewObj

def formateText(*values, types = '+', listOfTypes = []):
    value = [*values]; NewText = ''; skip = 0; IntFl = [int, float]; count = 0

    for DataInText in range(len(value)):
        if skip == 0:
            if isinstance(value[DataInText], str): NewText += value[DataInText]

            elif type(value[DataInText]) in IntFl:

                if type(value[DataInText + 1]) in IntFl:

                    if len(listOfTypes) == 0:
                        NewText += CheckFunction(types, value, DataInText) 
                    else:
                        NewText += CheckOverTypes(count, value, DataInText, listOfTypes)
                        if (len(listOfTypes) - 1) > count: count += 1

                    skip = 1
                elif isinstance(value[DataInText + 1], str): NewText += value[DataInText]
            
            else:
                return f"❌ Unsupported operation type: {type(value[DataInText])} in formateText Function. \nIndex Position at {DataInText}"

        else: skip = 0

    return NewText

a = '12'
b = 1
c = 3.3
d = '45'
e = '10'
f = 12
g = 3.3

# NewObject = formateText(a, b, c, d, e, f, g, listOfTypes=['+', '-', '*'])
# print(NewObject)

# class and object to count, types in list
class CountTypes:
    integer = 0; floating = 0; string = 0; boolen = 0; lst = 0; tpl = 0; dct = 0; sets = 0
    lstOfInt = []; lstOfFloat = []; lstOfSrting = []; lstOfBool = []; lstOfLst = []; lstOfTuple = []; lstOfSet = []; lstOfDict = []

    def __init__(self, value):
        self.value = value

        for i in self.value:
            if isinstance(i, bool): CountTypes.boolen += 1; CountTypes.lstOfBool.append(i)
            elif isinstance(i, int): CountTypes.integer += 1; CountTypes.lstOfInt.append(i)
            elif isinstance(i, float): CountTypes.floating += 1; CountTypes.lstOfFloat.append(i)
            elif isinstance(i, str): CountTypes.string += 1; CountTypes.lstOfSrting.append(i)
            elif isinstance(i, list): CountTypes.lst += 1; CountTypes.lstOfLst.append(i)
            elif isinstance(i, tuple): CountTypes.tpl += 1; CountTypes.lstOfTuple.append(i)
            elif isinstance(i, set): CountTypes.sets += 1; CountTypes.lstOfSet.append(i)
            elif isinstance(i, dict): CountTypes.dct += 1; CountTypes.lstOfDict.append(i)
    
    def Total(self):
        return f"Int : {CountTypes.integer}\nFloat : {CountTypes.floating}\nStr : {CountTypes.string}\nbool : {CountTypes.boolen}\nlist : {CountTypes.lst}\nTuple : {CountTypes.tpl}\nSet : {CountTypes.sets}\nDict : {CountTypes.dct}"

    def NonZeroTotal(self):
        NewSet = ''
        if CountTypes.integer: NewSet += f'Int : {CountTypes.integer}\n'
        if CountTypes.floating: NewSet += f'Float : {CountTypes.floating}\n'
        if CountTypes.string: NewSet += f'Str : {CountTypes.string}\n'
        if CountTypes.boolen: NewSet += f'Bool : {CountTypes.boolen}\n'
        if CountTypes.lst: NewSet += f'List : {CountTypes.lst}\n'
        if CountTypes.tpl: NewSet += f'Tuple : {CountTypes.tpl}\n'
        if CountTypes.sets: NewSet += f'Set : {CountTypes.sets}\n'
        if CountTypes.dct: NewSet += f'Dict : {CountTypes.dct}\n'
        return NewSet[:-1]
        

from countertypes import core

lst = [1, 2, '1', '0', 2, [1, 2], (2, 6), {1, 2, 4}, True]
C1 = CountTypes(lst)
print(C1.Total())
print(C1.NonZeroTotal())
