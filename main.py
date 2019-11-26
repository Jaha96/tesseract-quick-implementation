############## main.py ###################################
# coding: utf-8
#

from PIL import Image
import pyocr
import cv2
import io, os, sys

currentDirectory = os.getcwd()
tess_path = os.path.join(currentDirectory, 'Tesseract-OCR')
os.environ["PATH"] += os.pathsep + tess_path
os.environ["TESSDATA_PREFIX"] = os.path.join(tess_path, 'tessdata')

# ※があるかないかで条件分岐するため初期値宣言
def tesseract_ocr(image_path):
    # OCRツールを指定　（「Tesseract」が[0]に収められていた）
    tools = pyocr.get_available_tools()
    if len (tools) == 0:
        print ("No Tesseract OCR tool found")

    tool = tools[0]
    # langs = tool.get_available_languages()

    # 画像を認識
    with Image.open(image_path) as im1:
        # ビルダーの設定
        builder = pyocr.builders.LineBoxBuilder(tesseract_layout=6)
        # テキスト抽出
        res = tool.image_to_string(
            im1,
            lang= 'digits_comma', #lang_setting,  # 言語を指定
            builder=builder
        )
    return res

def getFileList(path) :
  files = []
  # r=root, d=directories, f = files
  for r, d, f in os.walk(path):
      for file in f:
          if '.jpg' in file:
              files.append(os.path.join(r, file))
  return files


files = getFileList(os.path.join(currentDirectory, 'images'))
if len(files) == 0:
    print('No files found. Create directory called images')
    input('Press any key to close')
for image_path in files:
    document = tesseract_ocr(image_path)
    for d in document:
        print(d.content)
    print('\n')
input('Press any key to close')