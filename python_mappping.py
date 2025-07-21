import pandas as pd
import os

# Use current script's directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# File paths relative to script's location
raw_data_path = os.path.join(script_dir, 'raw_data.csv')
reference_data_path = os.path.join(script_dir, 'reference_data.xlsx')
output_path = os.path.join(script_dir, 'mapped_output.csv')

# Column names (update based on your actual headers)
raw_key_column = 'lookup_key'             # Column in raw_data.csv
reference_key_column = 'lookup_key'  # Column in reference_data.xlsx

try:
    # Load the files
    if not os.path.isfile(raw_data_path):
        raise FileNotFoundError(f"❌ File not found: {raw_data_path}")
    if not os.path.isfile(reference_data_path):
        raise FileNotFoundError(f"❌ File not found: {reference_data_path}")

    raw_df = pd.read_csv(raw_data_path)
    ref_df = pd.read_excel(reference_data_path)

    # Check if key columns exist
    if raw_key_column not in raw_df.columns:
        raise KeyError(f"❌ Column '{raw_key_column}' not found in raw_data.csv")
    if reference_key_column not in ref_df.columns:
        raise KeyError(f"❌ Column '{reference_key_column}' not found in reference_data.xlsx")

    # Remove duplicates from raw data
    unique_keys = raw_df[raw_key_column].dropna().drop_duplicates()

    # Match rows from reference data
    matched_df = ref_df[ref_df[reference_key_column].isin(unique_keys)]

    if matched_df.empty:
        print("⚠ No matching rows found between raw and reference data.")
    else:
        matched_df.to_csv(output_path, index=False)
        print(f"✅ Mapping complete. Output saved to: {output_path}")
        print(f"🧾 Rows matched: {matched_df.shape[0]}, Columns: {matched_df.shape[1]}")

except FileNotFoundError as fnf_err:
    print(str(fnf_err))
except KeyError as key_err:
    print(str(key_err))
except Exception as ex:
    print(f"❌ Unexpected error: {ex}")
