import csv
import datetime as dt
from pathlib import Path

BASE_DIR = Path('scrapy_pasrser_pep').parent
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:

    def __init__(self):
        self.total = 0
        self.count_status = {}
        self.results = [('Статус', 'Количество')]

    def open_spider(self, spider):
        pass

    def process_item(self, item, spider):
        status = item['status']
        if status not in self.count_status:
            self.count_status[status] = 0
        self.count_status[status] += 1
        self.total += 1
        return item

    def close_spider(self, spider):
        for item in self.count_status.items():
            self.results.append(item)
        self.results.append(('Total', self.total))
        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(self.results)
