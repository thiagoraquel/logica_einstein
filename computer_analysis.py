from collections import deque
import copy
import time
import random

# --- ESTRUTURAS DE DADOS GLOBAIS ---

# Lista para armazenar as restrições definidas pelo usuário
# Cada restrição será um dicionário com seus detalhes
user_constraints = []

# Variáveis
vars_cor = ['Casa1_cor', 'Casa2_cor', 'Casa3_cor', 'Casa4_cor', 'Casa5_cor']
vars_nac = ['Casa1_nac', 'Casa2_nac', 'Casa3_nac', 'Casa4_nac', 'Casa5_nac']
vars_beb = ['Casa1_beb', 'Casa2_beb', 'Casa3_beb', 'Casa4_beb', 'Casa5_beb']
vars_cig = ['Casa1_cig', 'Casa2_cig', 'Casa3_cig', 'Casa4_cig', 'Casa5_cig']
vars_pet = ['Casa1_pet', 'Casa2_pet', 'Casa3_pet', 'Casa4_pet', 'Casa5_pet']
vars_all = vars_nac + vars_cor + vars_cig + vars_pet + vars_beb

# Definições iniciais das categorias e seus possíveis valores
categories = {
    'cor': ['Branco', 'Verde', 'Azul', 'Amarelo', 'Vermelho'],
    'nac': ['Noruegues', 'Ingles', 'Alemao', 'Sueco', 'Dinamarques'],
    'cig': ['Dunhill', 'Blends', 'Pall Mall', 'Prince', 'Blue Master'],
    'pet': ['Cavalo', 'Peixe', 'Passaro', 'Cachorro', 'Gato'],
    'beb': ['Cha', 'Agua', 'Leite', 'Cafe', 'Cerveja'],
}

# Template do domínio inicial para cada variável
domain_template = {}
for cat, values in categories.items():
    for i in range(1, 6):
        var = f'Casa{i}_{cat}'
        domain_template[var] = set(values)

# Restrições binárias (arestas) para AC-3
arcs = set()
for var1 in vars_all:
    for var2 in vars_all:
        if var1 != var2:
            arcs.add((var1, var2))

# --- LÓGICA DE VERIFICAÇÃO DE RESTRIÇÕES (MODIFICADA) ---

def remove_borda_dominios(dom, cat_x, val_x, cat_y, val_y):
    """
    Remove val_x da casa 5 e val_y da casa 1, com suas respectivas categorias.
    Usado para otimizar domínios em relações com orientação (esquerda/direita).
    """
    var_x = f"Casa5_{cat_x}"
    var_y = f"Casa1_{cat_y}"
    dom[var_x].discard(val_x)
    dom[var_y].discard(val_y)

