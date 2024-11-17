import requests


class ProjectPage:
    BASE_URL = "https://ru.yougile.com/api-v2/projects"
    HEADERS = {
        "Content-Type": "application/json",
        "Authorization": "Bearer itda9Qq1nsn4T5iVGEPDR6JeoiMdXuFEzptbB6PoMDNupkE0I5v1pwgpIe1aoM7k"
    }

    def create_project(self, title="Тестовое питон", users=None):
        if users is None:
            users = {
                "9cd8bd05-0883-4978-b576-5b90900a872e": "worker"
            }
        payload = {
            "title": title,
            "users": users
        }
        response = requests.post(self.BASE_URL, json=payload, headers=self.HEADERS)
        response.raise_for_status()  # Выдает ошибку для статусов 4xx и 5xx
        return response.json()['id']

    def get_projects(self):
        response = requests.get(self.BASE_URL, headers=self.HEADERS)
        response.raise_for_status()
        return response.json()

    def update_project(self, project_id, title="Тестовое питон измененное", users=None):
        if users is None:
            users = {
                "9cd8bd05-0883-4978-b576-5b90900a872e": "worker"
            }
        update_url = f"{self.BASE_URL}/{project_id}"
        payload = {
            "deleted": False,
            "title": title,
            "users": users
        }
        response = requests.put(update_url, json=payload, headers=self.HEADERS)
        response.raise_for_status()
        return self.get_project_by_id(project_id)

    def get_project_by_id(self, project_id):
        response = requests.get(f"{self.BASE_URL}/{project_id}", headers=self.HEADERS)
        response.raise_for_status()
        return response.json()

    def create_project_without_title(self):
        payload = {
            "users": {
                "9cd8bd05-0883-4978-b576-5b90900a872e": "worker"
            }
        }
        response = requests.post(self.BASE_URL, json=payload, headers=self.HEADERS)
        return response.status_code

    def update_project_without_id(self):
        update_url = f"{self.BASE_URL}/invalid_id"
        payload = {
            "deleted": True,
            "title": "Тестовое питон измененное"
        }
        response = requests.put(update_url, json=payload, headers=self.HEADERS)
        return response.status_code


# Примеры использования
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