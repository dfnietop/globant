import pandas as pd
from pandas import DataFrame

from src.globant.global_sql.global_etl import GlobalEtl
from src.globant.global_utils import database, sql


class EmployedFacade:

    def __init__(self, db: database, schema: str = None):
        self.database = db
        self.schema = schema
        self.__global_etl = GlobalEtl(self.database, self.schema)

    def __insertData(self, list: list) -> None:
        self.__global_etl.insert(list)

    def search_group(self, year: int) -> DataFrame:
        #query = sql.group_q_numbers_employess
        # df = self.__global_etl.searchGroup(query, year  )
        df = self.__global_etl.searchGroup(year)
        return df

    def search_total(self, year: int) -> DataFrame:
        query = sql.group_q_numbers_employess
        df = self.__global_etl.searchTotal(year)
        return df

    def insert_employe(self, list: list):
        self.__insertData(list)
