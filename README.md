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
This repository is part of a research paper. For reuse or citation, please refer to the accompanying publication.
If you use this codebase in your work, please cite or credit the original repository.
