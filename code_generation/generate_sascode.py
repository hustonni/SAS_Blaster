# Create SAS code block based on user inputs

import os # For path specifications

# Specify template (general structure) and target file (file to be written)
template = os.path.dirname(__file__) + "\\templates\\proc_means.txt"
target = os.path.dirname(__file__) + "\\created_blocks\\proc_means_output.txt"


# Search for dataset name
text_to_search = "*data_set*"

# Replace with user input
replacement_text = "user_data"

# Open template, replace specified variable, and write to output file
with open(template, "r") as read_file:
    with open(target, "w") as write_file:
        for line in read_file:

        	# Replace dataset name
            write_file.write(line.replace(text_to_search, replacement_text))