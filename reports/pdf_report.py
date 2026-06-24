from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf():
    pdf = canvas.Canvas("employee_report.pdf", pagesize=letter)

    pdf.drawString(100, 750, "Employee Report")
    pdf.drawString(100, 730, "This PDF report is generated using ReportLab.")

    pdf.save()

if __name__ == "__main__":
    create_pdf()
