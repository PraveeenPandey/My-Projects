#Log Digestion Project
This Python project aims to analyze log files and provide insights based on the data. The logs are processed to obtain various statistics, including the number of times each endpoint is called, the total API calls per minute, and the total API calls for each HTTP status code.

##Getting Started
Prerequisites
Make sure you have Python installed on your system. If not, you can download and install Python from the official website: Python.org

###Installation
1. Clone this repository to your local machine using the following command:
   git clone this repo

2. Change to the project directory:
   cd log-digestion

3. Download the data from this link:
   https://drive.google.com/drive/folders/1DzmYjCawYct6kfstCyUzU_kxIHnahGWD?usp=sharing

4. Install the required dependencies (pandas library):
   pip install pandas

###Usage
1. Place the log files (in the format specified below) inside the project directory.

2. Run the Python script log_analysis.py to analyze the log files:

python log_analysis.py

The script will process the log files and display the following insights in the terminal:

Number of times each endpoint is called.
API calls per minute.
Total API calls for each HTTP status code.

#Log File Format
The script expects log files to follow a specific format:

timestamp: message

Where:

timestamp: The timestamp of the log entry in the format "YYYY-MM-DD HH:MM +TZ:TZ" (e.g., "2023-03-25 01:59 +11:00").
message: The log message or information.
Ensure that each log entry in the log files adheres to this format.

##Contributing
Contributions to this project are welcome! If you encounter any issues, have suggestions for improvements, or want to add new features, please open an issue or submit a pull request.

