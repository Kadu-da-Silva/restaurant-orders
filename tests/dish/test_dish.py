import pytest
from src.models.dish import Dish
from src.models.ingredient import Ingredient


# Req2
def test_dish():
    # Teste para verificar se a classe pode ser instanciada corretamente
    prato1 = Dish("Lasanha", 29.99)
    assert isinstance(prato1, Dish)
    assert prato1.name == "Lasanha"
    assert prato1.price == 29.99
    assert prato1.recipe == {}

    # Teste para verificar o método mágico __repr__
    assert repr(prato1) == "Dish('Lasanha', R$29.99)"

    # Teste para verificar o método mágico __eq__
    prato2 = Dish("Lasanha", 29.99)
    assert prato1 == prato2

    # Teste para verificar o método mágico __hash__
    assert hash(prato1) == hash(prato2)

    # Teste para verificar a adição de ingredientes à receita
    ingrediente1 = Ingredient("Massa de Lasanha")
    prato1.add_ingredient_dependency(ingrediente1, 2)
    assert prato1.recipe == {ingrediente1: 2}

    # Teste para verificar a quantidade correta de um ingrediente na receita
    assert prato1.recipe.get(ingrediente1) == 2

    # Teste para verificar o método get_restrictions
    assert prato1.get_restrictions() == set()

    # Teste para verificar o método get_ingredients
    assert prato1.get_ingredients() == {ingrediente1}

    # Teste para verificar os hashes de pratos diferentes
    prato3 = Dish("Macarrão", 15.99)
    assert hash(prato1) != hash(prato3)

    # Teste para verificar os hashes de pratos iguais
    prato4 = Dish("Lasanha", 29.99)
    assert hash(prato1) == hash(prato4)

    # Teste para verificar o construtor emitindo TypeError quando deveria
    with pytest.raises(TypeError):
        _ = Dish("Salada", "invalid_price")

    # Teste para verificar o construtor emitindo ValueError quando deveria
    with pytest.raises(ValueError):
        _ = Dish("Sopa", -5.0)

# usando o _ (underscore) para indicar que a variável está
# sendo usada apenas para ignorar o aviso
