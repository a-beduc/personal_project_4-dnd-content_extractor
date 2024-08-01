from src.Shop import Shop
from src.CSVLoader import CSVLoader


def main():
    url = "https://www.thievesguild.cc/shops/shop-adventurer"
    shop = Shop(init_url=url)
    shop.init_shop_from_url()
    csv_loader = CSVLoader(shop)
    print(csv_loader.list_of_items)
    csv_loader.load_shop()


if __name__ == '__main__':
    main()
