# este teste é para brecar o modelo que tenta atribuir variáveis no mesmo padrão sempre
# Test 1: 0.0588 segundos
# Test 2: 17.0880 segundos
# Test 3: 0.0044 segundos
# Test 4: 0.0041 segundos
# Test 5: 7.7127 segundos
# Test 6: 0.0045 segundos
# Test 7: 0.0037 segundos
# Test 8: 0.0040 segundos
# Test 9: 0.0080 segundos
# Test 10: 0.0038 segundos
simple_test = [
    {'type': 'neighbor_left_of', 'left_cat': 'beb', 'left_val': 'Leite', 'right_cat': 'cor', 'right_val': 'Amarelo'}
]

# sem nenhuma regra de restrição
# Test 1:  0.0028 segundos
# Test 2:  0.0031 segundos
# Test 3:  0.0036 segundos
# Test 4:  0.0029 segundos
# Test 5:  0.0031 segundos
# Test 6:  0.0036 segundos
# Test 7:  0.0032 segundos
# Test 8:  0.0029 segundos
# Test 9:  0.0029 segundos
# Test 10: 0.0029 segundos
empty = []

# 10 regras
# Test 1:  20.5774 segundos
# Test 2:  3.9716 segundos
# Test 3:  0.6723 segundos
# Test 4:  0.0259 segundos
# Test 5:  0.0303 segundos
# Test 6:  0.0350 segundos
# Test 7:  0.0323 segundos
# Test 8:  0.0103 segundos
# Test 9:  1.0214 segundos
# Test 10: 0.0098 segundos
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
# Test 1:  0.1592 segundos
# Test 2:  0.4377 segundos
# Test 3:  0.3248 segundos
# Test 4:  0.0271 segundos
# Test 5:  0.0836 segundos
# Test 6:  0.2435 segundos
# Test 7:  0.2266 segundos
# Test 8:  0.2747 segundos
# Test 9:  0.1092 segundos
# Test 10: 0.0413 segundos
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
# Test 1:  0.4037 segundos
# Test 2:  0.3783 segundos
# Test 3:  0.7606 segundos
# Test 4:  0.4594 segundos
# Test 5:  0.4824 segundos
# Test 6:  0.6076 segundos
# Test 7:  0.2856 segundos
# Test 8:  0.2620 segundos
# Test 9:  0.1772 segundos
# Test 10: 0.0646 segundos
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
# Test 1:  8.2150 segundos
# Test 2:  2.1260 segundos
# Test 3:  6.3046 segundos
# Test 4:  6.6648 segundos
# Test 5:  0.6267 segundos
# Test 6:  4.2166 segundos
# Test 7:  3.9773 segundos
# Test 8:  5.7766 segundos
# Test 9:  8.5516 segundos
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
# Test 1:  2.8417 segundos
# Test 2:  2.9497 segundos
# Test 3:  2.9360 segundos
# Test 4:  2.9895 segundos
# Test 5:  3.1426 segundos
# Test 6:  2.8300 segundos
# Test 7:  2.9362 segundos
# Test 8:  3.0933 segundos
# Test 9:  2.9490 segundos
# Test 10: 2.9524 segundos
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