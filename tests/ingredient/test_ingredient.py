from src.models.ingredient import Ingredient


# Req 1
def test_ingredient():
    # Teste para verificar se a classe pode ser instanciada corretamente
    ingrediente1 = Ingredient("Tomate")
    assert isinstance(ingrediente1, Ingredient)
    assert ingrediente1.name == "Tomate"
    assert ingrediente1.restrictions == set()

    # Teste para verificar o método mágico __repr__
    assert repr(ingrediente1) == "Ingredient('Tomate')"

    # Teste para verificar o método mágico __eq__
    ingrediente2 = Ingredient("Tomate")
    assert ingrediente1 == ingrediente2

    # Teste para verificar o método mágico __hash__
    assert hash(ingrediente1) == hash(ingrediente2)

    # Teste para verificar o método mágico __hash__
    # retornando hashes diferentes
    ingrediente3 = Ingredient("Cebola")
    assert hash(ingrediente1) != hash(ingrediente3)

    # Teste para verificar a comparação de igualdade
    # entre ingredientes diferentes
    assert ingrediente1 != Ingredient("Alho")

    # Teste para verificar se o atributo name é diferente
    # do passado ao construtor
    assert ingrediente1.name == "Tomate"

    # Teste para verificar se o atributo restrictions
    # contém os valores corretos
    assert ingrediente1.restrictions == set()
