from PyPDF2 import PdfFileReader, PdfFileMerger
from pathlib import Path 
import os

def main():
    current_directory = Path.cwd()
    data_folder = current_directory / Path('archivos')
    mergeFile = PdfFileMerger()

    file_list = os.listdir(data_folder)
    print(file_list)


    for file in file_list:
        if str(file)[-3:] == "pdf":
            filename = data_folder / Path(file)
            print(filename)
            mergeFile.append(PdfFileReader(str(filename), 'rb'))

    mergeFile.write("nuevo_archivo.pdf")

if __name__ == "__main__":
    main()