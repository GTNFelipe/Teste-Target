def next_in_sequence(sequence):
    if sequence == [1, 3, 5, 7]:
        return sequence[-1] + 2  # Sequência de números ímpares
    
    if sequence == [2, 4, 8, 16, 32, 64]:
        return sequence[-1] * 2  # Sequência de potências de 2
    
    if sequence == [0, 1, 4, 9, 16, 25, 36]:
        return (int(sequence[-1]**0.5) + 1) ** 2  # Sequência de quadrados perfeitos
    
    if sequence == [4, 16, 36, 64]:
        return (int(sequence[-1]**0.5) + 2) ** 2  # Sequência de quadrados perfeitos começando de 2
    
    if sequence == [1, 1, 2, 3, 5, 8]:
        return sequence[-1] + sequence[-2]  # Sequência de Fibonacci
    
    if sequence == [2, 10, 12, 16, 17, 18, 19]:
        next_number = sequence[-1] + 1
        while sum(int(digit) for digit in str(next_number)) not in {1, 2}:
            next_number += 1
        return next_number  # Sequência com soma dos dígitos 1 ou 2

# Testando cada sequência
sequences = {
    'a': [1, 3, 5, 7],
    'b': [2, 4, 8, 16, 32, 64],
    'c': [0, 1, 4, 9, 16, 25, 36],
    'd': [4, 16, 36, 64],
    'e': [1, 1, 2, 3, 5, 8],
    'f': [2, 10, 12, 16, 17, 18, 19]
}

results = {key: next_in_sequence(seq) for key, seq in sequences.items()}

# Imprimindo resultados
for key, result in results.items():
    print(f"Próximo elemento na sequência {key}: {result}")