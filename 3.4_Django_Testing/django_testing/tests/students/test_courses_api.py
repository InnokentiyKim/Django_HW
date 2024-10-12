from tests.conftest import courses_factory, students_factory, client


def test_retrieve_course(client, students_factory, courses_factory):
    base_url = "/api/v1/courses/"
    course = courses_factory()


