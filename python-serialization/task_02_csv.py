#!/usr/bin/env python3
import csv
import json

def convert_csv_to_json(csvFilePath):
    try:
        with open(csvFilePath, mode="r") as csv:
            csv_reader = csv.DictReader(csv)
            csv_data = [row for row in csv_reader]

        json_data = json.dumps(data, ident=4)

        with open("data.json", mode="w") as json_file:
            json_file.write(json_data)

        return True
    except FileNotFoundError:
        print("file not found.")
        return False
