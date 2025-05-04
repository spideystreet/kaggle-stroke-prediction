# -*- coding: utf-8 -*-
"""
Module for importing common data science libraries and applying basic configurations.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import os

# Apply configurations directly upon import
try:
    sns.set_theme(style="whitegrid")
    plt.rcParams['figure.figsize'] = (12, 7)
    print("Common libraries imported and configured.")
except NameError:
    # Handle cases where seaborn or matplotlib might not be installed yet
    print("Common libraries imported, but configuration failed (likely missing seaborn/matplotlib).")

if __name__ == "__main__":
     print("Executing load_libs.py script (usually not run directly)...")
     # Example usage: Create a dummy DataFrame
     df_test = pd.DataFrame({'col1': np.random.rand(5)})
     print("\nTest DataFrame head:")
     print(df_test.head())