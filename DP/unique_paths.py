def uniquePaths(m: int, n: int) -> int:
    paths = dict()

    def traverse(loc, m, n):

        # If we're out of bounds, return 0
        if loc[0] >= m or loc[1] >= n:
            return 0

        # If we got a success, return 1
        if loc == (m-1, n-1):
            return 1

        # If we've seen this path before, return
        if loc in paths.keys():
            return paths[loc]

        right = traverse((loc[0], loc[1] + 1), m, n)
        down = traverse((loc[0] + 1, loc[1]), m, n)

        paths[loc] = right + down
        return right + down

    return traverse((0, 0), m, n)

print(uniquePaths(2,2))