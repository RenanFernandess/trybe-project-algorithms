def find_duplicate(nums):
    """Faça o código aqui."""
    previous_count = 0
    count = 0
    for n in nums:
        for m in nums:
            if n == m:
                count += 1
        if count > previous_count:
            previous_count = count
        count = 0

    return previous_count
