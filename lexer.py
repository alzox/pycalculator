import re

scanner=re.Scanner([
  (r"[0-9]+",       lambda scanner,token:("INTEGER", token)),
  (r"[()]",        lambda scanner,token:("PARENTHESIS", token)),
  (r"[\*\+\-\/]",   lambda scanner,token:("OPERATION", token)),
  (r"\s+", None), # None == skip token.
])

def get_token_int(token: tuple[str, str]) -> int:
    return int(token[1])

def get_token_op(token: tuple[str, str]) -> str:
    return token[1]

def find_matching_paren(tokens, start):
    depth = 0
    for i in range(start, len(tokens)):
        if tokens[i][1] == "(":
            depth += 1
        elif tokens[i][1] == ")":
            depth -= 1
            if depth == 0:
               return i
    # crashes if parenthesis aren't there
    raise Exception("Unmatched parenthesis")

def apply(op, lval, rval) -> float:
    if op == "+":
        result = lval + rval
    elif op == "-":
        result = lval - rval
    elif op == "*":
        result = lval * rval
    elif op == "/":
        try:
            result = lval // rval
        except:
            result = float('inf')
    else:
        raise Exception("Unknown operator")
    return result

def calculate(tokens: list[tuple[str, str]]) -> float:
    # Edge Case of starting w/ (x+(x+1))
    if tokens[0][1] == "(" and find_matching_paren(tokens, 0) == len(tokens) - 1:
        return calculate(tokens[1:-1])

    # Base Cases
    if len(tokens) == 1:
        return get_token_int(tokens[0])
    if len(tokens) < 3:
        raise Exception("Bad input")

    # Left 
    if tokens[0][1] == "(":
        end = find_matching_paren(tokens, 0)
        lval = calculate(tokens[1:end])
        rest = tokens[end + 1:]
    else:
        lval = get_token_int(tokens[0])
        rest = tokens[1:]

    if not rest:
        return lval

    # Operator
    op = get_token_op(rest[0])

    # Right 
    if rest[1][1] == "(":
        end = find_matching_paren(rest, 1)
        rval = calculate(rest[2:end])
        remaining = rest[end + 1:]
    else:
        rval = get_token_int(rest[1])
        remaining = rest[2:]
    
    result = apply(op,lval,rval)
    if remaining:
        return calculate([("INTEGER", str(result))] + remaining)
    return result

results, remainder=scanner.scan("(45*(2+1))")
print(calculate((results)))
