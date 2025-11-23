# Import required libraries
import requests  # For making HTTP requests
import base64    # For decoding base64 encoded images
import pytesseract  # For OCR (Optical Character Recognition)
import cv2       # OpenCV for image processing
import re        # Regular expressions for text processing
import time      # For measuring execution time

# Set the path to Tesseract OCR executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Example target URL (replace with your actual target)
# This is a placeholder - real CAPTCHA URLs will vary by website
url = "https://example.com/captcha_challenge"
headers = {"User-Agent": "Mozilla/5.0"}  # User-Agent header to mimic a browser

def solve_captcha():
    """Main function to handle CAPTCHA solving process"""
    start_time = time.time()  # Start timer to measure execution time

    try:
        # Make GET request to fetch the CAPTCHA page
        print("[*] Fetching CAPTCHA challenge...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise exception for bad status codes
        html = response.text

        # Use regex to find the base64 encoded CAPTCHA image in the HTML
        # Note: Different websites may have different CAPTCHA image formats
        match = re.search(r'data:image/(png|jpeg);base64,(.*?)"', html)
        if not match:
            print("[-] CAPTCHA not found in page!")
            return False

        image_type, captcha_base64 = match.groups()
        print(f"[+] Found {image_type} CAPTCHA image")

        # Extract and decode the base64 CAPTCHA image
        captcha_data = base64.b64decode(captcha_base64)

        # Save the CAPTCHA image to a file
        captcha_filename = f"captcha.{image_type}"
        with open(captcha_filename, "wb") as file:
            file.write(captcha_data)
        print(f"[*] CAPTCHA saved as {captcha_filename}")

        # Read and preprocess the image
        image = cv2.imread(captcha_filename, cv2.IMREAD_GRAYSCALE)
        
        # Apply thresholding to improve text recognition
        _, thresh_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

        # Use Tesseract OCR to extract text
        # psm 6 assumes a single uniform block of text
        captcha_text = pytesseract.image_to_string(thresh_image, config="--psm 6")
        
        # Clean the extracted text
        captcha_text = re.sub(r'\W+', '', captcha_text)
        if not captcha_text:
            print("[-] Failed to extract text from CAPTCHA")
            return False

        print(f"[+] Extracted CAPTCHA text: {captcha_text}")

        # Prepare and submit the solution
        # Note: Form field name ('cametu' in original) may vary by website
        form_data = {"captcha_text": captcha_text}
        
        print("[*] Submitting solution...")
        response = requests.post(url, headers=headers, data=form_data, timeout=10)

        # Check result - success condition varies by website
        if "success" in response.text.lower():
            print(f"[✔] CAPTCHA solved in {time.time() - start_time:.2f} seconds!")
            return True
        else:
            print("[-] CAPTCHA solution rejected")
            return False

    except Exception as e:
        print(f"[-] Error occurred: {str(e)}")
        return False

# Run the CAPTCHA solver
if __name__ == "__main__":
    solve_captcha()