from PyPDF2 import PdfFileWriter, PdfFileReader
import io
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter


########################################################

firstName = input('First name (client):\n')
lastName = input('Last name (client):\n')
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

fullAddress  = addressApt + " , " + city + " , " + state + " " + zipCode


########################################################
packet_1 = io.BytesIO()

can_1 = canvas.Canvas(packet_1, pagesize=letter)
can_1.setFillColorRGB(0, 0, 1)
can_1.setFont("Times-Roman", 14)
can_1.drawString(123, 88, fullName)
can_1.drawString(382, 88, signatureDate)
can_1.save()

########################################################


packet_1.seek(0)
new_pdf = PdfFileReader(packet_1)


output = PdfFileWriter()

page_1 = PdfFileReader(open("pdfFiles/01._Consumer_Rights_And_Responsibility_Policy.pdf", "rb")).getPage(0)
page_1.mergePage(new_pdf.getPage(0))
output.addPage(page_1)

# ########################################################
output.addPage(PdfFileReader(open("pdfFiles/01._Consumer_Rights_And_Responsibility_Policy.pdf", "rb")).getPage(1))
#




# ########################################################
#
# ########################################################
#
#
packet_2 = io.BytesIO()

can_2 = canvas.Canvas(packet_2, pagesize=letter)
can_2.setFillColorRGB(0, 0, 1)
can_2.setFont("Times-Roman", 16)

can_2.drawString(105, 665, stateID[0])
can_2.drawString(126, 665, stateID[1])
can_2.drawString(148, 665, stateID[2])
can_2.drawString(170, 665, stateID[3])
can_2.drawString(191, 665, stateID[4])
can_2.drawString(215, 665, stateID[5])
can_2.drawString(236, 665, stateID[6])
can_2.drawString(257, 665, stateID[7])

can_2.drawString(388, 665, EIN[0])
can_2.drawString(408, 665, EIN[1])
can_2.drawString(429, 665, EIN[3])
can_2.drawString(452, 665, EIN[4])
can_2.drawString(475, 665, EIN[5])
can_2.drawString(496, 665, EIN[6])
can_2.drawString(519, 665, EIN[7])
can_2.drawString(539, 665, EIN[8])
can_2.drawString(560, 665, EIN[9])

can_2.drawString(99, 629, SSN[0])
can_2.drawString(120, 629, SSN[1])
can_2.drawString(144, 629, SSN[2])
can_2.drawString(171, 629, SSN[4])
can_2.drawString(193, 629, SSN[5])
can_2.drawString(220, 629, SSN[7])
can_2.drawString(243, 629, SSN[8])
can_2.drawString(262, 629, SSN[9])
can_2.drawString(283, 629, SSN[10])


can_2.setFont("Times-Roman", 12)
can_2.drawString(43, 575, fullName)

can_2.drawString(43, 523, addressApt)
can_2.drawString(43, 499, city)
can_2.drawString(241, 499, state)
can_2.drawString(297, 499, zipCode)

can_2.drawString(400, 499, cellPhone[0])
can_2.drawString(414, 499, cellPhone[1])
can_2.drawString(427, 499, cellPhone[2])
can_2.drawString(445, 499, cellPhone[4])
can_2.drawString(457, 499, cellPhone[5])
can_2.drawString(473, 499, cellPhone[6])
can_2.drawString(492, 499, cellPhone[8])
can_2.drawString(504, 499, cellPhone[9])
can_2.drawString(520, 499, cellPhone[10])
can_2.drawString(533, 499, cellPhone[11])

can_2.drawString(43, 472, email)

can_2.save()
packet_2.seek(0)
new_pdf_2 = PdfFileReader(packet_2)

page_2 = PdfFileReader(open("pdfFiles/02._MO_Power_of_Attorney_2827.pdf", "rb")).getPage(0)
page_2.mergePage(new_pdf_2.getPage(0))
output.addPage(page_2)
#


# ########################################################
#
#
packet_3 = io.BytesIO()

can_3 = canvas.Canvas(packet_3, pagesize=letter)
can_3.setFillColorRGB(0, 0, 1)
can_3.setFont("Times-Roman", 12)
can_3.drawString(305, 708, "Owner")
can_3.drawString(62, 708, fullName)

