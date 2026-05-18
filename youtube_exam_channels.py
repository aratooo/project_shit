import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import os

# ─────────────────────────────────────────
#  1. DATA
# ─────────────────────────────────────────

data = {
    "Rank": list(range(1, 21)),
    "Channel Name": [
        "Physics Wallah", "Vedantu", "Unacademy", "Aakash Digital",
        "Khan Academy India", "Mathongo", "Neev by PW", "Apni Kaksha",
        "Magnet Brains", "Exam Fear", "Let's Tute", "Commerce Wallah by PW",
        "Xylem App", "Infinity Learn", "BYJU'S", "Doubtnut",
        "Motion Education", "Resonance Eduventures", "Career Point", "V Mathematics"
    ],
    "Subscribers (M)": [
        12.8, 8.2, 6.5, 3.1, 2.8, 2.1, 1.9, 3.4,
        4.1, 1.2, 0.98, 1.4, 1.1, 2.3, 5.8, 3.7,
        0.87, 0.76, 0.65, 0.54
    ],
    "Total Views (B)": [
        1.8, 0.95, 0.72, 0.38, 0.41, 0.29, 0.21, 0.44,
        0.61, 0.31, 0.18, 0.16, 0.22, 0.27, 0.68, 0.43,
        0.11, 0.09, 0.08, 0.07
    ],
    "Primary Subject": [
        "Physics/Chem", "All Subjects", "All Subjects", "All Subjects",
        "Maths/Science", "Maths", "All Subjects", "All Subjects",
        "All Subjects", "Science/Maths", "All Subjects", "Commerce",
        "All Subjects", "All Subjects", "All Subjects", "Maths/Science",
        "Physics/Maths", "All Subjects", "All Subjects", "Maths"
    ],
    "Target Exam": [
        "JEE/NEET", "JEE/NEET/Boards", "JEE/NEET", "JEE/NEET",
        "Boards", "JEE", "Boards", "Boards/JEE",
        "Boards", "Boards", "Boards", "Boards",
        "Boards/KEAM", "JEE/NEET", "JEE/NEET/Boards", "JEE/NEET",
        "JEE", "JEE/NEET", "JEE/NEET", "JEE/Boards"
    ],
    "Model": [
        "Freemium", "Freemium", "Freemium", "Paid",
        "Free", "Freemium", "Freemium", "Free",
        "Free", "Free", "Free", "Freemium",
        "Freemium", "Freemium", "Paid", "Freemium",
        "Paid", "Paid", "Paid", "Free"
    ],
    "Year Started": [
        2014, 2014, 2015, 2016, 2013, 2017, 2020, 2019,
        2018, 2011, 2013, 2021, 2017, 2019, 2015, 2017,
        2018, 2019, 2018, 2016
    ],
    "Avg Views Per Video (K)": [
        850, 420, 310, 180, 220, 310, 195, 380,
        290, 140, 95, 175, 160, 210, 270, 245,
        88, 72, 65, 58
    ]
}

df = pd.DataFrame(data)

# ─────────────────────────────────────────
#  2. COLOUR PALETTE
# ─────────────────────────────────────────

BG      = "#0d1117"
CARD    = "#161b22"
RED     = "#ff4d4d"
ORANGE  = "#ff9900"
CYAN    = "#00d4ff"
GREEN   = "#39d353"
PURPLE  = "#a855f7"
WHITE   = "#e6edf3"
GREY    = "#8b949e"

plt.rcParams.update({
    "figure.facecolor":  BG,
    "axes.facecolor":    CARD,
    "axes.edgecolor":    GREY,
    "axes.labelcolor":   WHITE,
    "xtick.color":       GREY,
    "ytick.color":       WHITE,
    "text.color":        WHITE,
    "grid.color":        "#21262d",
    "grid.linestyle":    "--",
    "grid.linewidth":    0.6,
    "font.family":       "monospace",
})

# ─────────────────────────────────────────
#  HELPER
# ─────────────────────────────────────────

def save(fig, name):
    path = r"C:\Users\USER\Downloads\\project"
    fig.savefig(path, dpi=150, bbox_inches="tight", facecolor=BG)
    plt.close(fig)
    print(f"  saved → project")

