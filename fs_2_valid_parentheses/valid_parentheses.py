def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    if (parens[0] == ")"):
        return False
    
    balancer = 0

    for p in parens:
        if p == '(':
            balancer += 1
        elif p == ')':
            balancer -= 1
    
    return balancer == 0