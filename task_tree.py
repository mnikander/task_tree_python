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

def indent(level):
    return '    ' * level;

def print_children(roots, children, level=0):
    for root in roots:
        if root in children:
            level = print_children(children[root], children)
        print(indent(level) + root)
    return level+1

def main():
    parser = argparse.ArgumentParser(description="Print task tree from CSV.")
    parser.add_argument("csv_file", help="Path to CSV file")
    args = parser.parse_args()
    df = pd.read_csv(args.csv_file, dtype=str).fillna("")
    [roots, children] = find_roots_and_children(df)
    print_children(roots, children)

if __name__ == "__main__":
    main()
