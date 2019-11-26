# Tesseract-ocr quick implementation

Tesseract-ocr quick implementation using python and generated exe file by pyinstaller

## Installation

Tested with Windows 10 64bit, python 3.6
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -U -r requirements.txt
```

## Usage

main.py extractes text from images located "images" directory. 
```python
python main.py
```

main.exe is same as main.py this file extracted by using pyinstaller
```bash
pyinstaller --onefile main.py
```
If you run main.exe file there are shows some warning messages see down below.
I have no idea why this warning messages appearing if you know about this problem please help me! 
```bash
Running from container, but no tessdata (C:Users/....) found!
Running from container, but no tesseract (C:Users/....) found!
```

## Contributing
Pull requests are welcome. 
