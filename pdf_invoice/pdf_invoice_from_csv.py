import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
	df = pd.read_excel(filepath, sheet_name="Sheet 1")

	pdf = FPDF(orientation="P", unit="mm", format="A4")
	pdf.add_page()
	filename = Path(filepath).stem
	invoice_no = filename.split("-")[0]
	date = filename.split("-")[1]
	pdf.set_font(family="Times", style="B", size=16)
	pdf.cell(w=50, h=5, txt=f"Invoice no. {invoice_no}", align="L", ln=1)
	pdf.cell(w=50, h=10, txt=f"Date. {date}", align="L")
	pdf.output(f"PDFs/{filename}.pdf")


