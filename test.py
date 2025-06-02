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

# Categorias disponíveis
categorias = ['cor', 'nac', 'beb', 'pet', 'cig']

# Adiciona arcos entre variáveis da mesma categoria (para garantir que não se repitam)
# Exemplo: Casa1_cor -> Casa2_cor
for cat in categorias:
  vars_cat = [f"Casa{i}_{cat}" for i in range(1, 6)]
  for i in range(len(vars_cat)):
    for j in range(len(vars_cat)):
      if i != j:
        arcs.add((vars_cat[i], vars_cat[j]))

# Adiciona arcos entre categorias diferentes na mesma casa (para aplicar dicas como inglês na casa vermelha)
# Exemplo: Casa1_cor -> Casa1_beb
for i in range(1, 6):
  for cat1 in categorias:
    for cat2 in categorias:
      if cat1 != cat2:
        arcs.add((f"Casa{i}_{cat1}", f"Casa{i}_{cat2}"))

# Adiciona arcos entre categorias diferentes da categoria em questão em casas diferentes
# Exemplo:
# Casa5_pet → Casa1_beb
# Casa5_pet → Casa1_cig
# Casa5_pet → Casa1_cor
# Casa5_pet → Casa1_nac
# Casa5_pet → Casa2_beb
# Casa5_pet → Casa2_cig
# Casa5_pet → Casa2_cor
# Casa5_pet → Casa2_nac...
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
  #funfa
  if arc_x.split('_')[1] == arc_y.split('_')[1]:
    return value_x != value_y  # Impede repetição de mesmo valor

  # Dica 5 (v2): A casa verde fica IMEDIATAMENTE à esquerda da casa branca
  # tmb não funciona, mas não tão importante assim
  #if ('cor' in arc_x and value_x == 'Verde' and 'cor' in arc_y and value_y == 'Branco'):
    #pos_x = int(arc_x[4])
    #pos_y = int(arc_y[4])
    #if pos_x + 1 != pos_y:
      #return False
  
  #casa verde e branca são vizinhas
  # ESTA AQUI NÃO FUNCIONA!!!
  #if ('cor' in arc_x and value_x == 'Verde' and 'cor' in arc_y and value_y == 'Branco') or \
    #('cor' in arc_x and value_x == 'Branco' and 'cor' in arc_y and value_y == 'Verde'):
    #pos_x = int(arc_x[4])
    #pos_y = int(arc_y[4])
    #if abs(pos_x - pos_y) != 1:
      #return False

  
  # mesma casa
  if arc_x.split('_')[0] == arc_y.split('_')[0]:
    # Dica 2: O inglês mora na casa vermelha
    #funfa
    if ('nac' in arc_x and value_x == 'Ingles' and 'cor' in arc_y and value_y != 'Vermelho') or \
       ('cor' in arc_x and value_x == 'Vermelho' and 'nac' in arc_y and value_y != 'Ingles'):
      return False

    # Dica 3: O sueco tem cachorro como animal de estimação
    #funfa
    if ('nac' in arc_x and value_x == 'Sueco' and 'pet' in arc_y and value_y != 'Cachorro') or \
       ('pet' in arc_x and value_x == 'Cachorro' and 'nac' in arc_y and value_y != 'Sueco'):
      return False
    
    # Dica 4: O dinamarques bebe chá
    #funfa
    if ('nac' in arc_x and value_x == 'Dinamarques' and 'beb' in arc_y and value_y != 'Cha') or \
       ('beb' in arc_x and value_x == 'Cha' and 'nac' in arc_y and value_y != 'Dinamarques'):
      return False
    
    # Dica 6: O homem que vive na casa verde bebe café
    #funfa
    if ('cor' in arc_x and value_x == 'Verde' and 'beb' in arc_y and value_y != 'Cafe') or \
       ('beb' in arc_x and value_x == 'Cafe' and 'cor' in arc_y and value_y != 'Verde'):
      return False
    
    # Dica 7: O homem que fuma Pall Mall cria pássaros
    #funfa
    if ('cig' in arc_x and value_x == 'Pall Mall' and 'pet' in arc_y and value_y != 'Passaro') or \
       ('pet' in arc_x and value_x == 'Passaro' and 'cig' in arc_y and value_y != 'Pall Mall'):
      return False
    
    # Dica 8: O homem que vive na casa amarela fuma Dunhill
    #funfa
    if ('cor' in arc_x and value_x == 'Amarelo' and 'cig' in arc_y and value_y != 'Dunhill') or \
       ('cig' in arc_x and value_x == 'Dunhill' and 'cor' in arc_y and value_y != 'Amarelo'):
      return False
    
    # Dica 12: O homem que fuma Blue Master bebe cerveja
    #funfa
    if ('cig' in arc_x and value_x == 'Blue Master' and 'beb' in arc_y and value_y != 'Cerveja') or \
       ('beb' in arc_x and value_x == 'Cerveja' and 'cig' in arc_y and value_y != 'Blue Master'):
      return False
    
    # Dica 13: O alemão fuma Prince
    #funfa
    if ('nac' in arc_x and value_x == 'Alemao' and 'cig' in arc_y and value_y != 'Prince') or \
       ('cig' in arc_x and value_x == 'Prince' and 'nac' in arc_y and value_y != 'Alemao'):
      return False

  # Dica 10: O homem que fuma blends é vizinho imediato do que tem gatos
  #funfa
  if ('cig' in arc_x and value_x == 'Blends' and 'pet' in arc_y and value_y == 'Gato') or \
    ('pet' in arc_x and value_x == 'Gato' and 'cig' in arc_y and value_y == 'Blends'):
    # Verifica se as casas são vizinhas (posição das casas)
    pos_x = int(arc_x[4])
    pos_y = int(arc_y[4])
    if abs(pos_x - pos_y) != 1:  # não são vizinhos imediatas
      return False
  
  # Dica 11: O homem que tem um cavalo vive ao lado do que fuma dunhill
  #funfa
  if ('pet' in arc_x and value_x == 'Cavalo' and 'cig' in arc_y and value_y == 'Dunhill') or \
    ('cig' in arc_x and value_x == 'Dunhill' and 'pet' in arc_y and value_y == 'Cavalo'):
    pos_x = int(arc_x[4])
    pos_y = int(arc_y[4])
    if abs(pos_x - pos_y) != 1:
      return False
  
  # Dica 14: O norueguês vive ao lado da casa azul
  #funfa
  if ('nac' in arc_x and value_x == 'Noruegues' and 'cor' in arc_y and value_y == 'Azul') or \
    ('cor' in arc_x and value_x == 'Azul' and 'nac' in arc_y and value_y == 'Noruegues'):
    pos_x = int(arc_x[4])
    pos_y = int(arc_y[4])
    if abs(pos_x - pos_y) != 1:
      return False
  
  # Dica 15: O homem que fuma blends é vizinho do que bebe água
  #funfa
  if ('cig' in arc_x and value_x == 'Blends' and 'beb' in arc_y and value_y == 'Agua') or \
     ('beb' in arc_x and value_x == 'Agua' and 'cig' in arc_y and value_y == 'Blends'):
    pos_x = int(arc_x[4])
    pos_y = int(arc_y[4])
    if abs(pos_x - pos_y) != 1:
      return False

  return True  # Categorias diferentes sempre são válidas

