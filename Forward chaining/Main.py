from forwardchaining import *
from helpers import *

if __name__ == "__main__":
    # Read the number of sentences in the knowledge base
    raw_clauses, query = get_input()
    clauses = [parse_clause(cl) for cl in raw_clauses]

    # Run the algorithm
    result = forward_chaining(clauses, query)

    # Note: The template above is just a suggestion. You need to
    # implement the parsing and the main algorithm logic.
    display_result(result) # Placeholder output