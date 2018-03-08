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

startTime = time.time()
searchTime=0;
printTime=0;
numTests=25
for i in range(0,numTests):
	t = time.time()
	data = inFile['/data/']
	#print("Open dataset: " +str(time.time()-t))
	rows = data.shape[0]
	cols = data.shape[1]
	chosenColumn = 0 #the starting column whose values we search over to match criteria
	rowList = []
	randomColumnList=[4,6,2000,10000,21325]
	#iterate through every row in chosenColumn, find all row numbers that have values > 6.4
	t=time.time()
	for x in range(0,rows):
		if(data[x,chosenColumn] > 6.4):
			rowList.append(x)
		
	searchTime+=(time.time()-t)

	t=time.time()
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
	printTime+=(time.time()-t)
avgSearch = searchTime/numTests
avgPrint = printTime/numTests
print("Average time to search column based on criteria: " + str(avgSearch))
print("Average time to write results to file: " + str(avgPrint))
