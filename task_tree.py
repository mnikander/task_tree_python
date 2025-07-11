import pandas as pd
import argparse

class TaskNode:
    def __init__(self, task):
        self.task = task
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        indent = "    " * level
        desc = self.task.get("description", "").strip()
        task_id = self.task.get("id", "")
        print(f"{indent}- [{task_id}] {desc}")
        for child in sorted(self.children, key=sort_by):
            child.print_tree(level + 1)

def sort_by(node):
    return node.task.get("estimate", "")

def build_tree(df):
    # Normalize ID fields as strings and strip whitespace
    df["id"] = df["id"].astype(str).str.strip()
    df["parent"] = df["parent"].astype(str).str.strip()
    df.replace("nan", "", inplace=True)  # clean up "nan" from str conversion

    nodes = {}
    root_nodes = []

    # First pass: create all nodes
    for _, row in df.iterrows():
        node = TaskNode(row.to_dict())
        nodes[row["id"]] = node

    # Second pass: attach children to parents
    for task_id, node in nodes.items():
        parent_id = node.task.get("parent", "")
        if parent_id and parent_id in nodes:
            nodes[parent_id].add_child(node)
        else:
            root_nodes.append(node)

    return root_nodes

def main():
    parser = argparse.ArgumentParser(description="Print task tree from CSV.")
    parser.add_argument("csv_file", help="Path to CSV file")
    args = parser.parse_args()

    df = pd.read_csv(args.csv_file, dtype=str).fillna("")
    roots = build_tree(df)

    for root in sorted(roots, key=sort_by):
        root.print_tree()

if __name__ == "__main__":
    main()
