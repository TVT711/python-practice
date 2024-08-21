def balance_sentence(sentence_input=None):
    if sentence_input is None:
        sentence_input = []

    required_symbol = {'{': '}', '[': ']', '(': ')'}
    stack = []
    result = []
    bal_str = 'This string is balanced'
    unbal_str = 'This string is not balanced'
    # print(required_symbol.values())
    for sentence in sentence_input:
        for char in sentence:
            if char in required_symbol:
                stack.append(char)
            elif char in required_symbol.values():
                if not stack:
                    result.append(unbal_str + '=>' + sentence)
                opening_symbol = stack.pop()
                if required_symbol[opening_symbol] != char:
                    result.append(unbal_str + '=>' + sentence)
        result.append(bal_str + '=>' + sentence)

    return result

arr_sentence_test = [
    "The {quick (brown [fox]) jumps} over {the lazy (dog)}",
    "She {bought [apples (and {oranges})]} from {the market (near {her house})}",
    "[The {big (red} ball] rolled {down the hill} quickly",
    "{The {old (man [walks} slowly)} with {his {walking [stick}]}"
]

print(balance_sentence(arr_sentence_test))
