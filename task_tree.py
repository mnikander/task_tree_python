import pandas as pd
import argparse

def sort_by(node):
    return node.task.get("estimate", "")

def find_children(df):
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

def substitute(roots, children):
    tree = []
    for root in roots:
        tree.append(root)
        if root in children:
            tree.append(substitute(children[root], children))
    return tree

def main():
    parser = argparse.ArgumentParser(description="Print task tree from CSV.")
    parser.add_argument("csv_file", help="Path to CSV file")
    args = parser.parse_args()
    df = pd.read_csv(args.csv_file, dtype=str).fillna("")
    [roots, children] = find_children(df)

    tree = substitute(roots, children)
    print(tree)

if __name__ == "__main__":
    main()
