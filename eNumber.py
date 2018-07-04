import math

def loadENumber():
    eFile = open('Euler number.txt')
    eNum = []
    for e in eFile.read().split(' '):
        eNum.append(e)
    newE = ''.join(eNum)
    return newE

def isPrime(num):
    num = int(num)
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def findListOfTenDiNums(num):
    someList = []
    for i in range(len(num)):
        tenDi = num[i:i+10]
        if len(tenDi) == 10:
            someList.append(tenDi)
    return someList

def stringsIntoInt(someList):
    integers = []
    for i in someList:
        integers.append(int(i))
    return integers

def main():
    eNumber = loadENumber()
    eNum = eNumber[:200]
    s = findListOfTenDiNums(eNum)

    listOfPrimeInts = stringsIntoInt(s)

    firstPrimeNums = []
    for i in listOfPrimeInts:
        if isPrime(i):
            firstPrimeNums.append(i)
            
    print('The first 5 10-digit primes  in  consecutive digits of e are: ')
    for d in firstPrimeNums:
        print(d)

if __name__ == '__main__':
    main()
            
    
        

    

    


        






