
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython import get_ipython
import sortingAlgorithms
import numpy as np
import mplcyberpunk

"""
def bubbleSort(arr1 = []):
    curr=0
    for i in range(len(arr1)-1):
        for j in range(len(arr1)-1):
            if(arr1[j]>arr1[j+1]):
                curr=arr1[j+1]
                arr1[j+1]=arr1[j]
                arr1[j]=curr
                sortingAlgorithms.write_to_file(arr1)
                sortingAlgorithms.printFile()
                print(str(i)+"\n\n")
    return arr1
"""
"""
arr1 = sortingAlgorithms.createRandomArr(10, 10)
#def plotGraph(arr1):
names = list(range(len(arr1)))
values = arr1
#plt.ion()
plt.bar(names, values)
plt.show()
time.sleep(10)
"""

def animate(i=0):
    with open('test112.txt', 'r') as graph_data:
        graph_data = graph_data.read()
        lines = graph_data.split('\n')
        ys = []
        for i in range(len(lines)-1):
            ys.append(int(lines[i]))
        ax1.clear()
        ax1.bar(range(len(ys)), ys)

"""
        for line in lines:
            print(lines, line)
            if(line!=""):
                ys.append(line)
            else: ys.append(0)
"""
plt.style.use("cyberpunk")
fig = plt.figure()
ax1 = plt.subplot(111)

def main():
    #plt.ylim(0, 10)
    #ax1 = plt.bar(111,0, color='b')
    #ax1.hist(arr1)
    #def main():
        #arr1 = sortingAlgorithms.read_array_file()
        #sortingAlgorithms.write_to_file(arr1)
    ani = animation.FuncAnimation(fig, animate, interval = 30)
    plt.show()


if (__name__=="__main__"):
    main()





