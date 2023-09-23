from fpdf import FPDF

class PDF(FPDF):
    def __init__(self, name):
        super().__init__()

        # Setting up page
        self.add_page()

        # Printing title
        self.set_font("helvetica", "B", 30)
        self.cell(0, 60, "CS50 Shirtificate", new_x="LMARGIN", new_y="NEXT", align="C")

        # Rendering image
        self.shirt_width = 180
        self.image("shirtificate.png", w=self.shirt_width)

        # Printing name on shirt
        self.set_font("helvetica", "B", size=23)
        self.set_text_color(255, 255, 255)
        self.text(self.shirt_width / 2 - 35, 140, name + "took CS50")

def main():
    name = input("Name: ")
    pdf = PDF(name)
    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
