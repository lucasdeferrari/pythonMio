def generate_initial_string(target_string):
    # Genera un string de '0' con la misma longitud que el objetivo
    initial_string = '0' * len(target_string)
    return initial_string

def count_flips_to_match_target(initial_string, target_string):
    flips = 0  # Inicialmente, no hemos realizado ningún flip

    for i in range(len(initial_string)):
        if initial_string[i] != target_string[i]:
            # Si los caracteres no coinciden, hacemos un flip en la posición i y a la derecha
            flips += 1
            initial_string = flip(initial_string, i)
    
    return flips

# Función para realizar el flip
def flip(string, position):
    flipped_string = ""
    for i in range(len(string)):
        if i >= position:
            if string[i] == '0':
                flipped_string += '1'
            else:
                flipped_string += '0'
        else:
            flipped_string += string[i]
    return flipped_string



def test_count_flips_to_match_target():
    test_cases = [
        ("00000", "10010", 4),  # 3 flips necesarios para convertir 00000 en 10010
        ("000000", "110101", 5),  # 5 flips necesarios para convertir 000000 en 110101
        ("0000", "0000", 0),  # No se necesitan flips si el objetivo es igual al inicial
        ("10101", "10101", 0),  # No se necesitan flips si el objetivo es igual al inicial
        ('00000', '11111', 1),  # 5 flips necesarios para convertir 00000 en 11111
        ('00000', '10101',5),
        ('000000', '101010',)
    ]

    for initial, target, expected_flips in test_cases:
        flips_required = count_flips_to_match_target(initial, target)
        assert flips_required == expected_flips, f"Inicial: '{initial}', Objetivo: '{target}', Flips necesarios: {flips_required} (Esperados: {expected_flips})"

test_count_flips_to_match_target()


