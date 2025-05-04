# -*- coding: utf-8 -*-
"""
Module for importing common data science libraries.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# You can add more libraries here as your project grows
# For example:
# from sklearn.model_selection import train_test_split
# from sklearn.ensemble import RandomForestClassifier
# etc.

print("Common libraries (pandas, numpy, matplotlib, seaborn, sys, os) imported.")

# Optional: Define a function if you want to explicitly call the import process,
# although simply importing this module already executes the imports above.
# def load_libraries():
#     """Imports common data science libraries."""
#     # The imports are already done when the module is loaded.
#     # This function could potentially do more, like setting configurations.
#     sns.set_theme(style="whitegrid") # Example: set seaborn style
#     plt.rcParams['figure.figsize'] = (12, 7) # Example: set default figure size
#     print("Common libraries loaded and configured.")

# --- Example of how to use (if you defined the function) ---
# if __name__ == "__main__":
#     print("Executing load_libs.py script...")
#     load_libraries()
#     print("Libraries ready.")
#     # Example usage: Create a dummy DataFrame
#     df_test = pd.DataFrame({'col1': np.random.rand(5)})
#     print("\nTest DataFrame head:")
#     print(df_test.head())