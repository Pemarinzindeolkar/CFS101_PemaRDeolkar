def isValid(s: str) -> bool:
    stack = []
    bracket_map = {")": "(", "}": "{", "]": "["}
    
    for char in s:
        if char in bracket_map:  # Closing bracket
            if not stack or stack[-1] != bracket_map[char]:
                return False
            stack.pop()
        else:  # Opening bracket
            stack.append(char)
    
    return len(stack) == 0


test_strings = [
    "()",
    "()[]{}",
    "(]",
    "([)]",
    "{[]}",
    "",
    "((()))",
    "(()",
    "[({})]",
]

for s in test_strings:
    print(f"Input: '{s}'")
    print("Is valid:", isValid(s))
