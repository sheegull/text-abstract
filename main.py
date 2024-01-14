import requests
from bs4 import BeautifulSoup


def generate_urls():
  base_url = "https://www.sony.com/ja/SonyInfo/CorporateInfo/History/SonyHistory"
  urls = []

  # URLを生成①
  for i in range(1, 17): # 1-16ページまで
    urls.append(f"{base_url}/1-{str(i).zfill(2)}.html")

  # URLを生成②
  for i in range(1, 26): # 1-25ページまで
    urls.append(f"{base_url}/2-{str(i).zfill(2)}.html")

  return urls


def extract_text_from_url(url):
  try:
    response = requests.get(url)
    response.raise_for_status() # Will raise an error for bad status codes
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text()
  except requests.HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
  except Exception as err:
    print(f"An error occurred: {err}")


# URLリストを生成
page_urls = generate_urls()


# テキストを抽出してファイルに書き込み
with open("/Users/shee/Documents/dev_data/sony_history.txt", 'w', encoding='utf-8') as file:
  for page_url in page_urls:
    print(f"Extracting {page_url}")
    page_text = extract_text_from_url(page_url)
    if page_text:
      file.write(page_text + '\n\n')


print('Extraction complete! The file sony_history.txt has been saved.')
