import pandas as pd
import numpy as np
import tabula
import os


output_dir = "pdfs/"

for file_path in os.listdir(output_dir):

    try:

        file_path = output_dir + file_path
        school_id = file_path.split("_")[1].split(".")[0]
        dfs = tabula.read_pdf(file_path, multiple_tables = True)
        means = []

        for df in dfs:

            if "Comunicación / Español" in df.columns:

                df = df[['Unnamed: 0', 'Unnamed: 3', 'Comunicación / Español']][2:]
                df["Comunicación / Español"] = df["Comunicación / Español"].str.split(" ").str[2]
                df["grade"] = df["Unnamed: 0"].str.split(" ").str[0]
                df = df.drop(["Unnamed: 0"], axis = 1)
                df = df.rename(columns = {"Unnamed: 3": "total_eval", "Comunicación / Español": "total_passed"})
                # df = df.fillna(0)
                df["pass_percent"] = (df["total_passed"].astype(int) / df["total_eval"].astype(int)) * 100
                means.append(df["pass_percent"].mean())

            elif "Matemáticas" in df.columns:

                df = df[['Unnamed: 0', 'Unnamed: 3', 'Unnamed: 4']][2:]
                df["grade"] = df["Unnamed: 0"].str.split(" ").str[0]
                df = df.drop(["Unnamed: 0"], axis = 1)
                df = df.rename(columns = {"Unnamed: 3": "total_eval", "Unnamed: 4": "total_passed"})
                # df = df.fillna(0)
                df["pass_percent"] = (df["total_passed"].astype(int) / df["total_eval"].astype(int)) * 100
                means.append(df["pass_percent"].mean())

            elif "Ciencias Naturales" in df.columns:

                df = df[['Unnamed: 0', 'Unnamed: 3', 'Ciencias Naturales']][2:]
                df["Ciencias Naturales"] = df["Ciencias Naturales"].str.split(" ").str[2]
                df["grade"] = df["Unnamed: 0"].str.split(" ").str[0]
                df = df.drop(["Unnamed: 0"], axis = 1)
                df = df.rename(columns = {"Unnamed: 3": "total_eval", "Ciencias Naturales": "total_passed"})
                df = df.fillna(0)
                df["pass_percent"] = (df["total_passed"].astype(int) / df["total_eval"].astype(int)) * 100  
                # df = df.fillna(0)
                means.append(df["pass_percent"].mean())

            elif "Ciencias Sociales" in df.columns:

                df = df[['Unnamed: 0', 'Unnamed: 3', 'Ciencias Sociales']][2:]
                df["Ciencias Sociales"] = df["Ciencias Sociales"].str.split(" ").str[2]
                df["grade"] = df["Unnamed: 0"].str.split(" ").str[0]
                df = df.drop(["Unnamed: 0"], axis = 1)
                df = df.rename(columns = {"Unnamed: 3": "total_eval", "Ciencias Sociales": "total_passed"})
                # df = df.fillna(0)
                df["pass_percent"] = (df["total_passed"].astype(int) / df["total_eval"].astype(int)) * 100   
                means.append(df["pass_percent"].mean())



        with open("pass_percents.txt", "a") as f:
            f.write(str(school_id) + " " + str(np.mean(means)) + "\n")

    except:

        with open("failed_conversion.txt", "a") as f:
            f.write(str(school_id) + "\n")