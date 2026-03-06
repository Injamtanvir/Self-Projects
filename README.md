# Image to Text Extractor

This simple Python project reads an image (`image.png` by default) and uses
Tesseract OCR (via the `pytesseract` wrapper) to extract any text it contains.
The output is written to `extracted_text.txt` in the same directory.

## Prerequisites

- Install required packages inside the environment:
  ```sh
  uv pip install pillow pytesseract
  ```
- **Tesseract OCR binary** must be installed separately:
  - macOS: `brew install tesseract`
  - verify with `tesseract --version`

## Running

1. Place the target image in the workspace (the script expects `image.png` but
   you can adjust the `image_input` variable in `main.py`).
2. Activate your virtualenv and run:
   ```sh
   uv run python main.py
   ```
3. After execution, view the extracted text in `extracted_text.txt`.

## Notes

- `uv pip install pytesseract` installs only the Python wrapper. The OCR engine
  itself comes from the `tesseract` package from Homebrew or your OS's package
  manager.
- `main.py` contains the example workflow.

