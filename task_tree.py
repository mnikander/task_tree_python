import pandas as pd
import argparse

#
#     4      1
#    / \     |
#   6   5    2
#            |
#            3
#

def find_roots_and_children(df):
    children = {}
    roots = []
    for _, row in df.iterrows():
        current = row["id"].strip()
        parent  = row["parent"].strip()
        if parent:
            children.setdefault(parent, [])
            children[parent].append(current)
        else:
            roots.append(current)
    return [roots, children];

def make_integer(str):
    if str.strip() == "":
        return 0
    else:
        return int(str)

def print_children(dictionary, roots, children, level=0):
    for root in sorted(roots, key=lambda x: make_integer(dictionary.get(x, "").get("estimate", ""))):
        if root in children:
            level = print_children(dictionary, children[root], children)
        row = dictionary.get(root, {})
        indent    = '    ' * level
        status    = row.get("status", "").strip()
        important = '*' if row.get("important", "").strip() == 'T' else ' '
        urgent    = '!' if row.get("urgent", "").strip() == 'T' else ' '
        description = row.get("description", "").strip()
        if (status != 'done'):
            print(f"{root} {important}{urgent} {status.ljust(8)} {indent}- {description}")
    return level+1

def main():
    parser = argparse.ArgumentParser(description="Print task tree from CSV.")
    parser.add_argument("csv_file", help="Path to CSV file")
    args = parser.parse_args()
    df = pd.read_csv(args.csv_file, dtype=str).fillna("")
    [roots, children] = find_roots_and_children(df)
    dictionary = {row["id"]: row for _, row in df.iterrows()}
    print_children(dictionary, roots, children, 0)

if __name__ == "__main__":
    main()
