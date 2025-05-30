from collections import deque
import copy

# Variáveis
vars_cor = ['Casa1_cor', 'Casa2_cor', 'Casa3_cor', 'Casa4_cor', 'Casa5_cor']
vars_nac = ['Casa1_nac', 'Casa2_nac', 'Casa3_nac', 'Casa4_nac', 'Casa5_nac']
vars_beb = ['Casa1_beb', 'Casa2_beb', 'Casa3_beb', 'Casa4_beb', 'Casa5_beb']
vars_cig = ['Casa1_cig', 'Casa2_cig', 'Casa3_cig', 'Casa4_cig', 'Casa5_cig']
vars_pet = ['Casa1_pet', 'Casa2_pet', 'Casa3_pet', 'Casa4_pet', 'Casa5_pet']
vars_all = vars_nac + vars_cor + vars_cig + vars_pet + vars_beb

# Domínios iniciais
domain_template = {
  'Casa1_cor': {'Branco', 'Verde', 'Azul', 'Amarelo', 'Vermelho'},
  'Casa2_cor': {'Branco', 'Verde', 'Azul', 'Amarelo', 'Vermelho'},
  'Casa3_cor': {'Branco', 'Verde', 'Azul', 'Amarelo', 'Vermelho'},
  'Casa4_cor': {'Branco', 'Verde', 'Azul', 'Amarelo', 'Vermelho'},
  'Casa5_cor': {'Branco', 'Verde', 'Azul', 'Amarelo', 'Vermelho'},

  'Casa1_nac': {'Noruegues', 'Ingles', 'Alemao', 'Sueco', 'Dinamarques'},
  'Casa2_nac': {'Noruegues', 'Ingles', 'Alemao', 'Sueco', 'Dinamarques'},
  'Casa3_nac': {'Noruegues', 'Ingles', 'Alemao', 'Sueco', 'Dinamarques'},
  'Casa4_nac': {'Noruegues', 'Ingles', 'Alemao', 'Sueco', 'Dinamarques'},
  'Casa5_nac': {'Noruegues', 'Ingles', 'Alemao', 'Sueco', 'Dinamarques'},

  'Casa1_cig': {'Dunhill', 'Blends', 'Pall Mall', 'Prince', 'Blue Master'},
  'Casa2_cig': {'Dunhill', 'Blends', 'Pall Mall', 'Prince', 'Blue Master'},
  'Casa3_cig': {'Dunhill', 'Blends', 'Pall Mall', 'Prince', 'Blue Master'},
  'Casa4_cig': {'Dunhill', 'Blends', 'Pall Mall', 'Prince', 'Blue Master'},
  'Casa5_cig': {'Dunhill', 'Blends', 'Pall Mall', 'Prince', 'Blue Master'},

  'Casa1_pet': {'Cavalo', 'Peixe', 'Passaro', 'Cachorro', 'Gato'},
  'Casa2_pet': {'Cavalo', 'Peixe', 'Passaro', 'Cachorro', 'Gato'},
  'Casa3_pet': {'Cavalo', 'Peixe', 'Passaro', 'Cachorro', 'Gato'},
  'Casa4_pet': {'Cavalo', 'Peixe', 'Passaro', 'Cachorro', 'Gato'},
  'Casa5_pet': {'Cavalo', 'Peixe', 'Passaro', 'Cachorro', 'Gato'},

  'Casa1_beb': {'Cha', 'Agua', 'Leite', 'Cafe', 'Cerveja'},
  'Casa2_beb': {'Cha', 'Agua', 'Leite', 'Cafe', 'Cerveja'},
  'Casa3_beb': {'Cha', 'Agua', 'Leite', 'Cafe', 'Cerveja'},
  'Casa4_beb': {'Cha', 'Agua', 'Leite', 'Cafe', 'Cerveja'},
  'Casa5_beb': {'Cha', 'Agua', 'Leite', 'Cafe', 'Cerveja'},
}

