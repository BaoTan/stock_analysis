import os
import time
import warnings
from datetime import timedelta, datetime
import akshare as ak
import pandas as pd
import numpy as np

# ##############################################打印版本号
print(f'pandas version: {pd.__version__}')
print(f'akshare version: {ak.__version__}')

# ##############################################获取期货展期收益率
# get_roll_yield_bar_df = ak.get_roll_yield_bar(type_method="date",
#                                               var="RB",
#                                               start_day="20180618",
#                                               end_day="20180718")
# print(get_roll_yield_bar_df)

# ##############################################获取基金仓位
# 易方达蓝筹精选，005827；前海开源公共事业股票，005669
# years = ['2019', '2020', '2021']
# data = pd.DataFrame()
# for yr in years:
#     df_tmp = ak.fund_portfolio_hold_em(symbol="005827", date=yr)
#     data = data.append(df_tmp)

# data['季度'] = data['季度'].apply(lambda x: x[:6])
# data['季度'] = data['季度'].str.replace('年', 'Q')
# data['占净值比例'] = pd.to_numeric(data['占净值比例'])
# print(data)

# ##############################################获取沪深京A股分钟级历史股票数据
warnings.filterwarnings("ignore")
# 输出显示设置
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 输入参数
start_date = '20220101'
end_date = '20220810'
adj = "hfq"  # 复权类型：None未复权 qfq前复权 hfq后复权
period = "1"  # 周期可选：1, 5, 15, 30, 60 分钟的数据频率。"daily", "weekly", "monthly"


# 创建文件存储路径
def create_path():
    global path
    date_str = str(pd.to_datetime(start_date).date())  # 日期转换成字符串
    path = os.path.join(".", "all_stock_candle", "stock", date_str)
    # 保存数据
    if not os.path.exists(path):
        # os.mkdir(path)  # 可以建一级文件夹
        os.makedirs(path)  # 可以建多级文件夹
    file_name = ak_code + ".csv"
    return os.path.join(path, file_name)


# 利用东财实时行情数据接口获取所有股票代码接口
df = ak.stock_zh_a_spot_em()
# code_list = df[['序号', '代码', '名称']].values
code_list = df[['代码', '名称']].values
print(code_list)

for i in range(len(code_list)):
    ak_code = code_list[i][0]
    ak_name = code_list[i][1]

    try:
        # 利用东财历史行情数据接口获取股票数据
        df = ak.stock_zh_a_hist(symbol=ak_code, period=period, start_date=start_date, end_date=end_date, adjust=adj)
    except Exception as e:
        print(e)

    df['股票代码'] = ak_code
    df['股票名称'] = ak_name
    df.rename(columns={'日期': '交易日期', '开盘': '开盘价', '最高': '最高价', '最低': '最低价', '收盘': '收盘价', '成交量': '成交量'}, inplace=True)
    df = df[['交易日期', '股票代码', '股票名称', '开盘价', '收盘价', '最高价', '最低价', '成交量', '成交额', '涨跌幅', '换手率']]

    # 在股票代码前加上交易所简称
    df['股票代码'] = df['股票代码'].astype(str)
    df.loc[df['股票代码'].str.startswith('6'), '股票代码'] = "sh" + df['股票代码']
    df.loc[df['股票代码'].str.startswith('4') | df['股票代码'].str.startswith('8'), '股票代码'] = "bj" + df['股票代码']
    df.loc[df['股票代码'].str.startswith('3') | df['股票代码'].str.startswith('0'), '股票代码'] = "sz" + df['股票代码']

    # 排序去重
    df.sort_values(by=['交易日期'], ascending=True, inplace=True)
    df.drop_duplicates(subset=['股票代码', '交易日期'], keep='first', inplace=True)
    df.reset_index(drop=True, inplace=True)

    # 存储文件
    path = create_path()
    df.to_csv(path, index=False, mode='w', encoding='gbk')
    time.sleep(2)

    print(f"已下载到{i+1}支股票，股票代码为:{ak_code}，股票名称为:{ak_name}")
