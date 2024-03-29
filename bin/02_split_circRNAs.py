#!/usr/bin/python3


import argparse

parser = argparse.ArgumentParser(description='give arguments to main primer_xc script')
parser.add_argument('-i', nargs=1, required=True, help='input circRNA bed file, 0-based')
args = parser.parse_args()
input_bed = args.i[0]

input_file = open(input_bed)
count_lines = 0
for line in input_file:
	count_lines +=1
input_file.close()

circ_nr = len(str(count_lines))
circ_nr = "circ{:0" + str(circ_nr) +"d}"

input_file = open(input_bed)

all_circ = [] # list with all circ to check if there are any doubles

ID = 0

# make a seperate input file for each circ
for circRNA in input_file:

	ID_str = circ_nr.format(ID)

	# strand needs to be separated to generate bed file
	chrom = circRNA.split()[0]
	start = str(circRNA.split()[1])
	end = str(circRNA.split()[2])
	strand = str(circRNA.split()[3])
	circ_str = chrom + '\t' + start + '\t' + end

	# add to bed file
	ind_circ_file = open(ID_str + ".bed", "w")
	ind_circ_file.write(circ_str + '\t' + ID_str + '\t' + strand + '\n')
	ind_circ_file.close()
	
	# add to list to check for duplicates
	all_circ.append(circRNA)
	
	ID += 1

def checkIfDuplicates(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

if checkIfDuplicates(all_circ):
	raise SystemExit('One or more circRNAs are present more than once in your input file. Please make sure each circRNA is unique.')

input_file.close()