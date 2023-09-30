from PIL import Image
from pytesseract import pytesseract
from glob import glob
from pathlib import Path

import os

main_dir = os.getcwd()
image_path = main_dir + "/img"
text_path = main_dir + "/text"

class Img2text(object):

  def __init__(self, filename):
    self.filename = filename
    image_path = self.imagePath(filename)
    #print(image_path)
    self.image = Image.open(image_path)
    self.text = self.conversion(self.image) 

  def imagePath(self, filename):
    for file in glob(image_path + f'/*{filename}*.*'):
      return file

  def conversion(self, image):
    text = pytesseract.image_to_string(image)
    return text[:-1]
  
  def export(self, text):
    txt_file = open(text_path + f"/{self.filename}.txt", 'w')
    txt_file.write(text)
    txt_file.close()
    return txt_file
   
  def run(self):
    self.export(self.text)

def main():
  # prompt user to enter filename
  while True:
    filename = str(input("Enter file name: "))
    if not filename or filename == '':
      continue

    else:
      break 

  # run program
  try: 
    program = Img2text(filename)
  
  except:
    print("File does not exist.")
    quit()

  program.run()

if __name__ == "__main__":
    main()
