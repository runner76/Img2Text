from PIL import Image
from pytesseract import pytesseract
from glob import glob
from pathlib import Path

import os

main_dir = os.getcwd()
image_path = main_dir + "/img"

class Img2text(object):

  def __init__(self, image):
    image_path = self.imagePath(image)
    print(image_path)
    self.image = Image.open(image_path)
    print(self.image)

  def imagePath(self, image):
    file = glob(image_path + f'/*{image}*.*')
    return file

  def conversion(self):

    # Providing the tesseract executable
    # location to pytesseract library
    #pytesseract.tesseract_cmd = path_to_tesseract
      
    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    text = pytesseract.image_to_string(self.image)
      
    # save the extracted text
    return text[:-1]

def main():
  # prompt user to enter filename
  filename = str(input("Enter file name: "))

  # run program
  program = Img2text(filename)
  print(program.conversion())

main()