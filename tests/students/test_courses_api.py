import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture()
def client():
    return APIClient()


@pytest.fixture()
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture()
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.fixture()
def validation_settings(settings):
    return settings.MAX_STUDENTS_PER_COURSE


@pytest.mark.django_db
def test_retrieve_course(client, course_factory):
    course = course_factory()
    url = f'/api/v1/courses/{str(course.id)}/'

    response = client.get(url)
    data = response.json()

    assert data['name'] == course.name
    assert response.status_code == 200


@pytest.mark.django_db
def test_list_courses(client, course_factory):
    courses = course_factory(_quantity=5)
    url = '/api/v1/courses/'

    response = client.get(url)
    data = response.json()

    assert len(data) == len(courses)
    for k, c in enumerate(courses):
        assert c.name == data[k]['name']
    assert response.status_code == 200


@pytest.mark.django_db
def test_course_id_filter(client, course_factory):
    courses = course_factory(_quantity=5)
    url = f'/api/v1/courses/?id={str(courses[0].id)}'

    response = client.get(url)
    data = response.json()

    assert data[0]['id'] == courses[0].id
    assert data[0]['name'] == courses[0].name
    assert response.status_code == 200


@pytest.mark.django_db
def test_course_name_filter(client, course_factory):
    courses = course_factory(_quantity=5)
    url = f'/api/v1/courses/?name={str(courses[0].name)}'

    response = client.get(url)
    data = response.json()

    assert data[0]['id'] == courses[0].id
    assert data[0]['name'] == courses[0].name
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_course(client):
    url = '/api/v1/courses/'
    body = {"name": "course"}

    response = client.post(url, data=body)
    data = response.json()
    assert data['name'] == 'course'
    assert response.status_code == 201


@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory()
    url = f'/api/v1/courses/{str(course.id)}/'
    body = {"name": "course"}

    response = client.patch(url, body)
    data = response.json()
    assert data['name'] == 'course'
    assert response.status_code == 200


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory()
    url = f'/api/v1/courses/{str(course.id)}/'

    first_response = client.delete(url)
    second_response = client.get(url)

    assert first_response.status_code == 204
    assert second_response.status_code == 404









