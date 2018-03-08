import sys
import numpy as np
import pandas as pd
import h5py
import gzip
import codecs
import time

class H5Converter:
    def numberRows(self, in_p):
        num_rows = -1 
        with gzip.open(in_p,'r') as in_f:
            for line in in_f:
                num_rows +=1
        return num_rows


    # Arguments:
    #	[1] InputPath (data.tsv.gz)
    #	[2] Transcript Split (where metadata ends)
    #	[3] New HDF5 file

    def convert(self, in_p, transcriptSplit, out_p):
        t = time.time()
        num_rows = self.numberRows(in_p)
        print("Find num_rows: "+str(time.time()-t))
        print("num_rows: " + str(num_rows))
        #number of rows we read into memory in one chunk before writing to the file
        chunkSize = 100 
        num_cols = 0
        t=time.time()
        with gzip.open(in_p,'r') as in_f:
            line = codecs.decode(in_f.readline()).split('\t')
            num_cols = len(line)
        print("Find num_cols: " + str(time.time()-t))
        print("num_cols: " + str(num_cols))
        t=time.time()
        #Initialize hdf5 file
        hdf = h5py.File(out_p,'a')        
        #Free up space for dataset
        data = hdf.create_dataset('data',(num_rows,num_cols - transcriptSplit),chunks=(1000,1000))
        print("Create file and dataset: "+ str(time.time()-t))
        
        t=time.time()
        #manually put data.tsv.gz into numpy array
        with gzip.open(in_p,'r') as in_f:
            tempNumPyArray = np.empty([chunkSize, num_cols-1])
            lineNum=0;
            iterator=0;
            counter=0;
            in_f.readline()
            for line in in_f:
                line=codecs.decode(line).split('\t')
                del line[0] #deletes row name
                #read each line into our temporary array 
                tempNumPyArray[iterator,:] = line
              
                #if our temp array is full, write it to the file
                if iterator == chunkSize-1:
                    data[counter:counter+chunkSize, :] = tempNumPyArray
                    counter+=chunkSize
                    iterator=0
                else:
                    iterator+=1
                
                lineNum+=1
                 
                #in case the file ends before we hit chunk size
                #this writes the remaining rows to the file
                if lineNum == num_rows:
                    data[counter:lineNum, :] = tempNumPyArray[0:lineNum-counter, :]
        print("Process and write to file: " + str(time.time()-t))  
        hdf.close()
if __name__ == "__main__":
    print("\033[91m[WARNING] \033[0m" + 
            "This program is to be used exclusively in type_converter.py")

