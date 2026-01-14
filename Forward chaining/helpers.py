def get_input():
    num_clauses = int(input())
    clauses_raw = [input() for _ in range(num_clauses)]

    if num_clauses != len(clauses_raw):
        print(f"Error: Expected {num_clauses} lines of input.")
        exit(1)

    query = input()
    return clauses_raw, query

def parse_clause(clause: str):
    clause = clause.strip()
    if "->" in clause:
        left, right = clause.split("->")
        premises = tuple(p.strip() for p in left.split("&"))
        conclusion = right.strip()
        return premises, conclusion
    else:
        return (), clause

def display_result(result: bool):
    if result:
        print("YES")
    else:
        print("NO")