def constraint(arc_x, value_x, arc_y, value_y):
    """
    Verifica se um par de valores para um par de variáveis é válido.
    Agora, em vez de regras fixas, itera sobre a lista 'user_constraints'.
    """
    pos_x = int(arc_x[4])
    pos_y = int(arc_y[4])
    cat_x = arc_x.split('_')[1]
    cat_y = arc_y.split('_')[1]

    # Itera sobre cada regra que o usuário adicionou
    for rule in user_constraints:
        # TIPO: Mesma casa (ex: O Inglês mora na casa Vermelha)
        if rule['type'] == 'same_house':
            # Verifica se as variáveis atuais correspondem à regra
            # (Ex: arc_x é 'nac' com valor 'Ingles' e arc_y é 'cor' com valor 'Vermelho')
            if (cat_x == rule['cat1'] and value_x == rule['val1'] and
                cat_y == rule['cat2'] and value_y != rule['val2'] and pos_x == pos_y):
                return False
            if (cat_x == rule['cat2'] and value_x == rule['val2'] and
                cat_y == rule['cat1'] and value_y != rule['val1'] and pos_x == pos_y):
                return False

        # TIPO: Casas vizinhas (ex: O fumante de Blends é vizinho de quem tem Gato)
        if rule['type'] == 'neighbor':
            if ((cat_x == rule['cat1'] and value_x == rule['val1'] and
                 cat_y == rule['cat2'] and value_y == rule['val2']) or
                (cat_x == rule['cat2'] and value_x == rule['val2'] and
                 cat_y == rule['cat1'] and value_y == rule['val1'])):
                if abs(pos_x - pos_y) != 1:
                    return False

        # TIPO: Imediatamente à esquerda de (ex: A casa Verde fica imediatamente à esquerda da Branca)
        if rule['type'] == 'neighbor_left_of':
            if ((cat_x == rule['left_cat'] and value_x == rule['left_val'] and
                 cat_y == rule['right_cat'] and value_y == rule['right_val'])):
                if pos_x != pos_y - 1:
                    return False
            if ((cat_x == rule['right_cat'] and value_x == rule['right_val'] and
                 cat_y == rule['left_cat'] and value_y == rule['left_val'])):
                if pos_y != pos_x - 1:
                    return False
        
        # TIPO: Imediatamente à direita de (ex: A casa Verde fica imediatamente à direita da Branca)
        if rule['type'] == 'neighbor_right_of':
            if ((cat_x == rule['left_cat'] and value_x == rule['left_val'] and
                 cat_y == rule['right_cat'] and value_y == rule['right_val'])):
                if pos_x != pos_y + 1:
                    return False
            if ((cat_x == rule['right_cat'] and value_x == rule['right_val'] and
                 cat_y == rule['left_cat'] and value_y == rule['left_val'])):
                if pos_y != pos_x + 1:
                    return False
                
        # TIPO: À esquerda de (ex: A casa Verde fica à esquerda (qualquer posição) da Branca)
        if rule['type'] == 'left_of':
            if ((cat_x == rule['left_cat'] and value_x == rule['left_val'] and
                 cat_y == rule['right_cat'] and value_y == rule['right_val'])):
                if pos_x >= pos_y:
                    return False
            if ((cat_x == rule['right_cat'] and value_x == rule['right_val'] and
                 cat_y == rule['left_cat'] and value_y == rule['left_val'])):
                if pos_y >= pos_x:
                    return False
                
        # TIPO: À direita de (ex: A casa Verde fica à direita (qualquer posição) da Branca)
        if rule['type'] == 'right_of':
            if ((cat_x == rule['left_cat'] and value_x == rule['left_val'] and
                 cat_y == rule['right_cat'] and value_y == rule['right_val'])):
                if pos_x <= pos_y:
                    return False
            if ((cat_x == rule['right_cat'] and value_x == rule['right_val'] and
                 cat_y == rule['left_cat'] and value_y == rule['left_val'])):
                if pos_y <= pos_x:
                    return False

    # RESTRIÇÃO FUNDAMENTAL: Se são da mesma categoria (ex: "_cor"), não podem ter o mesmo valor
    # em casas diferentes.
    if cat_x == cat_y and pos_x != pos_y and value_x == value_y:
        return False
        
    # RESTRIÇÃO FUNDAMENTAL: Se são da mesma casa, mas de categorias diferentes, tudo bem por padrão.
    # Mas se são de categorias iguais, os valores devem ser iguais (redundante mas seguro).
    if pos_x == pos_y and cat_x == cat_y and value_x != value_y:
        return False

    return True  # Se nenhuma restrição do usuário foi violada

# --- ALGORITMOS DE SOLUÇÃO (SEM ALTERAÇÕES) ---

def revise(domain, arc_x, arc_y):
    revised = False
    to_remove = set()
    for value_x in domain[arc_x]:
        if not any(constraint(arc_x, value_x, arc_y, value_y) for value_y in domain[arc_y]):
            to_remove.add(value_x)
            revised = True
    domain[arc_x] -= to_remove
    return revised

def ac3(dom, arcs):
    queue = deque(arcs)
    while queue:
        arc_x, arc_y = queue.popleft()
        if revise(dom, arc_x, arc_y):
            if not dom[arc_x]:
                return False
            # Otimização: Re-adicionar apenas arcos relevantes
            # detalhe: aqui só funciona se os arcs tiverem todos os casos
            # em compensação é mais eficiente)
            for var_k in vars_all:
                if var_k != arc_y and (var_k, arc_x) in arcs:
                    queue.append((var_k, arc_x))
    return True

