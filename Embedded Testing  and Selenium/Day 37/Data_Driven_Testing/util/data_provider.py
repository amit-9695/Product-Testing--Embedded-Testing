from util.csv_util import CSVUtil

class DataProvider:
    
    @staticmethod
    def get_data_from_csv(file_path):
        return CSVUtil.read_data(file_path)