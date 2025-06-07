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

NewObject = formateText(a, b, c, d, e, f, g, listOfTypes=['+', '-', '*'])
print(NewObject)

# class and object to count, types in list