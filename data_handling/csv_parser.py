import csv, sys
def read_csv(path, limit=5):
    with open(path, newline='') as f:
        reader = csv.reader(f)
        for i, row in enumerate(reader):
            print(row)
            if i + 1 >= limit:
                break
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python csv_parser.py <path-to-csv>")
    else:
        read_csv(sys.argv[1])
