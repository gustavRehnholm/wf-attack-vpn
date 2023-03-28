# basic script to run from start to end


# Extract VPN traffic, and store them depending on the application
touch stdout/extract_dataset.txt
python wf-attack-vpn/Parse_noise/MIT-h5-parsing/extract_dataset.py | tee stdout/extract_dataset.txt


# Divide the captures after application useage
touch stdout/split_dataset_application.txt
python wf-attack-vpn/Parse_noise/MIT-h5-parsing/split_dataset_application.py | tee stdout/split_dataset_application.txt


# Parse the data (from one capture per row, to one packet per row)
touch stdout/parse_dataset.txt
python wf-attack-vpn/Parse_noise/MIT-h5-parsing/parse_dataset.py | tee stdout/parse_dataset.txt


# Merge the data after category
touch stdout/parse_dataset.txt
python wf-attack-vpn/Parse_noise/MIT-h5-parsing/parse_dataset.py | tee stdout/parse_dataset.txt



