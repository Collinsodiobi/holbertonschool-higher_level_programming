#!/usr/bin/env python3

import csv
import json


def convert_csv_to_json(filename):
    try:
        # Read CSV file
        with open(filename, mode="r", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        # Write JSON file
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except FileNotFoundError:
        return False