# ─────────────────────────────────────────
#  CHART 1 — Top 10 Subscribers (bar)
# ─────────────────────────────────────────

top10 = df.nlargest(10, "Subscribers (M)").sort_values("Subscribers (M)")

fig, ax = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor(BG)

colors = [RED if v == top10["Subscribers (M)"].max() else CYAN for v in top10["Subscribers (M)"]]
bars = ax.barh(top10["Channel Name"], top10["Subscribers (M)"],
               color=colors, edgecolor="none", height=0.6)

for bar, val in zip(bars, top10["Subscribers (M)"]):
    ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2,
            f"{val}M", va="center", fontsize=9, color=WHITE)

ax.set_xlabel("Subscribers (Millions)", fontsize=10)
ax.set_title("TOP 10 EXAM PREP CHANNELS BY SUBSCRIBERS", fontsize=13,
             fontweight="bold", color=RED, pad=14)
ax.grid(axis="x")
ax.set_xlim(0, top10["Subscribers (M)"].max() + 2)
fig.tight_layout()
save(fig, "chart1_subscribers.png")

# ─────────────────────────────────────────
#  CHART 2 — Free vs Paid vs Freemium (pie)
# ─────────────────────────────────────────

model_counts = df["Model"].value_counts()
pie_colors   = [GREEN, ORANGE, CYAN]

fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

wedges, texts, autotexts = ax.pie(
    model_counts,
    labels=model_counts.index,
    autopct="%1.1f%%",
    colors=pie_colors,
    startangle=140,
    pctdistance=0.78,
    wedgeprops=dict(edgecolor=BG, linewidth=2)
)
for t in texts:
    t.set_color(WHITE); t.set_fontsize(11)
for at in autotexts:
    at.set_color(BG); at.set_fontweight("bold"); at.set_fontsize(10)

ax.set_title("REVENUE MODEL DISTRIBUTION", fontsize=13,
             fontweight="bold", color=ORANGE, pad=14)
fig.tight_layout()
save(fig, "chart2_model_pie.png")

# ─────────────────────────────────────────
#  CHART 3 — Subscribers vs Avg Views/Video (scatter)
# ─────────────────────────────────────────

model_color_map = {"Free": GREEN, "Freemium": CYAN, "Paid": RED}
dot_colors = df["Model"].map(model_color_map)

fig, ax = plt.subplots(figsize=(11, 7))
fig.patch.set_facecolor(BG)

sc = ax.scatter(df["Subscribers (M)"], df["Avg Views Per Video (K)"],
                c=dot_colors, s=120, edgecolors=BG, linewidths=0.8, zorder=3)

for _, row in df.iterrows():
    ax.annotate(row["Channel Name"],
                (row["Subscribers (M)"], row["Avg Views Per Video (K)"]),
                textcoords="offset points", xytext=(6, 4),
                fontsize=7, color=GREY)

legend_handles = [mpatches.Patch(color=c, label=m)
                  for m, c in model_color_map.items()]
ax.legend(handles=legend_handles, facecolor=CARD, edgecolor=GREY,
          labelcolor=WHITE, fontsize=9, loc="upper left")

ax.set_xlabel("Subscribers (Millions)", fontsize=10)
ax.set_ylabel("Avg Views Per Video (K)", fontsize=10)
ax.set_title("SUBSCRIBERS vs AVG VIEWS PER VIDEO", fontsize=13,
             fontweight="bold", color=CYAN, pad=14)
ax.grid(True)
fig.tight_layout()
save(fig, "chart3_scatter.png")

# ─────────────────────────────────────────
#  CHART 4 — Target Exam breakdown (bar)
# ─────────────────────────────────────────

# Explode combined tags so each exam gets counted
exam_series = df["Target Exam"].str.split("/").explode()
exam_counts = exam_series.value_counts()

fig, ax = plt.subplots(figsize=(9, 5))
fig.patch.set_facecolor(BG)

bar_colors = [PURPLE, RED, ORANGE, GREEN, CYAN][:len(exam_counts)]
bars = ax.bar(exam_counts.index, exam_counts.values,
              color=bar_colors, edgecolor="none", width=0.5)

for bar, val in zip(bars, exam_counts.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.1,
            str(val), ha="center", fontsize=10, color=WHITE, fontweight="bold")

