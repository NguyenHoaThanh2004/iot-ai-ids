import pandas as pd

file_path = "../data/raw/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"

df = pd.read_csv(file_path)

print(df.head())

print(df.shape)

print(df.columns)