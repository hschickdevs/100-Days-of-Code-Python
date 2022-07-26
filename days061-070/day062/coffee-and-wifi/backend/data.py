import csv


class CafeDatabase:
    @staticmethod
    def load():
        with open('cafe-data.csv', newline='') as csv_file:
            return [row for row in csv.reader(csv_file, delimiter=',')]

    @staticmethod
    def update(cafe_data: list[list]):
        with open('cafe-data.csv', 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(cafe_data)