import requests
from bs4 import BeautifulSoup
import re


def get_website_info(url):
    # Make a GET request to the given URL
    response = requests.get(url)

    # Parse the HTML content of the response
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the <a> tags in the HTML
    links = soup.find_all("a")

    # Initialize empty lists for storing the social links, emails, and contact information
    social_links = []
    emails = []
    contact = []

    # Loop through the <a> tags and check each link for social links, emails, and contact information
    for link in links:
        href = link.get("href")
        text = link.get_text().strip()

        if href:
            # Check if the link is a social link
            if "facebook" in href or "linkedin" in href or "twitter" in href:
                social_links.append(href)

            # Check if the link is an email address
            if "mailto:" in href:
                emails.append(href.replace("mailto:", ""))

    # Look for the contact information in the HTML
    contact_info = soup.find_all(string=re.compile(
        "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"))

    # Extract the phone numbers from the contact information
    for info in contact_info:
        phone_number = re.findall(
            r"[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}", info)
        if phone_number:
            contact.append(phone_number[0])

    # Print the social links, emails, and contact information
    print("Social links:")
    for link in social_links:
        print(link)

    print("\nEmail/s:")
    for email in emails:
        print(email)

    print("\nContact:")
    for phone in contact:
        print(phone)


# Test the function with the example URL from the prompt
get_website_info("https://ful.io")
