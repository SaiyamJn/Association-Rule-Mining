import pandas as pd
import csv
import os
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# ------------------ Load transactions from CSV ------------------
def load_transactions(file_path):
    transactions = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip header
        for row in reader:
            items = [item for item in row[1:] if item]  # Skip TID
            transactions.append(items)
    return transactions

# ------------------ Run Apriori ------------------
def run_apriori(transactions, min_support, min_confidence):
    te = TransactionEncoder()
    te_ary = te.fit(transactions).transform(transactions)
    df = pd.DataFrame(te_ary, columns=te.columns_)
    frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
    return frequent_itemsets, rules

# ------------------ Format frequent itemsets ------------------
def format_frequent_itemsets(frequent_itemsets, total_transactions):
    output = ""
    grouped = frequent_itemsets.copy()
    grouped['length'] = grouped['itemsets'].apply(lambda x: len(x))
    max_k = grouped['length'].max()

    for k in range(1, max_k + 1):
        output += f"\nL{k} (Frequent {k}-itemsets):\n"
        Lk = grouped[grouped['length'] == k]
        for _, row in Lk.iterrows():
            itemset = set(row['itemsets'])
            count = int(row['support'] * total_transactions)
            output += f"{itemset}: {count}\n"
    return output

# ------------------ Format rules ------------------
def format_rules(rules):
    output = "\n\n=== ASSOCIATION RULES (min_conf >= threshold) ===\n"
    for _, row in rules.iterrows():
        antecedent = set(row['antecedents'])
        consequent = set(row['consequents'])
        support = row['support']
        confidence = row['confidence']
        lift = row['lift']
        output += f"{antecedent} => {consequent} (support={support:.4f}, confidence={confidence:.2f}, lift={lift:.2f})\n"
    return output

# ------------------ Save Output ------------------
def save_output(frequent_itemsets, rules, output_file, total_transactions):
    output_text = format_frequent_itemsets(frequent_itemsets, total_transactions)
    output_text += format_rules(rules)
    with open(output_file, 'w') as f:
        f.write(output_text)

# ------------------ Main Loop ------------------

# Dataset paths (update these paths as needed)
file_paths = {
    100000: r"C:\Users\saiya\Desktop\Association Rule Mining\transactions_1lakh.csv",
    200000: r"C:\Users\saiya\Desktop\Association Rule Mining\transactions_2lakh.csv",
    300000: r"C:\Users\saiya\Desktop\Association Rule Mining\transactions_3lakh.csv",
    400000: r"C:\Users\saiya\Desktop\Association Rule Mining\transactions_4lakh.csv",
    500000: r"C:\Users\saiya\Desktop\Association Rule Mining\transactions_5lakh.csv",
}

# Support levels and confidence
min_support_counts = [5000, 10000, 15000, 20000, 25000]
min_confidence = 0.25

# Output folder
output_dir = r"C:\Users\saiya\Desktop\Association Rule Mining\Support_Experiments"
os.makedirs(output_dir, exist_ok=True)

# Loop over datasets and support values
for total_transactions, file_path in file_paths.items():
    transactions = load_transactions(file_path)

    for support_count in min_support_counts:
        # Skip very low thresholds for larger datasets
        if total_transactions >= 300000 and support_count < 15000:
            continue

        min_support = support_count / total_transactions
        frequent_itemsets, rules = run_apriori(transactions, min_support, min_confidence)

        # Filename: e.g., 100k_s5000.txt
        shortname = f"{total_transactions//1000}k_s{support_count}.txt"
        output_file = os.path.join(output_dir, shortname)

        save_output(frequent_itemsets, rules, output_file, total_transactions)
        print(f"Saved: {output_file}")
