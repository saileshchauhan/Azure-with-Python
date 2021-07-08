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