import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Year": [2020, 2021, 2022, 2023, 2024, 2025],


    "Real Estate - Madurai": [100, 112, 128, 145, 160, 178],
    "Real Estate - Theni": [100, 108, 120, 135, 148, 162],

    "Medical": [100, 106, 115, 123, 130, 138],
    "Food": [100, 112, 128, 136, 144, 152],
    "Fuel": [100, 118, 145, 150, 160, 170],
    "Gold": [100, 110, 125, 135, 148, 160],
    "Silver": [100, 115, 132, 140, 152, 165]
}

df = pd.DataFrame(data)

print("=" * 60)
print("INFLATION ANALYSIS DATA (2020-2025)")
print("=" * 60)
print(df)


fig = plt.line(df, x="Year", y=df.columns[1:], title="Inflation Trends Across All Sectors")
fig.show()

for column in df.columns[1:]:
    plt.plot(
        df["Year"],
        df[column],
        marker='o',
        linewidth=2,
        label=column
    )

plt.title("Inflation Trends Across All Sectors")
plt.xlabel("Year")
plt.ylabel("Price Index")
plt.legend()
plt.grid(True)

plt.show()


plt.figure(figsize=(12, 6))

sectors = df.columns[1:]
values_2025 = df.iloc[-1, 1:]

colors = [
    "blue",
    "green",
    "purple",
    "orange",
    "red",
    "gold",
    "gray"
]

bars = plt.bar(
    sectors,
    values_2025,
    color=colors
)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 2,
        f"{height}",
        ha='center'
    )

plt.title("Sector Comparison in 2025")
plt.xlabel("Sector")
plt.ylabel("Price Index")

plt.xticks(rotation=20)

plt.show()


plt.figure(figsize=(8, 8))

plt.pie(
    values_2025,
    labels=sectors,
    autopct="%1.1f%%",
    colors=colors
)

plt.title("2025 Sector Distribution")

plt.show()


df["Average"] = df.iloc[:, 1:].mean(axis=1)

plt.figure(figsize=(10, 6))

plt.plot(
    df["Year"],
    df["Average"],
    marker='o',
    linewidth=3,
    color='black'
)

for x, y in zip(df["Year"], df["Average"]):
    plt.text(x, y + 2, f"{y:.1f}", ha="center")

plt.title("Average Inflation Across All Sectors")
plt.xlabel("Year")
plt.ylabel("Average Price Index")
plt.grid(True)

plt.show()


plt.figure(figsize=(10, 6))

plt.plot(
    df["Year"],
    df["Real Estate - Madurai"],
    marker='o',
    linewidth=3,
    color='blue',
    label='Madurai'
)

plt.plot(
    df["Year"],
    df["Real Estate - Theni"],
    marker='s',
    linewidth=3,
    color='green',
    label='Theni'
)

for x, y in zip(df["Year"], df["Real Estate - Madurai"]):
    plt.text(x, y + 2, str(y), ha='center')

for x, y in zip(df["Year"], df["Real Estate - Theni"]):
    plt.text(x, y - 5, str(y), ha='center')

plt.title("Real Estate Inflation Comparison: Madurai vs Theni")
plt.xlabel("Year")
plt.ylabel("Price Index")
plt.legend()
plt.grid(True)

plt.show()


sector_colors = {
    "Medical": "purple",
    "Food": "orange",
    "Fuel": "red",
    "Gold": "gold",
    "Silver": "gray"
}

for sector in sector_colors:

    plt.figure(figsize=(10, 5))

    plt.plot(
        df["Year"],
        df[sector],
        marker='o',
        linewidth=3,
        color=sector_colors[sector]
    )

    for x, y in zip(df["Year"], df[sector]):
        plt.text(
            x,
            y + 2,
            str(y),
            ha='center'
        )

    plt.title(f"{sector} Inflation Trend (2020-2025)")
    plt.xlabel("Year")
    plt.ylabel("Price Index")
    plt.grid(True, linestyle='--', alpha=0.7)

    plt.show()


print("\n")
print("=" * 60)
print("INFLATION PERCENTAGE REPORT")
print("=" * 60)

for sector in df.columns[1:8]:

    start = df[sector].iloc[0]
    end = df[sector].iloc[-1]

    inflation = ((end - start) / start) * 100

    print(f"{sector:<25}: {inflation:.2f}%")


overall_average = df["Average"].mean()

print("\nOverall Average Inflation Index (2020-2025)")
print(f"{overall_average:.2f}")