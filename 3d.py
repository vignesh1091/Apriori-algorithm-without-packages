import numpy as np
import pandas as pand

from itertools import combinations
import itertools

dataframe=pand.readtable('inputfile')
dataframe = pand.readtaable('inputfile')
print(dataframe)

"""  script used to read file and coverted the dataframe to sparse  matrix  """
def dataset():

    converteddatasetlist = []
    for index in range(len(datafram)):
        originalrow = list(dataframe.ix[index])
        print (originalrow)
        count = 1
        dflist = []
        for rowalue in originalrow:
            if rowalue == 1:
                dflist.append(count)
            count = count + 1
        converteddatasetlist.append(dflist)
    print (converteddatasetlist)
    return(converteddatasetlist)


def crea1(dataset):
    "Create a list of candidate item sets of size one."
    a1 = []
    for transaction in dataset:
        for item in transaction:
            if not [item] in a1:
                a1.append([item])
    a1.sort()
    #frozenset because it will be a ket of a dictionary.
    return map(frozenset, a1)


def scand(dataset, candidat, minsupport):
    "Returns all candidates that meets a minimum support level"
    scnt = {}
    for lid in dataset:
        for ck in candidat:
            if can.issubset(lid):
                scnt.setdefault(ck, 0)
                scnt[ck] += 1

    numitems = float(len(dataset))
    relist = []
    supportdata = {}
    for key in scnt:
        support = scnt[key] / numitems
        if support >= minsupport:
            relist.insert(0, key)
        supportdata[key] = support
    return relist, supportdata



def apr(frequentsets, k):
    "Generate the joint transactions from candidate sets"
    reList = []
    lenk = len(frequentsets)
    for x in range(lenk):
        for y in range(x + 1, lenk):
            h1 = list(frequentsets[i])[:k - 2]
            h2 = list(frequentsets[j])[:k - 2]
            h1.sort()
            h2.sort()
            if h1 == h2:
                reList.append(frequentsets[i] | frequentsets[j])
    return reList


def apriori(dataset, minsupport=0.5):
    "Generate a list of candidate item sets"
    l1 = crea1(dataset)
    d= map(set, dataset)
    l1, supportdata = scanD(D, C1, minsupport)
    k = [l1]
    k = 2
    while (len(i[k - 2]) > 0):
        dk = apr(L[k - 2], k)
        ik, supK = scand(k, dk, minsupport)
        support_data.update(supK)
        L.append(ik)
        k += 1

    return d, supportdata

def generateRules(d, supportdata, minconfidence=0.7):
    """Create the association rules
    L: list of frequent item sets
    support_data: support data for those itemsets
    min_confidence: minimum confidence threshold
    """
    rules = []
    for x in range(1, len(d)):
        for freqSet in L[x]:
            H1 = [frozenset([item]) for item in frequentset]
            print ("frequentSet", frequentSet, 'H1', l1)
            if (i > 1):
                      
                rulesfromconseq(frequentSet, H1, supportdata, rules, minconfidence)
            else:
                calcconfidence(frequentSet, H1, supportdata, rules, minconfidence)
    return rules


def calcconfidence(frequentSet, H, supportdata, rules, minconfidence=0.7):
    "Evaluate the rule generated"
    pruned_H = []
    for conseq in H:
        conf = supportdata[frequentSet] / supportdata[frequentSet - conseq]
        if conf >= minconfidence:
            print (frequenSet - conseq, '--->', conseq, 'conf:', conf)
            rules.append((frequentSet - conseq, conseq, conf))
            pruned_H.append(conseq)
    return pruned_H


def rulesfromconseq(frequentSet, H, supportdata, rules, minconfidence=0.7):
    "Generate a set of candidate rules"
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hm1 = apr(H, m + 1)
        Hm1 = calcconfidence(frequentSet, Hm1,  supportdata, rules, minconfidence)
        if len(Hm1) > 1:
            rulesfromconseq(frequentSet, Hm1, supportdata, rules, minconfidence)

    return(frequentset,m)






