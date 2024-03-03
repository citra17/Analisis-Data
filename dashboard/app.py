import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns, streamlit as st
day_df=pd.read_csv("/content/day.csv")
hour_df=pd.read_csv("/content/hour.csv")

st.subheader('Daily Orders')
fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    day_df["dteday"],
    day_df["cnt"],
    marker='o',
    linewidth=2,
    color="#90CAF9"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)

st.pyplot(fig)

st.subheader("Produk Terjual Setiap Bulan")
fig1, ax = plt.subplots()
visualisasi_df = day_df.groupby(by="mnth").agg({"cnt":["sum"]})
visualisasi_df
colors_ = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
    "#FF5733", "#FFC300"]
sns.barplot(
    y="cnt",
    x="mnth",hue="mnth",legend=False,
    data=day_df,
    palette=colors_,ax=ax
)
ax.set_title("Number of Customer per Month", loc="center", fontsize=15)
st.pyplot(fig1)
plt.show()

st.subheader("Produk Terjual Setiap Jam")
fig2, ax = plt.subplots()
visualisasi2_df = hour_df.groupby(by="hr").agg({"cnt": ["sum"]})
visualisasi2_df
colors_ = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd",
    "#8c564b", "#e377c2", "#7f7f7f", "#bcbd22", "#17becf",
    "#aec7e8", "#ffbb78", "#98df8a", "#ff9896", "#c5b0d5",
    "#c49c94", "#f7b6d2", "#c7c7c7", "#dbdb8d", "#9edae5",
    "#393b79", "#5254a3", "#6b6ecf", "#9c9ede"]
sns.barplot(
    y="cnt",
    x="hr", hue="hr", legend=False,
    data=hour_df,
    palette=colors_,ax=ax
)
ax.set_title("Number of Customer per Hour", loc="center", fontsize=15)
st.pyplot(fig2)
plt.show()
