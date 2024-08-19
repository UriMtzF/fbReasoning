import .ruleset from rule_set

def backward_reasoning(goal, kb, rules_used=None, visited_goals=None):
    if rules_used is None:
        rules_used = []
    if visited_goals is None:
        visited_goals = set()

    # Si el objetivo ya está en la base de conocimiento, retorna verdadero
    if goal in kb:
        return True, f"H{goal} ya está en la base de conocimiento"

    # Evitar bucles infinitos
    if goal in visited_goals:
        return False, f"Se detectó un bucle al intentar alcanzar H{goal}"

    visited_goals.add(goal)

    # Verifica todas las reglas para ver si alguna puede generar la meta
    for rule in ruleset:
        rule_number = rule[0]
        conclusion = rule[2]
        
        # Si la conclusión de la regla es la meta que estamos buscando
        if conclusion == goal:
            # Verifica si todas las condiciones de la regla están satisfechas
            all_conditions_met = True
            for condition in rule[1]:
                # Si una condición no está en la base de conocimiento, intenta satisfacerla recursivamente
                if condition not in kb:
                    subgoal_met, subgoal_message = backward_reasoning(condition, kb, rules_used, visited_goals)
                    if not subgoal_met:
                        all_conditions_met = False
                        break

            # Si todas las condiciones se cumplen, añade la regla a la lista de reglas usadas
            if all_conditions_met:
                rules_used.append(rule_number)
                kb[goal] = None  # Añade la meta a la base de conocimiento
                return True, f"Reglas usadas: {', '.join(f'R{r}' for r in rules_used)}"

    # Si no se puede satisfacer la meta, retorna falso
    return False, f"No se pudo alcanzar H{goal} con la base de conocimiento actual"

# para correrlo 
def main():
    goal = 2
    kb = {7: None, 8: None}
    success, message = backward_reasoning(goal, kb)
    print(message)

if __name__ == '__main__':
    main()