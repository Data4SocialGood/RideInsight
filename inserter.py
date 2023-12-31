import csv
import argparse
from pymongo import MongoClient

"""
CSV using ; to separate values
"""

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filename', type=str, required=True, help='CSV file to import')
parser.add_argument('-c', '--collection', type=str, required=True, help='MongoDB collection to insert into')
parser.add_argument('-s', '--separator', type=str, required=False, default=';', help='value separator')
args = parser.parse_args()


client = MongoClient('mongodb://localhost:27017/')
db = client['OASA1']
collection = db[args.collection]


try:
    data = []
    with open(args.filename, 'r', encoding='utf-8-sig') as ake:
        reader = csv.DictReader(ake, delimiter=args.separator)
        for row in reader:
            data.append(row)
            #collection.insert_one(row)
        collection.insert_many(data)
except:
    #print("problmatic row: ", row, ' file: ', args.filename)
    print('problmatic row at', 'file: ', args.filename)
