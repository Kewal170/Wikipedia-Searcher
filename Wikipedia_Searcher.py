import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(user_input):
    url = "https://en.wikipedia.org/wiki/"
    result = url + user_input

    try:
        page = requests.get(result)
        page.raise_for_status()  # Raise an HTTPError for bad requests
    except requests.RequestException as e:
        print(f"Error: Unable to retrieve information for {user_input}. {e}")
        return

    soup = BeautifulSoup(page.text, 'html.parser')
    paragraphs = soup.find_all('p')
    content = [p.text.strip() for p in paragraphs[1:]]

    with open(f"{user_input}_info.txt", 'a', encoding="utf-8") as file:
        file.write("\n".join(content))

def main():
    user_input = input("Enter what you want to get information on: ").replace(" ", "_")
    scrape_wikipedia(user_input)

if __name__ == "__main__":
    main()
