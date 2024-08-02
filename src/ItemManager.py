import os
from src.Shop import Shop


class ItemManager:
    def __init__(self, directory_path):
        self.directory_path = directory_path
        self.list_of_path = self.get_list_of_path()
        self.list_of_shop = self.create_shops_from_csvs()
        self.stock_of_item = self.get_dict_of_items()

    def get_list_of_path(self):
        list_of_path = []
        for filename in os.listdir(self.directory_path):
            if filename.endswith('equipement.csv'):
                file_path = os.path.join(self.directory_path, filename)
                list_of_path.append(file_path)
        return list_of_path

    def create_shops_from_csvs(self):
        list_of_shop = []
        for filename in self.list_of_path:
            shop = Shop(init_url=None, init_csv_file_path=filename)
            list_of_shop.append(shop)
        return list_of_shop

    def get_dict_of_items(self):
        dict_of_item = {}
        i = 0
        for shop in self.list_of_shop:
            for item_id, item in shop.stock.items():
                if item.item_name not in dict_of_item:
                    i += 1
                    dict_of_item[item.item_name] = {"id": i,
                                                    "item_name": item.item_name,
                                                    "description": item.description,
                                                    "category": item.category,
                                                    "sub-category": item.sub_category,
                                                    "price": item.price_base,
                                                    "weight": item.weight}
        return dict_of_item


def main():
    pass


if __name__ == '__main__':
    main()
