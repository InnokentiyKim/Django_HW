import pytest
from tests.conftest import courses_factory, students_factory, client

BASE_COURSE_URL = "/api/v1/courses/"
BASE_STUDENT_URL = "/api/v1/students/"

@pytest.mark.django_db
def test_retrieve_course(client, courses_factory):
    course = courses_factory()
    response = client.get(f"{BASE_COURSE_URL}{course.id}/")
    data = response.json()

    assert response.status_code == 200
    assert data['name'] == course.name


@pytest.mark.django_db
def test_list_courses(client, courses_factory):
    courses = courses_factory(_quantity=10)
    response = client.get(BASE_COURSE_URL)
    data = response.json()

    assert response.status_code == 200
    assert len(data) == len(courses)
    for i, course in enumerate(courses):
        assert data[i]['name'] == course.name


@pytest.mark.django_db
def test_filter_course_by_id(client, courses_factory):
    courses = courses_factory(_quantity=10)
    course_index = 3
    course_id = courses[course_index].id
    response = client.get(f"{BASE_COURSE_URL}?id={course_id}")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == courses[course_index].name

