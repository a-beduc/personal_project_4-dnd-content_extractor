from src.CSVExtractor import CSVExtractor
from src.ShopScraper import ShopScraper
from src.Item import Item
import os


class Shop:
    def __init__(self, init_url=None, init_csv_file_path=None):
        self.stock = {}
        if init_url is not None:
            self.url = init_url
            self.shop_name = init_url.split("/")[-1]
            self.scraper = ShopScraper(init_url)
            self.init_shop_from_url()
        if init_csv_file_path is not None:
            self.csv_file_path = init_csv_file_path
            self.shop_name = init_csv_file_path.split(".")[-2].split("\\")[-1]
            self.csv_extractor = CSVExtractor(init_csv_file_path)
            self.init_shop_from_csv()

    def init_shop_from_url(self):
        i = 0
        for item in self.scraper.contents:
            current_item = Item()
            current_item.id = i + 1
            current_item.shop = item["shop"]
            current_item.category = item["category"]
            current_item.sub_category = item["sub_category"]
            current_item.item_name = item["item_name"]
            current_item.price_base = item["price_base"]
            current_item.weight = item["weight"]
            current_item.limited_stock = item["limited_stock"]
            current_item.rural = item["rural"]
            current_item.urban = item["urban"]
            current_item.description = item["description"]

            self.stock[current_item.id] = current_item
            i += 1

    def init_shop_from_csv(self):
        i = 0
        for item in self.csv_extractor.dict_shop:
            current_item = Item()
            current_item.id = i + 1
            current_item.shop = item["shop"]
            current_item.category = item["category"]
            current_item.sub_category = item["sub_category"]
            current_item.item_name = item["item_name"]
            current_item.price_base = item["price_base"]
            current_item.weight = item["weight"]
            current_item.limited_stock = item["limited_stock"]
            current_item.rural = item["rural"]
            current_item.urban = item["urban"]
            current_item.description = item["description"]

            self.stock[current_item.id] = current_item
            i += 1


def main():
    # url = "https://www.thievesguild.cc/shops/shop-inntavern"
    # shop = Shop(init_url=url)
    # shop.init_shop_from_url()
    # print(shop.shop_name)
    # print(shop.stock)
    # print(shop.stock[90])
    # print(shop.stock[90].id)
    # print(shop.stock[90].shop)
    # print(shop.stock[90].category)
    # print(shop.stock[90].sub_category)
    # print(shop.stock[90].item_name)
    # print(shop.stock[90].price_base)
    # print(shop.stock[90].weight)
    # print(shop.stock[90].limited_stock)
    # print(shop.stock[90].rural)
    # print(shop.stock[90].urban)
    # print(shop.stock[90].description)

    path = os.path.join("..", "csv-extracted", "shop-inntavern.csv")
    print(path)
    shop2 = Shop(init_csv_file_path=path)
    shop2.init_shop_from_csv()
    print(shop2.shop_name)
    print(shop2.stock)
    print(shop2.stock[90])
    print(shop2.stock[90].id)
    print(shop2.stock[90].shop)
    print(shop2.stock[90].category)
    print(shop2.stock[90].sub_category)
    print(shop2.stock[90].item_name)
    print(shop2.stock[90].price_base)
    print(shop2.stock[90].weight)
    print(shop2.stock[90].limited_stock)
    print(shop2.stock[90].rural)
    print(shop2.stock[90].urban)
    print(shop2.stock[90].description)


if __name__ == '__main__':
    main()