can_3.drawString(298, 682, signatureDate[0])
can_3.drawString(311, 682, signatureDate[1])
can_3.drawString(329, 682, signatureDate[3])
can_3.drawString(340, 682, signatureDate[4])
can_3.drawString(358, 682, signatureDate[6])
can_3.drawString(370, 682, signatureDate[7])
can_3.drawString(383, 682, signatureDate[8])
can_3.drawString(396, 682, signatureDate[9])

can_3.drawString(415, 682, cellPhone[0])
can_3.drawString(432, 682, cellPhone[1])
can_3.drawString(447, 682, cellPhone[2])
can_3.drawString(465, 682, cellPhone[4])
can_3.drawString(480, 682, cellPhone[5])
can_3.drawString(494, 682, cellPhone[6])
can_3.drawString(513, 682, cellPhone[8])
can_3.drawString(528, 682, cellPhone[9])
can_3.drawString(542, 682, cellPhone[10])
can_3.drawString(558, 682, cellPhone[11])

can_3.save()
packet_3.seek(0)
new_pdf_3 = PdfFileReader(packet_3)

page_3 = PdfFileReader(open("pdfFiles/02._MO_Power_of_Attorney_2827.pdf", "rb")).getPage(1)
page_3.mergePage(new_pdf_3.getPage(0))
output.addPage(page_3)
#
#
#
#
# ########################################################
#
#
#
#
packet_4 = io.BytesIO()

can_4 = canvas.Canvas(packet_4, pagesize=letter)
can_4.setFillColorRGB(0, 0, 1)
can_4.setFont("Times-Roman", 12)

can_4.drawString(334, 519, EIN[0])
can_4.drawString(361, 519, EIN[1])
can_4.drawString(401, 519, EIN[3])
can_4.drawString(427, 519, EIN[4])
can_4.drawString(453, 519, EIN[5])
can_4.drawString(475, 519, EIN[6])
can_4.drawString(504, 519, EIN[7])
can_4.drawString(529, 519, EIN[8])
can_4.drawString(552, 519, EIN[9])

can_4.drawString(266, 495, fullName)

can_4.drawString(265, 446, address)
can_4.drawString(499, 446, aptNumber)
can_4.drawString(266, 416, city)
can_4.drawString(461, 416, state)
can_4.drawString(500, 416, zipCode)

can_4.drawString(429, 113, fullName)
can_4.drawString(429, 65, cellPhone)

can_4.drawString(135, 65, signatureDate[0:2])
can_4.drawString(162, 65, signatureDate[3:5])
can_4.drawString(188, 65, signatureDate[6:])

can_4.save()
packet_4.seek(0)
new_pdf_4 = PdfFileReader(packet_4)

page_4 = PdfFileReader(open("pdfFiles/03.Fed_Power_of_Attorney_2678.pdf", "rb")).getPage(1)
page_4.mergePage(new_pdf_4.getPage(0))
output.addPage(page_4)
# ########################################################
output.addPage(PdfFileReader(open("pdfFiles/03.Fed_Power_of_Attorney_2678.pdf", "rb")).getPage(2))
#
# ########################################################
#
# ########################################################
#
#
packet_5 = io.BytesIO()

can_5 = canvas.Canvas(packet_5, pagesize=letter)
can_5.setFillColorRGB(0, 0, 1)
can_5.setFont("Times-Roman", 12)

can_5.drawString(47, 657, fullName)
can_5.drawString(47, 631, addressApt)
can_5.drawString(295, 631, city)
can_5.drawString(440, 631, state)
can_5.drawString(497, 631, zipCode)

can_5.drawString(47, 598, cellPhone)
can_5.drawString(224, 598, EIN)
can_5.drawString(403, 598, UI)

can_5.drawString(47, 331, fullName)
can_5.drawString(317, 331, "Owner")
can_5.drawString(446, 305, signatureDate)

can_5.save()
packet_5.seek(0)
new_pdf_5 = PdfFileReader(packet_5)

page_5 = PdfFileReader(open("pdfFiles/04._DES_Power_of_Attorney.pdf", "rb")).getPage(0)
page_5.mergePage(new_pdf_5.getPage(0))
output.addPage(page_5)
#
# ########################################################
output.addPage(PdfFileReader(open("pdfFiles/04._DES_Power_of_Attorney.pdf", "rb")).getPage(1))
#
# ########################################################

output.addPage(PdfFileReader(open("pdfFiles/05._Training_and_Orientation.pdf", "rb")).getPage(0))
# ########################################################


packet_7 = io.BytesIO()

