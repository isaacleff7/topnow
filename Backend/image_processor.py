from paddleocr import PaddleOCR, draw_ocr
import cv2

# Initialize the OCR model (use 'en' for English language model)
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Main function that processes an image and returns just the text
def process_image(image_path):
    # Get the OCR result
    image_text = ocr.ocr(image_path)

    # Extract text from the result
    extracted_text = ""
    for line in image_text:
        for word_info in line:
            extracted_text += word_info[1][0] + " "  # Extract only the recognized text

    return extracted_text.strip()  # Return the extracted text without extra spaces

# Example usage
text = process_image("IMG_7325.jpg")
print("below is the extracted string.")
print("Extracted Text:", text)
