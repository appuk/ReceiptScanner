from PIL import Image
import pytesseract
import os


for file in os.listdir("/home/apurva/Desktop/Receipts/recs"):
    if file.endswith(".jpg"):
		im = Image.open(file)
		text = pytesseract.image_to_string(im)
		file = file[:-3]
		textfile = file+"txt"
		file = open (textfile,"w")
		file.write(text.encode("utf-8")) 
		file.close() 
