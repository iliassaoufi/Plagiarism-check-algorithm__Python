import PyPDF2


def pdf_to_txt(pdfFile):

    try:
        pdfFileObj = open(pdfFile, 'rb')
    except:
        print("Error opening ")
        exit()

    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    numPages = pdfReader.numPages
    text = ""

    for i in range(numPages):
        pageText = pdfReader.getPage(i).extractText().replace("\n", "")
        # .replace("  ", "\n")
        text += pageText

    pdfFileObj.close()

    return text


# f = open("demofile.txt", "a", encoding='utf-8')
# pdf = pdf_to_txt("test/Mtg_Indus.pdf")
# f.write(pdf)
# f.close()
