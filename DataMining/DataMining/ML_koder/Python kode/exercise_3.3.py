# -*- coding: utf-8 -*-
"""
Created on Wed Jun 22 18:17:25 2022

@author: gamer
"""

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

dataset = [[1,2,3],
           [1,2,4],
           [1,2,5],
           [1,3,4],
           [1,3,5],
           [2,3,4],
           [2,3,5],
           [3,4,5]]

dataset2 = [["A","B","E"],
           ["B","D"],
           ["C","D","F"],
           ["A","B","D"],
           ["A","C","E"],
           ["B","C","E","F"],
           ["A","C","E"],
           ["A","B","C","E"],
           ["A","B","C","D","F"],
           ["B","C","D","E"]]

te = TransactionEncoder()
te2 = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
te_ary2 = te2.fit(dataset2).transform(dataset2)
df = pd.DataFrame(te_ary, columns=te.columns_)
df2 = pd.DataFrame(te_ary2, columns=te2.columns_)
print(df2)
print("--------------------")
frequent_itemsets = apriori(df2, min_support=0.2, use_colnames=True)
print(apriori(df2, min_support=2, use_colnames=True)) ##use colnames bruger faktiske værdier istedet for indexer
#min_support for at sætte minimum support
rules = association_rules(frequent_itemsets, metric="support", min_threshold=0.2)
print(rules)