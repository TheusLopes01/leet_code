nums = [2, 7, 11, 15]
target = 9

def two_sum():
# Etapa 1: itere sobre os números na matriz. 
    for i in range(len(nums)):
# Etapa 2: para cada número, itere sobre o restante dos números na matriz.
        for j in range(i+1, len(nums)):
# Etapa 3: verifique se os dois números atuais somam o alvo.
            if nums[i] + nums[j] == target:
                return [i, j]
# Etapa 4: se nenhum par for encontrado, retorne uma lista vazia.
    return []

print(two_sum())