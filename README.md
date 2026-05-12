markdown
# Freelancer Business Activities Dataset Analysis

## Overview
The Freelancer Business Activities Dataset provides comprehensive information on freelancer activities in Abu Dhabi. It includes details such as activity ID, English and Arabic names, and categories like consultancy services, sports services, and more. This dataset is a valuable resource for entrepreneurs, policymakers, businesses, and researchers.

## Features
- **Activity ID**: Unique identifier for each activity.
- **English Name**: Name of the activity in English.
- **Arabic Name**: Name of the activity in Arabic.
- **Category**: Classification of activities (e.g., Consultancy Services, Sports Services).

## Usage Instructions
1. **Download the Dataset**: Obtain the dataset in XLSX format from the Abu Dhabi Open Data Platform.
2. **Load the Dataset**: Use Python and Pandas to load the data for analysis.
3. **Analyze the Data**: Filter and analyze the dataset to extract insights. For example, identify all consultancy services or sports-related activities.
4. **Save Processed Data**: Save the filtered data to a new XLSX file for further use.

## Python Example
Below is an example code to load, filter, and save the dataset:

### Prerequisites
- Python 3.7+
- pandas library

### Installation
Install the pandas library using pip if not already installed:
bash
pip install pandas


### Code Example
python
import pandas as pd

# Load the Freelancer Business Activities Dataset
file_path = 'Freelancer-Business-Activities-AD-OD.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataset
print("Dataset Preview:")
print(data.head())

# Filter dataset for a specific category, e.g., 'Consultancy Services'
consultancy_services = data[data['Category'].str.contains('Consultancy', na=False)]
print("\nConsultancy Services:")
print(consultancy_services)

# Example: Find all activities related to 'Sports'
sports_services = data[data['Category'].str.contains('Sports', na=False)]
print("\nSports Services:")
print(sports_services)

# Save filtered data to a new file
output_file_path = 'Filtered_Freelancer_Activities.xlsx'
consultancy_services.to_excel(output_file_path, index=False)
print(f"Filtered dataset saved to {output_file_path}")


## Applications
- Identify potential business opportunities for freelancers.
- Study economic trends and propose policies to encourage economic growth.
- Explore marketing and event planning services.
- Discover specialized freelancer services for personal or business use.
- Facilitate government monitoring and regulation of freelancer activities.

## Support and Feedback
For questions or feedback, contact the Abu Dhabi Open Data Support team:
- **Email**: support@opendata.abudhabi

## License
This dataset is made available under the terms and conditions outlined by the Abu Dhabi Open Data Platform.
