#Notes about performance speed with various tweaks: 25 trials of each set

Baseline control, using 1904 x 24367:
	Average time to search column based on given criteria: 0.2712676525115967
	Average time to write results to file: 0.1013493537902832

Chunking on same file, chunk size 100 x 1000, uncompressed
	Average time to search column based on given criteria: 0.24039077758789062
	Average time to write results to file: 0.13865923881530762

Chunking on same file, chunk size 100 x 10, uncompressed
	Average time to search column based on given criteria: 0.22863388061523438
	Average time to write results to file: 0.09726333618164062

Chunking on same file, chunk size 1 x 1, uncompressed
	Average time to search column based on given criteria: 1.108745813369751
	Average time to write results to file: 0.2993950843811035
	NOTE: Creating the HDF5 file with this small of chunk size took ~50x as long as usual

Chunking on same file, chunk size automatically selected by H5py using chunks=true, uncompressed
	Average time to search column based on given criteria: 0.2328193187713623
	Average time to write results to file: 0.10095024108886719

Chunking on same file, chunk size 1000 x 1, uncompressed
	Average time to search column based on criteria: 0.23516319274902345
	Average time to write results to file: 0.09558402061462402
	NOTE: Again, chunking took much longer than usual

Chunking on same file, chunk size 1000 x 1000, uncompressed
	Average time to search column based on criteria: 0.2429338836669922
	Average time to write results to file: 0.10015613555908204

NOTES SO FAR: Chunking in sizes where the row number is high and the column number is low seems to
work well, possibly due to the nature of selection in the program; every row must be accessed,
but relatively few columns need to be.
