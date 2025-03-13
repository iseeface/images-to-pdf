# Image to PDF Converter

## Description
Image to PDF Converter is a simple and user-friendly desktop application that allows users to convert multiple images into a single PDF file. The application supports drag-and-drop functionality for easy file selection and provides an intuitive user interface.

## Features
- Drag and drop images to add them to the list
- Supports multiple image formats (PNG, JPG, JPEG, GIF, BMP, WebP, ICO)
- Remove selected images before conversion
- Move images up or down to reorder before conversion
- Choose between Portrait and Landscape orientation
- Select PDF quality (High, Medium, Low) to control file size
- Progress bar to show conversion status
- Multi-threaded conversion for a responsive UI

## Installation
### Prerequisites
- Python 3.10 or later
- Required dependencies:
  ```sh
  pip install pillow tkinterdnd2 pyinstaller
  ```

## How to Run
1. Clone this repository or download the script.
2. Run the script using Python:
   ```sh
   python ImagesToPDF.py
   ```

## How to Build as an Executable (.exe)
To create an executable version of this application:
1. Install PyInstaller:
   ```sh
   pip install pyinstaller
   ```
2. Run the following command to generate an executable:
   ```sh
   pyinstaller --onefile --windowed --icon=your_icon.ico ImagesToPDF.py
   ```
3. The `.exe` file will be available in the `dist/` directory.

## Download Executable Version
If you prefer to use the application without installing Python, you can download the precompiled `.exe` file from the [Releases](https://github.com/iseeface/images-to-pdf/releases) section.

## Usage
1. Open the application.
2. Drag and drop images or use the **Add Images** button.
3. (Optional) Remove unwanted images using the **Remove Selected Images** button.
4. (Optional) Reorder images using the **Move Up** and **Move Down** buttons.
5. Choose the orientation (Portrait or Landscape).
6. Select the desired PDF quality (High, Medium, Low).
7. Click **Convert to PDF** and select the output file location.
8. The progress bar will update as the conversion happens.

## License
This project is open-source and available under the MIT License.