can_7 = canvas.Canvas(packet_7, pagesize=letter)
can_7.setFillColorRGB(0, 0, 1)
can_7.setFont("Times-Roman", 12)
can_7.drawString(463, 123, signatureDate)
can_7.drawString(463, 97, signatureDate)

can_7.save()
packet_7.seek(0)
new_pdf_7 = PdfFileReader(packet_7)

page_7 = PdfFileReader(open("pdfFiles/05._Training_and_Orientation.pdf", "rb")).getPage(1)
page_7.mergePage(new_pdf_7.getPage(0))
output.addPage(page_7)
#
# ########################################################

# ########################################################

#
packet_8 = io.BytesIO()

can_8 = canvas.Canvas(packet_8, pagesize=letter)
can_8.setFillColorRGB(0, 0, 1)
can_8.setFont("Times-Roman", 12)
can_8.drawString(133, 706, fullName)
can_8.drawString(36, 549, fullName)
can_8.drawString(313, 549, dateOfBirth)
can_8.drawString(453, 549, SSN)

can_8.save()
packet_8.seek(0)
new_pdf_8 = PdfFileReader(packet_8)

page_8 = PdfFileReader(open("pdfFiles/06._Auth._For_disclosure_form.pdf", "rb")).getPage(0)
page_8.mergePage(new_pdf_8.getPage(0))
output.addPage(page_8)
#
# ########################################################
# ########################################################


packet_9 = io.BytesIO()

can_9 = canvas.Canvas(packet_9, pagesize=letter)
can_9.setFillColorRGB(0, 0, 1)
can_9.setFont("Times-Roman", 12)
can_9.drawString(457, 311, signatureDate)


can_9.save()
packet_9.seek(0)
new_pdf_9 = PdfFileReader(packet_9)

page_9 = PdfFileReader(open("pdfFiles/06._Auth._For_disclosure_form.pdf", "rb")).getPage(1)
page_9.mergePage(new_pdf_9.getPage(0))
output.addPage(page_9)
#
# ########################################################


packet_10 = io.BytesIO()

can_10 = canvas.Canvas(packet_10, pagesize=letter)
can_10.setFillColorRGB(0, 0, 1)
can_10.setFont("Times-Roman", 12)
can_10.drawString(62, 685, fullName)
can_10.drawString(62, 557, fullName)
can_10.drawString(62, 648, dateOfBirth)
can_10.drawString(269, 648, SSN)
can_10.drawString(446, 648, DCN)

can_10.drawString(383, 516, signatureDate)
can_10.drawString(53, 407, "X")

can_10.save()
packet_10.seek(0)
new_pdf_10 = PdfFileReader(packet_10)

page_10 = PdfFileReader(open("pdfFiles/07._Privacy_Policies_Acknowledgement.pdf", "rb")).getPage(0)
page_10.mergePage(new_pdf_10.getPage(0))
output.addPage(page_10)


# ########################################################

output.addPage(PdfFileReader(open("pdfFiles/07._Privacy_Policies_Acknowledgement.pdf", "rb")).getPage(1))
# ########################################################

# ########################################################


packet_11 = io.BytesIO()

can_11 = canvas.Canvas(packet_11, pagesize=letter)
can_11.setFillColorRGB(0, 0, 1)
can_11.setFont("Times-Roman", 12)
can_11.drawString(33, 655, fullName)
can_11.drawString(33, 605, addressApt)
can_11.drawString(33, 580, city + ", " + state + ", " + zipCode )
can_11.drawString(21, 470, "X")
can_11.drawString(119, 471, SSN[0:3])
can_11.drawString(149, 471, SSN[4:6])
can_11.drawString(180, 471, SSN[7:11])
can_11.drawString(130, 27, fullName)
can_11.drawString(409, 27, cellPhone[0:3])
can_11.drawString(442, 27, cellPhone[4:])
can_11.drawString(325, 5, signatureDate)

can_11.save()
packet_11.seek(0)
new_pdf_11 = PdfFileReader(packet_11)

page_11 = PdfFileReader(open("pdfFiles/08._Form_SS-4.pdf", "rb")).getPage(0)
page_11.mergePage(new_pdf_11.getPage(0))
output.addPage(page_11)


# ########################################################


output.addPage(PdfFileReader(open("pdfFiles/08._Form_SS-4.pdf", "rb")).getPage(1))

# ########################################################


packet_12 = io.BytesIO()