ax.set_ylabel("Number of Channels", fontsize=10)
ax.set_title("CHANNELS BY TARGET EXAM", fontsize=13,
             fontweight="bold", color=PURPLE, pad=14)
ax.grid(axis="y")
ax.set_ylim(0, exam_counts.max() + 2)
fig.tight_layout()
save(fig, "chart4_exam_bar.png")

# ─────────────────────────────────────────
#  CHART 5 — Year Started timeline (line)
# ─────────────────────────────────────────

year_counts = df["Year Started"].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor(BG)

ax.plot(year_counts.index, year_counts.values,
        color=ORANGE, linewidth=2.5, marker="o",
        markersize=8, markerfacecolor=RED, markeredgecolor=BG, zorder=3)

ax.fill_between(year_counts.index, year_counts.values,
                alpha=0.15, color=ORANGE)

for x, y in zip(year_counts.index, year_counts.values):
    ax.text(x, y + 0.08, str(y), ha="center", fontsize=9,
            color=WHITE, fontweight="bold")

ax.set_xlabel("Year", fontsize=10)
ax.set_ylabel("Channels Launched", fontsize=10)
ax.set_title("GROWTH OF EXAM PREP CHANNELS OVER THE YEARS", fontsize=13,
             fontweight="bold", color=ORANGE, pad=14)
ax.set_xticks(year_counts.index)
ax.grid(True)
fig.tight_layout()
save(fig, "chart5_timeline.png")

# ─────────────────────────────────────────
#  CHART 6 — Total Views Top 10 (bar)
# ─────────────────────────────────────────

top10v = df.nlargest(10, "Total Views (B)").sort_values("Total Views (B)")

fig, ax = plt.subplots(figsize=(11, 6))
fig.patch.set_facecolor(BG)

bar_c = [GREEN if v == top10v["Total Views (B)"].max() else PURPLE
         for v in top10v["Total Views (B)"]]
bars = ax.barh(top10v["Channel Name"], top10v["Total Views (B)"],
               color=bar_c, edgecolor="none", height=0.6)

for bar, val in zip(bars, top10v["Total Views (B)"]):
    ax.text(bar.get_width() + 0.01, bar.get_y() + bar.get_height() / 2,
            f"{val}B", va="center", fontsize=9, color=WHITE)

ax.set_xlabel("Total Views (Billions)", fontsize=10)
ax.set_title("TOP 10 CHANNELS BY TOTAL VIEWS", fontsize=13,
             fontweight="bold", color=GREEN, pad=14)
ax.grid(axis="x")
ax.set_xlim(0, top10v["Total Views (B)"].max() + 0.3)
fig.tight_layout()
save(fig, "chart6_total_views.png")

# ─────────────────────────────────────────
#  3. DISPLAY FULL TABLE
# ─────────────────────────────────────────

print("\n" + "=" * 70)
print("  TOP 20 EXAM PREP YOUTUBE CHANNELS — FULL DATA")
print("=" * 70)
print(df.to_string(index=False))

# ─────────────────────────────────────────
#  4. BASIC STATS
# ─────────────────────────────────────────

print("\n" + "=" * 70)
print("  KEY STATISTICS")
print("=" * 70)
print(f"  Total Subscribers across all channels : {df['Subscribers (M)'].sum():.1f}M")
print(f"  Total Views across all channels       : {df['Total Views (B)'].sum():.2f}B")
print(f"  Most subscribed channel               : {df.loc[df['Subscribers (M)'].idxmax(), 'Channel Name']}")
print(f"  Highest avg views/video               : {df.loc[df['Avg Views Per Video (K)'].idxmax(), 'Channel Name']}")
print(f"  Oldest channel in dataset             : {df.loc[df['Year Started'].idxmin(), 'Channel Name']} ({df['Year Started'].min()})")
print(f"  Free channels                         : {(df['Model'] == 'Free').sum()}")
print(f"  Paid channels                         : {(df['Model'] == 'Paid').sum()}")
print(f"  Freemium channels                     : {(df['Model'] == 'Freemium').sum()}")
print("=" * 70)
print("\n  All 6 charts saved to /mnt/user-data/outputs/")
