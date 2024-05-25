# Image Processing Web Interface
## Introduction
This project aims to create a web interface that allows users to upload an image and get details about it using AWS Rekognition. The application detects text and labels in the uploaded images and displays the results back to the user.

## Features
- Image Upload: Users can upload images through a simple web interface.
- Text Detection: Uses AWS Rekognition to detect text within the image.
- Label Detection: Uses AWS Rekognition to identify and label objects within the image.
- Visual Annotations: Annotates the image with bounding boxes around detected labels.

## Technologies Used
- Backend: Python with Flask framework.
- Frontend: HTML, CSS, JavaScript.
- Image Processing: AWS Rekognition, Pillow, OpenCV.
- Deployment: Deployed locally using Flask.

## Directory Structure
your_project_directory/
│
├── app.py
├── static/
│   └── index.html
├── uploads/
└── rekognition_accessKeys.csv
## Setup and Installation
### 1. Clone the Repository:

git clone https://github.com/your-username/image-processing-web-interface.git
cd image-processing-web-interface
### 2. Create a Virtual Environment:


python3 -m venv env
source env/bin/activate
### 3. Install Dependencies:

pip install -r requirements.txt
### 4. AWS Credentials:

- Ensure you have AWS credentials in a CSV file (e.g., rekognition_accessKeys.csv) with your Access Key ID and Secret Access Key.
- The CSV file should be formatted as follows:

Access key ID,Secret access key
YOUR_ACCESS_KEY_ID,YOUR_SECRET_ACCESS_KEY
### 5. Run the Flask Application:

python app.py

### 6. Access the Application:
Open your web browser and go to http://127.0.0.1:5000.

## How to Use
Open the Web Interface:
Navigate to http://127.0.0.1:5000 in your web browser.

Upload an Image:
Click on the "Choose File" button, select an image, and click "Upload".

View Results:
The detected text and the processed image with labeled annotations will be displayed on the web page.

## Challenges Faced
1. API Choice:
Initially used Google Vision API but faced issues after payment and configuration, leading to a switch to AWS Rekognition.
2. Deployment Issues:
Encountered problems with deploying the .csv file containing API keys on GitHub. Solved by using alternative methods to manage API keys securely.
3. Overall Experience:
The development process was mostly smooth, with minor issues resolved promptly. The final product is a functional and user-friendly application.
## Conclusion
This project demonstrates the integration of a web interface with cloud-based image processing services using AWS Rekognition. It provides a user-friendly way for users to upload images and receive detailed analysis, including text detection and labeled annotations. The project serves as a practical example of combining frontend and backend technologies to build a cohesive application.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to customize this README file as needed. If you have any questions or run into issues, please open an issue in the GitHub repository.

## Contact
For any inquiries or feedback, please contact:

Lakshay Narula
GitHub: lakshay909








