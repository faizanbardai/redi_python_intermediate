from poke_ubersetzung import pokemon_to_german, pokemon_to_english


def test_pokemon_to_german():
    assert pokemon_to_german('Bulbasaur') == 'Bisasam'
    assert pokemon_to_german('Pikachu') == 'Pikachu'
    assert pokemon_to_german('Blacephalon') == 'Kopplosio'

    assert pokemon_to_german('ninetales') == 'Vulnona'
    assert pokemon_to_german('FERALIGATR') == 'Impergator'
    assert pokemon_to_german('LuDiCoLo') == 'Kappalores'

    assert pokemon_to_german('Kein pokemon') is None


def test_pokemon_to_english():
    assert pokemon_to_english('Bisasam') == 'Bulbasaur'
    assert pokemon_to_english('Pikachu') == 'Pikachu'
    assert pokemon_to_english('Kopplosio') == 'Blacephalon'

    assert pokemon_to_english('vulnona') == 'Ninetales'
    assert pokemon_to_english('IMPERGATOR') == 'Feraligatr'
    assert pokemon_to_english('KaPpAlOrEs') == 'Ludicolo'

    assert pokemon_to_english('Not a pokemon') is None
