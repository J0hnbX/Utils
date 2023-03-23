import pefile
from sys import argv
from os import path

if len(argv) != 2:
	print("You need to provide name of exe to find its imports with absolute path")
	exit(1)

if path.isfile(argv[1]):
	pe=pefile.PE(argv[1])
else:
	print("File does not exist")
	exit(1)
count=0

while count < len(pe.DIRECTORY_ENTRY_IMPORT):
	print("_______________________________________")
	print(pe.DIRECTORY_ENTRY_IMPORT[count].dll)
	innercount = len (pe.DIRECTORY_ENTRY_IMPORT[count].imports)
	iter=0
	while iter < innercount:
		print(pe.DIRECTORY_ENTRY_IMPORT[count].imports[iter].name)
		iter+=1	
	count+=1
