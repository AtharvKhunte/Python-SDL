from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Function to get user input for data
def get_user_data():
    date = input("Enter Date: ")
    name = input("Enter Name: ")
    subscription = input("Enter Subscription: ")
    price = input("Enter Price (Rs.): ")
    return [date, name, subscription, price]

# Get user input for individual transactions
num_transactions = int(input("Enter the number of transactions: "))
user_data = [["Date", "Name", "Subscription", "Price (Rs.)"]]
for _ in range(num_transactions):
    user_data.append(get_user_data())

# Get user input for Sub Total, Discount, and Total
sub_total = input("Enter Sub Total: ")
discount = input("Enter Discount: ")
total = input("Enter Total: ")

# Append Sub Total, Discount, and Total to the user data
user_data.append(["Sub Total", "", "", sub_total])
user_data.append(["Discount", "", "", discount])
user_data.append(["Total", "", "", total])

# creating a Base Document Template of page size A4
pdf = SimpleDocTemplate("receipt.pdf", pagesize=A4)

# standard stylesheet defined within reportlab itself
styles = getSampleStyleSheet()

# fetching the style of Top level heading (Heading1)
title_style = styles["Heading1"]

# 0: left, 1: center, 2: right
title_style.alignment = 1

# creating the paragraph with
# the heading text and passing the styles of it
title = Paragraph("GeeksforGeeks", title_style)

# creates a Table Style object and in it,
# defines the styles row wise
# the tuples which look like coordinates
# are nothing but rows and columns
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

# creates a table object and passes the style to it
table = Table(user_data, style=style)

# final step which builds the
# actual pdf putting together all the elements
pdf.build([title, table])