can_12 = canvas.Canvas(packet_12, pagesize=letter)
can_12.setFillColorRGB(0, 0, 1)
can_12.setFont("Times-Roman", 16)
can_12.drawString(103, 665, stateID[0])
can_12.drawString(126, 665, stateID[1])
can_12.drawString(148, 665, stateID[2])
can_12.drawString(170, 665, stateID[3])
can_12.drawString(191, 665, stateID[4])
can_12.drawString(215, 665, stateID[5])
can_12.drawString(236, 665, stateID[6])
can_12.drawString(257, 665, stateID[7])

can_12.drawString(388, 665, EIN[0])
can_12.drawString(408, 665, EIN[1])
can_12.drawString(429, 665, EIN[3])
can_12.drawString(452, 665, EIN[4])
can_12.drawString(475, 665, EIN[5])
can_12.drawString(496, 665, EIN[6])
can_12.drawString(519, 665, EIN[7])
can_12.drawString(539, 665, EIN[8])
can_12.drawString(560, 665, EIN[9])

can_12.setFont("Times-Roman", 12)

can_12.drawString(43, 615, fullName)
can_12.drawString(43, 592, addressApt)
can_12.drawString(284, 592, city)
can_12.drawString(447, 592, state)
can_12.drawString(496, 592, zipCode)


can_12.drawString(414, 615, cellPhone[0])
can_12.drawString(430, 615, cellPhone[1])
can_12.drawString(445, 615, cellPhone[2])
can_12.drawString(466, 615, cellPhone[4])
can_12.drawString(479, 615, cellPhone[5])
can_12.drawString(494, 615, cellPhone[6])
can_12.drawString(514, 615, cellPhone[8])
can_12.drawString(528, 615, cellPhone[9])
can_12.drawString(542, 615, cellPhone[10])
can_12.drawString(557, 615, cellPhone[11])

can_12.save()
packet_12.seek(0)
new_pdf_12 = PdfFileReader(packet_12)

page_12 = PdfFileReader(open("pdfFiles/09._Tax_ID_Register_(Form_126).pdf", "rb")).getPage(0)
page_12.mergePage(new_pdf_12.getPage(0))
output.addPage(page_12)


# ########################################################


packet_13 = io.BytesIO()

can_13 = canvas.Canvas(packet_13, pagesize=letter)
can_13.setFillColorRGB(0, 0, 1)
can_13.setFont("Times-Roman", 12)
can_13.drawString(336, 200, fullName)
can_13.drawString(60, 177, "Owner")
can_13.drawString(336, 177, signatureDate[0])
can_13.drawString(349, 177, signatureDate[1])
can_13.drawString(366, 177, signatureDate[3])
can_13.drawString(379, 177, signatureDate[4])
can_13.drawString(396, 177, signatureDate[6])
can_13.drawString(411, 177, signatureDate[7])
can_13.drawString(425, 177, signatureDate[8])
can_13.drawString(440, 177, signatureDate[9])

can_13.save()
packet_13.seek(0)
new_pdf_13 = PdfFileReader(packet_13)

page_13 = PdfFileReader(open("pdfFiles/09._Tax_ID_Register_(Form_126).pdf", "rb")).getPage(1)
page_13.mergePage(new_pdf_13.getPage(0))
output.addPage(page_13)

# ########################################################



packet_14 = io.BytesIO()

can_14 = canvas.Canvas(packet_14, pagesize=letter)
can_14.setFillColorRGB(0, 0, 1)
can_14.setFont("Times-Roman", 12)
can_14.drawString(336, 200, fullName)
can_14.drawString(60, 177, "Owner")
can_14.drawString(336, 177, signatureDate[0])
can_14.drawString(349, 177, signatureDate[1])
can_14.drawString(366, 177, signatureDate[3])
can_14.drawString(379, 177, signatureDate[4])
can_14.drawString(396, 177, signatureDate[6])
can_14.drawString(411, 177, signatureDate[7])
can_14.drawString(425, 177, signatureDate[8])
can_14.drawString(440, 177, signatureDate[9])

can_14.save()
packet_14.seek(0)
new_pdf_14 = PdfFileReader(packet_14)

page_14 = PdfFileReader(open("pdfFiles/09._Tax_ID_Register_(Form_126).pdf", "rb")).getPage(1)
page_14.mergePage(new_pdf_14.getPage(0))
output.addPage(page_14)
# ########################################################
output.addPage(PdfFileReader(open("pdfFiles/blank.pdf", "rb")).getPage(0))
# #

