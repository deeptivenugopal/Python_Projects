from qrtools import * 

my_qr = qrtools.QR(data = u"Example")

my_qr.encode()

print(my_qr.filename)
