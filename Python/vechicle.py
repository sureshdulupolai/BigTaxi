import time, random

class Model():
    def __init__(self, value, limit, typeof):

        self._saved = False
        if value == True:
            self.Value = True
            self.vPassangerLimit = limit
            self.vType = typeof
        else:
            self.Value = False

    def save(self):
        if self.Value == True:
            self._saved = True
            return self  # Return the object itself
        else:
            return None

    def Check(self):
        if not self._saved:
            return ('"Error: You must call .save() before .Check()" ⚠')

        else:
            # print(self.vPassangerLimit)
            return {'Passenger Limit' : self.vPassangerLimit, 'Vechicle Type' : self.vType}

def CheckFunction(vType, vLimitNo):
    vLimit = int(vLimitNo); lstOfType = ['Bicycle', 'Motor Bike', '4 Wheeler', 'More than 4 Wheeler']

    if vType in ['Bicycle', 'Motor Bike']:
        if vLimit == 1:
            print('SuccessFull Parmit')
            return True
        
        else:
            print("Warning : Max No Of Passenger. You Can Take Is '1' ⚠")
            return False

    elif vType == '4 Wheeler':
        if vLimit <= 10:
            print('Parmit Granted For Big Taxi!')
            return True
        
        else:
            print('Warning : No, Parmit Granted For Big Taxi...!, Max Limit is 10 Passeneger ⚠')
            return False

    elif vType == 'More than 4 Wheeler':
        print('Access Parmit Granted For Big truck or Bus!, but after some days you need to upload all vechicle proof to me after that you can Run your vechicle on big taxi')
        return True
    
    else:
        if vType in lstOfType:
            CheckFunction(vType, vLimit)

        else:
            print('Warning : No Vechicle Type Matched ⚠')
            return False

def ModlesStatus(statusReturn):
    if statusReturn == True:
        print('Data Save Success Full')
    elif statusReturn == False:
        print('Warning : Data Not!, Saved in Model Due To Some Error Check Input Model Data Again! ⚠')
    else:
        print('Error : Dont Pass Value By Your Self ⚠ ⚠')

def OwnModelData(NoOfPassenger, VechicleType):

    FinalDataList = []
    if bool(NoOfPassenger) == True and bool(VechicleType) == True:
        for passenger in range(len(NoOfPassenger)):
            passengerNo = NoOfPassenger[passenger]
            vechicleTypes = VechicleType[passenger]

            CF = CheckFunction(vLimitNo= passengerNo, vType= vechicleTypes)
            # return object of Data saved
            ModelData = Model(value=CF, limit=passengerNo, typeof=vechicleTypes).save()

            # To Check Status Code if save or not!
            # ModlesStatus(statusReturn= ModelData)

            # time.sleep(random.randint(1, 4))
            time.sleep(1)
            if ModelData:
                # returning a dct of data save
                Data = ModelData.Check()
                # adding that dct into a lst
                FinalDataList.append(Data)
            else:
                # print("Skipping entry due to invalid data.")
                continue
        
        time.sleep(2)
        print('Every Thing Done SuccessFully!!')
        print()

        time.sleep(5)
        return FinalDataList
    
    else:
        print('Empty Data Cannot Store')

# Main Program Start from Here
NoOfPassenger = ['1', '11', '1']
VechicleType = ['Motor Bike', 'Bike', 'Motor Bike']

# OMD = OwnModelData(NoOfPassenger= NoOfPassenger, VechicleType= VechicleType)
# print(OMD)

# ------------------------------------------------------------------------------------
# Common Element Inside Set - 1 in both set. 0 set1, 1 set2 = 1
# --------------------------------------------------------------------------------
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1 - set2) # 1