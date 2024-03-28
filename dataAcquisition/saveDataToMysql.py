import akshare as ak
import pandas as pd
from sqlalchemy import create_engine

# ##############################################打印版本号
print(f'pandas version: {pd.__version__}')
print(f'akshare version: {ak.__version__}')


class DataToMysql(object):
    def __init__(self):
        pass

    def connect_engine(self, database_name='astocks'):
        # 连接到 MySQL 数据库
        self.engine = create_engine('mysql+pymysql://root:root@localhost:3306/' + database_name)

    def close_engine(self):
        # 关闭数据库连接
        self.engine.dispose()

    def save_stock_simple_info(self, table_name='stock_code_name'):
        # 沪深京 A 股简要数据 代码 名称
        all_stock_info = ak.stock_info_a_code_name()

        # 将 DataFrame 数据存入 MySQL 数据库的表中
        # 如果表已存在，数据将被追加到该表中；如果表不存在，将会创建该表并存入数据
        all_stock_info.to_sql(table_name, con=self.engine, if_exists='replace', index=True)

    def save_history_stock_info(self):
        pass

    def save_today_stock_info(self,table_name='stock_trade_data_day'):
        # 描述: 东方财富网-沪深京 A 股-实时行情数据
        stock_zh_a_spot_em_df = ak.stock_zh_a_spot_em()
        stock_zh_a_spot_em_df.to_sql(table_name, con=self.engine, if_exists='append', index=True)

def test():
    data_to_mysql = DataToMysql()
    data_to_mysql.connect_engine()
    data_to_mysql.save_stock_simple_info()
    data_to_mysql.connect_engine()


if __name__ == '__main__':
    test()
