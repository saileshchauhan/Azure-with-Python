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
sys.path.append('D:\AzureWithPython')
import logconfig
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

    def create_table(self):
        '''
        Description:
            Method executes query for creating table in Azure database after connecting with database.
        Parameters:
            Object of class to get attribute connection.
        Returns:
            None.
        '''
        crsr=self.db.cursor()
        query=('CREATE TABLE employee(emp_id INT PRIMARY KEY,name VARCHAR(150) NOT NULL,department VARCHAR(150) not null)')
        crsr.execute(query)
        logging.info('Table created')

    def insert_values(self):
        '''
        Description:
            Method executes query for inserting record in table in Azure database after connecting with database.
        Parameters:
            Object of class to get attribute connection.
        Returns:
            None.
        '''
        crsr=self.db.cursor()
        query=('CREATE TABLE employee(emp_id INT PRIMARY KEY,name VARCHAR(150) NOT NULL,department VARCHAR(150) not null)')
        query='INSERT INTO employee(emp_id,name,department) VALUES (?,?,?)'
        records=[(3,'Hardy','OR'),(4,'Sandra','HR')]
        crsr.executemany(query,records)
        crsr.commit()
        logging.info('Record inserted')

    def retrieve_rows(self):
        '''
        Description:
            Method executes query for retrieving record in table in Azure database after connecting with database.
        Parameters:
            Object of class to get attribute connection.
        Returns:
            None.
        '''
        crsr=self.db.cursor()
        query='SELECT * FROM employee'
        rows=crsr.execute(query)
        for row in rows:
            logging.info(row)
        logging.info('record retrieved')
    
    def update_record(self):
        '''
        Description:
            Method executes query for updating record in table in Azure database after connecting with database.
        Parameters:
            Object of class to get attribute connection.
        Returns:
            None.
        '''
        crsr=self.db.cursor()
        queryAlter='ALTER TABLE employee ADD gender VARCHAR(10) null'
        queryUpdate=('UPDATE employee SET gender=M WHERE emp_id in (2)')
        crsr.execute(queryAlter)
        crsr.commit()
        crsr.execute(queryUpdate)
        crsr.commit()
    
    def delete_record(self):
        '''
        Description:
            Method executes query for deleting record in table in Azure database after connecting with database.
        Parameters:
            Object of class to get attribute connection.
        Returns:
            None.
        '''
        crsr=self.db.cursor()
        queryDelete='DELETE FROM dbo.employee WHERE emp_id=1'
        crsr.execute(queryDelete)
        crsr.commit()

def main():
    '''
    Description:
        This is main method for executing method of class AzureSQL.
    Parameters:
        None.
    Returns:
        None.
    '''
    obj=AzureSQL()
    obj.create_table()
    obj.insert_values()
    #obj.update_record()
    obj.delete_record()
    obj.retrieve_rows()
    obj.db.close()

if __name__=='__main__':
    main()