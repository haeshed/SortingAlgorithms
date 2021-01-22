
import random, time, logging
from numpy import zeros
#import plotWorld
logging.basicConfig(filename='sorting_log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.DEBUG)
logging.debug('start of program\n\n\n')

def createRandomArr(length = 0, height = 0):
    arr1 = []
    for i in range(length):
        arr1.append(random.randint(0, height))
    logging.debug('created random array:  {}'.format(arr1))
    return arr1

#print(createRandomArr(50))

def write_to_file(arr = []):
    logging.debug('         start write to file')
    with open('test112.txt', 'w') as tstfl2:
        for i in range(len(arr)):
            tstfl2.write(str(arr[i]))
            tstfl2.write("\n")
        logging.debug('         wrote to file')


def printFile():
    with open('test112.txt') as tstfl2:
        print(tstfl2.read())


def read_array_file():
    logging.debug('         start read file')
    with open('test112.txt', 'r') as graph_data:
        graph_data = graph_data.read()
        lines = graph_data.split('\n')
        ys = []
        for i in range(len(lines)-1):
            ys.append(int(lines[i]))
        logging.debug('         finish read file')
    return ys


def bubbleSort(arr1 = []):
    logging.debug('start bubble sort')
    curr=0
    for i in range(len(arr1)-1):
        for j in range(len(arr1)-1):
            if(arr1[j]>arr1[j+1]):
                curr=arr1[j+1]
                arr1[j+1]=arr1[j]
                arr1[j]=curr
                #time.sleep(.03)
                print(arr1)
                write_to_file(arr1)
            time.sleep(.01)
    logging.debug('finished bubble sort')
    return arr1
#write_to_file(createRandomArr(10,10))
#temp2 = createRandomArr(100, 100)
#print(bubbleSort(temp2))

def insertionSort(arr1 = []):
    logging.debug('start insertion sort')
    tem1=0
    for i in range(len(arr1)-1):
        for j in reversed(range(i+1)):
            print("{}   J+1-{}  arr[j]{}  arr[j+1]{}".format(arr1 , j+1, arr1[j], arr1[j+1]))
            if(arr1[j+1]<arr1[j]):
                tem1 = arr1[j+1]
                arr1[j+1]=arr1[j]
                arr1[j]=tem1
                #time.sleep(.03)
                print(arr1)
                write_to_file(arr1)
            time.sleep(.01)
    logging.debug('finish insertion sort')
    return arr1


def selectionSort(arr1 = []):
    logging.debug('start selection sort')
    ind=0
    tem1=0
    for i in range(len(arr1)-1):
        #min1=arr1[i]
        ind=i
        for j in range(i, len(arr1)-1):
            print("{}  i {}  J+1 {}  arr[ind] {}  arr[j+1] {}".format(arr1 , i, j+1, arr1[ind], arr1[j+1]))
            if(arr1[j+1]<arr1[ind]):
                print("yes")
                ind = j+1
                time.sleep(.01)
            else: print("no")
        tem1 = arr1[i]
        arr1[i]=arr1[ind]
        arr1[ind]=tem1
        write_to_file(arr1)
    logging.debug('finish selection sort')
    return arr1

def countingSort(k, arr1=[]):
    logging.debug('start counting sort')
    indexes = [0] * (k+1)
    for i in range(len(arr1)):
        indexes[arr1[i]] +=1
        print("arr1[]   {} {} {}".format(arr1, i, arr1[i]))
        print ("1 indexes:   {}".format(indexes))
        print("")
    for i in range(k):
        indexes[i+1]+=indexes[i]
        print ("2 indexes:   {}".format(indexes))
        time.sleep(.01)
    newarr1 = [0] * len(arr1)
    print (newarr1)
    print(len(arr1))
    for i in range(len(arr1)):
        ind2 = arr1[i]
        ind3 = indexes[ind2]
        newarr1[ind3-1]=ind2
        indexes[ind2]-=1
        arr1[:i+1]=newarr1[:i+1]
        #time.sleep(.01)
        write_to_file(arr1)
    logging.debug('finished counting sort')

#temp2 = createRandomArr(100, 10)
#print(insertionSort(temp2))



def recTest(num:int):
    print (num)
    if(num==2):
        return 2
    return num*recTest(num-1)

def quickSort(arr1, low: int, high: int):
    time.sleep(.01)
    if(low<high):
        print("Q quick full {} low {} high {}".format(arr1, low, high))
        pi = partition(high, low, arr1)
        print("Q low sort {}  low {}  pi-1 {}".format(arr1, low, pi-1))
        quickSort(arr1, low, pi-1)
        print("Q high sort {}  pi+1  {}  high  {}".format(arr1, pi+1, high))
        quickSort(arr1, pi, high)

def partition(high: int, low = 0, arr1 = []):
    print("\n           partition: \n           P arr1[low:high]  {}   len = {}".format(arr1[low:high], len(arr1[low:high])))
    piv = arr1[high-1]
    temp = 0
    i = low-1
    print("\n           P StartSort:")
    for j in range(low, high):
        print("         P {}   i {}  j {}  arr[j] {}   piv {}".format(arr1 ,i,  j, arr1[j], piv))
        if(arr1[j]<=piv):
            i += 1
            temp = arr1[j]
            arr1[j] = arr1[i]
            arr1[i] = temp
            print("         P yes arr1[j] {} <= piv {}".format(arr1[j], piv))
        print("         P {}   i {}  j {}  arr[j] {}   piv {}".format(arr1 ,i,  j, arr1[j], piv))
        #quickSort(arr1[0:])
    write_to_file(arr1)
    print("\n           P LAST:\n           {}   i {}  j {}  arr[j] {}   piv {}  pivin  {}".format(arr1 ,i,  j, arr1[j], piv, -1))
    print("         P i+1 == {}".format(i+1))
    return i+1
    #arr1=insertPivot(i+1, high, arr1)
    #print("fst  {} len = {}   sec {}   len  {}    pivin  {}".format(arr1[0:i], len(arr1[0:i]), arr1[i+1:], len(arr1[i+1:]), high))
    #print("finished1:   ".format(arr1))
    #print(quickSort(pivin, arr1[0:i]))
    #print("piv:   {}".format(piv))
    #print(quickSort(-1,arr1[i+1:]))
    #arr2 = quickSort(pivin, arr1[0:i])+[piv]+quickSort(-1, arr1[i+1:])
    #print("11 arr2:   {}".format(arr2))
    #arr1 = quickSort(pivin, arr1[0:i]).
    #arr2 = quickSort(-1,arr1[i+1:])
    #arr1 = quickSort(i,arr1[0:i+1]) + quicksort(-1, arr1[1+2:])
"""
    quickSort(-1,arr1[0:i])
    print(arr1)
"""

def heapSort(arr1):
    logging.debug('start heap sort')
    arr2 = []
    count = 0
    while(len(arr1)>0):
        time.sleep(.01)
        high = 0
        for i in range(len(arr1)):
            if(arr1[i]>=arr1[high]):
                high=i
        arr2.insert(0,arr1[high])
        arr1.pop(high)
        print(arr2)
        write_to_file(arr1+arr2)
    write_to_file(arr2)
    logging.debug('finished heap sort')
    return arr2

def radixSort(arr1):
    logging.debug('start radix sort')
    count = 0
    arr2 = [2, 3]
    while(sum(arr2)>0):
        arr2=[]
        for i in range(len(arr1)-1):
            arr2.append(get_digit(arr1[i+1],count))
        print(arr2)
        write_to_file(arr1+arr2)
    write_to_file(arr2)
    logging.debug('finished radix sort')
    return arr2

def countingRadixSort(n:int, arr1=[]):
    indexes = [0] * (11)
    for i in range(len(arr1)):
        indexes[get_digit(arr1[i], n)] +=1
        print("arr1[]   {} {} {}".format(arr1, i, get_digit(arr1[i], n)))
        print ("1 indexes:   {}".format(indexes))
        print("")
    for i in range(k):
        indexes[i+1]+=indexes[i]
        print ("2 indexes:   {}".format(indexes))
    newarr1 = [0] * len(arr1)
    print (newarr1)
    print(len(arr1))
    for i in range(len(arr1)):
        ind2 = arr1[i]
        ind3 = indexes[ind2]
        newarr1[ind3-1]=ind2
        indexes[ind2]-=1
        arr1[:i+1]=newarr1[:i+1]
        #time.sleep(.03)
    return arr1

def chckSort(arr1 = []):
    for i in range(len(arr1)-1):
        if(arr1[i]>arr1[i+1]):
            return False
    return True


def get_digit(number, n):
    return number // 10**n % 10


def userRun():
    logging.debug('userRun()')
    print("Welcome to sortingAlgorithms.py !")
    #plotWorld.main()
    num = int(input("enter number of objects in list:  "))
    high = int(input("enter highest number in list:   "))
    type = input("choose sorting algorithm:\n\n1. quickSort\n2. insertionSort\n3. selectionSort\n4. bubbleSort\n5. countingSort\n6. heapSort\n")
    write_to_file(createRandomArr(num,high))
    #plotWorld.main()
    now = time.time()
    if(type=="1"):
        logging.debug('start quick sort')
        quickSort(read_array_file(), 0,len(read_array_file()))
        logging.debug('finished quick sort')
    if(type=="2"):
        selectionSort(read_array_file())
    if(type=="3"):
        selectionSort(read_array_file())
    if(type=="4"):
        bubbleSort(read_array_file())
    if(type=="5"):
        countingSort(high, read_array_file())
    if(type=="6"):
        heapSort(read_array_file())
    print("\n\n\n\n\nfinished:   {}".format(read_array_file()))
    print("\nend of sort: \n")
    print("Succesful sorting:    {}".format(chckSort(read_array_file())))
    print("time to finish:   {}s".format(round(time.time()-now, 2)))
    logging.debug('array = {}\n\n'.format(read_array_file()))
    if(input("\n\nrun again? y/n\n")=="y"):
        logging.debug('run again - yes\n\n')
        print("\n\n")
        userRun()
    print("\n\n\n")

def main():
    logging.debug('main()')
    userRun()
    #write_to_file(createRandomArr(400,highest))
    #print(recTest(6))
    #recursionSample(read_array_file())
    #print(insertPivot(8, 5, read_array_file()))
    #quickSort(read_array_file(), 0,len(read_array_file()))
    #countingSort(100, read_array_file())
    #selectionSort(read_array_file())
    #insertionSort(read_array_file())

if (__name__ == "__main__"):
    logging.debug('__name__ == __main__')
    main()
