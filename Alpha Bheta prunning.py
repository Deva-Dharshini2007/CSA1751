# Alpha-Beta Pruning : MAX -> MIN -> MAX

def alphabeta(node, depth, alpha, beta, is_max_turn):

    # Leaf node
    if isinstance(node, int):
        return node

    if is_max_turn:     # MAX player
        best = float('-inf')
        for child in node:
            value = alphabeta(child, depth+1, alpha, beta, False)
            best = max(best, value)
            alpha = max(alpha, best)

            # Pruning condition
            if beta <= alpha:
                print("Pruned at MAX level")
                break
        return best

    else:               # MIN player
        best = float('inf')
        for child in node:
            value = alphabeta(child, depth+1, alpha, beta, True)
            best = min(best, value)
            beta = min(beta, best)

            # Pruning condition
            if beta <= alpha:
                print("Pruned at MIN level")
                break
        return best


# -------- Tree matching your notebook diagram --------
# Level-1 : MAX (Root)
# Level-2 : MIN nodes (B , C)
# Level-3 : MAX nodes below each

game_tree = [
    [ [2, 3], [5] ],     # Subtree B  -> MAX picks 3
    [ [9, 0], [1] ]      # Subtree C  -> MAX picks 1
]

result = alphabeta(game_tree, 0, float('-inf'), float('inf'), True)

print("Final Value using Alpha-Beta Pruning =", result)
