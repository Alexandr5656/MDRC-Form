from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


def projectHeader(can, name, team):
    can.drawString(125, 650, name)
    can.drawString(400, 650, team)


def vendor(can, name, contact, address, city, number, fax, email):
    can.drawString(217, 605, name)
    can.drawString(217, 592, contact)
    can.drawString(217, 575, address)
    can.drawString(217, 550, city)
    can.drawString(217, 535, number)
    can.drawString(217, 520, fax)
    can.drawString(217, 505, email)


def add_Item(can, amount, partNum, partName, unitPrice, lineNum):
    lineNum %= 5
    #42
    can.drawString(65, 460 - (lineNum * 29), str(int(amount)))
    can.drawString(92, 460 - (lineNum * 29), partNum)
    can.drawString(450, 460 - (lineNum * 29), "$" + str(unitPrice))
    can.drawString(500, 460 - (lineNum * 29), "$" + str(amount * unitPrice))

    if len(partName)>42:
        wordIndex = 0
        letterIndex = 0
        words = partName.split(" ")
        for word in words:
            letterIndex += len(word)
            if letterIndex >42:
                letterIndex-=len(word)
                break
            letterIndex+=1
        can.setFontSize(10)
        can.drawString(175, 460 - (lineNum * 28)+5, partName[0:letterIndex-1])
        can.drawString(175, 460 - (lineNum * 28)-10, partName[letterIndex:len(partName)])
    else:
        can.drawString(175, 460 - (lineNum * 28), partName)
    return amount * unitPrice


def createPdf(parts, team, company,count):
    # Create Page
    packet = io.BytesIO()
    can = canvas.Canvas(packet, pagesize=letter)

    projectHeader(can, "Alex", "BrainBot")

    # Vendor Input
    vendor(can, "amazon", "", "380 john st", "Rochester", "696-969-6969", "Fax Who?", "corgie@rit.edu")

    # Part Purchase
    subTotal = 0.0
    for i in range(len(parts)):
        subTotal += add_Item(can,parts[i].quantity, "", parts[i].part, parts[i].price, i)


    can.drawString(500, 323, "$" + str(subTotal))
    # Name Line
    can.drawString(300, 243, "Alex Burbano arb8590@rit.edu")
    can.drawString(530, 243, "9/20/21")
    can.save()
    # move to the beginning of the StringIO buffer
    packet.seek(0)

    # create a new PDF with Reportlab
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("Form.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("./finished/" + team +"-"+ company+"-"+str(count) + ".pdf", "wb")
    output.write(outputStream)
    outputStream.close()


def createPdfs(partDictionary):
    for team in partDictionary:
        for company in partDictionary[team]:
            for i in range(len(partDictionary[team][company])):
                createPdf(partDictionary[team][company][i], team, company,i)
