import pandas as pd

url = "https://docs.google.com/spreadsheets/d/1kc262HZSMAWI6FVsh0zJwbB-ooYvzhCHaHcNUiA0_hY/export?format=csv&id=1kc262HZSMAWI6FVsh0zJwbB-ooYvzhCHaHcNUiA0_hY&gid=1158069878"
df = pd.read_csv(url, header=1)

# 必要なカラムのみ残す
df = df[["Model", "Lab", "Parameters \n(B)", "Announced\n▼", "Public?"]]
# カラム名を変更
df.columns = ["Model", "Lab", "Parameters(B)", "Announced", "Public?"]

# "Public?" が NaN の行を削除
df = df.dropna(subset=["Public?"]) 

# Announced が TBA の行を削除
df = df[df["Announced"] != "TBA"]
# Announced の日付を YYYY/MM/DD に変換
df["Announced"] = pd.to_datetime(df["Announced"], format='%b/%Y').dt.strftime('%Y/%m/%d')

# 2020-05-01 より前のデータを削除
df = df[df["Announced"] >= "2020/05/01"]

# Public? が 🟢 と一致する行の Type を EN-available に、そうでない場合は EN-unavailable に
df["Type"] = df["Public?"].apply(lambda x: "EN-available" if x == "🟢" else "EN-unavailable")

# Type が EN-available の行を先に表示。その中で、新しいものが上に来るようにソート
df = df.sort_values(by=["Type", "Announced"], ascending=[True, False])

# Model,Lab,Parameters(B),Announced,Type のみ残す
df = df[["Model", "Lab", "Parameters(B)", "Announced", "Type"]]

print(df)

# データを出力
df.to_csv("parameter_size_overview.csv", index=False)
