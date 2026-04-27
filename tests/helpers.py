import allure

@allure.step('Проверяем статус-код')
def check_status_code(response, expected_status=200):
    assert response.status_code == expected_status
    f'Ожидался статус-код {expected_status}, но получен {response.status_code}'