# ########################################################
packet_15 = io.BytesIO()

can_15 = canvas.Canvas(packet_15, pagesize=letter)
can_15.setFillColorRGB(0, 0, 1)
can_15.setFont("Times-Roman", 12)
can_15.drawString(82, 412, fullName)
can_15.drawString(440, 412, dateOfBirth + "     " + DCN)
# can_15.drawString(82, 390, fullAddress)
# can_15.drawString(82, 368, fullAddress)
can_15.drawString(82, 342, email)
can_15.drawString(440, 342, cellPhone)

can_15.save()
packet_15.seek(0)
new_pdf_15 = PdfFileReader(packet_15)

page_15 = PdfFileReader(open("pdfFiles/10._Authorized_Representative.pdf", "rb")).getPage(0)
page_15.mergePage(new_pdf_15.getPage(0))
output.addPage(page_15)

# ########################################################
packet_16 = io.BytesIO()

can_16 = canvas.Canvas(packet_16, pagesize=letter)
can_16.setFillColorRGB(0, 0, 1)
can_16.setFont("Times-Roman", 12)
can_16.drawString(82, 756, fullName)
can_16.drawString(440, 756, dateOfBirth + "     " + DCN)

can_16.save()
packet_16.seek(0)
new_pdf_16 = PdfFileReader(packet_16)

page_16 = PdfFileReader(open("pdfFiles/10._Authorized_Representative.pdf", "rb")).getPage(1)
page_16.mergePage(new_pdf_16.getPage(0))
output.addPage(page_16)

# ########################################################
packet_17 = io.BytesIO()

can_17 = canvas.Canvas(packet_17, pagesize=letter)
can_17.setFillColorRGB(0, 0, 1)
can_17.setFont("Times-Roman", 12)
can_17.drawString(82, 750, fullName)
can_17.drawString(440, 750, dateOfBirth + "     " + DCN)

can_17.save()
packet_17.seek(0)
new_pdf_17 = PdfFileReader(packet_17)

page_17 = PdfFileReader(open("pdfFiles/10._Authorized_Representative.pdf", "rb")).getPage(2)
page_17.mergePage(new_pdf_17.getPage(0))
output.addPage(page_17)

# #######################################################
output.addPage(PdfFileReader(open("pdfFiles/blank.pdf", "rb")).getPage(0))
# #######################################################
packet_18 = io.BytesIO()

can_18 = canvas.Canvas(packet_18, pagesize=letter)
can_18.setFillColorRGB(0, 0, 1)
can_18.setFont("Times-Roman", 16)
can_18.drawString(103, 665, stateID[0])
can_18.drawString(126, 665, stateID[1])
can_18.drawString(148, 665, stateID[2])
can_18.drawString(170, 665, stateID[3])
can_18.drawString(191, 665, stateID[4])
can_18.drawString(215, 665, stateID[5])
can_18.drawString(236, 665, stateID[6])
can_18.drawString(257, 665, stateID[7])

can_18.drawString(388, 665, EIN[0])
can_18.drawString(408, 665, EIN[1])
can_18.drawString(429, 665, EIN[3])
can_18.drawString(452, 665, EIN[4])
can_18.drawString(475, 665, EIN[5])
can_18.drawString(496, 665, EIN[6])
can_18.drawString(519, 665, EIN[7])
can_18.drawString(539, 665, EIN[8])
can_18.drawString(560, 665, EIN[9])

can_18.setFont("Times-Roman", 12)

can_18.drawString(68, 473, fullName)

can_18.drawString(68, 450, addressApt)
can_18.drawString(337, 450, city)
can_18.drawString(232, 425, state)
can_18.drawString(332, 425, zipCode)

can_18.drawString(417, 427, cellPhone[0])
can_18.drawString(433, 427, cellPhone[1])
can_18.drawString(446, 427, cellPhone[2])
can_18.drawString(463, 427, cellPhone[4])
can_18.drawString(477, 427, cellPhone[5])
can_18.drawString(493, 427, cellPhone[6])
can_18.drawString(513, 427, cellPhone[8])
can_18.drawString(528, 427, cellPhone[9])
can_18.drawString(545, 427, cellPhone[10])
can_18.drawString(560, 427, cellPhone[11])


can_18.save()
packet_18.seek(0)
new_pdf_18 = PdfFileReader(packet_18)

