import pandas as pd
import argparse

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

def build_trees(roots, children):
    trees = []
    for root in roots:
        if root in children:
            trees.append(root)
            trees.append(build_trees(children[root], children))
        else:
            trees.append(root)
    return trees

def print_tree(trees, level=0):
    for node in trees:
        if isinstance(node, list):
            print_tree(node, level + 1)
        else:
            print("  " * level + str(node))

def main():
    parser = argparse.ArgumentParser(description="Print task tree from CSV.")
    parser.add_argument("csv_file", help="Path to CSV file")
    args = parser.parse_args()
    df = pd.read_csv(args.csv_file, dtype=str).fillna("")
    [roots, children] = find_roots_and_children(df)
    trees = build_trees(roots, children)
    print_tree(trees)

if __name__ == "__main__":
    main()
