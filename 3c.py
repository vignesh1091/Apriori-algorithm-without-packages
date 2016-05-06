import numpy as np
import pandas as pand
import itertools
from collections import OrderedDict

"""
This script to read the input
file and returns them as a dataframe.
"""

def readata(inputfile, supportcount, frequentitemlist, unfrequentitemdict):


    datafram = pand.read_csv(inputfile)
    print(datafram)
    fl1 = []
    for x in datafram.columns:
        fl1.append(tuple((x,)))
        if sum(datafram[x]) >= supportcount:
            frequentitemlist[tuple((x,))] = sum(datafram[x])
        else:
            unfrequentitemdict[tuple((x,))] = sum(datafram[x])
    return fl1, datafram


""" implmentation of  Apriori   """

def apr(itemlist, datafram, supportcount, frequentitemdict, unfrequentitemdict, k = 3):

    frequentitemlist = []

    for ita in iter(itemlist):

        if k < 3:
            if sum(datafram[list(ita)].prod(axis=1)) >= supportcount:
                frequentitemlist.append(ita)
                frequentitemdict[ita] = sum(datafram[list(ita)].prod(axis=1))
            else:
                unfrequentitemdict[ita] = sum(datafram[list(ita)].prod(axis=1))
        else:
            if sum(datafram[list(ita)].prod(axis=1)) < supportcount:
                unfrequentitemdict[ita] = sum(datafram[list(ita)].prod(axis=1))
            else:
                for subset in itertools.combinations(ita, k-1):

                    if subset in frequentitemdict:

                        pass
                    else:
                        unfrequentitemdict[ita] = sum(datafram[list(ita)].prod(axis=1))
                        break
                else:
                    frequentitemlist.append(ita)
                    frequentitemdict[ita] = sum(datafram[list(ita)].prod(axis=1))

    return sorted(frequentitemlist)

""" this srcipt used merge the  item """
def union(*args):

    return tuple(sorted(set(args[0]).union(*args[1:])))


"""
script to find the maximal
frequent items in the dataset
"""

def maximalfrequentitemsets (frequentitemdict):

    for x in frequentitemdict:
        flag = True
        for y in frequentitemdict:
            if len(x) + 1 == len(y) and set(x).issubset(set(y)):
                flag = False
            elif len(x) + 2 == len(y):
                break
        if flag:
            print (x)


"""
  script to find closed frequency itemsets
  """
def closedfrequentitemset(frequentitemdict, alitem):

    for x in frequentitemdict:

        flag = True
        for y in all_item:

            if len(x) + 1 == len(y) and set(x).issubset(set(x)):

                if frequentitemdict[x] == all_item[y]:
                    flag = False
                    break
        if flag:
            print (y)

""" implemntion of f1 method"""
def f1method(frequentdataset, f1, datafram, supportcount, k = 2, candidatecount=0,frequentcount=0):

    frequentcount += len(frequentdataset)
    itemsetarray = []

    for x in frequentdataset:
        for y in f1:
            if x[-1] < y[0] and x != y:
                values = union(x, y)
                if values not in itemsetarray:
                    itemsetarray.append(values)
    candidatecount += len(itemsetarray)
    frequentdata = apr(itemsetarray, datafram, supportcount, frequentitemdict,unfrequentitemdict, k = k)
    if len(frequentdata) == 0:
        print (" the number candidate count", candidatecount)
        print ("the Frequent count", frequentcount)
        frequent.maximalfrequentitemset(frequentitemdict)
        frequent.closedfrequentitemset(frequentitemdict, unfrequentitemdict.update(frequentitemdict))
        return 0
    else:
        frequentdataset = frequentdata
    f1method(frequentdataset, f1, datafram, supportcount, k = k+1, candidatecount=candidate_count,frequentcount=frequentcount)


"""
   This function helps to perform
   combination of the freq itemset.
   """

def fk1method(frequentdataset, datafram, supportcount, k = 2, candidatecount = 0, frequentcount = 0):


    frequentcount += len(frequentdataset)
    itmarray = []
    for x in range(len(frequentdataset)):
        for y in range(x+1, len(frequentdataset)):
            if frequentdataset[x][:abs(k-2)] == frequentdataset[y][:abs(k-2)]:
                values = union(frequentdataset[x], frequentdataset[y])
                itemsetarray.append(values)
    candidatecount += len(itmarray)
    frequentdata = apriori(itmarray, datafram, supportcount, frequentitemdict,unfrequentitemdict, k = k)
    if len(frequentdata) == 0:
        print (" the no candidate count", candidatecount)
        print ("the Frequent count", frequentcount)
        print (frequentitemdict)
        alitemsdict = frequentitemdict.copy()
        alitemsdict.update(unfrequentitemdict)
        print (alitemsdict)
        frequent.closedfrequentitemset(frequentitemdict, alitemsdict)
        frequent.maximalfrequentitemsets(frequentitemdict)
        return 0
    else:
        frequentdataset = frequentdata

    fk1method(frequentdataset, datafram, supportcount, k = k+1, candidatecount = candidatecount,frequentcount = frequentcount)

def main():

    inputfile = "C:/Users/Dell/Downloads/car.csv"
    support = 0.
    fl1, datafram, supportcount = readata(inputfile,support,frequentitemdict, unfrequentitemdict)
    frequentdataset = apr(fl1, datafram, supportcount,frequentitemdict, unfrequentitemdict)

    """implment to generate frequent itemset """

    fk1method(frequentdataset, datafram, supportcount, candidatecount=len(fl1))
    print(fk1method)
    frequentitemdict.clear()
    unfrequentitemdict.clear()
    f1method(frequentdataset, frequentdataset, datafram, supportcount, candidatecount=len(fl1))
    print(f1method)


if __main__ == '__main__':

    frequentitemdict = OrderedDict()
    unfrequentitemdict = OrderedDict()
    l= main()
    print(frequentitemdict)
