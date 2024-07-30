from src.ShopScraper import ShopScraper
from src.Item import Item


class Shop:
    def __init__(self, url):
        self.url = url
        self.shop_name = url.split("/")[-1]
        self.scraper = ShopScraper(url)
        self.stock = {}

    def init_shop(self):
        i = 0
        for item in self.scraper.contents:
            current_item = Item()
            current_item.id = i+1
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
    url = "https://www.thievesguild.cc/shops/shop-inntavern"
    shop = Shop(url)
    shop.init_shop()
    print(shop.shop_name)
    print(shop.stock)
    print(shop.stock[1])
    print(shop.stock[1].id)
    print(shop.stock[1].shop)
    print(shop.stock[1].category)
    print(shop.stock[1].sub_category)
    print(shop.stock[1].item_name)
    print(shop.stock[1].price_base)
    print(shop.stock[1].weight)
    print(shop.stock[1].limited_stock)
    print(shop.stock[1].rural)
    print(shop.stock[1].urban)
    print(shop.stock[1].description)


if __name__ == '__main__':
    main()