def revise(domain, arc_x, arc_y):
  # Indica se algum valor foi removido do domínio de arc_x
  revised = False

  # Conjunto de valores que serão removidos do domínio de arc_x
  to_remove = set()

  # Para cada valor possível de arc_x
  for value_x in domain[arc_x]:
    # Verifica se existe ao menos um value_y em arc_y tal que (value_x, value_y) satisfaça a restrição
    # Se nenhum value_y satisfaz, então value_x não é válido e deve ser removido
    if not any(constraint(arc_x, value_x, arc_y, value_y) for value_y in domain[arc_y]):
      # Marca value_x para remoção do domínio de arc_x
      to_remove.add(value_x)
      # Indica que o domínio de arc_x foi modificado
      revised = True

  # Remove do domínio de arc_x todos os valores que não têm suporte em arc_y
  domain[arc_x] -= to_remove

  # Retorna True se houve qualquer modificação no domínio (algum valor removido)
  return revised

def ac3(dom, arcs):
  # Inicializa a fila de arcos (restrições binárias) a serem verificados
  queue = deque(arcs)

  # Enquanto houver arcos na fila para processar
  while queue:
    # Remove o próximo arco da fila
    # arcs são do tipo (x, y), como ('Casa1_beb', 'Casa2_beb')
    arc_x, arc_y = queue.popleft()
    
    # Verifica se o domínio de arc_x precisa ser revisado em relação a arc_y
    if revise(dom, arc_x, arc_y):
      # Se o domínio de arc_x ficou vazio após a revisão, o problema é inconsistente
      if not dom[arc_x]:
        return False

      # Para todas as outras variáveis da mesma categoria (mesmo sufixo, como "_beb") que arc_x
      for other_var in dom:
        # Evita revisitar o próprio arc_x
        # Garante que other_var seja da mesma categoria que arc_x
        if other_var != arc_x and (other_var.split('_')[1] == arc_x.split('_')[1]):
          # Adiciona o arco (other_var, arc_x) de volta à fila para verificar a consistência
          queue.append((other_var, arc_x))

  
  # Se todos os arcos foram processados sem inconsistência, retorna True
  return True

