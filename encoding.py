import argparse
import csv

parser = argparse.ArgumentParser(description='Decode Unicode escape sequences in a CSV file')
parser.add_argument('--file', dest='input_filename', required=True,
                    help='input CSV file name')
args = parser.parse_args()

output_filename = "output.csv"
encodings = ['utf-8', 'windows-1251', 'iso-8859-1', 'cp1252']

for encoding in encodings:
    try:
        with open(args.input_filename, "rb") as input_file:
            content = input_file.read().decode(encoding, errors='ignore')
        with open(output_filename, "w", encoding="utf-8", newline='') as output_file:
            writer = csv.writer(output_file)
            reader = csv.reader(content.splitlines())

            for row in reader:
                new_row = []
                for cell in row:
                    decoded_cell = bytes(cell, encoding).decode("unicode_escape")
                    new_row.append(decoded_cell)
                writer.writerow(new_row)

            break  # stop if we found a working encoding
    except (UnicodeDecodeError, csv.Error):
        continue  # try next encoding
else:
    print('Unable to read file with any of the specified encodings')