page_18 = PdfFileReader(open("pdfFiles/11._MO_tax_registation_form_2643A.pdf", "rb")).getPage(0)
page_18.mergePage(new_pdf_18.getPage(0))
output.addPage(page_18)


# ########################################################
packet_19 = io.BytesIO()

can_19 = canvas.Canvas(packet_19, pagesize=letter)
can_19.setFillColorRGB(0, 0, 1)
can_19.setFont("Times-Roman", 12)
can_19.drawString(70, 321, fullName)

can_19.drawString(70, 299, addressApt)
can_19.drawString(347, 299, email)
can_19.drawString(70, 277, city)
can_19.drawString(266, 277, state)
can_19.drawString(337, 277, zipCode)


can_19.drawString(58, 242, SSN[0])
can_19.drawString(77, 242, SSN[1])
can_19.drawString(99, 242, SSN[2])
can_19.drawString(121, 242, SSN[4])
can_19.drawString(144, 242, SSN[5])
can_19.drawString(164, 242, SSN[7])
can_19.drawString(186, 242, SSN[8])
can_19.drawString(207, 242, SSN[9])
can_19.drawString(229, 242, SSN[10])

can_19.drawString(252, 242, dateOfBirth[0])
can_19.drawString(266, 242, dateOfBirth[1])
can_19.drawString(288, 242, dateOfBirth[3])
can_19.drawString(303, 242, dateOfBirth[4])
can_19.drawString(319, 242, dateOfBirth[6])
can_19.drawString(335, 242, dateOfBirth[7])
can_19.drawString(352, 242, dateOfBirth[8])
can_19.drawString(366, 242, dateOfBirth[9])

can_19.drawString(411, 242, cellPhone[0])
can_19.drawString(427, 242, cellPhone[1])
can_19.drawString(439, 242, cellPhone[2])
can_19.drawString(458, 242, cellPhone[4])
can_19.drawString(475, 242, cellPhone[5])
can_19.drawString(488, 242, cellPhone[6])
can_19.drawString(506, 242, cellPhone[8])
can_19.drawString(522, 242, cellPhone[9])
can_19.drawString(537, 242, cellPhone[10])
can_19.drawString(549, 242, cellPhone[11])

can_19.save()
packet_19.seek(0)
new_pdf_19 = PdfFileReader(packet_19)

page_19 = PdfFileReader(open("pdfFiles/11._MO_tax_registation_form_2643A.pdf", "rb")).getPage(1)
page_19.mergePage(new_pdf_19.getPage(0))
output.addPage(page_19)

# ########################################################



output.addPage(PdfFileReader(open("pdfFiles/11._MO_tax_registation_form_2643A.pdf", "rb")).getPage(2))
# ########################################################
packet_20 = io.BytesIO()

can_20 = canvas.Canvas(packet_20, pagesize=letter)
can_20.setFillColorRGB(0, 0, 1)
can_20.setFont("Times-Roman", 12)
can_20.drawString(73, 164, fullName)
can_20.drawString(295, 164, email)
can_20.drawString(295, 186, "Owner")
can_20.drawString(452, 186, signatureDate[0])
can_20.drawString(468, 186, signatureDate[1])
can_20.drawString(485, 186, signatureDate[3])
can_20.drawString(499, 186, signatureDate[4])
can_20.drawString(515, 186, signatureDate[6])
can_20.drawString(531, 186, signatureDate[7])
can_20.drawString(545, 186, signatureDate[8])
can_20.drawString(560, 186, signatureDate[9])
can_20.save()
packet_20.seek(0)
new_pdf_20 = PdfFileReader(packet_20)

page_20 = PdfFileReader(open("pdfFiles/11._MO_tax_registation_form_2643A.pdf", "rb")).getPage(3)
page_20.mergePage(new_pdf_20.getPage(0))
output.addPage(page_20)

# ########################################################

packet_21 = io.BytesIO()

can_21 = canvas.Canvas(packet_21, pagesize=letter)
can_21.setFillColorRGB(0, 0, 1)
can_21.setFont("Times-Roman", 12)
can_21.drawString(57, 659, fullName)
# can_21.drawString(57, 639, fullAddress)
# can_21.drawString(351, 639, cellPhone)

can_21.drawString(54, 90, fullName)
# can_21.drawString(442, 122, signatureDate)
can_21.drawString(442, 90, "Owner")
can_21.save()
packet_21.seek(0)
new_pdf_21 = PdfFileReader(packet_21)

