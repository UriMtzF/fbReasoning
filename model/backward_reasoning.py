from model.rule_set import ruleset

def backward_reasoning(goal, kb, rules_used=None, visited_goals=None):
    if rules_used is None:
        rules_used = []
    if visited_goals is None:
        visited_goals = set()

    if goal in kb:
        return True, f"H{goal} ya está en la base de conocimiento"

    if goal in visited_goals:
        return False, f"Se detectó un bucle al intentar alcanzar H{goal}"

    visited_goals.add(goal)

    applicable_rules = [rule for rule in ruleset if rule[2] == goal]

    if not applicable_rules:  # Check if there are any applicable rules
        return False, f"No se pudo alcanzar H{goal} con la base de conocimiento actual"

    for rule in applicable_rules:
        rule_number = rule[0]
        all_conditions_met = True
        for condition in rule[1]:
            if condition not in kb:
                subgoal_met, subgoal_message = backward_reasoning(condition, kb, rules_used, visited_goals)
                if not subgoal_met:
                    all_conditions_met = False
                    break

        if all_conditions_met:
            rules_used.append(rule_number)
            kb[goal] = None
            return True, "\n".join(f'Regla: {r}' for r in rules_used)

    return False, f"No se pudo alcanzar H{goal} con la base de conocimiento actual"


# para correrlo
def main():
    goal = 2
    kb = {7: None, 8: None}
    success, message = backward_reasoning(goal, kb)
    print(message)

if __name__ == '__main__':
    main()
