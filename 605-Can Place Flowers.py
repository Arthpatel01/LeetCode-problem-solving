def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:

    for i, row in enumerate(flowerbed):
        if n == 0:
            return True
        if row == 0:
            if i == 0:
                if len(flowerbed)> i + 1:
                    if flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n = n - 1
                else:
                    if n <=1:
                        return True
                
            elif i == len(flowerbed) - 1:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n = n-1
            else:
                if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1]== 0:
                    flowerbed[i] = 1
                    n = n-1
    
    if n == 0:
        return True
    else:
        return False



flowerbed = [1,0,0,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n))