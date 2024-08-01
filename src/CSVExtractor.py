import os
import csv


class CSVExtractor:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.dict_shop = []
        self.csv_extractor()

    def csv_extractor(self):
        with open(self.csv_file_path, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter=',')
            for rows in csv_reader:
                self.dict_shop.append(rows)


def main():
    path = os.path.join("..", "csv", "shop-inntavern.csv")

    extract = CSVExtractor(path)

    extract.csv_extractor()
    print(extract.dict_shop)


if __name__ == '__main__':
    main()
