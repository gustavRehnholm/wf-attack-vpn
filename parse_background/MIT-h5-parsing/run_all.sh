# basic script to run from start to end

# Extract VPN traffic, and store them depending on the application
python wf-attack-vpn/Parse_noise/MIT-h5-parsing/extract_dataset.py

# Divide the captures after application useage
python wf-attack-vpn/Parse_noise/MIT-h5-parsing/split_dataset_application.py

# Parse the data (from one capture per row, to one packet per row)
python wf-attack-vpn/Parse_noise/MIT-h5-parsing/parse_dataset.py

# Merge the data after category
python wf-attack-vpn/Parse_noise/MIT-h5-parsing/parse_dataset.py