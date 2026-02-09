import qrcode as qr

img = qr.make("https://www.chess.com/play/online")
img.save("chess.png")