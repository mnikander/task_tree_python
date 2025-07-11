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

def build_tree(roots, children):
    tree = []
    for root in roots:
        tree.append(root)
        if root in children:
            tree.append(build_tree(children[root], children))
    return [tree]

def print_tree(tree, level=0):
    for node in tree:
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
    tree = build_tree(roots, children)
    print_tree(tree)

if __name__ == "__main__":
    main()
