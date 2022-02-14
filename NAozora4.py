import pandas as pd
import csv
pd.options.display.max_rows=None
pd.options.display.width=None
names=['人物ID',	'著者名',	'作品ID',	'作品名',	'仮名遣い種別',	'翻訳者名等',	'入力者名',	'校正者名',	'状態',	'状態の開始日',	'底本名',	'出版社名',	'入力に使用した版',	'校正に使用した版']
df=pd.read_csv('Double_list_person_all_utf8.csv',names=names,header=0)
#print(pd.options.display.max_rows)#デフォルトは60
#print(df[df.duplicated(subset=['著者名','作品名'],keep=False)])
#
Non_Double=df.drop_duplicates(subset=['著者名','作品名'])
writefile='Non＿Double_list_person_all_utf8.csv'

Non_Double.to_csv('Non＿Double_list_person_all_utf8.csv')
#Non_Doubleデータフレームの行数を取得
print(len(Non_Double))
