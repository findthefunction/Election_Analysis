


#      :::::::::  :::   :::          :::::::::   ::::::::  :::        :::  
#     :+:    :+: :+:   :+:          :+:    :+: :+:    :+: :+:        :+:   
#    +:+    +:+  +:+ +:+           +:+    +:+ +:+    +:+ +:+        +:+    
#   +#++:++#+    +#++:            +#++:++#+  +#+    +:+ +#+        +#+     
#  +#+           +#+             +#+        +#+    +#+ +#+        +#+      
#  #+#           #+#             #+#        #+#    #+# #+#        #+#       
#####           ###             ###         ########  ########## ########## 



#   Project out comes:

# #  Total Number of Votes cast

# # #  A complete list of candidates who received votes

# # # #  Total number of votes each candidate received

# # #  Percentage of votes each candidate won

# #  The winner of the election based on popular vote   



#   1. Load Data Set

##  Import the datetime class from the dateime module

import os 
import csv
import random
import numpy as np

# Assign a variable to load a file from a path.

file_to_load = os.path.join("Resources", "election_results.csv")

#  Assign a variable to save the file to a path.

file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file.

with open(file_to_load) as election_data:

    ## Open the election results and read the file.
    
    file_reader = csv.reader(election_data)

    ## Read and print the header row in the CSV file.
    
    headers = next(file_reader)
    
    print(headers)
   

## Close the file

#   2. Compile a list of all the candidates

#   3. Add a vote for each candidate

#   4. Get the total votes for each candidate

#   5. Get the total votes cast for the election


