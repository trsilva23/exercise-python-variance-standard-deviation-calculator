import numpy as np

def calculate(list_of_nine_numbers):
    # Verifica se a lista de entrada tem exatamente 9 números
    if len(list_of_nine_numbers) != 9:
        # Se não tiver 9, levanta um erro com a mensagem especificada
        raise ValueError("List must contain nine numbers.")
    
    # Converte a lista em um array NumPy e remodela para uma matriz 3x3
    matrix = np.array(list_of_nine_numbers).reshape(3, 3)
    
    # Dicionário para armazenar todos os resultados
    calculations = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }
    
    # Lista de funções NumPy para iterar e aplicar
    functions = [np.mean, np.var, np.std, np.max, np.min, np.sum]
    
    # Nomes das chaves no dicionário
    keys = ['mean', 'variance', 'standard deviation', 'max', 'min', 'sum']
    
    # Itera sobre cada função e sua chave correspondente
    for func, key in zip(functions, keys):
        # Calcula para o Eixo 1 (linhas), Eixo 0 (colunas) e matriz achatada (None)
        # Usa .tolist() para converter arrays NumPy de volta para listas Python
        calculations[key].append(func(matrix, axis=0).tolist())
        calculations[key].append(func(matrix, axis=1).tolist())
        calculations[key].append(func(matrix).tolist())              
        # axis=None: Opera em todos os elementos da matriz como se fosse uma única lista ("flattened"/achatada).
        # É o comportamento padrão se o argumento 'axis' não for especificado na chamada da função. 
        
    return calculations

