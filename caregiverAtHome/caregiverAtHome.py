from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


########################################################


# firstName = "Kevin"
# lastName = "Nguyen"
# fullName = firstName + " " + lastName
# address = "1268 Lansdowne Ave"
# city = "Saint Louis"
# county = "Saint Louis"
# state = "MO"
# zipCode = "63116-1269"
# homePhone = "314-329-6099"
# cellPhone = "314-329-6099"
# signatureDate =  "09/12/2022"
# dateOfBirth = "09/12/1999"
# gender = "M"
# SSN = "123-45-6789"
# email = "helloworld@gmail.com"
# aptNumber = "135"

firstName = input('First name (caregiver):\n')
lastName = input('Last name (caregiver):\n')
address = input('Address:\n')
aptNumber = input('Apt Number: \n')
city = input('City:\n')
county = input('County:\n')
state = input('State (MO):\n')
zipCode = input('Zip code (format 63123 or 63123-1234):\n')
homePhone = input('Home phone (format 314-329-6099):\n')
cellPhone = input('Cell phone (format 314-329-6099):\n')
signatureDate =  input('Signature date (format 09/12/2022)\n')
dateOfBirth = input('Birthday (format 09/12/2022)\n')
gender = input('Gender (format M or F)\n')
SSN = input('SSN (format 123-45-6789)\n')
EIN = input('EIN (format 88-1234568)\n')
stateID = input('state ID (format 34567899)\n')
DCN = input('DCN (format 02345678)\n')
UI = input('UI (format 09-99559-0-00)\n')
email = input('Email: \n')
driverLicense = input('Driver License: \n')
driverLicenseExpDate = input('Driver License Expired Date: \n')



if not SSN:
    SSN = "                   "
if not EIN:
    EIN = "                   "
if not stateID:
    stateID = "                   "
if not DCN:
    DCN = "                   "
if not UI:
    UI = "                   "
if not signatureDate:
    signatureDate = "                   "
if not dateOfBirth:
    dateOfBirth = "                   "
if not cellPhone:
    cellPhone = "                   "
if not homePhone:
    homePhone = "                   "

fullName = firstName + " " + lastName
if not aptNumber:
    addressApt = address
else:
    addressApt = address + " Apt " + aptNumber

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


output = PdfFileWriter()

page_1 = PdfFileReader(open("pdfFiles/1._employee_Job_App.pdf", "rb")).getPage(0)
page_1.mergePage(new_pdf.getPage(0))
output.addPage(page_1)

########################################################


packet_2 = io.BytesIO()

can_2 = canvas.Canvas(packet_2, pagesize=letter)
can_2.setFillColorRGB(0, 0, 1)
can_2.setFont("Times-Roman", 12)
can_2.drawString(116, 684, firstName)
can_2.drawString(350, 684, lastName)
can_2.drawString(100, 664, addressApt)
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

page_2 = PdfFileReader(open("pdfFiles/1._employee_Job_App.pdf", "rb")).getPage(1)
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

page_3 = PdfFileReader(open("pdfFiles/1._employee_Job_App.pdf", "rb")).getPage(2)
page_3.mergePage(new_pdf_3.getPage(0))
output.addPage(page_3)




########################################################




packet_4 = io.BytesIO()

can_4 = canvas.Canvas(packet_4, pagesize=letter)
can_4.setFillColorRGB(0, 0, 1)
can_4.setFont("Times-Roman", 12)
# can_4.drawString(360, 110, signatureDate)
can_4.drawString(360, 73, signatureDate)
can_4.drawString(360, 149, signatureDate)

can_4.save()
packet_4.seek(0)
new_pdf_4 = PdfFileReader(packet_4)

page_4 = PdfFileReader(open("pdfFiles/1._employee_Job_App.pdf", "rb")).getPage(3)
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

page_5 = PdfFileReader(open("pdfFiles/1._employee_Job_App.pdf", "rb")).getPage(4)
page_5.mergePage(new_pdf_5.getPage(0))
output.addPage(page_5)

########################################################
output.addPage(PdfFileReader(open("pdfFiles/1._employee_Job_App.pdf", "rb")).getPage(5))

########################################################
packet_7 = io.BytesIO()

can_7 = canvas.Canvas(packet_7, pagesize=letter)
can_7.setFillColorRGB(0, 0, 1)
can_7.setFont("Times-Roman", 12)

can_7.drawString(29, 488, SSN[0:3])
can_7.drawString(72, 488, SSN[4:6])
can_7.drawString(118, 488, SSN[7:])

can_7.drawString(37, 448, lastName)
can_7.drawString(218, 448, firstName)
can_7.drawString(405, 425, dateOfBirth)
if gender == 'M':
    can_7.drawString(519, 425, "X")
