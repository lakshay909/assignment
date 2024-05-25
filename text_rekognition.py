import boto3
import csv

# Read AWS credentials from CSV file
with open('/Users/lakshaynarula/Desktop/Codes/Text and Visual analysis/vision-rekongnition_accessKeys.csv', 'r') as file:
    next(file)
    reader = csv.reader(file)
    for line in reader:
        access_key_id = line[0]
        secret_access_key = line[1]

# Initialize Rekognition client
client = boto3.client('rekognition', region_name='us-west-2',
                      aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)

# Path to the image file
photo = '/Users/lakshaynarula/Desktop/Codes/Text and Visual analysis/IMG_0204.jpeg'

# Read the image file
with open(photo, 'rb') as image_file:
    source_bytes = image_file.read()

# Call Rekognition to detect text
detect_text_response = client.detect_text(Image={'Bytes': source_bytes})

# Print detected text
print('Detected text:\n')
for text in detect_text_response['TextDetections']:
    print(text['DetectedText'])