def print_horizontal(assignment):
    casas = {i: {} for i in range(1, 6)}
    for var, val in assignment.items():
        casa_num = int(var[4])
        cat = var.split('_')[1]
        casas[casa_num][cat] = val

    categorias = sorted(list(categories.keys()))
    print("\n" + "-" * 80)
    print("          ", end="")
    for i in range(1, 6):
        print(f"Casa {i:<12}", end="")
    print()
    for cat in categorias:
        print(f"{cat.capitalize():<10}", end="")
        for i in range(1, 6):
            valor = casas[i].get(cat, "—")
            print(f"{valor:<14}", end="")
        print()
    print("-" * 80)

def brute_force(domains):
    assignment = {}

    def backtrack():
        if len(assignment) == len(domains):
            #print_horizontal(assignment);input("✅ Solução completa encontrada! Pressione Enter para continuar.")
            return assignment.copy()

        # Escolhe a variável com menor domínio entre as não atribuídas
        # Em caso de empate (mesmo tamanho de domínio), desempata aleatoriamente
        unassigned = [v for v in domains if v not in assignment]
        random.shuffle(unassigned)  # evita ordem fixa entre categorias como 'beb', 'cig', etc
        var = min(unassigned, key=lambda v: len(domains[v]))

        # Embaralha os valores possíveis para evitar sempre tentar em ordem alfabética
        values = list(domains[var])
        random.shuffle(values)

        # Tenta os valores na ordem embaralhada
        for value in values:
            is_consistent = True
            for other in assignment:
                if not constraint(var, value, other, assignment[other]):
                    is_consistent = False
                    break
            
            if is_consistent:
                assignment[var] = value
                #print_horizontal(assignment);input(f"Tentando {var} = {value} ... Pressione Enter para continuar.")
                result = backtrack()
                if result:
                    return result
                del assignment[var]
                #print_horizontal(assignment);input(f"⏪ Backtracking de {var} = {value} ... Pressione Enter para continuar.")
        return None

    return backtrack()

# --- INTERFACE COM O USUÁRIO (NOVA FUNCIONALIDADE) ---

def print_options():
    """Mostra as categorias e valores disponíveis para o usuário."""
    print("\n--- Categorias e Valores Disponíveis ---")
    for cat, values in categories.items():
        print(f"  {cat.capitalize()}: {', '.join(values)}")
    print("----------------------------------------")

def get_input_from_options(prompt, options):
    """Pede um input ao usuário e valida contra uma lista de opções."""
    while True:
        user_input = input(f"{prompt} ({', '.join(options)}): ").strip().capitalize()
        if user_input in options:
            return user_input
        # Tratamento especial para 'Noruegues', 'Ingles', etc que podem não capitalizar corretamente
        for option in options:
            if user_input.lower() == option.lower():
                return option
        print(f"Opção inválida. Por favor, escolha uma das opções disponíveis.")

