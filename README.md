# CodeAlpha Webpage Title Scraper

## Description
This project is a simple Python application that extracts the title of a webpage and saves it to a text file. It uses the Requests library to fetch webpage content and BeautifulSoup to parse the HTML.

## Features
- Accepts a website URL from the user
- Connects to the webpage
- Extracts the webpage title
- Displays the title on the screen
- Saves the title to a text file
- Handles invalid URLs and connection errors

## Technologies Used
- Python 3
- Requests
- BeautifulSoup (bs4)

## How to Run

1. Install the required libraries:
   ```bash
   python -m pip install requests beautifulsoup4
   ```

2. Run the program:
   ```bash
   python webpage_title_scraper.py
   ```

3. Enter a valid website URL when prompted.

## Example

**Input**
```
https://www.python.org
```

**Output**
```
==================================================
      WEBPAGE TITLE SCRAPER
==================================================

Website Title:
Welcome to Python.org

The webpage title has been saved successfully.
```

## Output File
The extracted title is saved in:

```
webpage_title.txt
```

## Project Structure
```
CodeAlpha_Webpage_Title_Scraper
│── webpage_title_scraper.py
│── webpage_title.txt
│── README.md
```

## Author
**Bhavya Chauhan**

**Python Programming Internship – CodeAlpha**
