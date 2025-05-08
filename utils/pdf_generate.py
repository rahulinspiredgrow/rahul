from fpdf import FPDF

def generate_pdf(hindi, english, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, "Hindi Text:\n" + hindi)
    pdf.add_page()
    pdf.multi_cell(0, 10, "English Translation:\n" + english)
    pdf.output(output_path)
