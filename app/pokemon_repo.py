from app.pokemon import Pokemon
from pydantic_mongo import AbstractRepository

class PokemonRepository(AbstractRepository[Pokemon]):
    class Meta:
        collection_name = "pokemons"