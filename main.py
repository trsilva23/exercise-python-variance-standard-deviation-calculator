# main.py para testar a função calculate localmente
from mean_var_std import calculate

# Exemplo de entrada que deve funcionar
input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
result = calculate(input_list)
print(result)

# Exemplo de entrada que deve causar um erro (descomente para testar)
# input_list_error = [1, 2, 3]
# calculate(input_list_error)
