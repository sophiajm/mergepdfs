## merge 2 PDF files using PyPDF2

## IMPORT NECESSARY PACKAGES ##
from PyPDF2 import PdfFileMerger
import os

## GET LOCATION FROM USER ##
pdflocation = input('Enter the full folder path to the PDFs, or press enter to use current directory at {}": '.format(os.getcwd()))

## change directory if requested
if len(pdflocation)>0:
    os.chdir(pdflocation)
## get current directory
source_dir = os.getcwd()
print("Using directory named ", source_dir)

## GET OUTPUT FILE NAME FROM USER ##
outputname = input("Enter the desired output new file name: ")+'.pdf'
## if file already exists
if outputname in os.listdir(source_dir):
    newname = input("A file named {} already exists in this directory. Enter a new file name, or press enter to overwrite existing file: ".format(outputname))
    if len(newname)>0:
        outputname = newname+'.pdf'

## GET FIRST FILE ##
while True:
    selectpdf = input("Enter the name of the first pdf, or press enter to merge all pdfs in current directory: ")
    if len(selectpdf) == 0:
        break
    ## check for incorrect file names (could also wrap entire code in try/except)
    elif selectpdf+'.pdf' not in os.listdir(source_dir):
        print("File does not exist. Try again, selecting from the files listed below.")
        print(os.listdir(source_dir))
        continue
    ## create list of filenames to merge
    else:
        all_pdfs=[selectpdf+'.pdf']
        break

## CREATE MERGER AND APPEND FILES ##
merger = PdfFileMerger()

## merge all files in directory
if len(selectpdf) == 0:
    for item in os.listdir(source_dir):
        if item.endswith('pdf'):
            merger.append(item)
    print("Merging ", [item for item in os.listdir(source_dir) if item.endswith('pdf')], " as ", outputname)

## merge all files requested by user
else:
    while len(selectpdf)>0:
        selectpdf = input("Enter the name of the next pdf (without file ending), or press enter to merge: ")
        ## check for incorrect file names
        if len(selectpdf)>0 and selectpdf+'.pdf' not in os.listdir(source_dir):
            print("File does not exist. Try again, selecting from the files listed below.")
            print(os.listdir(source_dir))
            continue
        if len(selectpdf)>0:
            all_pdfs.append(selectpdf+'.pdf')
    for item in all_pdfs:
        merger.append(item)
    print("Merging ", all_pdfs, " as ", outputname)

## WRITE OUTPUT FILE AND CLOSE MERGER ##
merger.write(outputname)
merger.close()
print("Complete.")

