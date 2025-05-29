import qrcode

data = 'Suresh Polai'
qr = qrcode.make(data)
qr.save('suresh.png')
print('QR Code Generated Successfully!')