def convertBinario(num):
    if num == 0:
        return ""
    else:
        return convertBinario(num//2) + str(num % 2) 

print(convertBinario(14))