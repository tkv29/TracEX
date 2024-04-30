import os
import csv

def create_csv_from_txt_files(folder_path):
    # Get a list of all .txt files in the folder
    txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]
    print(txt_files)

    # Create a new CSV file
    with open('patient_journeys.csv', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['name', 'patient_journey'])

        # Iterate over each .txt file
        for txt_file in txt_files:
            file_path = os.path.join(folder_path, txt_file)

            # Read the content of the .txt file
            with open(file_path, 'r') as file:
                content = file.read()

            # Extract the file name (without the .txt extension)
            name = os.path.splitext(txt_file)[0]

            # Write the name and content to the CSV file
            writer.writerow([name, content])

    print("CSV file created successfully.")

# Specify the folder path containing the .txt files
folder_path = '/home/tkv29/ba-tracex/TracEX/tracex_project/extraction/content/inputs'

# Call the function to create the CSV file
create_csv_from_txt_files(folder_path)
