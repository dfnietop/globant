import pandas as pd
from sqlalchemy.orm import Session
from sqlalchemy import text
from globant.global_core import schema, model
from globant.global_utils import database, config, sql


class GlobalEtl:
    def __init__(self, db: Session, schema: str):
        print('inicion etl')
        self.db = db
        self.schema = schema

    def insert(self, list: list):
        try:
            print(f'insertar:{self.schema}')
            number_of_chunks = int(len(list) / config.MAX_DATAFRAME_SIZE) + 1

            while number_of_chunks > 0:
                number_of_chunks = number_of_chunks - config.MAX_DATAFRAME_SIZE
                if self.schema == 'job':
                    mod = model.Job
                elif self.schema == 'department':
                    mod = model.Departemnt
                elif self.schema == 'hired_employees':
                    mod = model.HiredEmployees
                else:
                    raise

                self.db.bulk_insert_mappings(mod, list)
            self.db.commit()

        except Exception as e:
            raise e


    def searchGroup(self, parameter):
        try:
            print(f'select proccess ')
            return self.db.execute(text(sql.group_q_numbers_employess),[{"year":parameter}]).fetchall()
        except Exception as e:
            raise e

    def searchTotal(self, parameter):
        try:
            print(f'select proccess ')
            return self.db.execute(text(sql.total_numbers_employess_hired),[{"year":parameter}]).fetchall()
            return output
        except Exception as e:
            raise e