def get_user_constraints(dom):
    """
    Função principal para obter as restrições do usuário através do terminal.
    Modifica 'user_constraints' (global) e 'dom' (local).
    """
    print("Bem-vindo ao Solucionador de Logigramas!")
    print("Vamos adicionar as restrições do problema uma a uma.")

    while True:
        print("\nEscolha o tipo de restrição a adicionar:")
        print("1. Atributos na mesma casa (ex: O Inglês mora na casa Vermelha)")
        print("2. Atributos em casas vizinhas (ex: A casa Azul é vizinha da casa do Norueguês)")
        print("3. Relação 'está em' (ex: O Norueguês mora na Casa 1)")
        print("4. Relação 'imediatamente à esquerda de' (ex: A casa Verde está imediatamente à esquerda da Branca)")
        print("5. Relação 'imediatamente à direita de' (ex: A casa Verde está imediatamente à direita da Branca)")
        print("6. Relação 'à esquerda de' (qualquer posição) (ex: A casa Verde está à esquerda (qualquer posição) da Branca)")
        print("7. Relação 'à direita de' (qualquer posição) (ex: A casa Verde está à direita (qualquer posição) da Branca)")
        print("8. Relação 'não está em' (ex: o Norueguês não está na casa 1)")                        
        print("\nDigite 'S' para solucionar o problema com as restrições atuais.")

        choice = input("Sua escolha: ").strip().lower()

        if choice == 's':
            print("\nIniciando a solução do problema...")
            return True

        elif choice == '1': # Mesma Casa
            print_options()
            print("-- Nova Restrição: Mesma Casa --")
            cat1 = get_input_from_options("Categoria do primeiro atributo", list(categories.keys()))
            val1 = get_input_from_options(f"Valor para '{cat1}'", categories[cat1])
            cat2 = get_input_from_options("Categoria do segundo atributo", list(categories.keys()))
            val2 = get_input_from_options(f"Valor para '{cat2}'", categories[cat2])
            user_constraints.append({'type': 'same_house', 'cat1': cat1, 'val1': val1, 'cat2': cat2, 'val2': val2})
            print(f"✅ Restrição adicionada: 'Quem tem {cat1} {val1} também tem {cat2} {val2}'.")

        elif choice == '2': # Casas Vizinhas
            print_options()
            print("-- Nova Restrição: Casas Vizinhas --")
            cat1 = get_input_from_options("Categoria do primeiro atributo", list(categories.keys()))
            val1 = get_input_from_options(f"Valor para '{cat1}'", categories[cat1])
            cat2 = get_input_from_options("Categoria do segundo atributo", list(categories.keys()))
            val2 = get_input_from_options(f"Valor para '{cat2}'", categories[cat2])
            user_constraints.append({'type': 'neighbor', 'cat1': cat1, 'val1': val1, 'cat2': cat2, 'val2': val2})
            print(f"✅ Restrição adicionada: 'A casa com {cat1} {val1} é vizinha da casa com {cat2} {val2}'.")

        elif choice == '3': # Posição Exata
            print_options()
            print("-- Nova Restrição: Posição Exata --")
            pos = int(get_input_from_options("Número da casa", [str(i) for i in range(1, 6)]))
            cat = get_input_from_options("Categoria do atributo", list(categories.keys()))
            val = get_input_from_options(f"Valor para '{cat}'", categories[cat])
            
            # Esta é uma restrição unária, podemos aplicá-la diretamente ao domínio
            var_name = f'Casa{pos}_{cat}'
            dom[var_name] = {val}
            print(f"✅ Restrição de domínio adicionada: '{var_name}' foi definido como '{val}'.")
            
        elif choice == '4': # Vizinho À esquerda De
            print_options()
            print("-- Nova Restrição: 'Imediatamente À Esquerda De' --")
            print("Defina a casa da ESQUERDA:")
            left_cat = get_input_from_options("Categoria da casa da esquerda", list(categories.keys()))
            left_val = get_input_from_options(f"Valor para '{left_cat}'", categories[left_cat])
            print("Defina a casa da DIREITA:")
            right_cat = get_input_from_options("Categoria da casa da direita", list(categories.keys()))
            right_val = get_input_from_options(f"Valor para '{right_cat}'", categories[right_cat])
            user_constraints.append({'type': 'neighbor_left_of', 'left_cat': left_cat, 'left_val': left_val, 'right_cat': right_cat, 'right_val': right_val})
            print(f"✅ Restrição adicionada: 'A casa com {left_cat} {left_val} está imediatamente à esquerda da casa com {right_cat} {right_val}'.")
        
        elif choice == '5': # Vizinho À direita De 
            print_options()
            print("-- Nova Restrição: 'Imediatamente À Direita De' --")
            print("Defina a casa da ESQUERDA:")
            right_cat = get_input_from_options("Categoria da casa da esquerda", list(categories.keys()))
            right_val = get_input_from_options(f"Valor para '{right_cat}'", categories[right_cat])
            print("Defina a casa da DIREITA:")
            left_cat = get_input_from_options("Categoria da casa da direita", list(categories.keys()))
            left_val = get_input_from_options(f"Valor para '{left_cat}'", categories[left_cat])
            user_constraints.append({'type': 'neighbor_right_of', 'left_cat': left_cat, 'left_val': left_val, 'right_cat': right_cat, 'right_val': right_val})
            print(f"✅ Restrição adicionada: 'A casa com {left_cat} {left_val} está imediatamente à direita da casa com {right_cat} {right_val}'.")

        elif choice == '6': #À esquerda de (qualquer posição)
            print_options()
            print("-- Nova Restrição: 'À Esquerda De (qualquer posição)' --")
            print("Defina a casa da ESQUERDA:")
            left_cat = get_input_from_options("Categoria da casa da esquerda", list(categories.keys()))
            left_val = get_input_from_options(f"Valor para '{left_cat}'", categories[left_cat])
            print("Defina a casa da DIREITA:")
            right_cat = get_input_from_options("Categoria da casa da direita", list(categories.keys()))
            right_val = get_input_from_options(f"Valor para '{right_cat}'", categories[right_cat])
            user_constraints.append({'type': 'left_of', 'left_cat': left_cat, 'left_val': left_val, 'right_cat': right_cat, 'right_val': right_val})
            print(f"✅ Restrição adicionada: 'A casa com {left_cat} {left_val} está à esquerda (qualquer posição) da casa com {right_cat} {right_val}'.")
        
        elif choice == '7': #À direita de (qualquer posição)
            print_options()
            print("-- Nova Restrição: 'À Direita De (qualquer posição)' --")
            print("Defina a casa da ESQUERDA:")
            right_cat = get_input_from_options("Categoria da casa da esquerda", list(categories.keys()))
            right_val = get_input_from_options(f"Valor para '{right_cat}'", categories[right_cat])
            print("Defina a casa da DIREITA:")
            left_cat = get_input_from_options("Categoria da casa da direita", list(categories.keys()))
            left_val = get_input_from_options(f"Valor para '{left_cat}'", categories[left_cat])
            user_constraints.append({'type': 'right_of', 'left_cat': left_cat, 'left_val': left_val, 'right_cat': right_cat, 'right_val': right_val})
            print(f"✅ Restrição adicionada: 'A casa com {left_cat} {left_val} está à direita (qualquer posição) da casa com {right_cat} {right_val}'.")

        elif choice == '8': # Posição Impossível (Exclusão)
            print_options()
            print("-- Nova Restrição: Posição Impossível --")
            pos = int(get_input_from_options("Número da casa", [str(i) for i in range(1, 6)]))
            cat = get_input_from_options("Categoria do atributo", list(categories.keys()))
            val = get_input_from_options(f"Valor que '{cat}' NÃO PODE SER", categories[cat])
            
            var_name = f'Casa{pos}_{cat}'
            if val in dom[var_name]:
                dom[var_name].discard(val)
                print(f"✅ Restrição de exclusão adicionada: '{val}' foi removido do domínio de '{var_name}'.")
            else:
                print(f"ℹ️ Informação: O valor '{val}' já não estava no domínio de '{var_name}'. Nenhuma alteração feita.")

        else:
            print("Escolha inválida. Por favor, tente novamente.")