page_21 = PdfFileReader(open("pdfFiles/12._8821_EIN Form.pdf", "rb")).getPage(0)
page_21.mergePage(new_pdf_21.getPage(0))
output.addPage(page_21)


# ########################################################
output.addPage(PdfFileReader(open("pdfFiles/blank.pdf", "rb")).getPage(0))
# #
# ########################################################
packet_23 = io.BytesIO()

can_23 = canvas.Canvas(packet_23, pagesize=letter)
can_23.setFillColorRGB(0, 0, 1)
can_23.setFont("Times-Roman", 12)
can_23.drawString(57, 636, fullName)
#can_23.drawString(57, 614, fullAddress)
#can_23.drawString(351, 614, cellPhone)


can_23.save()
packet_23.seek(0)
new_pdf_23 = PdfFileReader(packet_23)

page_23 = PdfFileReader(open("pdfFiles/13._2848_Power_of_Attorney_form.pdf", "rb")).getPage(0)
page_23.mergePage(new_pdf_23.getPage(0))
output.addPage(page_23)
# ########################################################
packet_24 = io.BytesIO()

can_24 = canvas.Canvas(packet_24, pagesize=letter)
can_24.setFillColorRGB(0, 0, 1)
can_24.setFont("Times-Roman", 12)

can_24.drawString(103, 516, fullName)
#can_24.drawString(291, 556, signatureDate)
can_24.drawString(422, 556, "Owner")
can_24.save()
packet_24.seek(0)
new_pdf_24 = PdfFileReader(packet_24)

page_24 = PdfFileReader(open("pdfFiles/13._2848_Power_of_Attorney_form.pdf", "rb")).getPage(1)
page_24.mergePage(new_pdf_24.getPage(0))
output.addPage(page_24)


# can_14 = canvas.Canvas(packet_14, pagesize=letter)
# can_14.setFillColorRGB(0, 0, 1)
# can_14.setFont("Times-Roman", 16)
# packet_14 = io.BytesIO()

# can_14.drawString(103, 665, stateID[0])
# can_14.drawString(126, 665, stateID[1])
# can_14.drawString(148, 665, stateID[2])
# can_14.drawString(170, 665, stateID[3])
# can_14.drawString(191, 665, stateID[4])
# can_14.drawString(215, 665, stateID[5])
# can_14.drawString(236, 665, stateID[6])
# can_14.drawString(257, 665, stateID[7])
#
# can_14.drawString(388, 665, EIN[0])
# can_14.drawString(408, 665, EIN[1])
# can_14.drawString(429, 665, EIN[3])
# can_14.drawString(452, 665, EIN[4])
# can_14.drawString(475, 665, EIN[5])
# can_14.drawString(496, 665, EIN[6])
# can_14.drawString(519, 665, EIN[7])
# can_14.drawString(539, 665, EIN[8])
# can_14.drawString(560, 665, EIN[9])
#
# can_14.setFont("Times-Roman", 12)
#
# can_14.drawString(43, 615, fullName)
# can_14.drawString(43, 592, address + " " + aptNumber)
# can_14.drawString(284, 592, city)
# can_14.drawString(447, 592, state)
# can_14.drawString(496, 592, zipCode)
#
#
# can_14.drawString(414, 615, cellPhone[0])
# can_14.drawString(430, 615, cellPhone[1])
# can_14.drawString(445, 615, cellPhone[2])
# can_14.drawString(466, 615, cellPhone[4])
# can_14.drawString(479, 615, cellPhone[5])
# can_14.drawString(494, 615, cellPhone[6])
# can_14.drawString(514, 615, cellPhone[8])
# can_14.drawString(528, 615, cellPhone[9])
# can_14.drawString(542, 615, cellPhone[10])
# can_14.drawString(557, 615, cellPhone[11])

# can_14.save()
# packet_14.seek(0)
# new_pdf_14 = PdfFileReader(packet_14)
#
# page_14 = PdfFileReader(open("pdfFiles/11._MO_tax_registation_form_2643A.pdf", "rb")).getPage(0)
# page_14.mergePage(new_pdf_14.getPage(0))
# output.addPage(page_14)


