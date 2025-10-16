import json, sys
def read_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    print("Top-level keys:", list(data.keys()))
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python json_reader.py <path-to-json>")
    else:
        read_json(sys.argv[1])