def test_instance(rules, description=""):
    global user_constraints
    user_constraints = []
    dom = copy.deepcopy(domain_template)

    print(f"\n== TESTE: {description} ==")
    
    # Aplica as regras fornecidas
    for rule in rules:
        if rule['type'] in {'same_house', 'neighbor', 'neighbor_left_of', 'neighbor_right_of', 'left_of', 'right_of'}:
            user_constraints.append(rule)

        # Aplica otimização de domínios para relações com orientação esquerda/direita
        if rule['type'] in {'neighbor_left_of', 'left_of'}:
            #print("  ➤ Otimizando domínio (removendo bordas à esquerda)")
            remove_borda_dominios(dom, rule['left_cat'], rule['left_val'], rule['right_cat'], rule['right_val'])
            #print(f"    Domínio Casa1_{rule['right_cat']}: {dom[f'Casa1_{rule['right_cat']}']}")
            #print(f"    Domínio Casa5_{rule['left_cat']}: {dom[f'Casa5_{rule['left_cat']}']}")

        elif rule['type'] in {'neighbor_right_of', 'right_of'}:
            #print("  ➤ Otimizando domínio (removendo bordas à direita)")
            remove_borda_dominios(dom, rule['right_cat'], rule['right_val'], rule['left_cat'], rule['left_val'])
            #print(f"    Domínio Casa1_{rule['left_cat']}: {dom[f'Casa1_{rule['left_cat']}']}")
            #print(f"    Domínio Casa5_{rule['right_cat']}: {dom[f'Casa5_{rule['right_cat']}']}")

        elif rule['type'] == 'position':
            var = f"Casa{rule['pos']}_{rule['cat']}"
            dom[var] = {rule['val']}

        elif rule['type'] == 'not_position':
            var = f"Casa{rule['pos']}_{rule['cat']}"
            dom[var].discard(rule['val'])

    start_time = time.time()
    ac3_success = ac3(dom, arcs)
    if not ac3_success:
        elapsed = time.time() - start_time
        print(f"❌ AC-3 detectou inconsistência. Tempo: {elapsed:.4f} s")
        return

    solution = brute_force(dom)
    elapsed = time.time() - start_time

    if solution:
        casas = {i: {} for i in range(1, 6)}
        for var, value in solution.items():
            pos = int(var[4])
            cat = var.split('_')[1]
            casas[pos][cat] = value
        #for i in range(1, 6):
            #print(f"\n--- Casa {i} ---")
            #for cat in sorted(casas[i]):
                #print(f"  {cat.capitalize():<12}: {casas[i][cat]}")
        print(f"✅ Solução encontrada em {elapsed:.4f} segundos")
    else:
        print(f"❌ Nenhuma solução encontrada. Tempo: {elapsed:.4f} segundos")

