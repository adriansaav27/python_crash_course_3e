import city_functions


def test_city_country():
    formatted_address = city_functions.formmated_address("santiago", "chile")
    assert formatted_address == "Santiago, Chile"


def test_city_country_population():
    formatted_address = city_functions.formmated_address("santiago", "chile", 5_000_000)
    assert formatted_address == "Santiago, Chile - population 5000000"
