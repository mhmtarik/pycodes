import pandas as pd

def analyze_csv(file_path):
    # Read the CSV file
    df = pd.read_csv(file_path)
    
    # Calculate unique counts for each column
    unique_counts = {}
    for column in df.columns:
        unique_counts[column] = df[column].nunique()
    
    # Convert the dictionary to a DataFrame for better visualization
    unique_counts_df = pd.DataFrame(list(unique_counts.items()), columns=['Column', 'Unique Count'])
    
    return unique_counts_df

# Example usage
if __name__ == "__main__":
    file_path = input("Enter the path to the CSV file: ")
    result = analyze_csv(file_path)
    print(result)
    