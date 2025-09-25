import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------ Extract Metrics ------------------
def extract_metrics(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    freq_itemset_count = 0
    rule_count = 0
    max_itemset_len = 0
    confidences = []

    for line in lines:
        itemset_match = re.match(r"^\{(.+?)\}:\s+(\d+)$", line.strip())
        if itemset_match:
            freq_itemset_count += 1
            length = len(itemset_match.group(1).split(","))
            if length > max_itemset_len:
                max_itemset_len = length

        rule_match = re.match(r"^\{(.+?)\} => \{(.+?)\} \(support=.*?, confidence=(.*?), lift=.*?\)", line.strip())
        if rule_match:
            rule_count += 1
            conf = float(rule_match.group(3))
            confidences.append(conf)

    avg_conf = round(sum(confidences) / len(confidences), 2) if confidences else 0
    return freq_itemset_count, rule_count, max_itemset_len, avg_conf

# ------------------ Directory of Results ------------------
input_dir = r"C:\Users\saiya\Desktop\Association Rule Mining\Support_Experiments"
files = [f for f in os.listdir(input_dir) if f.endswith(".txt")]

# ------------------ Build DataFrame ------------------
data = []

for file in files:
    path = os.path.join(input_dir, file)
    match = re.match(r"(\d+)k_s(\d+)\.txt", file)
    if match:
        dataset = f"{match.group(1)}k"
        support = int(match.group(2))
        fi_count, r_count, max_len, avg_conf = extract_metrics(path)
        data.append({
            "Dataset": dataset,
            "Support": support,
            "FrequentItemsets": fi_count,
            "Rules": r_count,
            "MaxLength": max_len,
            "AvgConfidence": avg_conf
        })

df = pd.DataFrame(data)

# Sort for proper heatmap formatting
df = df.sort_values(by=["Support", "Dataset"])

# ------------------ Bar Chart: Max Itemset Length ------------------
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x="Support", y="MaxLength", hue="Dataset")
plt.title("Maximum itemset length vs. support across dataset sizes.")
plt.xlabel("Support Count")
plt.ylabel("Max Length")
plt.legend(title="Dataset")
plt.tight_layout()
plt.savefig("bar_max_length.png", dpi=300)
plt.close()

# ------------------ Heatmaps ------------------
# Pivot for heatmaps
pivot_fi = df.pivot(index="Support", columns="Dataset", values="FrequentItemsets").fillna(0)
pivot_rules = df.pivot(index="Support", columns="Dataset", values="Rules").fillna(0)
pivot_conf = df.pivot(index="Support", columns="Dataset", values="AvgConfidence").fillna(0)

# Sort columns in correct dataset order
order = ['100k', '200k', '300k', '400k', '500k']
pivot_fi = pivot_fi[order]
pivot_rules = pivot_rules[order]
pivot_conf = pivot_conf[order]

# Heatmap 1 – Frequent Itemsets
plt.figure(figsize=(6, 5))
sns.heatmap(pivot_fi, annot=True, fmt=".0f", cmap="Blues", linewidths=0.5)
plt.title("Frequent itemset count across dataset sizes and support thresholds.")
plt.xlabel("Dataset")
plt.ylabel("Support")
plt.tight_layout()
plt.savefig("heatmap_itemsets.png", dpi=300)
plt.close()

# Heatmap 2 – Rules
plt.figure(figsize=(6, 5))
sns.heatmap(pivot_rules, annot=True, fmt=".0f", cmap="Greens", linewidths=0.5)
plt.title("Number of association rules across varying dataset sizes and support levels.")
plt.xlabel("Dataset")
plt.ylabel("Support")
plt.tight_layout()
plt.savefig("heatmap_rules.png", dpi=300)
plt.close()

# Heatmap 3 – Confidence
plt.figure(figsize=(6, 5))
sns.heatmap(pivot_conf, annot=True, fmt=".2f", cmap="Purples", linewidths=0.5)
plt.title("Average confidence of rules by dataset size and support value.")
plt.xlabel("Dataset")
plt.ylabel("Support")
plt.tight_layout()
plt.savefig("heatmap_confidence.png", dpi=300)
plt.close()
