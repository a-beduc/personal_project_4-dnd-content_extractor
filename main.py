from src.Shop import Shop
from src.CSVManager import CSVLoader


def main():
    url = "https://www.thievesguild.cc/shops/shop-inntavern"
    shop = Shop(url)
    shop.init_shop()
    csv_loader = CSVLoader(shop)
    print(csv_loader.list_of_items)
    csv_loader.load_shop()


if __name__ == '__main__':
    main()
