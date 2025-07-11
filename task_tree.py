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

def build_forest(roots, children):
    forest = []
    for root in roots:
        if root in children:
            forest.append(root)
            forest.append(build_forest(children[root], children))
        else:
            forest.append(root)
    return forest

def print_forest(forest, level=0):
    for tree in forest:
        if isinstance(tree, list):
            print_forest(tree, level + 1)
        else:
            print("  " * level + str(tree))

def main():
    parser = argparse.ArgumentParser(description="Print task tree from CSV.")
    parser.add_argument("csv_file", help="Path to CSV file")
    args = parser.parse_args()
    df = pd.read_csv(args.csv_file, dtype=str).fillna("")
    [roots, children] = find_roots_and_children(df)
    forest = build_forest(roots, children)
    print_forest(forest)

if __name__ == "__main__":
    main()
