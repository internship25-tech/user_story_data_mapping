# Data Mapping and Filtering Script

## Overview

This Python script reads a list of raw identifiers from a CSV file and filters rows from a reference Excel file (`.xlsx`) where a matching key exists. The matched rows are then written to a new CSV file.

## Use Case

You have:
- `raw_data.csv`: Contains a list of unique identifiers.
- `reference_data.xlsx`: A master file containing detailed records for many identifiers.

The script:
- Matches identifiers from `raw_data.csv` with a column (`lookup_key`) in `reference_data.xlsx`.
- Extracts and saves all matching rows to `mapped_output.csv`.

## File Structure

Place all files in the same folder:

