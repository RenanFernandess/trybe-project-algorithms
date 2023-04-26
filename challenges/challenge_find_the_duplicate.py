def find_duplicate(nums: list):
    """Faça o código aqui."""
    nums.sort()
    num = False
    for index in range(1, len(nums)):
        prev_num = nums[index - 1]
        current_num = nums[index]
        if not (type(current_num) == int and type(prev_num) == int) or (
            current_num < 0 or prev_num < 0
        ):
            return num
        if current_num == prev_num:
            num = current_num
    return num
