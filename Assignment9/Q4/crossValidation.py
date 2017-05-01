# coding: utf-8
import docclass
import re


input_1 = open('dataTitles.txt', 'r')
input_2 = open('dataClassification.txt', 'r')
input_3 = open('combinedsumtitle2.txt', 'r')
titles=[]
categories=[]
summaryTitles=[]

for entry in input_1:
   titles.append(entry)
for entry in input_2:
   categories.append(entry)
for entry in input_3:
   summaryTitles.append(entry)

count = 0
count2 = 0

#n is used as a constraint for the range of items cross validated, when n = 2
#items 11-20 will be cross validated
n = 10

filename = "CrossValidation" + str(n*10)+".txt"
outfile = open(filename,"wb")
classifier = docclass.fisherclassifier(docclass.getwords)

classifier.setdb('mln.db')

summariesToBeClassified = summaryTitles[((n-1)*10):(n*10)]
subList_1 = summaryTitles[:(n-1)*10]
subList_2 = summaryTitles[(n)*10:]
trainingdata_Entries = subList_1 + subList_2
categoriesToBeClassified = categories[((n-1)*10):(n*10)]
subList_3 = categories[:(n-1)*10]
subList_4 = categories[(n)*10:]
trainingdata_Categories= subList_3+subList_4

while count < 90:
    print count
    docclass.train(classifier, trainingdata_Entries[count], trainingdata_Categories[count])
    count += 1
count =0

while count2<10:
   print count2
   print summariesToBeClassified[(count2)]
   prediction = classifier.classify(summariesToBeClassified[(count2)])
   outfile.write(prediction)
   count2+=1