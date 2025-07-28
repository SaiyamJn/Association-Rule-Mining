import random
import string
import csv

def generate_transactions(num_transactions, min_items=2, max_items=13, output_file='transactions.csv'):
    items = list(string.ascii_uppercase)  # ['A', 'B', ..., 'Z']

    with open(output_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["TID"] + ["Item1", "Item2", "Item3", "Item4", "Item5", "Item6", "Item7", "Item8", "Item9", "Item10"])  # Max item headers

        for tid in range(1, num_transactions + 1):
            num_items = random.randint(min_items, max_items)
            transaction_items = random.sample(items, num_items)
            row = [f"T{tid}"] + transaction_items
            writer.writerow(row)

    print(f"{num_transactions} transactions with IDs saved to {output_file}")

# Generate datasets of various sizes

generate_transactions(100_000, output_file=r"C:\Users\saiya\Desktop\Association Rule Mining\transactions_1lakh.csv")
generate_transactions(200_000, output_file=r"C:\Users\saiya\Desktop\Association Rule Mining\transactions_2lakh.csv")
generate_transactions(300_000, output_file=r"C:\Users\saiya\Desktop\Association Rule Mining\transactions_3lakh.csv")
generate_transactions(400_000, output_file=r"C:\Users\saiya\Desktop\Association Rule Mining\transactions_4lakh.csv")
generate_transactions(500_000, output_file=r"C:\Users\saiya\Desktop\Association Rule Mining\transactions_5lakh.csv")
