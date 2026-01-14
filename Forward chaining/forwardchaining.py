import collections

def forward_chaining(clauses, query):
    rules = []
    inferred = set()

    for premises, conclusion in clauses:
        if not premises:
            inferred.add(conclusion)
        else:
            rules.append((premises, conclusion))

    premises_remaining = {rule: len(rule[0]) for rule in rules}

    agenda = collections.deque(inferred)

    while agenda:
        fact = agenda.popleft()
        if fact == query:
            return True

        for rule in rules:
            premises, conclusion = rule
            if fact in premises:
                premises_remaining[rule] -= 1
                if premises_remaining[rule] == 0 and conclusion not in inferred:
                    inferred.add(conclusion)
                    agenda.append(conclusion)

    return query in inferred