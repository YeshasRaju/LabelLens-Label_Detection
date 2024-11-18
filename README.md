## **LabelLens - Label Detection Using Machine Learning** 📷

![Python](https://img.shields.io/badge/Python-3.12.2-blue?style=for-the-badge)  
![Libraries](https://img.shields.io/badge/Libraries-torch%20%7C%20numpy%20%7C%20opencv--python%20%7C%20customtkinter%20%7C%20Pillow-blue?style=for-the-badge)   
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20MacOS-green?style=for-the-badge)
---
## 🖼️ **Project Demo**  
👉 Screenshots of the GUI application are provided below:

![App Screenshot 1](images/pass_run.png)  

![App Screenshot 2](images/fail_run.png) 
---
## Features 🚀

- **Real-time Label Detection:** Detects product labels in real-time using a webcam. 

- **Customizable Label Sets:** Choose between different label sets (e.g., Samsung, OnePlus, or all available labels) for inspection.

- **Pass/Fail Detection:** Displays whether all labels are correctly detected with "PASS" or "FAIL" status.

- **Dynamic GUI:** Built with customtkinter for an interactive and visually appealing interface.

- **Machine Learning Integration:** Utilizes YOLOv5 for accurate and efficient object detection.

---

## Usage 📦

1. Run the `app.py` script to start the application:
    ```bash
    python app.py
    ```

2. Select a label set (All, Samsung, or OnePlus) using the dropdown in the GUI.

3. The webcam feed will show in real-time. The application will automatically detect and label items according to the selected set.

4. The status will update to "PASS" if all required labels are detected; otherwise, it will show "FAIL".

5. Press **'P'** to pause and resume the webcam feed.

6. Click **EXIT** to close the application.

---

## Files 📂

- **app.py:** Main Python script to run the application.

- **requirements.txt:** Contains all necessary libraries to run the project.

- **weights/last.pt:** Pre-trained YOLOv5 model weights (ensure this file is present in the `weights/` directory).

- **images:** Folder containing images for the background, check and cross icons, exit button, etc.

---

## Dependencies 📚

- `requests>=2.28.1` - For HTTP requests.
- `customtkinter>=5.0.1` - For building the GUI with tkinter.
- `Pillow>=9.3.0` - For image manipulation.
- `opencv-python>=4.7.0.72` - For webcam and image processing.
- `torch>=2.0.0` - For running the YOLOv5 model.
- `numpy>=1.23.5` - For array and matrix operations.
---
## Contributing 🤝

- Feel free to fork the repository, make changes, and submit a pull request. Contributions are welcome to enhance label detection accuracy, improve the UI, or add more label sets.
---
## About the Developers 👨‍💻👩‍💻  

- This project was collaboratively developed by **Tharunkrishna M** and teammate **Yeshas Raju**, leveraging their expertise in Python, machine learning, and GUI development to create an innovative label detection application
---