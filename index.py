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
