def countBinarySubstrings(s: str) -> int:
    """
    About maximizing the number of 0's to the left of the breakpoint, and the number of ones to the right of the breakpoint
    :param s:
    :return:
    """

    one_tracker = [0] * len(s) + 1

    for i in range(len(s)):
        

