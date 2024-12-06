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

from typing import Literal


# use universal colors
# https://www.jma.go.jp/jma/kishou/info/colorguide/HPColorGuide_202007.pdf
LEGEND_COLORS = {
    # "JP-available-API": "#B40068"
    "JP-available": "#FF2800", 
    "JP-available-CP": "#FF9900",
    "JP-unavailable": "#FFF500",
    "EN-available": "#0096FF",
    "EN-unavailable": "#B9EBFF",
}

legend_labels_ja = {
    # "JP-available-API": "日本語 (APIとして公開)"
    "JP-available": "日本語 (公開, フルスクラッチ学習されたモデル)",
    "JP-available-CP": "日本語 (公開)",
    "JP-unavailable": "日本語 (非公開)",
    "EN-available": "日本語以外 (公開)",
    "EN-unavailable": "日本語以外 (非公開)",
}

legend_labels_en = {
    # "JP-available-API": "Japanese (public, model weights closed)"
    "JP-available": "Japanese (public, built from scratch)",
    "JP-available-CP": "Japanese (public)",
    "JP-unavailable": "Japanese (private)",
    "EN-available": "non-Japanese (public)",
    "EN-unavailable": "non-Japanese (private)",
}

LEGEND_LABELS = {
    "ja": legend_labels_ja,
    "en": legend_labels_en
}

RELEASE_CHATGPT_MESSAGE = {
    "ja": "ChatGPT公開",
    "en": "Release of ChatGPT"
}

DATE_FORMAT = {
    "ja": "%Y年%m月",
    "en": "%Y/%m"
}

YAXIS_LABEL = {
    "ja": "パラメータ数（単位: 10億）",
    "en": "Num. of Parameters (B)"
}


def load_llms_data() -> pd.DataFrame:
    df_en = pd.read_csv('parameter_size_overview.csv')
    df_ja = pd.read_csv('parameter_size_overview_ja.csv')

    # 日本語モデルのデータを英語モデルのデータに結合
    df = pd.concat([df_en, df_ja], ignore_index=True)

    df["label"] = np.where(df["Model"].isna(), df["Lab"], df["Model"])
    df["Announced"] = pd.to_datetime(df["Announced"], format='%Y/%m/%d')
    df['Parameters(B)'] = pd.to_numeric(df['Parameters(B)'], errors='coerce')
    df = df.dropna(subset=['Parameters(B)'])
    df = df.reset_index(drop=True)

    return df


def draw_figure(df: pd.DataFrame, locale: Literal['ja', 'en']):
    fig, ax = plt.subplots(figsize=(10, 8))

    ax.scatter(
        df[df["Type"] == "EN-unavailable"]["Announced"],
        df[df["Type"] == "EN-unavailable"]["Parameters(B)"],
        color=LEGEND_COLORS["EN-unavailable"],
        label=LEGEND_LABELS[locale]["EN-unavailable"],
        s=30
    )

    ax.scatter(
        df[df["Type"] == "EN-available"]["Announced"],
        df[df["Type"] == "EN-available"]["Parameters(B)"],
        color=LEGEND_COLORS["EN-available"],
        label=LEGEND_LABELS[locale]["EN-available"],
        s=30
    )

    ax.scatter(
        df[df["Type"] == "JP-unavailable"]["Announced"],
        df[df["Type"] == "JP-unavailable"]["Parameters(B)"],
        color=LEGEND_COLORS["JP-unavailable"],
        label=LEGEND_LABELS[locale]["JP-unavailable"],
        s=150,
        linewidth=0.5,
        edgecolors="gray"
    )

    ax.scatter(
        df[df["Type"] == "JP-available-CP"]["Announced"],
        df[df["Type"] == "JP-available-CP"]["Parameters(B)"],
        color=LEGEND_COLORS["JP-available-CP"],
        label=LEGEND_LABELS[locale]["JP-available-CP"],
        s=150,
        linewidth=0.5,
        edgecolors="gray"
    )

    ax.scatter(
        df[df["Type"] == "JP-available"]["Announced"],
        df[df["Type"] == "JP-available"]["Parameters(B)"],
        color=LEGEND_COLORS["JP-available"],
        label=LEGEND_LABELS[locale]["JP-available"],
        s=150,
        linewidth=0.5,
        edgecolors="gray"
    )

    for y in [0.1, 1, 10, 100, 1000]:
        ax.axhline(y=y, color='gray', linestyle='--', linewidth=0.5)

    # ChatGPT が公開された 2022年11月30日 に縦線を引き、"ChatGPT" という文字列を添える
    chatgpt_announced = pd.to_datetime("2022/11/30", format='%Y/%m/%d')
    ax.axvline(x=chatgpt_announced, color='gray', linestyle='--', linewidth=0.5)
    ax.text(
        chatgpt_announced,
        3500,
        RELEASE_CHATGPT_MESSAGE[locale],
        fontsize=10,
        fontweight='bold',
        verticalalignment='top',
        horizontalalignment='center'
    )

    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax.xaxis.set_major_formatter(mdates.DateFormatter(DATE_FORMAT[locale])) 

    ax.set_ylabel(YAXIS_LABEL[locale])
    ax.set_yscale('log')
    ax.set_ylim(0.09, 4000)


    plt.xticks(rotation=45)
    plt.subplots_adjust(left=0.075, right=0.975, bottom=0.1, top=0.975)
    plt.legend()
    plt.savefig(f"../parameter_size_overview_{locale}.png", dpi=72)


if __name__ == "__main__":
    df = load_llms_data()
    draw_figure(df, "en")
    draw_figure(df, "ja")