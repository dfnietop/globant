import pandas as pd
from pandas import DataFrame

from src.globant.global_sql.global_etl import GlobalEtl
from src.globant.global_utils import database


class DepartmentFacade:

    def __init__(self, db: database, schema: str):
        self.database = db
        self.schema = schema
        self.__global_etl = GlobalEtl(self.database, self.schema)

    def __insertData(self, list: list) -> None:
        self.__global_etl.insert(list)

    def __searchDepartment(self, id: int = None, deparment: str = None) -> DataFrame:
        df = pd.DataFrame()
        return df

    def insert_department(self, list: list):
        self.__insertData(list)
