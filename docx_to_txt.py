from docx import Document


def docx_to_txt(docxfile):
    try:
        document = Document(docxfile)
    except:
        print("Error opening")
        exit()

    paratextlist = document.paragraphs
    newparatextlist = []
    for paratext in paratextlist:
        newparatextlist.append(paratext.text)

    return '\n'.join(newparatextlist)


# d = docx_to_txt("gg.docx")
# f = open("demofile.txt", "a", encoding='utf-8')
# f.write(d)
# f.close()
