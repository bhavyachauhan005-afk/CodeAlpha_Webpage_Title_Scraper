import requests
from bs4 import BeautifulSoup

print("=" * 50)
print("      WEBPAGE TITLE SCRAPER")
print("=" * 50)

url = input("Enter the website URL: ").strip()

if not url.startswith("http://") and not url.startswith("https://"):
    url = "https://" + url

try:
    print("\nConnecting to the website...")

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    print("Website connected successfully.")

    soup = BeautifulSoup(response.text, "html.parser")

    if soup.title:
        title = soup.title.string.strip()
    else:
        title = "No title found on this webpage."

    print("\n" + "=" * 50)
    print("WEBSITE TITLE")
    print("=" * 50)
    print(title)

    filename = "webpage_title.txt"

    with open(filename, "w", encoding="utf-8") as file:
        file.write("WEBPAGE TITLE SCRAPER\n")
        file.write("=" * 50 + "\n\n")
        file.write(f"Website URL : {url}\n")
        file.write(f"Website Title : {title}\n")

    print("\nThe webpage title has been saved successfully.")
    print(f"File Name: {filename}")

except requests.exceptions.MissingSchema:
    print("\nInvalid URL format.")

except requests.exceptions.ConnectionError:
    print("\nUnable to connect to the website.")

except requests.exceptions.Timeout:
    print("\nRequest timed out.")

except requests.exceptions.HTTPError:
    print("\nThe webpage returned an HTTP error.")

except Exception as e:
    print("\nAn unexpected error occurred.")
    print(e)

print("\nThank you for using the Webpage Title Scraper!")