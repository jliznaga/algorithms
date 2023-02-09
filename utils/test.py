from typing import Dict, Optional, Tuple
import itertools

# Complete the max_result_expression function below.
# You may add any imports you require from the standard library.
# Feel free to define your own helper functions, classes etc as you see fit.


def evaluate(exp):
    stack = []
    for c in exp[::-1].replace(' ', ''):
        if c.isdigit():
            stack.append(int(c))
        else:
            lop = stack.pop()
            rop = stack.pop()
        if c == '+':
            stack.append(lop + rop)
        elif c == '-':
            stack.append(lop - rop)
        elif c == '*':
            stack.append(lop * rop)
        elif c == '/':
            stack.append(lop / rop)

    return stack.pop()


def generate_lists_from_vars(variables, key):
    return [n for n in range(variables[key][0], variables[key][1])]


def max_result_expression(expression: str, variables: Dict[str, Tuple[int, int]]) -> Optional[int]:
    """
    Evaluates the prefix expression and calculates the maximum result for the given variable ranges.

    Arguments:
        expression: the prefix expression to evaluate.
        variables: Keys of this dictionary may appear as variables in the expression.
            Values are tuples of `(min, max)` that specify the range of values of the variable.
            The upper bound `max` is NOT included in the range, so (2, 5) expands to [2, 3, 4].

    Returns:
        int:  the maximum result of the expression for any combination of the supplied variables.
        None: in the case there is no valid result for any combination of the supplied variables.
    """
    try:
        results = []
        if len(variables.keys()) == 0:
            results.append(evaluate(expression))
        else:
            # TODO: Get conbinations of variables
            lists = []
            combinations = []
            for key in variables.keys():
                lists.append(generate_lists_from_vars(variables, key)) 
            # combinations = itertools.combinations(lists, len(variables.keys()))
            combinations = itertools.product(lists)
            # TODO: Replace all possible values on expression
            for cb in combinations:
                new_expression = expression
                for index, key in enumerate(variables.keys()):
                    new_expression = new_expression.replace(key, str(cb[index]))

                # TODO: Evaluate and append to results
                results.append(evaluate(new_expression))

        return max(results)
    except Exception as error:
        print(error)
        return


print(max_result_expression('* + 2 x y', { "x": (0, 2), "y": (2, 4) }))