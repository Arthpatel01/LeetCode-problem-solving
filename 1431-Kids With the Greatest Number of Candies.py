def kidsWithCandies(candies: list[int], extraCandies: int):
    output = []

    for i in range(len(candies)):
        total_can = candies[i] + extraCandies
        if total_can >= max(candies):
            output.append(True)
        else:
            output.append(False)
    return output

print(kidsWithCandies([2,8,7], 1))
    