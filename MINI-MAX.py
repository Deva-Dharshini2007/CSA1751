# Minimax that alternates: MAX -> MIN -> MAX

def minimax(node, depth, is_max_turn):

    # Leaf node -> return value
    if isinstance(node, int):
        return node

    if is_max_turn:      # MAX player's turn
        best = float('-inf')
        for child in node:
            best = max(best, minimax(child, depth+1, False))
        return best

    else:                # MIN player's turn
        best = float('inf')
        for child in node:
            best = min(best, minimax(child, depth+1, True))
        return best


# -------- Tree matching your notebook diagram --------
# Level-1 : MAX (root)
# Level-2 : MIN nodes  B ,  C
# Level-3 : MAX nodes under each

game_tree = [
    [ [2, 3], [5] ],     # Subtree B  -> MAX picks 3
    [ [9, 0], [1] ]      # Subtree C  -> MAX picks 1
]

# Root is MAX
result = minimax(game_tree, 0, True)

print("Final Minimax Value =", result)
