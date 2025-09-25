# Association Rule Mining Project

This project explores the impact of varying minimum support thresholds on frequent itemset generation and association rule discovery using the Apriori algorithm.

## 📊 Key Features
- Analysis across datasets with 100k to 500k transactions
- Support values ranging from 5000 to 25000
- Frequent itemsets and rule generation with confidence ≥ 25%
- Heatmaps and bar plots for comparison
- Output includes support, confidence, and lift values

## 🛠️ Technologies Used
- Python
- Pandas
- mlxtend
- Matplotlib
- Seaborn

## 📁 Output Format
Each experiment generates:
- `frequent_itemsets_<dataset>_<support>.txt`
- `association_rules_<dataset>_<support>.txt`
- Graphs: Heatmaps and bar charts in PNG format

## 📂 Datasets
Simulated transactional data with 26 items across varying volumes:
- 100k, 200k, 300k, 400k, 500k records

## 📈 Visualization Samples
- Max itemset length by support
- Count of frequent itemsets
- Number of rules
- Average confidence

## 📄 License
- Code: Licensed under the [MIT License](./LICENSE).
- Research Outputs: All documentation, visualizations, graphs, and written content are licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).
