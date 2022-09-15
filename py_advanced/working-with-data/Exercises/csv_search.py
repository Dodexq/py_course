import csv
import os

os.chdir(os.path.dirname(__file__))

state = input("State: ")
year = input("Year: " )

csvfile = "../data/population-by-state.csv"
with open(csvfile, newline="", encoding="utf8") as csvfile:
    popul = csv.DictReader(csvfile)
    for row in popul:
        if row["State"] == state:
            print(f"{state}'s population in {year}: {row[year]}")