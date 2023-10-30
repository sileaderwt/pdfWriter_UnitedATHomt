from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


########################################################


firstName = "Kevin"
lastName = "Nguyen"
fullName = firstName + " " + lastName
address = "1268 Lansdowne Ave"
city = "Saint Louis"
county = "Saint Louis"
state = "MO"
zipCode = "63116-1269"
homePhone = "314-329-6099"
cellPhone = "314-329-6099"
signatureDate =  "09/12/2022"
dateOfBirth = "09/12/1999"
gender = "M"
SSN = "123-45-6789"
email = "helloworld@gmail.com"
aptNumber = "135"



########################################################
packet_1 = io.BytesIO()

can_1 = canvas.Canvas(packet_1, pagesize=letter)
can_1.setFillColorRGB(0, 0, 1)
can_1.setFont("Times-Roman", 14)
can_1.drawString(460, 80, signatureDate)
can_1.save()

########################################################


packet_1.seek(0)
new_pdf = PdfFileReader(packet_1)

existing_pdf = PdfFileReader(open("caregiverAtHome/caregiver_At_Home_Print_this.pdf", "rb"))
output = PdfFileWriter()

page_1 = existing_pdf.getPage(0)
page_1.mergePage(new_pdf.getPage(0))
output.addPage(page_1)

########################################################


packet_2 = io.BytesIO()

can_2 = canvas.Canvas(packet_2, pagesize=letter)
can_2.setFillColorRGB(0, 0, 1)
can_2.setFont("Times-Roman", 12)
can_2.drawString(116, 684, firstName)
can_2.drawString(350, 684, lastName)
can_2.drawString(100, 664, address)
can_2.setFont("Times-Roman", 10)
can_2.drawString(88, 644, city)
can_2.drawString(300, 644, state)
can_2.drawString(399, 644, zipCode)
can_2.drawString(290, 624, cellPhone)
can_2.drawString(120, 604, dateOfBirth)
can_2.drawString(300, 604, gender)
can_2.drawString(389, 604, SSN)
can_2.save()
packet_2.seek(0)
new_pdf_2 = PdfFileReader(packet_2)

page_2 = existing_pdf.getPage(1)
page_2.mergePage(new_pdf_2.getPage(0))
output.addPage(page_2)

########################################################


packet_3 = io.BytesIO()

can_3 = canvas.Canvas(packet_3, pagesize=letter)
can_3.setFillColorRGB(0, 0, 1)
can_3.setFont("Times-Roman", 12)
can_3.drawString(360, 95, signatureDate)

can_3.save()
packet_3.seek(0)
new_pdf_3 = PdfFileReader(packet_3)

page_3 = existing_pdf.getPage(2)
page_3.mergePage(new_pdf_3.getPage(0))
output.addPage(page_3)




########################################################




packet_4 = io.BytesIO()

can_4 = canvas.Canvas(packet_4, pagesize=letter)
can_4.setFillColorRGB(0, 0, 1)
can_4.setFont("Times-Roman", 12)
can_4.drawString(360, 73, signatureDate)

can_4.save()
packet_4.seek(0)
new_pdf_4 = PdfFileReader(packet_4)

page_4 = existing_pdf.getPage(3)
page_4.mergePage(new_pdf_4.getPage(0))
output.addPage(page_4)


########################################################


packet_5 = io.BytesIO()

can_5 = canvas.Canvas(packet_5, pagesize=letter)
can_5.setFillColorRGB(0, 0, 1)
can_5.setFont("Times-Roman", 12)
can_5.drawString(380, 53, signatureDate)

can_5.save()
packet_5.seek(0)
new_pdf_5 = PdfFileReader(packet_5)

page_5 = existing_pdf.getPage(4)
page_5.mergePage(new_pdf_5.getPage(0))
output.addPage(page_5)

########################################################
output.addPage(existing_pdf.getPage(5))

########################################################
packet_7 = io.BytesIO()

can_7 = canvas.Canvas(packet_7, pagesize=letter)
can_7.setFillColorRGB(0, 0, 1)
can_7.setFont("Times-Roman", 12)
can_7.drawString(28, 385, address)
can_7.drawString(28, 365, city)
can_7.drawString(315, 365, state)
can_7.drawString(400, 365, zipCode)
can_7.drawString(500, 365, county)
can_7.drawString(28, 340, cellPhone)
can_7.drawString(170, 340, email)
can_7.drawString(380, 40, signatureDate)

