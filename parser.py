#!/usr/bin/python3

import argparse
import os.path

parser = argparse.ArgumentParser(description='Unscramble a pdf file.')

def input_check(choices, fname):
    # checks if fname is an actual file
    if not is_file(fname):
        parser.error('the file "{}" does not exist'.format(fname))
    # checks if file has correct file extension

    fname = file_choices(choices, fname)

    return fname

def output_check(choices, fname):
    #checks if output has the correct file extension
    fname = file_choices(choices,fname)

    #checks if the output directory exists
    dirname = os.path.dirname(fname)
    is_valid_output(dirname)

    #checks if the file already exists. If it does it'll append a number so as not to overwrite
    counter = 1
    while is_file(fname):
        print("file already exists")
        first_half, second_half = os.path.splitext(fname)

        new_fname = '{0}({1}){2}'.format(first_half,counter,second_half)
        print(new_fname)
        fname = new_fname
        counter += 1

    # if not then append a number to the end of the filename before extension

    return fname

def file_choices(choices,fname):
    # choices and ext both need to be cast as lists for the set().issubset to function
    choices = list(choices)
    ext = [os.path.splitext(fname)[1][1:]]
    # checks the extension matches excactly the allowed choices
    if not set(ext).issubset(set(choices)):
        parser.error('filename "{0}" doesnt have the correcte extension. Allowed extensions are: {1}'.format(fname, choices))
    
    return fname

def is_file(fname):
    # veriifes that a file exists on the system
    exists = os.path.isfile(fname)
    return exists

def is_valid_output(outname):
    # check if outname exists
    exists = os.path.exists(outname)
    # verifies that a directory exists on the system
    
    if not exists:
        parser.error('output directory "{}" does not exist'.format(outname))
    return outname

# the pdf file to work on
parser.add_argument('pdf', type=lambda s:input_check((["pdf","PDF"]),s)) 
# where to store the new file
# this needs to default to the same location as the original file
# it should be able to check for a file with the same name and if so append a number so as not to overwrite
parser.add_argument('--output', '-o', type=lambda s:output_check((['pdf','PDF']),s))

args = parser.parse_args()

print("\n\nargs: ",args,"\n")
