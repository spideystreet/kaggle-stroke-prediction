# Install dependencies as needed:
# pip install 'kagglehub[pandas-datasets]' pandas
import kagglehub
from kagglehub import KaggleDatasetAdapter
import pandas as pd # Assurez-vous que pandas est importé

def load_stroke_data(file_name="healthcare-dataset-stroke-data.csv"):
    """
    Downloads and loads the stroke prediction dataset from Kaggle.

    Args:
        file_name (str): The name of the file to load from the dataset.
                         Defaults to "healthcare-dataset-stroke-data.csv".

    Returns:
        pandas.DataFrame: The loaded data as a pandas DataFrame, or None if loading fails.
    """
    print(f"Attempting to load file: {file_name} from dataset fedesoriano/stroke-prediction-dataset")
    try:
        # Load the latest version using the specified file_name as a positional argument
        df = kagglehub.load_dataset(
          KaggleDatasetAdapter.PANDAS,
          "fedesoriano/stroke-prediction-dataset",
          file_name, # Pass file_name positionally
          # Provide any additional arguments like pandas_kwargs if needed
          # pandas_kwargs={'sep': ','}
        )
        print("Dataset loaded successfully!")
        return df
    except kagglehub.KaggleApiHTTPError as e:
        print(f"Error loading dataset (Kaggle API): {e}")
        print("Please check your Kaggle API credentials (e.g., ~/.kaggle/kaggle.json) and internet connection.")
        return None
    except ValueError as e:
         print(f"Error loading dataset (Value Error): {e}")
         print("Please check if the file name and format are correct for the Pandas adapter.")
         return None
    except Exception as e:
        print(f"An unexpected error occurred during dataset loading: {e}")
        return None

# --- Example of how to use the function ---
# This block only runs when the script is executed directly
if __name__ == "__main__":
    print("Executing load_data.py script...")
    stroke_df = load_stroke_data() # Call the function to load data

    if stroke_df is not None:
        print("\n--- Data Loading Successful ---")
        print("\nFirst 5 rows of the dataset:")
        print(stroke_df.head())
    else:
        print("\n--- Data Loading Failed ---")