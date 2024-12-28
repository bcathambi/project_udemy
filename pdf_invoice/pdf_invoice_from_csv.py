import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:

	pdf = FPDF(orientation="P", unit="mm", format="A4")
	pdf.add_page()

	filename = Path(filepath).stem
	invoice_no, date = filename.split("-")

	pdf.set_font(family="Times", style="B", size=15)
	pdf.cell(w=50, h=8, txt=f"Invoice no. {invoice_no}", align="L", ln=1)
	pdf.cell(w=50, h=8, txt=f"Date. {date}", align="L", ln=1)

	df = pd.read_excel(filepath, sheet_name="Sheet 1")

	column = list(df.columns)
	column = [item.replace("_", " ").title() for item in column]
	print(column)
	pdf.set_font(family="Times", size=12, style="B")
	pdf.set_text_color(20, 20, 20)
	pdf.cell(w=25, h=9, txt=column[0], border=1)
	pdf.cell(w=55, h=9, txt=column[1], border=1)
	pdf.cell(w=40, h=9, txt=column[2], border=1)
	pdf.cell(w=35, h=9, txt=column[3], border=1)
	pdf.cell(w=25, h=9, txt=column[4], border=1, ln=1)

	for index, row in df.iterrows():
		pdf.set_font(family="Times", size=12)
		pdf.set_text_color(20, 20, 20)
		pdf.cell(w=25, h=9, txt=str(row["product_id"]), border=1)
		pdf.cell(w=55, h=9, txt=str(row["product_name"]), border=1)
		pdf.cell(w=40, h=9, txt=str(row["amount_purchased"]), border=1)
		pdf.cell(w=35, h=9, txt=str(row["price_per_unit"]), border=1)
		pdf.cell(w=25, h=9, txt=str(row["total_price"]), border=1, ln=1)

	pdf.output(f"PDFs/{filename}.pdf")


