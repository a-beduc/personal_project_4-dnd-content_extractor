import requests
from bs4 import BeautifulSoup

def contains_checkmark(value):
    return "✔" in value

def main():
    url = "https://www.thievesguild.cc/shops/shop-adventurer"
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    table = soup.find("div", class_="shoptable flextable")

    current_category = None
    current_sub_category = None
    default_sub_category = "default"

    results = []

    divs = table.find_all('div', recursive=False)

    for div in divs:
        if 'rowCat' in div.get('class', []):
            current_category = div.get_text(strip=True)

        elif 'rowSec' in div.get('class', []):
            current_sub_category = div.get_text(strip=True)

        elif 'flexrow' in div.get('class', []) and 'contentrow' in div.get('class', []):
            item_name = div.find('a').get_text(strip=True)
            price_base = div.find('div', class_='col2').get_text(strip=True).replace('Cost: ', '')
            weight = div.find('div', class_='col5').get_text(strip=True).replace('Weight: ', '')

            limited_stock = contains_checkmark(div.find('div', class_='col6').get_text(strip=True))
            rural = contains_checkmark(div.find('div', class_='col7').get_text(strip=True))
            urban = contains_checkmark(div.find('div', class_='col8').get_text(strip=True))

            description_div = div.find_next_sibling('div')

            description = ''
            if description_div:
                coldesc_div = description_div.find('div', class_='coldesc')
                if coldesc_div:
                    description = ''.join([str(t).strip() for t in coldesc_div.children if isinstance(t, str)])

            sub_category = current_sub_category if div.find('div', class_='dmtabind') else default_sub_category

            results.append({
                'category': current_category,
                'sub_category': sub_category,
                'item_name': item_name,
                'price_base': price_base,
                'weight': weight,
                'limited_stock': limited_stock,
                'rural': rural,
                'urban': urban,
                'description': description
            })

    for result in results:
        print("\n")
        print(result["category"])
        print(result["sub_category"])
        print(result["item_name"])
        print(result["rural"])
        print(result["urban"])
        print(result["description"])


if __name__ == '__main__':
    main()
