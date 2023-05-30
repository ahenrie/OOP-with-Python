def make_receipt(data, out_file_name):
    from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import getSampleStyleSheet

    pdf = SimpleDocTemplate(out_file_name, pagesize=A4)
    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    title_style.alignment = 1
    title = Paragraph("Receipt", title_style)

    style = TableStyle(
        [
            ("BOX", (0, 0), (-1, -1), 1, colors.black),
            ("GRID", (0, 0), (4, 4), 1, colors.black),
            ("BACKGROUND", (0, 0), (3, 0), colors.gray),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
        ]
    )

    table = Table(data, style=style)

    pdf.build([title, table])
    print(f"Receipt generated and saved as {out_file_name}")


def main():
    data = [
        ["Date", "Name", "Subscription", "Price (Rs.)"],
        [
            "16/11/2020",
            "Full Stack Development with React & Node JS - Live",
            "Lifetime",
            "10,999.00/-",
        ],
        ["16/11/2020", "Geeks Classes: Live Session", "6 months", "9,999.00/-"],
        ["Sub Total", "", "", "20,9998.00/-"],
        ["Discount", "", "", "-3,000.00/-"],
        ["Total", "", "", "17,998.00/-"],
    ]

    make_receipt(data, "receipt.pdf")


if __name__ == "__main__":
    main()
