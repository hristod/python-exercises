import requests
from bs4 import BeautifulSoup

def print_html_elements_of_type(url, element):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html)

    for element in soup.find_all(element):
        print(element)

def main():
    """Get all h2 titles from nytimes.com"""
    print_html_elements_of_type("http://nytimes.com", "h2")

main()
