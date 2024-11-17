import pytest
from project_page import ProjectPage
project_page = ProjectPage()


def test_get_projects():
    response = project_page.get_projects()
    assert isinstance(response.get('content'), list)


def test_create_project_increases_count():
    initial_count = project_page.get_projects().get('paging', {}).get('count', 0)
    project_page.create_project()
    updated_count = project_page.get_projects().get('paging', {}).get('count', 0)
    assert updated_count == initial_count + 1


def test_update_project():
    project_id = project_page.create_project()
    response = project_page.update_project(project_id)
    assert response['title'] == "Тестовое питон измененное"


def test_get_project_by_id():
    project_id = project_page.create_project()
    response = project_page.get_project_by_id(project_id)
    assert response['id'] == project_id


def test_create_project_without_title():
    status_code = project_page.create_project_without_title()
    assert status_code == 400


def test_update_project_without_id():
    status_code = project_page.update_project_without_id()
    assert status_code == 404