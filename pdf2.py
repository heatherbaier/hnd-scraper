import pandas as pd
import numpy as np
import tabula
import os


output_dir = "pdfs2/"

for file_path in os.listdir(output_dir)[0:15]:

    try:

        file_path = output_dir + file_path
        school_id = file_path.split("_")[1].split(".")[0]
        dfs = tabula.read_pdf(file_path, multiple_tables = True)

        totals = dfs[0].values[-1]
        totals = [b for b in totals if not isinstance(b, float)]
        totals = [i.split(" ") for i in totals]
        totals = totals[1:]
        totals = [int(item) for sublist in totals for item in sublist]

        # mat_final = 5
        # apr_final = 17

        pass_percent = totals[17] / totals[5]
        print(totals, len(totals), pass_percent)

        with open("pass_percents2.txt", "a") as f:
            f.write(str(school_id) + " " + str(pass_percent) + "\n")

    except:

        with open("failed_conversion2.txt", "a") as f:
            f.write(str(school_id) + "\n")

    


