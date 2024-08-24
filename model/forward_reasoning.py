from model.rule_set import ruleset

def forward_reasoning(goal, kb):
    if goal in kb:
        return "La meta ya existe en la base de conocimiento"
    new_items = {}
    rules_used = {}
    is_repeating = False
    previous_kb_size = len(kb)  # Keep track of the KB size

    while goal not in kb and not is_repeating:
        for h in kb:
            found_in = []
            for rule in ruleset:
                rule_number = rule[0]
                conditions = rule[1]
                if h in conditions:
                    found_in.append(rule_number)
            for local_rule in found_in:
                for rule in ruleset:
                    if local_rule == rule[0] and all(knowledge_item in kb for knowledge_item in rule[1]):
                        rules_used[rule[0]] = None
                        new_items[rule[2]] = None
        if new_items == {} or len(kb) == previous_kb_size:  # Check if KB size changed
            is_repeating = True
        kb.update(new_items)
        previous_kb_size = len(kb)  # Update previous KB size
        new_items.clear()

    description = '\n'.join([f"Regla: {keys}" for keys in rules_used.keys()])
    if goal in kb:
        return description
    else: 
        return "La meta no se puede alcanzar"  # Indicate that the goal is unreachable



# Main method for trying independently
def main():
    goal = 2
    kb: dict[int, None] = {7: None, 8: None}
    print(forward_reasoning(goal, kb))


if __name__ == '__main__':
    main()