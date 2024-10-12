import pytest
from random import randint
from students.models import Course
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
    amount = 10
    courses = courses_factory(_quantity=amount)
    course_index = randint(0, amount - 1)
    course_id = courses[course_index].id
    response = client.get(f"{BASE_COURSE_URL}?id={course_id}")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['id'] == course_id
    assert data[0]['name'] == courses[course_index].name


@pytest.mark.django_db
def test_filter_course_by_name(client, courses_factory):
    amount = 10
    courses = courses_factory(_quantity=amount)
    course_index = randint(0, amount - 1)
    course_name = courses[course_index].name
    response = client.get(f"{BASE_COURSE_URL}?name={course_name}")
    data = response.json()

    assert response.status_code == 200
    assert len(data) == 1
    assert data[0]['name'] == course_name
    assert data[0]['id'] == courses[course_index].id


@pytest.mark.django_db
def test_create_course(client, students_factory):
    student = students_factory()
    course = {
        'name': 'test course',
        'students': [student.id],
    }
    response = client.post(BASE_COURSE_URL, course)
    data = response.json()
    assert response.status_code == 201
    assert data['name'] == course['name']
    assert data['students'][0] == student.id


@pytest.mark.django_db
def test_update_course(client, courses_factory):
    course = courses_factory()
    new_name = 'new test course'
    response = client.patch(f"{BASE_COURSE_URL}{course.id}/", {'name': new_name}, format='json')
    data = response.json()

    assert response.status_code == 200
    assert data['name'] == new_name


@pytest.mark.django_db
def test_delete_course(client, courses_factory):
    course = courses_factory()
    response = client.delete(f"{BASE_COURSE_URL}{course.id}/")

    assert response.status_code == 204
    assert Course.objects.count() == 0
    assert Course.objects.filter(id=course.id).exists() is False

