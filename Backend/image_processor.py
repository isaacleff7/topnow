from paddleocr import PaddleOCR, draw_ocr
import cv2

# Initialize the OCR model (use 'en' for English language model)
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Main function that fully processes an image start to finish with return values.
def process_image(image_path):
    #getting the image text using the ocr object
    image_text = ocr.ocr(image_path)
    # Extract text from the result
    extracted_text = ""
    for line in image_text:
        for word_info in line:
            extracted_text += word_info[1][0] + " "  # word_info[1][0] contains the recognized text
    print(extracted_text)

# Executed line of code -> processing the th.jpg image
process_image("R.jpg")