# ########################################################
#
# packet_9 = io.BytesIO()
#
# can_9 = canvas.Canvas(packet_9, pagesize=letter)
# can_9.setFillColorRGB(0, 0, 1)
# can_9.setFont("Times-Roman", 12)
# can_9.drawString(38, 572, address)
# can_9.drawString(40, 603, firstName)
# can_9.drawString(210, 603, lastName)
# can_9.drawString(310, 572, city)
# can_9.drawString(450, 572, state)
# can_9.drawString(493, 572, zipCode)
# can_9.drawString(483, 540, cellPhone)
# can_9.drawString(42, 540, dateOfBirth)
# can_9.drawString(253, 540, email)
#
# can_9.drawString(145, 540, SSN[0])
# can_9.drawString(155, 540, SSN[1])
# can_9.drawString(166, 540, SSN[2])
# can_9.drawString(180, 540, SSN[4])
# can_9.drawString(191, 540, SSN[5])
# can_9.drawString(205, 540, SSN[7])
# can_9.drawString(216, 540, SSN[8])
# can_9.drawString(227, 540, SSN[9])
# can_9.drawString(238, 540, SSN[10])
#
# can_9.drawString(500, 230, signatureDate)
#
# can_9.save()
# packet_9.seek(0)
# new_pdf_9 = PdfFileReader(packet_9)
#
# page_9 = PdfFileReader(open("caregiverAtHome/3._employment_Eligibility_Verification_(I-9).pdf", "rb")).getPage(0)
# page_9.mergePage(new_pdf_9.getPage(0))
# output.addPage(page_9)
#
# ########################################################
# output.addPage(PdfFileReader(open("caregiverAtHome/3._employment_Eligibility_Verification_(I-9).pdf", "rb")).getPage(1))
#
# ########################################################
#
#
#
# packet_11 = io.BytesIO()
#
# can_11 = canvas.Canvas(packet_11, pagesize=letter)
# can_11.setFillColorRGB(0, 0, 1)
# can_11.setFont("Times-Roman", 12)
# can_11.drawString(60, 652, address)
# can_11.drawString(60, 675, fullName)
# can_11.drawString(303, 652, city)
# can_11.drawString(436, 652, state)
# can_11.drawString(500, 652, zipCode)
#
#
#
# can_11.drawString(435, 675, SSN[0])
# can_11.drawString(449, 675, SSN[1])
# can_11.drawString(465, 675, SSN[2])
# can_11.drawString(481, 675, SSN[4])
# can_11.drawString(496, 675, SSN[5])
# can_11.drawString(511, 675, SSN[7])
# can_11.drawString(526, 675, SSN[8])
# can_11.drawString(541, 675, SSN[9])
# can_11.drawString(556, 675, SSN[10])
#
#
# can_11.drawString(464, 336, signatureDate[0])
# can_11.drawString(477, 336, signatureDate[1])
# can_11.drawString(496, 336, signatureDate[3])
# can_11.drawString(509, 336, signatureDate[4])
# can_11.drawString(526, 336, signatureDate[6])
# can_11.drawString(539, 336, signatureDate[7])
# can_11.drawString(552, 336, signatureDate[8])
# can_11.drawString(565, 336, signatureDate[9])
#
#
#
# can_11.save()
# packet_11.seek(0)
# new_pdf_11 = PdfFileReader(packet_11)
#
# page_11 = PdfFileReader(open("caregiverAtHome/4._new_MO_W-4.pdf", "rb")).getPage(0)
# page_11.mergePage(new_pdf_11.getPage(0))
# output.addPage(page_11)
#
#
#
# ########################################################
# output.addPage(PdfFileReader(open("caregiverAtHome/1._employee_Job_App.pdf", "rb")).getPage(5))
#
# ########################################################
# packet_13 = io.BytesIO()
#
# can_13 = canvas.Canvas(packet_13, pagesize=letter)
# can_13.setFillColorRGB(0, 0, 1)
# can_13.setFont("Times-Roman", 12)
# can_13.drawString(96, 688, firstName)
# can_13.drawString(280, 688, lastName)
# can_13.drawString(481, 688, SSN)
# can_13.drawString(96, 662, address)
# tempCity = city + " " + state + " " + zipCode
# can_13.drawString(96, 640, tempCity)
# can_13.drawString(468,142, signatureDate)
#
# can_13.save()
# packet_13.seek(0)
# new_pdf_13 = PdfFileReader(packet_13)
#
# page_13 = PdfFileReader(open("caregiverAtHome/5._new_W_4.pdf", "rb")).getPage(0)
# page_13.mergePage(new_pdf_13.getPage(0))
# output.addPage(page_13)
#
# ########################################################
outputStream = open("clientAtHome.pdf", "wb")
output.write(outputStream)
outputStream.close()