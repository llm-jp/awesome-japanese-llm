"""
パラメータサイズの推移を描画するスクリプト

CSVデータ作成に関するメモ
1. 日本語公開モデルに関しては、プレスリリースから作成
2. 英語モデルに関しては、LifeArchitect.ai からデータを抽出。具体的には、
    a. Public? が緑色のものと、黄色・赤色のものでそれぞれフィルターをかける
    b. GPT-3 以前のモデルは落とす
    c. まだ非公開のモデルは落とす
    d. Announced の日付を YYYY/MM/DD に変換
    e. Model, Lab, Parameters, Announced の順にカラムを入れ替えてコピペ
（なお、2.の操作は現在 parameter_size_overview_retrieve.py で自動化されている）
"""

import japanize_matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.ticker import FuncFormatter
import numpy as np
import pandas as pd



BIGTECH_LIST = [
    "Google DeepMind",  # Google
    "Google",  # Google
    "DeepMind",  # Google
    "Meta AI",  # Meta
    "Anthropic",  # Amazon
    "Microsoft",  # Microsoft
    "OpenAI",  # Microsoft,
    "Mistral AI",  # Microsoft
]

df_en = pd.read_csv('parameter_size_overview.csv')
df_ja = pd.read_csv('parameter_size_overview_ja.csv')

# 日本語モデルのデータを英語モデルのデータに結合
df = pd.concat([df_en, df_ja], ignore_index=True)

df["label"] = np.where(df["Model"].isna(), df["Lab"], df["Model"])
df["Announced"] = pd.to_datetime(df["Announced"], format='%Y/%m/%d')
df['Parameters(B)'] = pd.to_numeric(df['Parameters(B)'], errors='coerce')
df = df.dropna(subset=['Parameters(B)'])
# 日本語のモデルだけ描画したい場合
# df = df[df["Type"].str.startswith("JP")]
df = df.reset_index(drop=True)

# use universal colors
# https://www.jma.go.jp/jma/kishou/info/colorguide/HPColorGuide_202007.pdf
colors = {
    # "JP-available-API": "#B40068"
    "JP-available": "#FF2800", 
    "JP-available-CP": "#FF9900",
    "JP-unavailable": "#FFF500",
    "EN-available": "#0096FF",
    "EN-unavailable": "#B9EBFF",
}

labels = {
    # "JP-available-API": "Japanese (public, model weights closed)"
    "JP-available": "Japanese (public, built from scratch)",
    "JP-available-CP": "Japanese (public)",
    "JP-unavailable": "Japanese (private)",
    "EN-available": "non-Japanese (public)",
    "EN-unavailable": "non-Japanese (private)",
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
    s=150,
    linewidth=0.5,
    edgecolors="gray"
)

ax.scatter(
    df[df["Type"] == "JP-available-CP"]["Announced"],
    df[df["Type"] == "JP-available-CP"]["Parameters(B)"],
    color=colors["JP-available-CP"],
    label=labels["JP-available-CP"],
    s=150,
    linewidth=0.5,
    edgecolors="gray"
)

ax.scatter(
    df[df["Type"] == "JP-available"]["Announced"],
    df[df["Type"] == "JP-available"]["Parameters(B)"],
    color=colors["JP-available"],
    label=labels["JP-available"],
    s=150,
    linewidth=0.5,
    edgecolors="gray"
)

# キャプションが増えすぎて図が見づらくなってきたので、一旦コメントアウト
# for i in reversed(range(len(df))):
#     if df["Type"][i].startswith("JP"):
#         ax.text(
#             df["Announced"][i],
#             df["Parameters(B)"][i] * 1.2,
#             df["label"][i],
#             fontsize=8,
#             verticalalignment='bottom',
#             horizontalalignment='center'
#         )
#     if df["Type"][i].startswith("EN") and df["Lab"][i] in BIGTECH_LIST and df["Parameters(B)"][i] > 100:
#         ax.text(
#             df["Announced"][i],
#             df["Parameters(B)"][i] * 1.2,
#             f'{df["label"][i]}\n({df["Lab"][i]})',
#             fontsize=8,
#             color="grey",
#             verticalalignment='bottom',
#             horizontalalignment='center',
#         )

for y in [0.1, 1, 10, 100, 1000]:
    ax.axhline(y=y, color='gray', linestyle='--', linewidth=0.5)

# ChatGPT が公開された 2022年11月30日 に縦線を引き、"ChatGPT" という文字列を添える
chatgpt_announced = pd.to_datetime("2022/11/30", format='%Y/%m/%d')
ax.axvline(x=chatgpt_announced, color='gray', linestyle='--', linewidth=0.5)
ax.text(
    chatgpt_announced,
    3500,
    "ChatGPT公開",
    fontsize=10,
    fontweight='bold',
    verticalalignment='top',
    horizontalalignment='center'
)

ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y年%m月')) 

ax.set_ylabel("パラメータ数（単位: billion）")
ax.set_yscale('log')
ax.set_ylim(0.09, 4000)


plt.xticks(rotation=45)
plt.subplots_adjust(left=0.075, right=0.975, bottom=0.1, top=0.975)
plt.legend()
plt.savefig("../parameter_size_overview.png", dpi=144)