def identificando_luz():
    # Simulação inicial dos estados das lâmpadas e interruptores
    # 'off' = desligado, 'on' = ligado
    # A lâmpada que estava ligada por mais tempo vai estar quente
    # As lâmpadas inicialmente estão apagadas e frias
    lampada = {'A': 'fria', 'B': 'fria', 'C': 'fria'}
    
    # Fase 1: Liga o primeiro interruptor e deixa ligado por um tempo
    # (Simula o aquecimento)
    lampada['A'] = 'esuentou'
    
    # Fase 2: Desliga o primeiro interruptor e liga o segundo
    # (Fica ligado até a checagem)
    # Simulando o estado das lâmpadas depois
    lampada['A'] = 'fria'  # Primeiro interruptor desligado
    lampada['B'] = 'quente'  # Segundo interruptor ligado
    lampada['C'] = 'fria'  # Terceiro interruptor permanece desligado
    
    # Checando os estados das lâmpadas
    results = {
        'Lâmpada controlada pelo primeiro interruptor': 'A' if lampada['A'] == 'qquente' else 'não identificado',
        'Lâmpada controlada pelo segundo interruptor': 'B' if lampada['B'] == 'quente' else 'não identificado',
        'Lâmpada controlada pelo terceiro interruptor': 'C' if lampada['C'] == 'fria' else 'não identificado'
    }
    
    return results

# Identificando as lâmpadas
results = identificando_luz()
for description, lamp in results.items():
    print(f"{description}: {lamp}")

