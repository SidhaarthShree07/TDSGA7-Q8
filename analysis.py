# analysis/analysis.py
# Quarterly Retention Analysis (Python)
# Contact: 22f3001480@ds.study.iitm.ac.in

import math
import pandas as pd
import matplotlib.pyplot as plt

# --- Data ---------------------------------------------------------------
data = {
    "Quarter": ["Q1", "Q2", "Q3", "Q4"],
    "Retention": [68.63, 73.13, 71.13, 75.85],  # 2024
}
INDUSTRY_TARGET = 85.0
DECLARED_AVERAGE = 72.19  # must match README.md

df = pd.DataFrame(data)
df["GapToTarget"] = INDUSTRY_TARGET - df["Retention"]

# --- Stats --------------------------------------------------------------
avg = round(df["Retention"].mean(), 2)

# Validate average against the declared value
if not math.isclose(avg, DECLARED_AVERAGE, abs_tol=0.01):
    raise ValueError(f"Average mismatch: computed={avg}, declared={DECLARED_AVERAGE}")

print("Quarterly Retention:")
print(df.to_string(index=False))
print(f"\nAverage Retention (2024): {avg}")
print(f"Industry Target: {INDUSTRY_TARGET}")
print(f"Average Gap to Target: {round(INDUSTRY_TARGET - avg, 2)}")

# --- Visualization: Trend vs Target ------------------------------------
plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["Retention"], marker="o", linewidth=2, label="Retention (2024)")
plt.axhline(INDUSTRY_TARGET, linestyle="--", color="red", label=f"Industry Target ({INDUSTRY_TARGET})")
for x, y in zip(df["Quarter"], df["Retention"]):
    plt.text(x, y + 0.5, f"{y:.2f}%", ha="center", fontsize=9)
plt.title("Customer Retention Rate — 2024 Trend vs. Industry Target")
plt.ylabel("Retention (%)")
plt.ylim(60, 90)
plt.grid(alpha=0.25)
plt.legend()
plt.tight_layout()
plt.savefig("trend_vs_target.png", dpi=150)

# --- Visualization: Gap to Target (lower is better) ---------------------
plt.figure(figsize=(8, 5))
bars = plt.bar(df["Quarter"], df["GapToTarget"], color="#6BBF59")
plt.title("Gap to Industry Target (85%) — Lower is Better")
plt.ylabel("Percentage Points from Target")
plt.ylim(0, max(df["GapToTarget"]) + 3)
for rect, gap in zip(bars, df["GapToTarget"]):
    plt.text(rect.get_x() + rect.get_width()/2, rect.get_height() + 0.2, f"{gap:.2f}", ha="center", fontsize=9)
plt.grid(axis="y", alpha=0.25)
plt.tight_layout()
plt.savefig("gap_to_target.png", dpi=150)
