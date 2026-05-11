from __future__ import annotations

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


class Visualizer:
    @staticmethod
    def plot_histogram(df: pd.DataFrame, column: str, bins: int = 20) -> None:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[column], bins=bins, kde=True)
        plt.title(f"Distribution of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_box(df: pd.DataFrame, column: str) -> None:
        plt.figure(figsize=(8, 4))
        sns.boxplot(x=df[column])
        plt.title(f"Boxplot of {column}")
        plt.xlabel(column)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_count(df: pd.DataFrame, column: str) -> None:
        plt.figure(figsize=(8, 4))
        sns.countplot(data=df, x=column, order=df[column].value_counts().index)
        plt.title(f"Count Plot of {column}")
        plt.xlabel(column)
        plt.ylabel("Count")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_bar(df: pd.DataFrame, x: str, y: str, estimator="mean") -> None:
        plt.figure(figsize=(8, 4))
        sns.barplot(data=df, x=x, y=y, estimator=estimator, errorbar=None)
        plt.title(f"{y} by {x}")
        plt.xticks(rotation=30)
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_scatter(df: pd.DataFrame, x: str, y: str) -> None:
        plt.figure(figsize=(8, 4))
        sns.scatterplot(data=df, x=x, y=y, alpha=0.7)
        plt.title(f"{y} vs {x}")
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_corr_heatmap(df: pd.DataFrame, cols: list[str]) -> None:
        plt.figure(figsize=(10, 6))
        corr = df[cols].corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
        plt.title("Austro Correlation Heatmap")
        plt.tight_layout()
        plt.show()