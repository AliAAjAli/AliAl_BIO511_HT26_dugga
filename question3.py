# ques 3

#a 
import argparse
import pandas as pd
import matplotlib.pyplot as plt

# Set up argparse so the file name 
parser = argparse.ArgumentParser(description="Read the cnv_data.") 
parser.add_argument("csv_file", help="Path to cnv_data.csv") 
args = parser.parse_args()

# Read the CSV file into a pandas dataframe called df
df = pd.read_csv(args.csv_file)


# we see if the data looks good 
print(df.shape)
print(df.columns)



# ploting
df = pd.read_csv("cnv_data.csv")

plt.figure(figsize=(12, 6))
plt.scatter(df["position_mb"], df["log2_ratio"], label="postion vs log2_ratio")

# Save the plot
plt.savefig("cnv_data.png")
plt.close()





