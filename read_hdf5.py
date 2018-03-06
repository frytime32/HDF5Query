#test file to work on speeding up reading operations
import sys
import numpy as np
import pandas as pd
import h5py
import gzip
import codecs
import time


inFilePath = sys.argv[1]
outFilePath = sys.argv[2]
inFile = h5py.File(inFilePath, 'r')

data = inFile['/data/']
rows = data.shape[0]
cols = data.shape[1]
chosenColumn = 0 #the starting column whose values we search over to match criteria
rowList = []
randomColumnList=[4,6,20,7,8]
#iterate through every row in chosenColumn, find all row numbers that have values > 6.4
for x in range(0,rows):
	if(data[x,chosenColumn] > 6.4):
		rowList.append(x)
	


outFile = open(outFilePath, "w")
#write column headers
outText = "\t"
for col in randomColumnList:
	outText+=str(col)
	outText+="\t"
outText+="\n"
outFile.write(outText)
#write rows
outText=""
for row in rowList:
	outText+=(str(row)+"\t")
	for col in randomColumnList:
		outText+= (str(data[row, col])+"\t")
	outText+="\n"
outFile.write(outText)
outFile.close()
