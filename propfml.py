from mathesis.forms import Negation, Conjunction, Disjunction, Conditional, Atom
import numpy as np
from itertools import product




def random_propfml_generator(depth, prop_variables, connectives):
  """Generates a random propositional formula.

  Parameters:

    depth: maximum depth of the formula (int).
    prop_variables: list of propositional variables list(str).
    connectives: list of connectives list(str). Choose between 'Conjunction', 'Disjunction', 'Conditional' and 'Negation'.

  Returns: a propositional formula.
  """
  rng = np.random.default_rng()

  Atoms = [Atom(symbol) for symbol in prop_variables]

  if depth == 1 or len(connectives) == 0:
    return Atoms[rng.integers(0, len(Atoms))]
  else:
    c = rng.integers(0, len(connectives))
    if connectives[c] == 'Negation':
      P = Negation(random_propfml_generator(rng.integers(1, depth), prop_variables, connectives))
      depth -= 1
      return P

    elif connectives[c] == 'Conjunction':
      P = random_propfml_generator(rng.integers(1, depth), prop_variables, connectives)
      Q = random_propfml_generator(rng.integers(1, depth), prop_variables, connectives)
      depth -= 1
      return Conjunction(P, Q)

    elif connectives[c] == 'Disjunction':
      P = random_propfml_generator(rng.integers(1, depth), prop_variables, connectives)
      Q = random_propfml_generator(rng.integers(1, depth), prop_variables, connectives)
      depth -= 1
      return Disjunction(P, Q)

    elif connectives[c] == 'Conditional':
      P = random_propfml_generator(rng.integers(1, depth), prop_variables, connectives)
      Q = random_propfml_generator(rng.integers(1, depth), prop_variables, connectives)
      depth -= 1
      return Conditional(P, Q)
    

def Eval_propfml(propfml, atomic_evals):

  # Atoms = dict((Atom(letter), value) for letter, value in atomic_evals.items())

  NegationClause = {1: 0, 0: 1}

  ConjunctionClause = {
        (1, 1): 1,
        (1, 0): 0,
        (0, 1): 0,
        (0, 0): 0 }

  DisjunctionClause = {
        (1, 1): 1,
        (1, 0): 1,
        (0, 1): 1,
        (0, 0): 0 }

  ConditionalClause = {
        (1, 1): 1,
        (1, 0): 0,
        (0, 1): 1,
        (0, 0): 1 }

  if isinstance(propfml, Atom):
    return atomic_evals[propfml.symbol]

  if isinstance(propfml, Negation):
    return NegationClause[Eval_propfml(propfml.sub, atomic_evals)]

  if isinstance(propfml, Conjunction):
    sub_l, sub_r = propfml.subs
    eval_l = Eval_propfml(sub_l, atomic_evals)
    eval_r = Eval_propfml(sub_r, atomic_evals)
    return ConjunctionClause[(eval_l, eval_r)]

  if isinstance(propfml, Disjunction):
    sub_l, sub_r = propfml.subs
    eval_l = Eval_propfml(sub_l, atomic_evals)
    eval_r = Eval_propfml(sub_r, atomic_evals)
    return DisjunctionClause[(eval_l, eval_r)]

  if isinstance(propfml, Conditional):
    sub_l, sub_r = propfml.subs
    eval_l = Eval_propfml(sub_l, atomic_evals)
    eval_r = Eval_propfml(sub_r, atomic_evals)
    return ConditionalClause[(eval_l, eval_r)]


def assignments(atom_symbols):
    """Generate all possible truth assignments for the atomic symbols in the formulas."""

    assignments = []
    for tv in product({0, 1}, repeat=len(atom_symbols)):
        assignment = dict(zip(atom_symbols, tv))
        assignments.append(assignment)

    return assignments


def Equiv_propfmls(fml1, fml2, assignments):
  i = 0
  while i < len(assignments):
    if Eval_propfml(fml1, assignments[i]) != Eval_propfml(fml2, assignments[i]):
      break
    i += 1

  if i == len(assignments):
    return True
  else:
    return False
  

def random_n_propfml(n, prop_variables, connectives, max_depth, assignments):

  l = [random_propfml_generator(max_depth, prop_variables, connectives)]

  while len(l) < n:
    fml = random_propfml_generator(max_depth, prop_variables, connectives)

    for f in l:
      tv = Equiv_propfmls(fml, f, assignments)
      if tv == True:
        break

    if tv == False:
      l.append(fml)
    else:
      continue

  return l

def fml_characters(fml_list, assignments):
    
    chars_info = []

    for fml in fml_list:
        
        evals = {tuple(assignments[i].values()) : Eval_propfml(fml, assignments[i]) for i in range(len(assignments))}
        # char_dict = {'name' : f'{fml}', **evals}
        chars_info.append((f'{fml}', evals))
    
    return chars_info
        

        
      



    
