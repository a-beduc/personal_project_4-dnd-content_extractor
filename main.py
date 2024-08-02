from src.Shop import Shop
from src.CSVLoader import CSVShopLoader, CSVItemLoader
from src.ItemManager import ItemManager
import os


def main():
    # directory_path = os.path.join("csv-extracted")
    # item_manager = ItemManager(directory_path)
    # csv_loader = CSVItemLoader(item_manager)
    # csv_loader.load_items()

    list_url = ["https://www.thievesguild.cc/shops/shop-adventurer",
                "https://www.thievesguild.cc/shops/shop-potion",
                "https://www.thievesguild.cc/shops/shop-blacksmith",
                "https://www.thievesguild.cc/shops/shop-bookstore",
                "https://www.thievesguild.cc/shops/shop-bowyer",
                "https://www.thievesguild.cc/shops/shop-general",
                "https://www.thievesguild.cc/shops/shop-inntavern",
                "https://www.thievesguild.cc/shops/shop-jeweler",
                "https://www.thievesguild.cc/shops/shop-leather",
                "https://www.thievesguild.cc/shops/shop-arcane",
                "https://www.thievesguild.cc/shops/shop-musicgames",
                "https://www.thievesguild.cc/shops/shop-shady",
                "https://www.thievesguild.cc/shops/shop-tailor",
                "https://www.thievesguild.cc/shops/shop-temple",
                "https://www.thievesguild.cc/shops/shop-vendor"]
    for url in list_url:
        shop = Shop(init_url=url)
        csv_loader = CSVShopLoader(shop)
        print(csv_loader.list_of_items)
        csv_loader.load_shop()

    url = "https://www.thievesguild.cc/equipment/"
    shop = Shop(init_url=url)
    csv_loader = CSVShopLoader(shop)
    print(csv_loader.list_of_items)
    csv_loader.load_shop()


if __name__ == '__main__':
    main()
