'''
@Author: Sailesh Chauhan
@Date: 08-07-2021
@Last Modified time: 08-07-2021
@Title : This Script provide method for CRUD operation in SQL Database table using
         methods of class AzureSQL
'''

import pyodbc
from decouple import config
import sys
sys.path.append('D:\AzureWithPython\logConfig.py')
import logConfig
import logging

class AzureSQL:
    '''
    Functions:
        1.__init__(constructor)
        2.create_table()
        3.retrieve_rows()
        4.insert_values()
        5.update_record()
        6.delete_record()

    '''
    def __init__(self):
        self.db=pyodbc.connect(
            Driver=config('driver'),
            Server=config('server_name'),
            Database=config('database_name'),
            Uid=config('user_name'),
            Pwd=config('password'),
            Encrypt='yes',
            TrustServerCertificate='no',
            Connection_Timeout=30
            )