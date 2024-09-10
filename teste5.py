def identify_lights():
    # Simulação inicial dos estados das lâmpadas e interruptores
    # 'off' = desligado, 'on' = ligado
    # A lâmpada que estava ligada por mais tempo vai estar quente
    # As lâmpadas inicialmente estão apagadas e frias
    lights = {'A': 'cold', 'B': 'cold', 'C': 'cold'}
    
    # Fase 1: Liga o primeiro interruptor e deixa ligado por um tempo
    # (Simula o aquecimento)
    lights['A'] = 'warm'
    
    # Fase 2: Desliga o primeiro interruptor e liga o segundo
    # (Fica ligado até a checagem)
    # Simulando o estado das lâmpadas depois
    lights['A'] = 'cold'  # Primeiro interruptor desligado
    lights['B'] = 'warm'  # Segundo interruptor ligado
    lights['C'] = 'cold'  # Terceiro interruptor permanece desligado
    
    # Checando os estados das lâmpadas
    results = {
        'Lâmpada controlada pelo primeiro interruptor': 'A' if lights['A'] == 'warm' else 'não identificado',
        'Lâmpada controlada pelo segundo interruptor': 'B' if lights['B'] == 'warm' else 'não identificado',
        'Lâmpada controlada pelo terceiro interruptor': 'C' if lights['C'] == 'cold' else 'não identificado'
    }
    
    return results

# Identificando as lâmpadas
results = identify_lights()
for description, lamp in results.items():
    print(f"{description}: {lamp}")