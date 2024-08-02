import requests
from bs4 import BeautifulSoup


class URLScraper:
    pass


class ShopScraper:
    def __init__(self, url):
        self.url = url
        self.table_soup = self.create_table_soup()
        self.contents = self.extract_content()

    def create_table_soup(self):
        page = requests.get(self.url).text
        soup = BeautifulSoup(page, "html.parser")
        table = soup.find("div", class_="flextable")
        return table

    @staticmethod
    def contains_checkmark(value):
        return "✔" in value

    @staticmethod
    def clean_weight(weight_text):
        weight_text = weight_text.replace("Weight:", "").strip()
        if weight_text == "—" or not weight_text:
            return "NULL"
        weight_text = weight_text.replace("lb.", "").strip()
        weight_text = weight_text.replace("¼", "0.25").replace("½", "0.5").strip()

        weight_list = list(filter(None, weight_text.split(" ")))
        weight_value = sum(map(float, weight_list))

        transformation_lb_to_kg = float(round(weight_value * 0.45359237, 2))

        return transformation_lb_to_kg

    @staticmethod
    def clean_price(price_text):
        price_text = price_text.replace("Cost:", "").strip()
        if "cp" in price_text:
            price_text = price_text.replace("cp", "").strip()
            price_text = int(price_text) / 100
        elif "sp" in price_text:
            price_text = price_text.replace("sp", "").strip()
            price_text = int(price_text) / 10
        elif "gp" in price_text:
            price_text = price_text.replace("gp", "").strip()
            price_text = float(price_text)
        else:
            price_text = "Error on the price"
        return price_text

    def extract_content(self):
        shop_name = self.url.split("/")[-1]
        current_category = None
        current_sub_category = None
        default_sub_category = "default"

        results = []

        divs = self.table_soup.find_all("div", recursive=False)

        for div in divs:
            if "rowCat" in div.get("class", []):
                current_category = div.get_text(strip=True)

            elif "rowSec" in div.get("class", []):
                current_sub_category = div.get_text(strip=True)

            elif "flexrow" in div.get("class", []) and "contentrow" in div.get("class", []):
                item_name = div.find("div", class_="col1").get_text(strip=True)
                price_base = self.clean_price(div.find("div", class_="col2").get_text(strip=True))
                weight = self.clean_weight(div.find("div", class_="col5").get_text(strip=True))

                col6 = div.find("div", class_="col6")
                limited_stock = self.contains_checkmark(col6.get_text(strip=True)) if col6 else False

                col7 = div.find("div", class_="col7")
                rural = self.contains_checkmark(col7.get_text(strip=True)) if col7 else False

                col8 = div.find("div", class_="col8")
                urban = self.contains_checkmark(col8.get_text(strip=True)) if col8 else False

                description_div = div.find_next_sibling("div")

                description = "NULL"
                if description_div:
                    coldesc_div = description_div.find("div", class_="coldesc")
                    if coldesc_div:
                        description = "".join([str(t).strip() for t in coldesc_div.children if isinstance(t, str)])

                sub_category = current_sub_category if div.find("div", class_="dmtabind") else default_sub_category

                results.append({
                    "shop": shop_name,
                    "category": current_category,
                    "sub_category": sub_category,
                    "item_name": item_name,
                    "price_base": price_base,
                    "weight": weight,
                    "limited_stock": limited_stock,
                    "rural": rural,
                    "urban": urban,
                    "description": description
                })

        return results


def main():
    scraper = ShopScraper("https://www.thievesguild.cc/shops/shop-inntavern")
    print(scraper.contents)
    # for result in results:
    #     print("\n")
    #     print(result.content)


if __name__ == "__main__":
    main()