# Restrições binárias (arestas) para AC-3 (todos pares de variáveis diferentes)
arcs = set()

# Restrições binárias (arestas) para AC-3 (todos pares de variáveis diferentes)
arcs = set()

# Categorias disponíveis
categorias = ['cor', 'nac', 'beb', 'pet', 'cig']

# Adiciona arcos entre variáveis da mesma categoria (para garantir que não se repitam)
for cat in categorias:
  vars_cat = [f"Casa{i}_{cat}" for i in range(1, 6)]
  for i in range(len(vars_cat)):
    for j in range(len(vars_cat)):
      if i != j:
        arcs.add((vars_cat[i], vars_cat[j]))

# Adiciona arcos entre categorias diferentes na mesma casa (para aplicar dicas como inglês na casa vermelha)
for i in range(1, 6):
  for cat1 in categorias:
    for cat2 in categorias:
      if cat1 != cat2:
        arcs.add((f"Casa{i}_{cat1}", f"Casa{i}_{cat2}"))

for i in range(1, 6):
  for j in range(1, 6):
    if i != j:
      for cat1 in categorias:
        for cat2 in categorias:
          if cat1 != cat2:
            arcs.add((f"Casa{i}_{cat1}", f"Casa{j}_{cat2}"))

def print_arcs(arcs):
  print("Arcos (restrições binárias):")
  for arc in sorted(arcs):
    print(f"{arc[0]} → {arc[1]}")
  print(f"Total de arcos: {len(arcs)}")

# Verifica se um par de variáveis (um arco no formato (arc_x, arc_y)) e seus valores propostos está
# de acordo com as regras do problema
# Retorna True quando não há conflito com as regras
def constraint(arc_x, value_x, arc_y, value_y):

  # Se são da mesma categoria (ex: "_cor"), não podem ter o mesmo valor
  if arc_x.split('_')[1] == arc_y.split('_')[1]:
    return value_x != value_y  # Impede repetição de mesmo valor

  return True  # Categorias diferentes sempre são válidas

def revise(domain, arc_x, arc_y):
  revised = False
  to_remove = set()

  for value_x in domain[arc_x]:
    # Se nenhum value_y em arc_y satisfaz a restrição -> remove value_x do domínio arc_x
    if not any(constraint(arc_x, value_x, arc_y, value_y) for value_y in domain[arc_y]):
      # Se não existir nenhum value_y em arc_y compatível, então value_x é removido do domínio de arc_x
      to_remove.add(value_x)
      revised = True

  domain[arc_x] -= to_remove

  # Retorna true se removeu algum valor.
  return revised

def ac3(dom, arcs):
  queue = deque(arcs)
  while queue:

    # arcs são do tipo (x, y) ex: Casa1_beb -> Casa2_beb
    # portanto arc_x será Casa1_beb e arc_y será Casa2_beb
    arc_x, arc_y = queue.popleft()
    
    if revise(dom, arc_x, arc_y):
      if not dom[arc_x]:
        return False  # Algum domínio ficou vazio → inconsistente
      for xk in dom:
        if xk != arc_x and (xk.split('_')[1] == arc_x.split('_')[1]):
          queue.append((xk, arc_x))
  return True

  # Função principal
def main():
  dom = copy.deepcopy(domain_template)

  #print_arcs(arcs)

  # Dica 1: O noruegues mora na primeira casa
  dom['Casa1_nac'] = {"Noruegues"}
  # Dica 9: O homem da casa do meio bebe leite
  dom['Casa3_beb'] = {'Leite'}

  if ac3(dom, arcs):
    print("Domínios após AC-3:")
    for var in sorted(dom):
      print(f"{var}: {dom[var]}")
  else:
    print("AC-3 detectou inconsistência nos domínios.")
  # até a parte de cima está funcionando


if __name__ == "__main__":
  main()