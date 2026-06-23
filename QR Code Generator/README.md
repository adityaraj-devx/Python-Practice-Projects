# QR Code Generator

## Overview
A simple Python application that generates a QR code from user-provided text or a URL and saves it as an image.

## Features
- Generate QR codes from text or URLs
- Save QR codes as PNG images
- Simple command-line interface

## Requirements
- Python 3
- qrcode library

## Installation

```bash
pip install qrcode[pil]
```

## Run

```bash
python main.py
```

## Usage
1. Run the program.
2. Enter the text or URL you want to convert into a QR code.
3. Enter a filename.
4. The QR code image will be generated and saved as a PNG file.

## Example

Input:
- URL: https://github.com
- Filename: github_qr

Output:
- QR code image saved as `some_file.png`