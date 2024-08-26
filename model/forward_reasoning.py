from model.rule_set import ruleset

def forward_reasoning(goal, kb):
    if goal in kb:
        return "La meta ya existe en la base de conocimiento"
    new_items = {}
    rules_used = {}
    is_repeating = False

    while goal not in kb and not is_repeating:
        previous_kb = kb.copy()  # Create a copy of the KB
        for rule in ruleset:
            rule_number = rule[0]
            conditions = rule[1]
            if all(knowledge_item in kb for knowledge_item in conditions):
                rules_used[rule_number] = None
                new_items[rule[2]] = None
        kb.update(new_items)
        if kb == previous_kb:  # Check if KB changed
            is_repeating = True
        new_items.clear()

    description = '\n'.join([f"Regla: {keys}" for keys in rules_used.keys()])
    print(kb)
    if goal in kb:
        return description
    else: 
        return "La meta no se puede alcanzar" 

# Main method for trying independently
def main():
    goal = 5
    kb: dict[int, None] = {7: None, 8: None, 1:None, 2:None, 9: None}
    print(forward_reasoning(goal, kb))

if __name__ == '__main__':
    main()