# Busca por backtracking
def brute_force(domains):
  # Dicionário (dict) vazio, armazena a atribuição de valores a variáveis
  #assignment = {'Casa1_cor': 'Vermelho', 'Casa2_cor': 'Verde', 'Casa1_nac': 'Ingles',...}
  assignment = {}
  
  # Lista de strings, representando cada variável do problema
  #['Casa1_cor', 'Casa2_cor', 'Casa3_cor', 'Casa4_cor', 'Casa5_cor',
  #'Casa1_nac', 'Casa2_nac', 'Casa3_nac', 'Casa4_nac', 'Casa5_nac',
  #'Casa1_cig', 'Casa2_cig', 'Casa3_cig', 'Casa4_cig', 'Casa5_cig',
  #'Casa1_pet', 'Casa2_pet', 'Casa3_pet', 'Casa4_pet', 'Casa5_pet',
  #'Casa1_beb', 'Casa2_beb', 'Casa3_beb', 'Casa4_beb', 'Casa5_beb']
  vars_list = list(domains.keys())

  # Função recursiva, explorando possiveis atribuições de valores às variáveis
  # idx é o índice da variável atual na lista vars_list, que estamos tentando atribuir um valor
  def backtrack(idx):
    # Se idx chegou no final de vars_list, então todas as variáveis já foram atribuídas
    if idx == len(vars_list):
      # Encerra a recursão, retorna a cópia da atribuição completa (solução válida) 
      return assignment.copy() 

    # Pega a variável atual (ex: 'Casa3_cor') Para tentar atribuir um valor a ela
    var = vars_list[idx]

    # Para cada valor possível da variável var, tenta fazer uma atribuição por tentativa
    for value in domains[var]:
      # Para cada variável other já atribuída em assignment, verifica se a atribuição
      # var = value é compatível com ela.
      # Se qualquer uma dessa verificações falhar, a tentativa é rejeitada
      # e o loop continua com outro valor em domains[var]
      if all(constraint(var, value, other, assignment[other]) and \
             constraint(other, assignment[other], var, value)
             for other in assignment):
        
        # Se passar pelas constraints, atribui value à variável var no dicionário assignment
        assignment[var] = value
        # Chama backtrack para a próxima variável
        result = backtrack(idx + 1)
        # Se o result retornou uma solução (não none), para a recursão 
        # e retorna a primeira solução encontrada
        if result:
          return result
        # Se a recursão falhou (não levou a uma solução), remove a atribuição de var
        # no backtrack para tentar outro valor
        del assignment[var]
    # Se nenhum valor do domínio de var dá solução válida, retorna none, sinaliza que 
    # o caminho atual está inválido
    return None
  # Inicia busca com backtrack pela a primeira variável
  return backtrack(0)

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

   # Find a complete solution
  solution = brute_force(dom)
  if solution:
    print("Solution found:")
    for v in sorted(solution): print(f"{v}: {solution[v]}")
  else:
    print("No solution found")

if __name__ == "__main__":
  main()

#tem que ter uma função constraint_positions com os assignments
#na versão anterior deu erro ao verificar a dica "a casa verde está a esquerda (qualquer posição) da casa branca"
