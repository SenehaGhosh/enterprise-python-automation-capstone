from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(data, filename="crypto_report.pdf"):
    doc = SimpleDocTemplate(filename, pagesize=letter)
    elements = []
    styles = getSampleStyleSheet()

    title = Paragraph(
        "<b>Market Intelligence Report</b>", styles["Heading1"]
    )
    elements.append(title)
    elements.append(Spacer(1, 12))

    table_data = [
        ["Rank", "Coin", "Price (USD)", "24h Change (%)", "Market Cap"]
    ]
    for idx, item in enumerate(data, 1):
        table_data.append(
            [
                str(idx),
                item["name"],
                f"${item['current_price']:,}",
                f"{item['price_change_percentage_24h']:.2f}%",
                f"${item['market_cap']:,}",
            ]
        )

    table = Table(table_data)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1e293b")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
                ("BACKGROUND", (0, 1), (-1, -1), colors.HexColor("#f8fafc")),
                ("GRID", (0, 0), (-1, -1), 0.5, colors.lightgrey),
            ]
        )
    )

    elements.append(table)
    doc.build(elements)
    return filename