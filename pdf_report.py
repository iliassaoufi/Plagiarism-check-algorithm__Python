from fpdf import FPDF


class PDF(FPDF):
    def __init__(self, v1, v2, v3):
        super().__init__(v1, v2, v3)
        self.__used_w = 0

    def get_used_w(self):
        return self.__used_w

    def set_used_w(self, a):
        self.__used_w = a

    def header(self):
        title = "plagiarism checker report"
        self.set_font('helvetica', 'B', 15)
        title_w = self.get_string_width(title) + 20
        doc_w = self.w
        self.set_x((doc_w - title_w) / 2)
        self.set_draw_color(0, 80, 180)
        self.set_fill_color(255, 255, 255)
        self.set_text_color(50, 50, 50)
        self.set_line_width(1)
        self.cell(title_w, 20, title, border=1, ln=1, align='C', fill=1)
        self.ln(20)

    def set_content(self, text, color="black"):
        text = text.encode('latin-1', 'ignore').decode('latin-1')

        list_word = text.split()
        for word in list_word:
            self.set_sentence(word, color)

        # n = 3
        # nbr_split = int(len(list_word)/n)+1

        # for k in range(nbr_split):
        #     sentence = " ".join(list_word[k*n:(k+1)*n])
        #     self.set_sentence(sentence, color)

    def set_sentence(self, text, color):

        text_w = self.get_string_width(text) + 1
        used_w = self.get_used_w()
        doc_w = self.w
        condition = doc_w-(used_w+2*text_w)

        if(condition < 0):
            self.ln()
            self.set_used_w(0)
        else:
            self.set_used_w(used_w+text_w+2)

        if color == "red":
            self.set_text_color(176, 58, 46)
        elif color == "green":
            self.set_text_color(29, 131, 72)
        else:
            self.set_text_color(40, 40, 40)

        self.set_font('Arial', 'B', 13)
        self.cell(text_w, 10, text, 0, 0, "C")


# pdf = PDF('P', 'mm', 'A4')
# pdf.set_auto_page_break(auto=True, margin=15)
# pdf.add_page()

# pdf.set_content('iliasssss', "green")
# pdf.set_content('iliasssss')
# pdf.set_content('To print the page number, a null value is', "red")

# pdf.output('pdf_1.pdf')
