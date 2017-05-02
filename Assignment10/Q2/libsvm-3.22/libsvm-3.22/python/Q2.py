# -*- coding: utf-8 -*-
from svm import *
from svmutil import *
from svm import __all__ as svm_all
out=open("blogNames.txt",'wb')


#
TrainingLabel=[]

lines=[]
for line in open("blogdataQ2.txt"):
    lines.append(line)
#seperates the labels data and
blogNames=[]
vectors=[]
words=lines[0].strip().split('\t')[1:]
for line in lines[1:]:
    names=line.strip().split('\t')
    blogNames.append(names[0])
    vectors.append([float(x) for x in names[1:]])
blogNames=blogNames
# print blogNames
# print vectors
# print len(vectors)
# print len([[1,0,1], [-1,0,-1]])
for name in blogNames:
    out.write(name)
    out.write('\n')
# param = svm_parameter()
# svm_model.predict = lambda self, x: svm_predict([0], [x], self)[0][0]
#
# #prob = svm_problem([1,-1], vectors)
# #prob = svm_problem([1,-1], [[1,0,1], [-1,0,-1]])
# prob = svm_problem([1,2,3,4,5], [[1,0,1], [-1,0,-1],[1,0,1], [-1,0,-1],[-1,0,-1]])
# #prob = svm_problem([1,-1],[vectors,vectors])
# param = svm_parameter()
# param.kernel_type = LINEAR
# param.C = 10
# param.cross_validation=10
#
#
#
# m=svm_train(prob, param)
# #m.predict([1,0,0])
#
# #svm_save_model('test.model',m)
# #m = svm_load_model('test.model')
# #svmstruct= svm_train(vectors,TrainingLabel,'v 10')
#check to make sure they match up
# print blogNames[1]
# print vectors[1]
#svm_model.predict = lambda self, x: svm_predict([0], [x], self)[0][0]
# print blogNames
#prob = svm_problem([1,-1], [vectors[1], [-1,0,-1]])
vectorL=[vectors[0],	vectors[1],	vectors[2],	vectors[3],	vectors[4],	vectors[5],	vectors[6],	vectors[7],	vectors[8],	vectors[9],
	vectors[10],	vectors[11],	vectors[12],	vectors[13],	vectors[14],	vectors[15],	vectors[16],	vectors[17],	vectors[18],	vectors[19],
	vectors[20],	vectors[21],	vectors[22],	vectors[23],	vectors[24],	vectors[25],	vectors[26],	vectors[27],	vectors[28],	vectors[29],
	vectors[30],	vectors[31],	vectors[32],	vectors[33],	vectors[34],	vectors[35],	vectors[36],	vectors[37],	vectors[38],	vectors[39],
	vectors[40],	vectors[41],	vectors[42],	vectors[43],	vectors[44],	vectors[45],	vectors[46],	vectors[47],	vectors[48],	vectors[49],
	vectors[50],	vectors[51],	vectors[52],	vectors[53],	vectors[54],	vectors[55],	vectors[56],	vectors[57],	vectors[58],	vectors[59],
	vectors[60],	vectors[61],	vectors[62],	vectors[63],	vectors[64],	vectors[65],	vectors[65],	vectors[67],	vectors[68],	vectors[69],
	vectors[70],	vectors[71],	vectors[72],	vectors[73],	vectors[74],	vectors[75],	vectors[76],	vectors[77],	vectors[78],	vectors[79],
	vectors[80],	vectors[81],	vectors[82],	vectors[83],	vectors[84],	vectors[85],	vectors[86],	vectors[87],	vectors[88],	vectors[89],
	vectors[90],	vectors[91],	vectors[92],	vectors[93],	vectors[94],	vectors[95],	vectors[96],	vectors[97],	vectors[98],	vectors[99]]

authorl=[0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,0,1,0,0,1,1,1,0,0,0,1,0,0,0,1,1,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,]
reviewl=[0,0,1,0,0,0,1,0,0,1,0,1,0,1,1,0,1,1,0,0,1,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0,0,0,0,1,1,1,1,0,1,1,0,1,0,1,1,0,1,1,0,1,1,0,1,0]
other1=[0,0,0,1,1,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,]
news1=[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,1,0,1,0,0,0,0,0,0,0,0,0,0,1,]
rac1=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]
social1=[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# comparing author spotlights
#prob = svm_problem(authorl,vectorL)
#prob = svm_problem(reviewl,vectorL)
#prob=svm_problem(other1,vectorL)
#prob=svm_problem(news1,vectorL)
#prob=svm_problem(rac1,vectorL)
prob=svm_problem(social1,vectorL)


param = svm_parameter()
param.kernel_type = LINEAR
param.cross_validation=10

cmd = ['-t 2 -c ',  ' -g ','-v 10']
m=svm_train(prob, param,cmd)


#svm_save_model('test.model',m)
#m = svm_load_model('test.model')


# answers,inputs=[r.match for r in scaledset],[r.data for r in scaledset]
# param = svm_parameter()
# param.kernel_type = RBF
# prob = svm_problem(answers,inputs)
# m=svm_train(prob, param)
