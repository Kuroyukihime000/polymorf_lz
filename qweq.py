import pandas as pd

class OperationResult:
    def __init__(self):
        self.data = pd.read_csv('var8.csv')
        self.df = self.data.copy() 

    def __pos__(self):
        value1 = self.df.shape[0] 
        self.df = self.df.drop_duplicates()
        value2 = self.df.shape[0] 
        deletion = value1 - value2
        print(f'В файле удалено дубликатов: {deletion}')

    def partition(self):
        dataframe1 = self.df[self.df['Результат операции'] == 'недостаточно средств']
        dataframe2 = self.df[self.df['Результат операции'] == 'успешно']   
        dataframe3 = self.df[self.df['Результат операции'] == 'неправильный ввод пин-кода']   
        
        dataframe1.to_csv('setfirst.csv', index = False)
        dataframe2.to_csv('setsecond.csv', index = False)
        dataframe3.to_csv('setthird.csv', index = False)

    def __del__(self):
        print('Удалено')
