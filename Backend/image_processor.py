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


def process_scorecard(text): 
    tops = 0
    zones = 0
    attemptsT = 0
    attemptsZ = 0
    tempString = ""

    #find start of score
    for val in text: 
        if val == 0 or val =="O" or val =="T" or val =="Z": #we can write a fxn to check for this
            tempString += val
        if val == "B": #shows that we are done looking at the scores of the last boulder
            #calc tops/zones/attemps
            print(tempString)
            top = False
            zone = False
            tempAttemptT = 0
            tempAttemptZ = 0

            for char in tempString: 
                if char == "0" or char == "O": 
                    tempAttemptT += 1
                    if zone == False: 
                        tempAttemptZ += 1
                if char == "Z": 
                    if zone == False: 
                        zone = True
                        zones +=1
                        attemptsZ += tempAttemptZ+1
                        tempAttemptT+=1
                if char == "T": 
                    tops += 1
                    
                    attemptsT = attemptsT + tempAttemptT + 1
                    if zone == False: 
                        zones += 1
                        attempsZ = attemptsZ + tempAttemptT + 1
                
            #reset our tempstring
            print(tops)
            print(zones)
            
            print(attemptsT)
            print(attemptsZ)
            tempString = ""



# Example usage
text = process_image("IMG_7325.jpg")
print("below is the extracted string.")
print("Extracted Text:", text)
process_scorecard(text)



