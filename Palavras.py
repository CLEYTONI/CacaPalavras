def palavra():
    from random import choice
    animais = choice(['CACHORRO', 'VACA', 'GATO', 'FOCA', 'TARTARUGA', 'RATO', 'COELHO', 'OVELHA'])
    objeto = choice(['FACA', 'CORDA', 'LAPÍS', 'CANETA', 'CELULAR', 'COPO', 'LATA', 'CHAVE', 'MOCHILA'])
    fruta = choice(['MAÇA', 'MANGA', 'KIWI', 'BANANA', 'LARANJA', 'LIMÃO', 'PÊSSEGO', 'ABACAXI', 'MORANGO'])
    escolhido = choice([animais, objeto, fruta])
    if escolhido in animais:
        categoria = 'ANIMAL'
    elif escolhido in objeto:
        categoria = 'OBJETO'
    else:
        categoria = 'FRUTA'
    return str(escolhido), categoria
