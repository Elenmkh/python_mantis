from model.project import Project
import random


def test_add_project(app):
    app.session.login("administrator", "root")
    old_list = app.project.get_project_list()
    if len(old_list)==0:
        project = Project(project_name="test", status="release", view_status="private", description="test")
        app.project.add_project(project)
        old_list = app.project.get_project_list()
    project = random.choice(old_list)
    index = project.index
    app.project.delete_project_by_index(index)
    new_list = app.project.get_project_list()
    old_list.remove(project)
    app.session.logout()
    assert len(old_list)==len(new_list)
    assert old_list == new_list