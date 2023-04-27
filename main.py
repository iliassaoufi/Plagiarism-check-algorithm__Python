#!/usr/bin/env python
import json
import sys
import os
import traceback
import random
from plagiat import plagiat
from docx_to_txt import docx_to_txt
from pdf_to_txt import pdf_to_txt


def main():

    if len(sys.argv) < 3:
        print("Usage: python main.py <input-filename>.txt <output-filename>.txt")
        sys.exit()

    elif sys.argv[1].endswith(".docx"):
        text = docx_to_txt(sys.argv[1])

    elif sys.argv[1].endswith(".pdf"):
        text = pdf_to_txt(sys.argv[1])

    else:
        file = open(sys.argv[1], 'r', encoding='utf-8')
        if not file:
            print("Invalid Filename")
            sys.exit()
        text = file.read()

    # pdftext = sys.argv[2]
    # report_name = "C:\\wamp64\\www\\iliass\\Laravel-plagiat\\storage\\app\public\\report"
    # r = os.path.join(report_name, pdftext+".pdf")

    pdf_path = sys.argv[2] + ".pdf"
    [result, Percentage_plagiat] = plagiat(str(text), str(pdf_path))

    output = {
        "state": True,
        "message": "good result",
        "report": pdf_path.split("/")[-1],
        "plagiat": Percentage_plagiat,
        "result": result
    }

    with open(sys.argv[2]+".json", 'w', encoding='utf-8') as outfile:
        json.dump(output, outfile)


if __name__ == "__main__":
    try:
        main()
    except:
        try:
            output = {
                "state": False,
                "message": "Plagiarism-Checker error!",
                "log_error": traceback.format_exc(),
            }
            with open(sys.argv[2]+".json", 'w', encoding='utf-8') as outfile:
                json.dump(output, outfile)
        except:
            print(" -> Plagiarism-Checker output json error\n")

        finally:
            error = traceback.format_exc()
            print("\n -> Plagiarism-Checker error!:\n"+error)