# este teste é para brecar o modelo que tenta atribuir variáveis no mesmo padrão sempre
simple_test = [
    {'type': 'neighbor_left_of', 'left_cat': 'beb', 'left_val': 'Leite', 'right_cat': 'cor', 'right_val': 'Amarelo'}
]

# sem nenhuma regra de restrição
empty = []

# funcionando
ten_rules = [
    {'type': 'same_house', 'cat1': 'nac', 'val1': 'Dinamarques', 'cat2': 'cig', 'val2': 'Dunhill'},
    {'type': 'same_house', 'cat1': 'cor', 'val1': 'Azul', 'cat2': 'pet', 'val2': 'Gato'},
    {'type': 'same_house', 'cat1': 'beb', 'val1': 'Agua', 'cat2': 'nac', 'val2': 'Sueco'},
    {'type': 'position', 'cat': 'cor', 'val': 'Verde', 'pos': 2},
    {'type': 'not_position', 'cat': 'cig', 'val': 'Prince', 'pos': 5},
    {'type': 'neighbor', 'cat1': 'pet', 'val1': 'Cavalo', 'cat2': 'beb', 'val2': 'Cerveja'},
    {'type': 'neighbor', 'cat1': 'cor', 'val1': 'Amarelo', 'cat2': 'nac', 'val2': 'Alemao'},
    {'type': 'neighbor_left_of', 'left_cat': 'cig', 'left_val': 'Blends', 'right_cat': 'beb', 'right_val': 'Cafe'},
    {'type': 'left_of', 'left_cat': 'pet', 'left_val': 'Passaro', 'right_cat': 'cor', 'right_val': 'Vermelho'},
    {'type': 'not_position', 'cat': 'beb', 'val': 'Cha', 'pos': 1},
]

