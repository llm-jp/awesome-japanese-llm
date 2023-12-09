"""
パラメータサイズの推移を描画するスクリプト

CSVデータ作成に関するメモ
1. 日本語公開モデルに関しては、この記事の情報から作成
2. 日本語非公開モデルに関しては、プレスリリースから作成
3. 英語モデルに関しては、LifeArchitect.ai からデータを抽出。具体的には、
    a. Public? が緑色のものと、黄色・赤色のものでそれぞれフィルターをかける
    b. GPT-3 以前のモデルは落とす
    c. まだ非公開のモデルは落とす
    d. Announced の日付を YYYY/MM/DD に変換
    e. Model, Lab, Parameters, Announced の順にカラムを入れ替えてコピペ
"""

import japanize_matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd



BIGTECH_LIST = [
    "Microsoft",
    "OpenAI",
    "Google DeepMind",
    "Google",
    "DeepMind",
    "Meta AI",
]

df = pd.read_csv('parameter_size_overview.csv')

df["label"] = np.where(df["Model"].isna(), df["Lab"], df["Model"])
df["Announced"] = pd.to_datetime(df["Announced"], format='%Y/%m/%d')
df['Parameters(B)'] = pd.to_numeric(df['Parameters(B)'], errors='coerce')
df = df.dropna(subset=['Parameters(B)'])
# 日本語のモデルだけ描画したい場合
# df = df[df["Type"].str.startswith("JP")]
df = df.reset_index(drop=True)

colors = {
    "JP-available": "#EA3323", 
    "JP-unavailable": "#F1BE42",
    "EN-available": "#5383EC",
    "EN-unavailable": "#B8CDF7",
}

labels = {
    "JP-available": "Japanese (public)",
    "JP-unavailable": "Japanese (private)",
    "EN-available": "English (public)",
    "EN-unavailable": "English (private)",
}

fig, ax = plt.subplots(figsize=(10, 8))

ax.scatter(
    df[df["Type"] == "EN-unavailable"]["Announced"],
    df[df["Type"] == "EN-unavailable"]["Parameters(B)"],
    color=colors["EN-unavailable"],
    label=labels["EN-unavailable"],
    s=30
)

ax.scatter(
    df[df["Type"] == "EN-available"]["Announced"],
    df[df["Type"] == "EN-available"]["Parameters(B)"],
    color=colors["EN-available"],
    label=labels["EN-available"],
    s=30
)

ax.scatter(
    df[df["Type"] == "JP-unavailable"]["Announced"],
    df[df["Type"] == "JP-unavailable"]["Parameters(B)"],
    color=colors["JP-unavailable"],
    label=labels["JP-unavailable"],
    s=100
)

ax.scatter(
    df[df["Type"] == "JP-available"]["Announced"],
    df[df["Type"] == "JP-available"]["Parameters(B)"],
    color=colors["JP-available"],
    label=labels["JP-available"],
    s=100
)

for i in reversed(range(len(df))):
    if df["Type"][i].startswith("JP"):
        ax.text(
            df["Announced"][i],
            df["Parameters(B)"][i] * 1.2,
            df["label"][i],
            fontsize=10,
            verticalalignment='bottom',
            horizontalalignment='center'
        )
    if df["Type"][i].startswith("EN") and df["Lab"][i] in BIGTECH_LIST and df["Parameters(B)"][i] > 100:
        ax.text(
            df["Announced"][i],
            df["Parameters(B)"][i] * 1.2,
            f'{df["label"][i]}\n({df["Lab"][i]})',
            fontsize=8,
            color="grey",
            verticalalignment='bottom',
            horizontalalignment='center',
        )

for y in [0.1, 1, 10, 100, 1000]:
    ax.axhline(y=y, color='gray', linestyle='--', linewidth=0.5)


ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y年%m月')) 

ax.set_ylabel("パラメータ数（単位: billion）")
ax.set_yscale('log')
ax.set_ylim(0.09, 4000)


plt.xticks(rotation=45)
plt.subplots_adjust(left=0.075, right=0.975, bottom=0.1, top=0.975)
plt.legend()
plt.savefig("../parameter_size_overview.png", dpi=144)