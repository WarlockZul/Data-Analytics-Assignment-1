import pandas as pd

# Load original full dataset (ground truth)
df_original = pd.read_csv("Dataset.csv", dtype={"timestamp": str})

# Load your KNN imputation report (the file you want to update)
df_report = pd.read_csv("KNN_Imputed_Values_Report.csv")

# For each row in the report, find the true original value
true_values = []

for idx, row in df_report.iterrows():
    vid = row["vehicle_id"]
    ts = row["timestamp"]
    column = row["column_imputed"]

    # Find the matching row from Dataset.csv using vehicle_id + timestamp
    true_val = df_original.loc[
        (df_original["vehicle_id"] == vid) &
        (df_original["timestamp"] == ts),
        column
    ].values[0]

    true_values.append(true_val)

# Add the true values as a NEW COLUMN inside the SAME file
df_report["true_original_value"] = true_values

# Save back to the SAME CSV
df_report.to_csv("KNN_Imputed_Values_Report.csv", index=False)

print("✔ The same CSV file has been updated with true_original_value.")