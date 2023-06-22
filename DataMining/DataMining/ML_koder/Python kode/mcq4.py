import math
import numpy as np

##TIL MCQ 4

#for S1
clusterm1 = np.array([1, 3, 5])
clusterm2 = np.array([7, 10, 11, 12])
centroidm1 = np.array([np.sum(clusterm1)/ len(clusterm1)])
centroidm2 = np.array([np.sum(clusterm2)/ len(clusterm2)])

#for S2
s21 = np.array([1, 3])
s22 = np.array([5, 7])
s23 = np.array([10, 11, 12])
sct21 = np.array([np.sum(s21)/ len(s21)])
sct22 = np.array([np.sum(s22)/ len(s22)])
sct23 = np.array([np.sum(s23)/ len(s23)])

#for S3
s31 = np.array([1, 3, 5, 7])
s32 = np.array([10, 11, 12])
sct31 = np.array([np.sum(s31)/ len(s31)])
sct32 = np.array([np.sum(s32)/ len(s32)])


def get_total_distanceMSC(a, b):
    for i in b:
        for j in a:
            p = b - a
    return np.array(np.sqrt((p*p)))

#for S1
s_am = get_total_distanceMSC(clusterm1, centroidm1)
s_bm = get_total_distanceMSC(clusterm1, centroidm2)
s_am2 = get_total_distanceMSC(clusterm2, centroidm2)
s_bm2 = get_total_distanceMSC(clusterm2, centroidm1)

##herefter beregner vi hver s(o) og summere dem sammen for at få the
#simplified silhoutte coefficient
testerm1 = sum([(b-a)/max(a,b) for a, b in zip(s_am, s_bm)])
testerm2 = sum([(b-a)/max(a,b) for a, b in zip(s_am2, s_bm2)])
print("The simplified silhoutte coefficient for S1 is:",
(testerm1+testerm2)/(len(clusterm1)+len(clusterm2)))

#for S2 #regn den ud manuelt svært, når der er tale om 3
s_am21 = get_total_distanceMSC(s21, sct21)
s_bm21 = get_total_distanceMSC(s21, sct22)
print(np.sum(s_bm21)/2) #pick this one in the code below its the
#lowest
s_bm212 = get_total_distanceMSC(s21, sct23)
print(np.sum(s_bm212)/2)

s_am22 = get_total_distanceMSC(s22, sct22)
s_bm22 = get_total_distanceMSC(s22, sct21)
print(np.sum(s_bm22)/2) #pick this one in the code below its the
#lowest
s_bm222 = get_total_distanceMSC(s22, sct23)
print(np.sum(s_bm222)/2)

s_am223 = get_total_distanceMSC(s23, sct23)
s_bm223 = get_total_distanceMSC(s23, sct21)
print(np.sum(s_bm223)/2)

s_bm2232 = get_total_distanceMSC(s23, sct22)
print(np.sum(s_bm2232)/2) #pick this one in the code below its the
#lowest

##herefter beregner vi hver s(o) og summere dem sammen for at få the
# simplified silhoutte coefficient
testerm12 = sum([(b-a)/max(a,b) for a, b in zip(s_am21, s_bm21)])
testerm22 = sum([(b-a)/max(a,b) for a, b in zip(s_am22, s_bm22)])
testerm233 = sum([(b-a)/max(a,b) for a, b in zip(s_am223, s_bm2232)])
print("The simplified silhoutte coefficient for S2 is:",
(testerm12+testerm22+testerm233)/(len(s21)+len(s22)+len(s23)))

#for S3
s_am3 = get_total_distanceMSC(s31, sct31)
s_bm3 = get_total_distanceMSC(s31, sct32)
s_am23 = get_total_distanceMSC(s32, sct32)
s_bm23 = get_total_distanceMSC(s32, sct31)

##herefter beregner vi hver s(o) og summere dem sammen for at få the
#simplified silhoutte coefficient
testerm13 = sum([(b-a)/max(a,b) for a, b in zip(s_am3, s_bm3)])
testerm23 = sum([(b-a)/max(a,b) for a, b in zip(s_am23, s_bm23)])
print("The simplified silhoutte coefficient for S3 is:",
(testerm13+testerm23)/(len(s31)+len(s32)))
