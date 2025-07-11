import pandas as pd
import argparse

def sort_by(node):
    return node.task.get("estimate", "")

def print_id_tree(tree, level=0):
    indent = "  " * level
    for node in tree:
        task_id, children = node
        print(f"{indent}- {task_id}")
        print_id_tree(children, level + 1)

def build_id_tree(df):
    # Build a mapping from ID to list of children
    children_map = {}
    id_set = set()

    for _, row in df.iterrows():
        task_id = row["id"].strip()
        parent_id = row["parent"].strip()
        id_set.add(task_id)

        if parent_id:
            children_map.setdefault(parent_id, []).append(task_id)
        else:
            children_map.setdefault(None, []).append(task_id)

    # Recursive function to build tree structure
    def build_node(task_id):
        return [task_id, [build_node(child_id) for child_id in children_map.get(task_id, [])]]

    # Start from root nodes (those with parent_id missing)
    root_ids = children_map.get(None, [])
    tree = [build_node(root_id) for root_id in root_ids]
    return tree

def main():
    parser = argparse.ArgumentParser(description="Print task tree from CSV.")
    parser.add_argument("csv_file", help="Path to CSV file")
    args = parser.parse_args()

    df = pd.read_csv(args.csv_file, dtype=str).fillna("")
    roots = build_id_tree(df)
    print_id_tree(roots)

if __name__ == "__main__":
    main()
