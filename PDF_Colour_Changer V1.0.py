# ssmcosmic

from PyPDF2 import PdfReader, PdfFileWriter 
from pdf2image import convert_from_path
from PIL import Image
import img2pdf

''' This program takes an input PDF path, and allows the user to change one colour to another '''


                                ''' Paths and Naming --> User Specific '''

# Input Path for PDF to operate on 
PDF_Path = "D:\Coding Projects\Lab5.pdf"

# Temp name for each image slice
PDF_Name = 'PDF_2_Image_'


# Output path
OutputDirectory = "D:\Coding Projects\Output\\"
OutPutFilePath = OutputDirectory+PDF_Name


# Choose a colour that you want to replace:
# This is an list, where each old colour corresponds to the new colour at the same index position
OldColour = [(0,0,0)]


# Choose a colour to change to
NewColour = [(0, 0, 150)]

# Include the poppler path
PopplerPath = r'C:\Users\SSM\Downloads\Release-24.02.0-0\poppler-24.02.0\Library\bin'

# ----------------------- Do Not Modify Anything Below This -----------------------------------------------#

temp_pdf = PdfReader(PDF_Path)
Pages = len(temp_pdf.pages)


# Convert each slice of the pdf into an image
images = convert_from_path(PDF_Path,poppler_path= PopplerPath,output_folder=OutputDirectory, fmt ="png", output_file = PDF_Name)


# Input from output folder
from PIL import Image
InputPath = OutputDirectory+PDF_Name+"0001-"



# Note: We need a png file for the pdf else it won't work (else compression makes the simple if condition useless)
FinalOutputName = "Output "
Image_List = []
File = ""
for index in range(Pages):
          
    if index < 9:
        File = InputPath+"0"+str(index+1)+".png"
    else:
        File = InputPath+str(index+1)+".png"
    
    LoadedImage = Image.open(File)  
    
    
    pixel_map = LoadedImage.load()
    width,height = LoadedImage.size

    # If the pixel is black (text/outline eg.), replace the pixel code with blue

    for i in range(width):
        for j in range(height):
          
            # Getting RGB pixel values
            r, g, b = LoadedImage.getpixel((i, j))

            for k in range(len(OldColour)):
                if pixel_map[i,j] == (OldColour[k]):
                    pixel_map[i,j] = (NewColour[k])
                
                
    print("Loading... Please do not exit the program!")
    LoadedImage.save(OutputDirectory+FinalOutputName+str(index)+".png")
    Image_List.append(OutputDirectory+FinalOutputName+str(index)+".png")

       


# Stitch back all output slices into a single PDF
with open(OutputDirectory+"output.pdf", "wb") as f:
    f.write(img2pdf.convert(Image_List))







print("Process has completed. You may exit the program!")

# Convert the images into a single image
print("-----------------------------------------------------------")


#print(Image_List)


print("-----------------------------------------------------------")
