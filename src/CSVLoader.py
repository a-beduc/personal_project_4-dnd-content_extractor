import csv
from src.Shop import Shop  # It's just for testing, so it may be removed later
import os


class CSVLoader:
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
        with open(csv_path, "w", newline="") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers.keys())
            csv_writer.writeheader()

            for item in self.list_of_items:
                dictionary_of_item = vars(item[1])
                csv_writer.writerow(dictionary_of_item)


def main():
    url = "https://www.thievesguild.cc/shops/shop-inntavern"
    shop = Shop(init_url=url)
    shop.init_shop_from_url()
    csv_loader = CSVLoader(shop)
    print(csv_loader.list_of_items)
    csv_loader.load_shop()


if __name__ == '__main__':
    main()
