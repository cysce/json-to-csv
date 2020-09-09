import pandas as pd

if len(sys.argv) != 2:
    print ("\nUsage: python json-to-csv.py <json_in_file_path> <csv_out_file_path>\n")
else:
    #Reading arguments
    json_file_path = sys.argv[1]
    csv_file_path = sys.argv[2]
        
    df = pd.read_json(json_file_path)
    #df = pd.read_json(json_file_path, orient='index')
    df.to_csv(csv_file_path, index = None, header=True)
    
    print ("File CSV created")
