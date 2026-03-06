# Image Background Remover

A small Python script that uses `Pillow` and the `rembg` library to remove
backgrounds from images. The output is saved as a PNG file with a transparent
background.

## Requirements

- Python 3.7+
- Packages:
  ```sh
  pip install pillow rembg onnxruntime
  ```

## Usage

1. Put the image you want to process in the project folder and name it
   `input_image.jpg` (or adjust the path in `main.py`).
2. Run the script:
   ```sh
   python main.py
   ```
3. After the script finishes, an `output_image.png` file will be created with
   its background removed.

## Notes

The script uses `onnxruntime` for faster model execution. Make sure the input
file exists before running the script. The example uses `input_image.jpg` but
this can be changed as needed.