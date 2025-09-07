from selenium.webdriver.common.by import By
import logging
class WebTable:
    def __init__(self,table_element):
        self.table=table_element
        logging.basicConfig(level=logging.INFO)
        self.logger=logging.getLogger(__name__)
    
    def get_row_count(self,include_header=True):
        "Returns the number of rows in the table"
        rows=self.table.find_elements(By.TAG_NAME,"tr")
        return len(rows) if include_header else len(rows)-1
    
    def get_column_count(self):
        """  Returns the number of columns in the first row."""
        first_row=self.table.find_element(By.TAG_NAME,"tr")
        columns=first_row.find_elements(By.TAG_NAME,"th") or first_row.find_elements(By.TAG_NAME,"td")
        return len(columns)
    
    
    def get_cell_data(self,row_index,col_index):
        """ Returns the data in the specified cell.
        :param row_index: Row index(1-based,includes header row)
        :param col_index: Column index(1-based)
        :return: Text content of the cell
        """
        try:
            row=self.table.find_elements(By.TAG_NAME,"tr")[row_index-1]
            cell=row.find_elements(By.TAG_NAME,"td")[col_index-1]
            return cell.text
        except IndexError:
            self.logger.error(f"Invalid row {row_index} or coloum{col_index}")
            return None
    
    def get_all_table_data(self):
        """ Returns all table data as a list of dictionariies."""
        rows=self.table.find_elements(By.TAG_NAME,"tr")
        headers=[header.text.strip() for header in rows[0].find_elements(By.TAG_NAME,"th")]
        print("Headers= ",headers)
        table_data=[]
        for row in rows[1:]: # skip header row
            cells=row.find_elements(By.TAG_NAME,"td")
            row_data={ headers[i]:cells[i].text.strip() for i in range(len(cells))  }
            print(row_data)
            table_data.append(row_data)
        return table_data