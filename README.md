# 🤖 CAPTCHA Solver

A Python-based tool to automatically fetch and solve image-based CAPTCHA challenges using OCR (Optical Character Recognition). Designed for educational purposes, testing, and legal automation tasks.

---

# ⭐ **DESCRIPTION**

**CAPTCHA Solver** automates the process of retrieving CAPTCHA images from web pages, processing them for OCR, extracting the text, and submitting solutions programmatically. This tool leverages `pytesseract` for text recognition and `OpenCV` for image preprocessing.

Ideal for:
- Automating repetitive CAPTCHA testing in development environments
- Learning OCR and web interaction techniques
- Educational or research purposes in cybersecurity and web automation

---

## 🔧 **Key Features**

- **Automated CAPTCHA Retrieval**  
  Fetches base64-encoded CAPTCHA images directly from web pages.

- **Image Preprocessing**  
  Uses OpenCV to enhance OCR accuracy with thresholding.

- **Text Extraction via OCR**  
  Employs Tesseract OCR to extract text from CAPTCHA images.

- **Solution Submission**  
  Submits the recognized text back to the website (adjustable form data).

- **Execution Timing**  
  Reports total execution time for each CAPTCHA solving attempt.

---

## 🎯 **Intended Use**

- **Educational Projects**  
  Learn OCR, image processing, and web automation techniques.

- **Personal Testing**  
  Automate CAPTCHA challenges for your own development environment.

**⚠️ Legal Disclaimer:**  
Use this tool responsibly. Only attempt to solve CAPTCHAs on websites you own or have explicit permission to test. Unauthorized use is illegal and unethical.

---

## 🛠️ **INSTALLATION**

1. Install required Python libraries:
```bash
pip install requests pytesseract opencv-python
```

2. Install Tesseract OCR engine:  
   [Tesseract installation instructions](https://github.com/tesseract-ocr/tesseract)

3. Update the `pytesseract.pytesseract.tesseract_cmd` path in the script to match your system.

4. Update the `TARGET_URL` in the script with the CAPTCHA page you want to test.

---

## 🚀 **USAGE**

Run the script via terminal or command prompt:
```bash
python captcha_solver.py
```

The script will:
1. Fetch the CAPTCHA image
2. Preprocess it for OCR
3. Extract text using Tesseract
4. Submit the solution
5. Display execution results and total time

---

## 💜 **Support**

If this project is useful:
- ⭐ **Star the repository**
- 🔁 **Share it with others**
- 🗨️ **Leave feedback or suggestions**

Your support helps maintain and improve open-source projects.
