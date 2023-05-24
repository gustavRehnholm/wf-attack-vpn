# Parsing data from RDS collect
This is for scripts to use data collected by [rds-collect](https://github.com/C-Sand/rds-collect), as background traffic. It should be able to use for all data gathered by rds-collect.

Before parsing the generated data, analyze it (scripts are in data_analysis/foreground_analysis), and sort out unusable captures.

## Scripts

### main.py
Script that run all steps to go from a raw dataset, to one merged dataset.

### log_2_h5.py
convert the data to hdf5 file format, which the data then will stay as 

### parse_background.py
Parse the captures (as hdf5 format)

### merge_parsed.py
merge the parsed captures, to one large dataset, which can be used as a background dataset