# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:29:59 2022

@author: gamer
"""

def MaxAssociationRules(uniqueItems):
    return (3**uniqueItems)-(2**(uniqueItems+1))+1

def TransactionInfo():
    transactions = dict([
        (0, ["Milk", "Beer", "Diapers"]),
        (1, ["Bread", "Butter", "Milk"]),
        (2, ["Milk", "Diapers", "Cookies"]),
        (3, ["Bread", "Butter", "Cookies"]),
        (4, ["Beer", "Cookies", "Diapers"]),
        (5, ["Milk", "Diapers", "Bread", "Butter"]),
        (6, ["Bread", "Butter", "Diapers"]),
        (7, ["Beer", "Diapers"]),
        (8, ["Milk", "Diapers", "Bread", "Butter"]),
        (9, ["Beer, Cookies"]),
    ])

    #CalculateSupport("Bread", "Butter", transactions)
    CalculateConfidence("Milk", "Diapers", transactions)
    MaxItemFrequency(transactions)

def CalculateConfidence(setX, setY, dictionary):
    support = CalculateSupport2(setX, setY, dictionary)
    conf = support/CalculateSupport1(setX, dictionary)
    print("The confidence of", setX,"->", setY, "is:", conf)
    return conf


def CalculateSupport1(set1, dictionary):
    count = 0
    appearances = 0
    for i in range(len(dictionary)):
        count = count+1
        if set1 in dictionary[i]:
            appearances = appearances+1
    print(set1, "appears: ", appearances, "times.")
    support = appearances/count
    print("The support is", support)
    return support


def CalculateSupport2(set1, set2, dictionary):
    count = 0
    appearances = 0
    for i in range(len(dictionary)):
        count = count+1
        if set1 in dictionary[i] and set2 in dictionary[i]:
            appearances = appearances+1
    print(set1, set2, "appears: ", appearances, "times.")
    support = appearances/count
    print("The support is", support)
    return support

def MaxItemFrequency(dictionary):
    supp = 0
    biggest = 0
    saveIndex = 0
    appearances = 0
    for i in range(len(dictionary)):
        count=0
        for j in range(len(dictionary[i])):
            count = count+1
            if count > biggest:
                print(count, ">", biggest)
                biggest = count
                print(dictionary[i])
                saveIndex = i
    print("Maximum size itemset:", (dictionary[saveIndex]), "with supp(", dictionary[saveIndex],") = ")

if __name__ == "__main__":
    uniqueItems = 6
    print("MaxAssociationRules from this data set given unique items =", uniqueItems, ":")
    print(MaxAssociationRules(uniqueItems))
    TransactionInfo()