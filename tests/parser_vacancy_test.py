import pytest
from src.parser_vacancy import ParserVacancy

@pytest.fixture
def sample_data():
    return [
        {"name": "Python Developer", "salary": {"from": 100, "to": 200}, "area": {"name": "IT", "url": "https://example.com/vacancy1"}},
        {"name": "Java Developer", "salary": {"from": 200, "to": 300}, "area": {"name": "IT", "url": "https://example.com/vacancy2"}, "snippet": {"requirement": "Java developer needed"}},
        {"name": "JavaScript Developer", "salary": {"from": 150, "to": 250}, "area": {"name": "IT", "url": "https://example.com/vacancy3"}},
        {"name": "C++ Developer", "salary": {"from": 300, "to": 400}, "area": {"name": "IT", "url": "https://example.com/vacancy4"}},
        {"name": "Ruby Developer", "salary": {"from": 120, "to": 220}, "area": {"name": "IT", "url": "https://example.com/vacancy5"}, "snippet": {"requirement": "Ruby developer needed"}},
        {"name": "PHP Developer", "salary": {"from": 250, "to": 350}, "area": {"name": "IT", "url": "https://example.com/vacancy6"}},
        {"name": "Go Developer", "salary": {"from": 180, "to": 280}, "area": {"name": "IT", "url": "https://example.com/vacancy7"}},
        {"name": "Swift Developer", "salary": {"from": 220, "to": 320}, "area": {"name": "IT", "url": "https://example.com/vacancy8"}, "snippet": {"requirement": "Swift developer needed"}},
        {"name": "Kotlin Developer", "salary": {"from": 190, "to": 290}, "area": {"name": "IT", "url": "https://example.com/vacancy9"}},
        {"name": "Rust Developer", "salary": {"from": 240, "to": 340}, "area": {"name": "IT", "url": "https://example.com/vacancy10"}},
        {"name": "Scala Developer", "salary": {"from": 260, "to": 360}, "area": {"name": "IT", "url": "https://example.com/vacancy11"}},
        {"name": "Haskell Developer", "salary": {"from": 210, "to": 310}, "area": {"name": "IT", "url": "https://example.com/vacancy12"}},
        {"name": "Perl Developer", "salary": {"from": 170, "to": 240}, "area": {"name": "IT", "url": "https://example.com/vacancy13"}},
    ]

@pytest.fixture
def parser(sample_data):
    return ParserVacancy(sample_data)

def test_create_parser(parser, sample_data):
    assert len(parser.data) == len(sample_data)
    assert len(parser.list_instances) == len(sample_data)

def test_filter_vacancies(parser):
    vacancy = parser.parse_vacansys(params={"filter_words": ["Python"]})
    assert len(vacancy) == 1
    assert vacancy[0].name == "Python Developer"

def test_get_vacancies_by_salary(parser):
    vacancy = parser.parse_vacansys(params={"salary_from": 150, "salary_to": 250})
    assert vacancy[0].name == "JavaScript Developer"
    assert len(vacancy) == 2

def test_sort_vacancies_from(parser):
    vacancy = parser.parse_vacansys(params={"sort_salary_from": True})
    assert vacancy[0].name == "C++ Developer"
    assert vacancy[1].name == "Scala Developer"
    assert vacancy[2].name == "PHP Developer"

def test_sort_vacancies_to(parser):
    vacancy = parser.parse_vacansys(params={"sort_salary_to": True})
    assert vacancy[0].name == "C++ Developer"
    assert vacancy[1].name == "Scala Developer"
    assert vacancy[2].name == "PHP Developer"

def test_get_top_vacancies(parser):
    vacancy = parser.parse_vacansys(params={"top_n": 5})
    assert len(vacancy) == 5

def test_create_empty_parser():
    parser = ParserVacancy([])
    assert len(parser.data) == 0
    assert len(parser.list_instances) == 0

def test_invalid_data_type():
    with pytest.raises(TypeError):
        ParserVacancy("invalid data")

def test_combination_filter_and_salary(parser):
    vacancy = parser.parse_vacansys(params={"filter_words":["Developer"], "salary_from":150, "salary_to":250})
    assert len(vacancy) == 2

def test_combination_filter_and_sort(parser):
    vacancy = parser.parse_vacansys(params={"filter_words":["Developer"], "sort_salary_from":True})
    assert vacancy[0].name == "C++ Developer"

def test_combination_salary_and_sort(parser):
    vacancy = parser.parse_vacansys(params={"salary_from":100, "salary_to":300, "sort_salary_to":True})
    assert vacancy[0].name == "Java Developer"
    assert vacancy[1].name == "Kotlin Developer"

def test_combination_all_arguments(parser):
    vacancy = parser.parse_vacansys(params={"filter_words": ["Developer"], "salary_from": 150, "salary_to": 250, "sort_salary_from": True, "top_n": 3})
    assert len(vacancy) == 2
    assert vacancy[0].name == "Perl Developer"

if __name__ == "__main__":
    pytest.main()
