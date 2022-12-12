from model.project import Project
import random


def test_delete_project(app):
    old_list = app.soap.get_projects_list()
    if len(old_list)==0:
        project = Project(project_name="test", status="release", view_status="private", description="test")
        app.project.add_project(project)
        old_list = app.soap.get_projects_list()
    project = random.choice(old_list)
    index = project.index
    app.project.delete_project_by_index(index)
    new_list = app.soap.get_projects_list()
    old_list.remove(project)
    assert len(old_list)==len(new_list)
    assert old_list == new_list