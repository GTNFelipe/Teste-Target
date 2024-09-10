def verificar_a(string):
    quantidade = string.lower().count('a')
    
    print(f"A letra 'a' aparece {quantidade} vez(es) na string.") if quantidade > 0 else print("A letra 'a' não aparece na string.")

# Exemplo de uso
texto = input("Informe uma palavra: ")
verificar_a(texto)