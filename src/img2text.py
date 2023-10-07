from PIL import Image
from pytesseract import pytesseract
from glob import glob
from pathlib import Path

import os

main_dir = os.getcwd()
image_path = main_dir + "/img"
text_path = main_dir + "/text"

class Img2text(object):

  def __init__(self, file):
    self.filename = file
    image_path = self.imagePath(self.filename)
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
  # instructions prompt
  print("The following program handles multiple files input—separated by comma.")
  # prompt user to enter filename
  while True:
    filenames = str(input("Enter file names: "))
    if not filenames or filenames == '':
      continue

    else:
      break
 
  # make list
  filelist = filenames.split(",")
  filelist = [x.strip(" ") for x in filelist]

  # check if file exists 
  for file in filelist:
    try:
      print(f"Processing {file}...") 
      program = Img2text(file)
      program.run()
 
    except:
      print("File does not exist.")
      continue 

if __name__ == "__main__":
    main()
