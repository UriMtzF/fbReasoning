from rule_set import ruleset

def forward_reasoning(goal, kb):
    if goal in kb:
        return "La meta ya existe en la base de conocimiento"
    new_items = {}
    rules_used = {}
    # Repeats the process until it finds the goal
    # TODO: Fix for the case when is not possible to find the goal using the ruleset
    while goal not in kb:
        # Search all facts from the KB
        for h in kb:
            ##print(f"Using fact H{h} from KB")
            found_in = []
            # Searches in all rules in the ruleset
            for rule in ruleset:
                rule_number = rule[0]
                conditions = rule[1]
                # If the fact is in the conditions, add it to the local rule list
                if h in conditions:
                    found_in.append(rule_number)
            ##print(f"Found in rules {found_in}")
            # From the list previously made use all
            for local_rule in found_in:
                # From the ruleset use each rule
                for rule in ruleset:
                    # If the local rule (found in the causes) is also in the ruleset and
                    # all of its causes are present in the KB, add the conclusion to the KB
                    if local_rule == rule[0] and all(knowledge_item in kb for knowledge_item in rule[1]):
                        ##print(f"The rule conclusion ({rule[2]}) of rule {rule[0]} should be added")
                        rules_used[rule[0]] = None
                        new_items[rule[2]] = None
        # Updates the KB in each cycle for continuing the search
        kb.update(new_items)
    # Returns the list of rules like: "Regla: i\n"
    description = '\n'.join([f"Regla: {keys}" for keys in rules_used.keys()])
    return description


# Main method for trying independently
def main():
    goal = 2
    kb: dict[int, None] = {7: None, 8: None}
    print(forward_reasoning(goal, kb))


if __name__ == '__main__':
    main()