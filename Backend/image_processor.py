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

# test commit for git.
#takes in the text from image processor and converts it into a score
def process_scorecard(text): 
    tops = 0
    zones = 0
    attemptsT = 0
    attemptsZ = 0
    tempString = ""
    char = 0

    #find start of score
    for val in text: 
        if val == "0" or val =="O" or val =="T" or val =="Z": #we can write a fxn to check for this
            tempString += str(val)
        if val == "B" or char == len(text)-1: #shows that we are done looking at the scores of the last boulder
            #calc tops/zones/attemps
            score = score_boulder(tempString)
            if score[0] : #true if topped
                tops +=1
                attemptsT += score[2] #score[2] is the attempts to zone
            if score[1]: #true if zoned
                zones +=1
                attemptsZ += score[3] #score[3] is the attempts to zone
            tempString = ""
        char +=1
    print("Tops: " + str(tops))
    print("Zones: " + str(zones))
    print("Attempts to top: " + str(attemptsT))
    print("Attempts to zone: " + str(attemptsZ))

#takes in a string in format 00Z0T which represents a boulder score and return if they top/zone on it and how many attempts it takesaaaa
def score_boulder(tempString):

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
                tempAttemptZ+=1
                tempAttemptT+=1
            else: 
                tempAttemptT+=1
        if char == "T": 
            top = True     
            tempAttemptT += 1
            if zone == False: 
                zone = True
                tempAttemptZ = tempAttemptZ + 1
    return [top, zone, tempAttemptT, tempAttemptZ]



# Example usage
text = process_image("card.jpg")
print("below is the extracted string.")
print("Extracted Text:", text)
process_scorecard(text)



