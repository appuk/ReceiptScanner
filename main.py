from PIL import Image
import pytesseract
import os


var = raw_input("Please enter a relevant description for this batch of receipts: ")
output_file = open (var,"w")
for file in os.listdir("/home/apurva/Desktop/Receipts"):
	if file.endswith(".jpg"):
		im = Image.open(file)
		text = pytesseract.image_to_string(im)
		textfile = file[:-3]
		output_file.write("\n**************************************************************************")		
		output_file.write("\nOutput for Receipt:\n")
		output_file.write(textfile)
		output_file.write("\n")		
		output_file.write(text.encode("utf-8")) 
		output_file.write("\n\n\n\n")	
output_file.close() 
