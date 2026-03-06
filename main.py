from PIL import Image            # PIL(Python Image Library) is used for image Open & processing
from rembg import remove        # rembg(AI based Library) is used for background removal
# uv pip install onnxruntime       # Install onnxruntime for running the rembg model efficiently

input_path = 'input_image.jpg'  # Path of the input image

input_image_open = Image.open(input_path)  # Open the input image using PIL
output_image = remove(input_image_open)  # Remove the background from the input image using rembg
output_image.save('output_image.png')  # Save the output image with transparent background as PNG format
print("Background removed successfully. Output image saved as 'output_image.png'.") 