#funcionando
einstein_rules = [
    {'type': 'same_house', 'cat1': 'nac', 'val1': 'Ingles', 'cat2': 'cor', 'val2': 'Vermelho'},
    {'type': 'same_house', 'cat1': 'nac', 'val1': 'Sueco', 'cat2': 'pet', 'val2': 'Cachorro'},
    {'type': 'same_house', 'cat1': 'nac', 'val1': 'Dinamarques', 'cat2': 'beb', 'val2': 'Cha'},
    {'type': 'neighbor_left_of', 'left_cat': 'cor', 'left_val': 'Verde', 'right_cat': 'cor', 'right_val': 'Branco'},
    {'type': 'same_house', 'cat1': 'cor', 'val1': 'Verde', 'cat2': 'beb', 'val2': 'Cafe'},
    {'type': 'same_house', 'cat1': 'cig', 'val1': 'Pall Mall', 'cat2': 'pet', 'val2': 'Passaro'},
    {'type': 'same_house', 'cat1': 'cor', 'val1': 'Amarelo', 'cat2': 'cig', 'val2': 'Dunhill'},
    {'type': 'position', 'cat': 'beb', 'val': 'Leite', 'pos': 3},
    {'type': 'position', 'cat': 'nac', 'val': 'Noruegues', 'pos': 1},
    {'type': 'neighbor', 'cat1': 'cig', 'val1': 'Blends', 'cat2': 'pet', 'val2': 'Gato'},
    {'type': 'neighbor', 'cat1': 'pet', 'val1': 'Cavalo', 'cat2': 'cig', 'val2': 'Dunhill'},
    {'type': 'same_house', 'cat1': 'cig', 'val1': 'Blue Master', 'cat2': 'beb', 'val2': 'Cerveja'},
    {'type': 'same_house', 'cat1': 'nac', 'val1': 'Alemao', 'cat2': 'cig', 'val2': 'Prince'},
    {'type': 'neighbor', 'cat1': 'nac', 'val1': 'Noruegues', 'cat2': 'cor', 'val2': 'Azul'},
    {'type': 'neighbor', 'cat1': 'cig', 'val1': 'Blends', 'cat2': 'beb', 'val2': 'Agua'},
]

#funcionando
new_twenty_rules = [
    # As 10 regras aleatórias que você já tinha:
    {'type': 'same_house', 'cat1': 'nac', 'val1': 'Dinamarques', 'cat2': 'cig', 'val2': 'Dunhill'},
    {'type': 'same_house', 'cat1': 'cor', 'val1': 'Azul', 'cat2': 'pet', 'val2': 'Gato'},
    {'type': 'same_house', 'cat1': 'beb', 'val1': 'Agua', 'cat2': 'nac', 'val2': 'Sueco'},
    {'type': 'position', 'cat': 'cor', 'val': 'Verde', 'pos': 2},
    {'type': 'not_position', 'cat': 'cig', 'val': 'Prince', 'pos': 5},
    {'type': 'neighbor', 'cat1': 'pet', 'val1': 'Cavalo', 'cat2': 'beb', 'val2': 'Cerveja'},
    {'type': 'neighbor', 'cat1': 'cor', 'val1': 'Amarelo', 'cat2': 'nac', 'val2': 'Alemao'},
    {'type': 'neighbor_left_of', 'left_cat': 'cig', 'left_val': 'Blends', 'right_cat': 'beb', 'right_val': 'Cafe'},
    {'type': 'left_of', 'left_cat': 'pet', 'left_val': 'Passaro', 'right_cat': 'cor', 'right_val': 'Vermelho'},
    {'type': 'not_position', 'cat': 'beb', 'val': 'Cha', 'pos': 1},

    # + As 10 regras adicionais que acabei de fornecer:
    {'type': 'same_house', 'cat1': 'beb', 'val1': 'Cafe', 'cat2': 'pet', 'val2': 'Peixe'},
    {'type': 'same_house', 'cat1': 'nac', 'val1': 'Alemao', 'cat2': 'cor', 'val2': 'Branco'},
    {'type': 'position', 'cat': 'cig', 'val': 'Pall Mall', 'pos': 3},
    {'type': 'not_position', 'cat': 'cor', 'val': 'Azul', 'pos': 1},
    {'type': 'not_position', 'cat': 'pet', 'val': 'Cachorro', 'pos': 2},
    {'type': 'not_position', 'cat': 'nac', 'val': 'Sueco', 'pos': 4},

    {'type': 'neighbor', 'cat1': 'cig', 'val1': 'Blue Master', 'cat2': 'nac', 'val2': 'Ingles'},
    {'type': 'neighbor', 'cat1': 'pet', 'val1': 'Passaro', 'cat2': 'beb', 'val2': 'Leite'},
    {'type': 'neighbor_right_of', 'left_cat': 'cor', 'left_val': 'Vermelho', 'right_cat': 'beb', 'right_val': 'Agua'},
    # sem esta regra abaixo demora mais!
    #{'type': 'right_of', 'left_cat': 'beb', 'left_val': 'Cerveja', 'right_cat': 'nac', 'right_val': 'Dinamarques'},
]

