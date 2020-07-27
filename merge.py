## merge 2 PDF files using PyPDF2
##cd /Documents/Merge

#import PyPDF2 as ppdf
from PyPDF2 import PdfFileMerger
#from PyPDF2 import PdfFileWriter
import os

def merge():
    pdflocation = input('Enter the folder path to the PDFs, or press enter to use current directory "/Documents/Merge": ')
    print(pdflocation)
    if len(pdflocation)>0:
        os.chdir(pdflocation)
    source_dir = os.getcwd()

    outputname = input("Enter the desired output new file name: ")+'.pdf'

    while True:
        selectpdf = input("Enter the name of the first pdf, or press enter to merge all pdfs in current directory: ")
        if len(selectpdf) == 0:
            break
        elif selectpdf+'.pdf' not in os.listdir(source_dir):
            print("File does not exist. Try again, selecting from the files listed below.")
            print(os.listdir(source_dir))
            continue
        else:
            all_pdfs=[selectpdf+'.pdf']
            break

    merger = PdfFileMerger()

    if len(selectpdf) == 0:
        #print(os.listdir(source_dir))
        for item in os.listdir(source_dir):
            if item.endswith('pdf'):
                #print(item, type(item))
                merger.append(item)
        print("Merging ", os.listdir(source_dir), " as ", outputname)

    else:
        while len(selectpdf)>0:
            selectpdf = input("Enter the name of the next pdf (without file ending), or press enter to merge: ")
            if len(selectpdf)>0 and selectpdf+'.pdf' not in os.listdir(source_dir):
                print("File does not exist. Try again, selecting from the files listed below.")
                print(os.listdir(source_dir))
                continue
            if len(selectpdf)>0:
                all_pdfs.append(selectpdf+'.pdf')
        for item in all_pdfs:
            #print(item,type(item))
            merger.append(item)
        print("Merging ", all_pdfs, " as ", outputname)


    merger.write(outputname)
    merger.close()
    print("Complete.")
merge()
