from PIL import Image
from zipfile import ZipFile
import glob
import os
from os.path import basename

def convert_tiff_to_jpg(filename):
    im = Image.open(filename)
    rgb_im = im.convert('RGB')
    rgb_im.save(filename.replace('.tiff', '.jpg').replace('.tif', '.jpg').replace('input/', 'output/'), 'JPEG')

def clean_up():
    output_path = os.path.join(os.getcwd(), 'output', '*')
    input_path = os.path.join(os.getcwd(), 'input', '*')
    o_files = glob.glob(output_path)
    i_files = glob.glob(input_path)
    for f in o_files:
        os.remove(f)
    for f in i_files:
        os.remove(f)

def zip_files():
    with ZipFile(os.path.join(os.getcwd(), 'output','converted.zip'), 'w') as zipObj:
        for folderName, subfolders, filenames in os.walk(os.path.join(os.getcwd(), 'output')):
            for filename in filenames:
                if(filename != 'converted.zip'):
                    filePath = os.path.join(folderName, filename)
                    zipObj.write(filePath, basename(filePath))