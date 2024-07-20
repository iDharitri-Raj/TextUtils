
# TextUtils

TextUtils is a comprehensive web application built with Django that offers a suite of text manipulation utilities. Whether you need to remove punctuation, convert text to uppercase, count characters, or perform other text operations, TextUtils provides an intuitive interface to accomplish these tasks efficiently.

## Features

- **Remove Punctuation**: Strip all punctuation marks from the input text.
- **Convert to Uppercase**: Transform all characters in the input text to uppercase.
- **Count Characters**: Calculate the total number of characters in the input text.
- **Additional Utilities**: More text manipulation features to come.

## Installation

### Prerequisites

Ensure you have Python and pip installed on your system.

1. **Clone the repository:**

   ```bash
   git clone "https://github.com/iDharitri-Raj/TextUtils"
   ```

2. **Navigate to the project directory:**

   ```bash
   cd TextUtils
   ```

3. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv env
   source env/bin/activate   # On Windows use `env\Scripts\activate`
   ```

4. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply migrations to set up the database:**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

7. **Access the application:**

   Open your web browser and go to `http://127.0.0.1:8000/`.

## Usage

1. **Home Page**: Enter the text you want to manipulate in the text area.
2. **Select Options**: Choose the desired text operations (e.g., remove punctuation, convert to uppercase).
3. **Analyze Text**: Click the "Analyze" button to see the processed text and results.
