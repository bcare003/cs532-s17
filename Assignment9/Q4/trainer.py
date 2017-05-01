# coding: utf-8
import docclass
import re
input = open('dataClassification.txt','r')
input_2 = open('dataCombined.txt','r')

count = 0
titles = []
categories = []
predictions = []
amountTrained = 0
summaryTitles = []
trainingCount50 = 50
trainingCount90 = 90
maxTrainingData = 100
remainingClassifications = 0


for entry in input:
  categories.append(entry)
for entry in input_2:
  summaryTitles.append(entry)

classifier = docclass.fisherclassifier(docclass.getwords)

#taken from lecture PowerPoint
classifier.setdb('mln.db')

for entry in summaryTitles:
    if count<trainingCount50:
     docclass.train(classifier, entry, categories[count])
     count += 1


w=maxTrainingData - count
intialpredictions = maxTrainingData - count

while count<maxTrainingData:
  print count
  prediction=classifier.classify(summaryTitles[(count)])
  predictions.append(prediction)
  count+=1

if len(predictions) > 49:
   output1=open('Classify50.txt','w')
if len(predictions) < 11:
   output2= open('Classify10.txt','w')

print(len(predictions))
for prediction in predictions:
   if len(predictions)>49:

       output1.write(prediction)
   if len(predictions)<11:

       output2.write(prediction)
