import pandas as pd

df = pd.read_csv("MUSCLE_complete_dataset.csv")

# Check class distribution
print(df['status'].value_counts())

# Desired number of samples per class
target_size = 40000
samples_per_class = target_size // 2

# Sample equally from each class
df_0 = df[df['status'] == 0].sample(n=samples_per_class, random_state=42)
df_1 = df[df['status'] == 1].sample(n=samples_per_class, random_state=42)

# Combine and shuffle
df_downsampled = pd.concat([df_0, df_1]).sample(frac=1, random_state=42).reset_index(drop=True)

# Save if needed
df_downsampled.to_csv("downsized_dataset.csv", index=False)
