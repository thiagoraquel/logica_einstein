# este teste é para brecar o modelo que tenta atribuir variáveis no mesmo padrão sempre
# Test 1: 0.0671 segundos
# Test 2: 0.0741 segundos
# Test 3: 0.0672 segundos
# Test 4: 0.0673 segundos
# Test 5: 0.0681 segundos
# Test 6: 0.0670 segundos
# Test 7: 0.0704 segundos
# Test 8: 0.0675 segundos
# Test 9: 0.0673 segundos
# Test 10: 0.0665 segundos
simple_test = [
    {'type': 'neighbor_left_of', 'left_cat': 'beb', 'left_val': 'Leite', 'right_cat': 'cor', 'right_val': 'Amarelo'}
]

# sem nenhuma regra de restrição
# Test 1:  0.0033 segundos
# Test 2:  0.0028 segundos
# Test 3:  0.0033 segundos
# Test 4:  0.0031 segundos
# Test 5:  0.0031 segundos
# Test 6:  0.0034 segundos
# Test 7:  0.0032 segundos
# Test 8:  0.0031 segundos
# Test 9:  0.0030 segundos
# Test 10: 0.0034 segundos
empty = []

# 10 regras
# Test 1:  0.3736 segundos
# Test 2:  0.3733 segundos
# Test 3:  0.3794 segundos
# Test 4:  0.3793 segundos
# Test 5:  0.3781 segundos
# Test 6:  0.3696 segundos
# Test 7:  0.3739 segundos
# Test 8:  0.3786 segundos
# Test 9:  0.3766 segundos
# Test 10: 0.3792 segundos
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

# Caso clássico
# Test 1:  0.1409 segundos
# Test 2:  0.1448 segundos
# Test 3:  0.1429 segundos
# Test 4:  0.1340 segundos
# Test 5:  0.1327 segundos
# Test 6:  0.1295 segundos
# Test 7:  0.1547 segundos
# Test 8:  0.1615 segundos
# Test 9:  0.1344 segundos
# Test 10: 0.1306 segundos
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

# Twenty rules com a última regra
# Test 1:  0.2975 segundos
# Test 2:  0.2923 segundos
# Test 3:   0.3093 segundos
# Test 4:  0.2923 segundos
# Test 5:  0.3173 segundos
# Test 6:  0.2890 segundos
# Test 7:  0.3026 segundos
# Test 8:  0.2900 segundos
# Test 9:  0.2874 segundos
# Test 10: 0.2965 segundos
new_twenty_rules = [
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
    {'type': 'right_of', 'left_cat': 'beb', 'left_val': 'Cerveja', 'right_cat': 'nac', 'right_val': 'Dinamarques'},
]

# Caso sem a útlima regra
# Test 1:  1.5930 segundos
# Test 2:  1.6321 segundos
# Test 3:  1.3649 segundos
# Test 4:  1.3469 segundos
# Test 5:  1.5883 segundos
# Test 6:  1.4302 segundos
# Test 7:  1.3556 segundos
# Test 8:  1.4222 segundos
# Test 9:  1.5630 segundos
# Test 10: 1.5720 segundos
new_twenty_rules = [
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
    {'type': 'right_of', 'left_cat': 'beb', 'left_val': 'Cerveja', 'right_cat': 'nac', 'right_val': 'Dinamarques'},
]

# Caso com 20 regras sem solução!
# Todos os resultados dos testes aqui deu a mesma resposta de solução não encontrada em X segundos.
# Test 1:  6.2825 segundos
# Test 2:  6.6465 segundos
# Test 3:  8.4106 segundos
# Test 4:  10.4236 segundos
# Test 5:  10.6438 segundos
# Test 6:  9.7254 segundos
# Test 7:  6.2165 segundos
# Test 8:  6.5910 segundos
# Test 9:  11.1972 segundos
# Test 10: 11.1761 segundos
twenty_rules_without_solution = [
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
    {'type': 'same_house', 'cat1': 'cig', 'val1': 'Pall Mall', 'cat2': 'beb', 'val2': 'Leite'},
    {'type': 'same_house', 'cat1': 'pet', 'val1': 'Peixe', 'cat2': 'nac', 'val2': 'Ingles'},
    {'type': 'same_house', 'cat1': 'cor', 'val1': 'Branco', 'cat2': 'cig', 'val2': 'Blue Master'},
    {'type': 'position', 'cat': 'pet', 'val': 'Cachorro', 'pos': 4},
    {'type': 'not_position', 'cat': 'nac', 'val': 'Noruegues', 'pos': 3},
    {'type': 'neighbor', 'cat1': 'beb', 'val1': 'Agua', 'cat2': 'pet', 'val2': 'Peixe'},
    {'type': 'neighbor', 'cat1': 'cig', 'val1': 'Dunhill', 'cat2': 'cor', 'val2': 'Branco'},
    {'type': 'neighbor_right_of', 'left_cat': 'cor', 'left_val': 'Amarelo', 'right_cat': 'cig', 'right_val': 'Dunhill'},
    {'type': 'right_of', 'left_cat': 'nac', 'left_val': 'Alemao', 'right_cat': 'beb', 'right_val': 'Cerveja'},
    {'type': 'position', 'cat': 'nac', 'val': 'Ingles', 'pos': 5},
]