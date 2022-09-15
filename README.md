# Wundernut Vol. 12

This is a quick&dirty program to solve the Wundernut vol. 12.

Wundernut vol. 12 can be found at https://github.com/wunderdogsw/wundernut-vol12

Download `parchment.png` from the Wundernut vol12 github.

## Installation

This program requires `tesseract` binary to be installed.

Ubuntu:
```shell

$ apt-get install tesseract-ocr
```
Create virtual env and install required Python libraries:

```shell

$ python3.8 -m venv venv

$ . venv/bin/activate

$ pip3 install -r requirements.txt
```

## Usage

```shell

$ ./nut.py parchment.png
```
