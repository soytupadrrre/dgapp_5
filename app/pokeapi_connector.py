import vlm_pypoke

client = vlm_pypoke.PokeClient()

# Obtención de Pokemon
# https://pokeapi.co/api/v2/pokemon/
# client.get_pokemon(name or id)

# Obtención de especie
# https://pokeapi.co/api/v2/pokemon-species/
# client.get_pokemon_species(name or id)

# Obtención de cadena de evolución
# El ID se obtiene desde el pokemon-species
# https://pokeapi.co/api/v2/evolution-chain/
# client.get_evolution_chain(id)