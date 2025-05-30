from collections import deque
import copy
import itertools

# Variables
vars_cor = ['House1_color', 'House2_color', 'House3_color', 'House4_color', 'House5_color']
vars_nac = ['House1_nation', 'House2_nation', 'House3_nation', 'House4_nation', 'House5_nation']
vars_beb = ['House1_drink', 'House2_drink', 'House3_drink', 'House4_drink', 'House5_drink']
vars_cig = ['House1_smoke', 'House2_smoke', 'House3_smoke', 'House4_smoke', 'House5_smoke']
vars_pet = ['House1_pet', 'House2_pet', 'House3_pet', 'House4_pet', 'House5_pet']
vars_all = vars_cor + vars_nac + vars_cig + vars_pet + vars_beb

# Initial domains
domain_template = {
  **{v: {'White', 'Green', 'Blue', 'Yellow', 'Red'} for v in vars_cor},
  **{v: {'Norwegian', 'English', 'German', 'Swedish', 'Danish'} for v in vars_nac},
  **{v: {'Tea', 'Water', 'Milk', 'Coffee', 'Beer'} for v in vars_beb},
  **{v: {'Dunhill', 'Blends', 'Pall Mall', 'Prince', 'Blue Master'} for v in vars_cig},
  **{v: {'Horse', 'Fish', 'Bird', 'Dog', 'Cat'} for v in vars_pet},
}

# Build binary arcs for AC-3
arcs = set()
categories = ['color', 'nation', 'drink', 'pet', 'smoke']
# All-different constraints within each category
for cat in categories:
  vars_cat = [f"House{i}_{cat}" for i in range(1, 6)]
  for x, y in itertools.permutations(vars_cat, 2):
    arcs.add((x, y))
# Pairwise house constraints
for i in range(1, 6):
  for c1, c2 in itertools.permutations(categories, 2):
    arcs.add((f"House{i}_{c1}", f"House{i}_{c2}"))

# Binary constraint function (basic)
def constraint(x, val_x, y, val_y):
  # if same category, values must differ
  if x.split('_')[1] == y.split('_')[1]:
    return val_x != val_y
  return True

# AC-3 revise
def revise(domain, x, y):
  revised = False
  to_remove = set()
  for vx in domain[x]:
    if not any(constraint(x, vx, y, vy) for vy in domain[y]):
      to_remove.add(vx)
      revised = True
  domain[x] -= to_remove
  return revised

# AC-3 algorithm
def ac3(dom, arcs):
  queue = deque(arcs)
  while queue:
    x, y = queue.popleft()
    if revise(dom, x, y):
      if not dom[x]:
        return False
      for z in dom:
        if z != x and z.split('_')[1] == x.split('_')[1]:
          queue.append((z, x))
  return True

# Brute-force backtracking search
def backtrack_search(domains):
  assignment = {}
  # collect variable list
  vars_list = list(domains.keys())
  def backtrack(idx):
    if idx == len(vars_list):
      return assignment.copy()
    var = vars_list[idx]
    for value in domains[var]:
      # check consistency with current assignment
      if all(constraint(var, value, other, assignment[other]) and \
             constraint(other, assignment[other], var, value)
             for other in assignment):
        assignment[var] = value
        result = backtrack(idx + 1)
        if result:
          return result
        del assignment[var]
    return None
  return backtrack(0)

# Main function
def main():
  dom = copy.deepcopy(domain_template)
  # Einstein clues:
  # Clue 1: The Norwegian lives in the first house
  dom['House1_nation'] = {'Norwegian'}
  # Clue 9: The man living in the center house drinks milk
  dom['House3_drink'] = {'Milk'}

  # Run AC-3
  if not ac3(dom, arcs):
    print("AC-3 detected inconsistency")
    return

  print("Domains after AC-3:")
  for v in sorted(dom): print(f"{v}: {dom[v]}")

  # Find a complete solution
  solution = backtrack_search(dom)
  if solution:
    print("Solution found:")
    for v in sorted(solution): print(f"{v}: {solution[v]}")
  else:
    print("No solution found")

if __name__ == "__main__":
  main()
