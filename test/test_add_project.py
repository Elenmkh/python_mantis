from model.project import Project


def test_add_project(app):
    old_list = app.soap.get_projects_list()
    project = Project(project_name="test", status="release", view_status="private", description="test")
    app.project.add_project(project)
    new_list = app.soap.get_projects_list()
    old_list.append(project)
    assert len(old_list)==len(new_list)
    assert old_list == new_list