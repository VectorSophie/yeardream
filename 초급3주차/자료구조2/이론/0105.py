def inorder(tree, depth):
    result = []

    if tree.left != None:
        result += inorder(tree.left, depth+1)
    
    tree.setDepth(depth)
    result.append(tree)

    if tree.right != None:
        result += inorder(tree.right, depth+1)
    return result

def getWidth(myTree) :
    result = inorder(myTree, 1)
    n = len(result)

    left = [1001] * 1000
    right = [-1] * 1000
    maxDepth = 0

    for i in range(n):
        d = result[i].depth

        left[d] = min(left[d], i)
        right[d] = max(right[d], i)
        maxDepth = max(maxDepth, d)

    ansDepth = 0
    ans = 0

    for i in range(1, maxDepth+1):
        temp = right[i] - left[i] + 1

        if ans< temp:
            ansDepth = i
            ans = temp

    return (ansDepth, ans)