import csv
import os
from src.Shop import Shop  # It's just for testing, so it may be removed later
from src.ItemManager import ItemManager


class CSVShopLoader:
    def __init__(self, shop):
        self.shop = shop
        self.csv_path = self.create_csv_directory()
        self.csv_name = f"{self.shop.shop_name}.csv"
        self.list_of_items = []
        self.extract_list_of_items()

    @staticmethod
    def create_csv_directory():
        category_dir = os.path.join("csv-extracted")
        os.makedirs(category_dir, exist_ok=True)
        return category_dir

    def extract_list_of_items(self):
        for item in self.shop.stock.items():
            self.list_of_items.append(item)

    def load_shop(self):
        csv_path = os.path.join(self.csv_path, self.csv_name)
        headers = vars(self.list_of_items[0][1])
        with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers.keys())
            csv_writer.writeheader()

            for item in self.list_of_items:
                dictionary_of_item = vars(item[1])
                csv_writer.writerow(dictionary_of_item)


class CSVItemLoader:
    def __init__(self, item_manager):
        self.item_manager = item_manager
        self.csv_path = self.create_csv_directory()
        self.csv_name = "items.csv"
        self.list_of_items = []

    @staticmethod
    def create_csv_directory():
        category_dir = os.path.join("csv-work")
        os.makedirs(category_dir, exist_ok=True)
        return category_dir

    def load_items(self):
        csv_path = os.path.join(self.csv_path, self.csv_name)
        first_key = next(iter(self.item_manager.stock_of_item))
        headers = self.item_manager.stock_of_item[first_key].keys()

        with open(csv_path, "w", newline="", encoding="utf-8") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
            csv_writer.writeheader()

            for item_name, item_value in self.item_manager.stock_of_item.items():
                csv_writer.writerow(item_value)


def main():
    url = "https://www.thievesguild.cc/shops/shop-inntavern"
    shop = Shop(init_url=url)
    shop.init_shop_from_url()
    csv_loader = CSVShopLoader(shop)
    print(csv_loader.list_of_items)
    csv_loader.load_shop()


if __name__ == '__main__':
    main()