#funcionando
twenty_rules_without_solution = [
    # As 10 regras anteriores (aleatórias)
    {'type': 'same_house', 'cat1': 'nac', 'val1': 'Dinamarques', 'cat2': 'cig', 'val2': 'Dunhill'},
    {'type': 'same_house', 'cat1': 'cor', 'val1': 'Azul', 'cat2': 'pet', 'val2': 'Gato'},
    {'type': 'same_house', 'cat1': 'beb', 'val1': 'Agua', 'cat2': 'nac', 'val2': 'Sueco'},
    {'type': 'position', 'cat': 'cor', 'val': 'Verde', 'pos': 2},
    {'type': 'not_position', 'cat': 'cig', 'val': 'Prince', 'pos': 5},
    {'type': 'neighbor', 'cat1': 'pet', 'val1': 'Cavalo', 'cat2': 'beb', 'val2': 'Cerveja'},
    {'type': 'neighbor', 'cat1': 'cor', 'val1': 'Amarelo', 'cat2': 'nac', 'val2': 'Alemao'},
    {'type': 'neighbor_left_of', 'left_cat': 'cig', 'left_val': 'Blends', 'right_cat': 'beb', 'right_val': 'Cafe'},
    {'type': 'left_of', 'left_cat': 'pet', 'left_val': 'Passaro', 'right_cat': 'cor', 'right_val': 'Vermelho'},
    {'type': 'not_position', 'cat': 'beb', 'val': 'Cha', 'pos': 1},

    # Novas 10 regras adicionais (aleatórias)
    # 3x 'same_house'
    {'type': 'same_house', 'cat1': 'cig', 'val1': 'Pall Mall', 'cat2': 'beb', 'val2': 'Leite'},
    {'type': 'same_house', 'cat1': 'pet', 'val1': 'Peixe', 'cat2': 'nac', 'val2': 'Ingles'},
    {'type': 'same_house', 'cat1': 'cor', 'val1': 'Branco', 'cat2': 'cig', 'val2': 'Blue Master'},

    # 2x 'position' ou 'not_position'
    {'type': 'position', 'cat': 'pet', 'val': 'Cachorro', 'pos': 4},
    {'type': 'not_position', 'cat': 'nac', 'val': 'Noruegues', 'pos': 3},
    
    # 2x 'neighbor'
    {'type': 'neighbor', 'cat1': 'beb', 'val1': 'Agua', 'cat2': 'pet', 'val2': 'Peixe'},
    {'type': 'neighbor', 'cat1': 'cig', 'val1': 'Dunhill', 'cat2': 'cor', 'val2': 'Branco'},
    
    # 1x 'neighbor_right_of'
    {'type': 'neighbor_right_of', 'left_cat': 'cor', 'left_val': 'Amarelo', 'right_cat': 'cig', 'right_val': 'Dunhill'},

    # 1x 'right_of'
    {'type': 'right_of', 'left_cat': 'nac', 'left_val': 'Alemao', 'right_cat': 'beb', 'right_val': 'Cerveja'},
    
    # 1x 'position' para uma casa diferente
    {'type': 'position', 'cat': 'nac', 'val': 'Ingles', 'pos': 5},
]

# Rodar experimento automaticamente
for i in range(1, 11):
    print(f"Teste número {i}:")
    test_instance(new_twenty_rules, "Instância de teste - Einstein simplificado")
    print("\n")