can_7.save()
packet_7.seek(0)
new_pdf_7 = PdfFileReader(packet_7)

page_7 = existing_pdf.getPage(6)
page_7.mergePage(new_pdf_7.getPage(0))
output.addPage(page_7)

########################################################
output.addPage(existing_pdf.getPage(7))

########################################################

packet_9 = io.BytesIO()

can_9 = canvas.Canvas(packet_9, pagesize=letter)
can_9.setFillColorRGB(0, 0, 1)
can_9.setFont("Times-Roman", 12)
can_9.drawString(38, 572, address)
can_9.drawString(40, 603, firstName)
can_9.drawString(210, 603, lastName)
can_9.drawString(310, 572, city)
can_9.drawString(450, 572, state)
can_9.drawString(493, 572, zipCode)
can_9.drawString(483, 540, cellPhone)
can_9.drawString(42, 540, dateOfBirth)
can_9.drawString(253, 540, email)

can_9.drawString(145, 540, SSN[0])
can_9.drawString(155, 540, SSN[1])
can_9.drawString(166, 540, SSN[2])
can_9.drawString(180, 540, SSN[4])
can_9.drawString(191, 540, SSN[5])
can_9.drawString(205, 540, SSN[7])
can_9.drawString(216, 540, SSN[8])
can_9.drawString(227, 540, SSN[9])
can_9.drawString(238, 540, SSN[10])

can_9.drawString(500, 230, signatureDate)

can_9.save()
packet_9.seek(0)
new_pdf_9 = PdfFileReader(packet_9)

page_9 = existing_pdf.getPage(8)
page_9.mergePage(new_pdf_9.getPage(0))
output.addPage(page_9)

########################################################
output.addPage(existing_pdf.getPage(9))

########################################################

packet_11 = io.BytesIO()

can_11 = canvas.Canvas(packet_11, pagesize=letter)
can_11.setFillColorRGB(0, 0, 1)
can_11.setFont("Times-Roman", 12)
can_11.drawString(60, 652, address)
can_11.drawString(60, 675, fullName)
can_11.drawString(303, 652, city)
can_11.drawString(436, 652, state)
can_11.drawString(500, 652, zipCode)



can_11.drawString(435, 675, SSN[0])
can_11.drawString(449, 675, SSN[1])
can_11.drawString(465, 675, SSN[2])
can_11.drawString(481, 675, SSN[4])
can_11.drawString(496, 675, SSN[5])
can_11.drawString(511, 675, SSN[7])
can_11.drawString(526, 675, SSN[8])
can_11.drawString(541, 675, SSN[9])
can_11.drawString(556, 675, SSN[10])


can_11.drawString(464, 336, signatureDate[0])
can_11.drawString(477, 336, signatureDate[1])
can_11.drawString(496, 336, signatureDate[3])
can_11.drawString(509, 336, signatureDate[4])
can_11.drawString(526, 336, signatureDate[6])
can_11.drawString(539, 336, signatureDate[7])
can_11.drawString(552, 336, signatureDate[8])
can_11.drawString(565, 336, signatureDate[9])



can_11.save()
packet_11.seek(0)
new_pdf_11 = PdfFileReader(packet_11)

page_11 = existing_pdf.getPage(10)
page_11.mergePage(new_pdf_11.getPage(0))
output.addPage(page_11)



########################################################
output.addPage(existing_pdf.getPage(11))

########################################################
packet_13 = io.BytesIO()

can_13 = canvas.Canvas(packet_13, pagesize=letter)
can_13.setFillColorRGB(0, 0, 1)
can_13.setFont("Times-Roman", 12)
can_13.drawString(96, 688, firstName)
can_13.drawString(280, 688, lastName)
can_13.drawString(481, 688, SSN)
can_13.drawString(96, 662, address)
tempCity = city + " " + state + " " + zipCode
can_13.drawString(96, 640, tempCity)
can_13.drawString(468,142, signatureDate)

can_13.save()
packet_13.seek(0)
new_pdf_13 = PdfFileReader(packet_13)

page_13 = existing_pdf.getPage(12)
page_13.mergePage(new_pdf_13.getPage(0))
output.addPage(page_13)

########################################################
outputStream = open("caregiverAtHome/destination.pdf", "wb")
output.write(outputStream)
outputStream.close()