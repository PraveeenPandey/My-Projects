import pandas as pd
import re

# Function to read log files line by line and extract timestamp and message
def read_log_file(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    data = []
    for line in lines:
        match = re.match(r'^([\d-]+ [\d:]+ [\+\-]\d+:\d+): (.+)$', line)
        if match:
            timestamp, message = match.groups()
            data.append([timestamp, message])
    return data

# Step 1: Read the data from the log files and combine them into one DataFrame
log_files = ["api-dev-out.log", "api-prod-out.log", "prod-api-prod-out.log"]
data_frames = [pd.DataFrame(read_log_file(file), columns=["timestamp", "message"]) for file in log_files]
combined_df = pd.concat(data_frames, ignore_index=True)

# Step 2: Extract the relevant information (timestamp and endpoint)
combined_df['timestamp'] = pd.to_datetime(combined_df['timestamp'], format='%Y-%m-%d %H:%M %z', errors='coerce')
combined_df['endpoint'] = combined_df['message'].str.extract(r'([a-zA-Z\s]+)')[0].str.strip()

# Step 3: Drop unnecessary columns
combined_df.drop('message', axis=1, inplace=True)

# Step 4: Remove rows with missing timestamps
combined_df.dropna(subset=['timestamp'], inplace=True)

# Step 5: Convert the timestamps to datetime objects and set it as the DataFrame index
combined_df['timestamp'] = pd.to_datetime(combined_df['timestamp'], utc=True)
combined_df.set_index('timestamp', inplace=True)

# Step 6: Calculate the number of times each endpoint is called
endpoint_counts = combined_df['endpoint'].value_counts()

# Step 7: Calculate the number of API calls on a per-minute basis
api_calls_per_minute = combined_df.resample('T').size()

# Step 8: Calculate the total number of API calls for each HTTP status code
status_code_counts = combined_df['endpoint'].groupby(combined_df['endpoint']).count()

# Step 9: Display the results in a formatted table
print("Endpoint Counts:")
print(endpoint_counts)

print("\nAPI Calls per Minute:")
print(api_calls_per_minute)

print("\nTotal API Calls for each HTTP Status Code:")
print(status_code_counts)


