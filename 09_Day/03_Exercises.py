#1
persona = {
    'primer_nombre': 'Asabeneh',
    'apellido': 'Yetayeh',
    'edad': 250,
    'país': 'Finlandia',
    'está_casado': True,
    'habilidades': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'dirección': {
        'calle': 'Calle del espacio',
        'código_postal': '02210'
    }
}

# habilidades
if 'habilidades' in persona:
    habilidades = persona['habilidades']
    # Imprimir habilidad del medio
    medio = habilidades[len(habilidades) // 2]
    print(f"La habilidad del medio es: {medio}")

    # python
    if 'Python' in habilidades:
        print("La persona tiene la habilidad Python.")
    else:
        print("La persona no tiene la habilidad Python.")

    # titulo según habilidades
    if 'JavaScript' in habilidades and 'React' in habilidades and len(habilidades) == 2:
        print("Él es un desarrollador de front end.")
    elif 'Node' in habilidades and 'Python' in habilidades and 'MongoDB' in habilidades:
        print("Él es un desarrollador de back end.")
    elif 'React' in habilidades and 'Node' in habilidades and 'MongoDB' in habilidades:
        print("Él es un desarrollador fullstack.")
    else:
        print("Título desconocido.")

# casado y en finlandia
if persona['está_casado'] and persona['país'] == 'Finlandia':
    print(f"{persona['primer_nombre']} {persona['apellido']} está casado y vive en Finlandia.")