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

""" implemntion of f1 method"""
def f1method(frequentdataset, f1, datafram, supportcount, k = 2):

    itemsetarray = []

    for x in frequentdataset:
        for y in f1:
            if x[-1] < y[0] and x != y:
                value = union(x, y)
                if value not in itemsetarray:
                    itemsetarray.append(value)
    frequentdata = apr(itemsetarray, datafram, supportcount, frequentitemdict, unfrequentitemdict, k = k-1)
    if len(frequentdata) == 0:

        return 0
    else:
        frequentdataset = frequentdata
    f1method(frequentdataset, f1, datafram, supportcount, k = k-1)

""" implemention of fk-1 method """
def fk1_method(frequentdataset, datafram, supportcount, k = 2):


    print (frequentdataset)
    itemsetarray = []

    for x in range(len(frequentdataset)):

        for y in range(x+1, len(frequentdataset)):

            if frequentdataset[x][:abs(k-2)] == frequentdataset[y][:abs(k-2)]:

                value = union(frequentdataset[x], frequentdataset[y])
                itemsetarray.append(value)

    frequentdata = apr(itemsetarray, datafram, supportcount, frequentitemdict,unfrequentitemdict, k = k-1)

    if len(frequentdata) == 0:
        return 0
    else:
        frequentdataset = frequentdata

    fk1_method(frequentdataset, datafram, supportcount, k = k-1)



def main():

    inputfile = "C:/Users/Dell/Downloads/sample.csv"
    supportcount = 2
    fl1, datafram = readata(inputfile, supportcount, frequentitemdict, unfrequentitemdict)
    frequentdataset = apr(fl1, datafram, supportcount,frequentitemdict, unfrequentitemdict)
    fk1_method(frequentdataset, datafram, supportcount)
    f1method(frequentdataset, frequentdataset, datafram, supportcount)


if __name__ == '__main__':

    frequentitemdict = OrderedDict()
    unfrequentitemdict=OrderedDict()
    l = main()
    print("the pattern and its suupportcount......................................")
    print(frequentitemdict)
    print("---fk-1 * f1----")
    print(len(frequentitemdict))
