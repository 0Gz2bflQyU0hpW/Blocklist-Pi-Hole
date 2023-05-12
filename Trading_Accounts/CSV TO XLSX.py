import pandas as pd

def csv_to_excel(input_file):
    """
    This function takes a CSV file as input, converts it to an Excel file, deletes rows whose column "A" value is not "EXERTIS",
    and deletes columns "I" and "A".
    
    Parameters:
    input_file (str): The path of the input CSV file
    
    Returns:
    str: The path of the output Excel file
    """
    try:
        # Read the CSV file
        df = pd.read_csv(input_file)
        
        # Filter rows where column "A" value is "EXERTIS"
        df = df[df['A'] == 'EXERTIS']
        
        # Drop columns "I" and "A"
        df = df.drop(columns=['I', 'A'])
        
        # Convert the dataframe to an Excel file
        output_file = input_file[:-4] + '.xlsx'
        df.to_excel(output_file, index=False)
        
        return output_file
    except Exception as e:
        # Log the error
        print(f"Error: {e}")
        return None