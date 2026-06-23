# Image Compressor

## Overview
A simple Python application that compresses image files by converting them to JPEG format and reducing image quality. This helps reduce file size while maintaining acceptable image quality.

## Features
- Compress image files
- Convert images to JPEG format
- Reduce file size using adjustable quality settings
- Easy command-line interface

## Requirements
- Python 3
- Pillow (PIL)

## Installation

```bash
pip install pillow
```

## Run

```bash
python main.py
```

## Usage

1. Run the program.
2. Enter the path or filename of the image.
3. The program compresses the image and saves it as:

```text
new_image.jpg
```

## Example

Input:

```text
Enter the filename: photo.png
```

Output:

```text
Compressed image has been saved photo.png
```

Generated file:

```text
new_image.jpg
```

## Learning Concepts

This project demonstrates:
- File handling
- Image processing with Pillow
- Image format conversion
- Image compression techniques
- User input handling