else:
    can_7.drawString(550, 425, "X")
can_7.drawString(28, 387, addressApt)
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

page_7 = PdfFileReader(open("pdfFiles/2._worker_Registration.pdf", "rb")).getPage(0)
page_7.mergePage(new_pdf_7.getPage(0))
output.addPage(page_7)

########################################################
output.addPage(PdfFileReader(open("pdfFiles/1._employee_Job_App.pdf", "rb")).getPage(5))

########################################################

packet_9 = io.BytesIO()

can_9 = canvas.Canvas(packet_9, pagesize=letter)
can_9.setFillColorRGB(0, 0, 1)
can_9.setFont("Times-Roman", 12)
can_9.drawString(40, 603, lastName)
can_9.drawString(210, 603, firstName)
can_9.drawString(38, 572, address)
can_9.drawString(254, 572, aptNumber)
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

page_9 = PdfFileReader(open("pdfFiles/3._employment_Eligibility_Verification_(I-9).pdf", "rb")).getPage(0)
page_9.mergePage(new_pdf_9.getPage(0))
output.addPage(page_9)

########################################################

output.addPage(PdfFileReader(open("pdfFiles/blank.pdf", "rb")).getPage(0))
# #######################################################



packet_90 = io.BytesIO()

can_90 = canvas.Canvas(packet_90, pagesize=letter)
can_90.setFillColorRGB(0, 0, 1)
can_90.setFont("Times-Roman", 12)


can_90.drawString(266, 618, "Driver License")
can_90.drawString(272, 598, "Missouri")
can_90.drawString(266, 575, driverLicense)
can_90.drawString(266, 551, driverLicenseExpDate)

can_90.drawString(456, 618, "Social Security")
can_90.drawString(460, 598, "USA")
can_90.drawString(440, 575, SSN)

can_90.save()
packet_90.seek(0)
new_pdf_90 = PdfFileReader(packet_90)

page_90 = PdfFileReader(open("pdfFiles/3._employment_Eligibility_Verification_(I-9).pdf", "rb")).getPage(1)
page_90.mergePage(new_pdf_90.getPage(0))
output.addPage(page_90)

# #######################################################
output.addPage(PdfFileReader(open("pdfFiles/blank.pdf", "rb")).getPage(0))
# #######################################################


packet_11 = io.BytesIO()

can_11 = canvas.Canvas(packet_11, pagesize=letter)
can_11.setFillColorRGB(0, 0, 1)
can_11.setFont("Times-Roman", 12)
can_11.drawString(60, 652, addressApt)
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

page_11 = PdfFileReader(open("pdfFiles/4._new_MO_W-4.pdf", "rb")).getPage(0)
page_11.mergePage(new_pdf_11.getPage(0))
output.addPage(page_11)



########################################################
output.addPage(PdfFileReader(open("pdfFiles/1._employee_Job_App.pdf", "rb")).getPage(5))

########################################################
packet_13 = io.BytesIO()

can_13 = canvas.Canvas(packet_13, pagesize=letter)
can_13.setFillColorRGB(0, 0, 1)
can_13.setFont("Times-Roman", 12)
can_13.drawString(96, 688, firstName)
can_13.drawString(280, 688, lastName)
can_13.drawString(481, 688, SSN)
can_13.drawString(96, 662, addressApt)
tempCity = city + " " + state + " " + zipCode
can_13.drawString(96, 640, tempCity)
can_13.drawString(468,142, signatureDate)

can_13.save()
packet_13.seek(0)
new_pdf_13 = PdfFileReader(packet_13)

page_13 = PdfFileReader(open("pdfFiles/5._new_W_4.pdf", "rb")).getPage(0)
page_13.mergePage(new_pdf_13.getPage(0))
output.addPage(page_13)

########################################################
output.addPage(PdfFileReader(open("pdfFiles/1._employee_Job_App.pdf", "rb")).getPage(5))

########################################################

packet_100 = io.BytesIO()

can_100 = canvas.Canvas(packet_100, pagesize=letter)
can_100.setFillColorRGB(0, 0, 1)
can_100.setFont("Times-Roman", 16)
can_100.drawString(103, 469, signatureDate)
can_100.setFont("Times-Roman", 24)
can_100.drawString(272, 664, fullName)

can_100.save()
packet_100.seek(0)
new_pdf_100 = PdfFileReader(packet_100)

page_100 = PdfFileReader(open("pdfFiles/Bank-Info.pdf", "rb")).getPage(0)
page_100.mergePage(new_pdf_100.getPage(0))
output.addPage(page_100)

########################################################
outputStream = open("caregiverAtHome.pdf", "wb")
output.write(outputStream)
outputStream.close()