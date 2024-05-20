import json
import pytest
from src.saver import JSONSaver

@pytest.fixture
def temp_json_file(tmp_path):
    """
    Создаёт временный JSON-файл для тестирования и удаляет его после использования.
    """
    temp_file = tmp_path / "temp_vacancies.json"
    yield temp_file
    if temp_file.exists():
        temp_file.unlink()

def test_save(temp_json_file):
    saver = JSONSaver(path=temp_json_file)
    data = [
        {"id": 1, "name": "Vacancy 1"},
        {"id": 2, "name": "Vacancy 2"},
    ]
    saver.save(data)

    with open(temp_json_file, 'r', encoding='utf-8') as file:
        saved_data = json.load(file)
        file.close()

    assert saved_data == data

def test_delete(temp_json_file):
    initial_data = [
        {"id": 1, "name": "Vacancy 1"},
        {"id": 2, "name": "Vacancy 2"},
        {"id": 3, "name": "Vacancy 3"},
    ]

    with open(temp_json_file, 'w', encoding='utf-8') as file:
        json.dump(initial_data, file, ensure_ascii=False, indent=4)

    saver = JSONSaver(path=temp_json_file)
    saver.delete(2)

    with open(temp_json_file, 'r', encoding='utf-8') as file:
        data_after_delete = json.load(file)
        file.close()

    expected_data = [
        {"id": 1, "name": "Vacancy 1"},
        {"id": 3, "name": "Vacancy 3"},
    ]

    assert data_after_delete == expected_data

def test_delete_nonexistent_id(temp_json_file):
    initial_data = [
        {"id": 1, "name": "Vacancy 1"},
        {"id": 2, "name": "Vacancy 2"},
    ]

    with open(temp_json_file, 'w', encoding='utf-8') as file:
        json.dump(initial_data, file, ensure_ascii=False, indent=4)

    saver = JSONSaver(path=temp_json_file)
    saver.delete(3)

    with open(temp_json_file, 'r', encoding='utf-8') as file:
        data_after_delete = json.load(file)
        file.close()

    assert data_after_delete == initial_data
