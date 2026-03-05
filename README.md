# QR Code Generator

A simple Python-based QR code generator that creates QR codes from URLs or text input.

## Description

This project provides a command-line tool to generate QR codes from any URL or text string. The generated QR code is saved as a PNG image file that can be easily shared or printed.

## Features

- Generate QR codes from any text or URL input
- Save QR codes as PNG images
- Simple and easy-to-use command-line interface

## Requirements

- Python 3.x
- uv (Python package manager)

## Installation

1. **Install required dependencies:**

```bash
uv pip install qrcode
uv pip install pillow
```

> **Note:** Both `qrcode` and `pillow` packages are required. The `pillow` library is essential for image generation and processing.

## Usage

Run the program using the following command:

```bash
uv run python main.py
```

You will be prompted to enter the URL or text you want to encode:

```
Enter the URL to encode in the QR code: https://your-url-here.com
```

The QR code will be generated and saved as `qrcode.png` in the current directory.

## Example

```bash
$ uv run python main.py
Enter the URL to encode in the QR code: https://github.com
QR code generated and saved as 'qrcode.png'
```

## Output

The program generates a file named `qrcode.png` containing the QR code for the entered text or URL.
