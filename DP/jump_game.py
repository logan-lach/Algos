visited = {int: bool}
trek = set()


def canJump(nums) -> bool:
        reach = 0
        for i in range(len(nums)):
            if reach < i:
                return False
            reach = max(reach, i + nums[i])

        return True;

print(canJump([2,3,1,1,4]))



