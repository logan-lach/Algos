def even_odd_tree(root):
    queue = [root]
    nodes_visited = 0
    level_barrier = 1
    prev_val = None
    child_count = 0
    actual_level = 0

    while len(queue) != 0:
        node = queue[0]
        queue = queue[1:]
        nodes_visited += 1
        child_count += len(root.children)

        for x in root.children:
            queue.append(x)

        if prev_val is not None:
            if actual_level % 2 == 0:
                if node.val >= prev_val:
                    return False

            else:
                if node.val <= prev_val:
                    return False

        if level_barrier == nodes_visited:
            level_barrier += child_count
            child_count = 0
            actual_level += 1
            prev_val = None
        else:
            prev_val = node.val

    return True