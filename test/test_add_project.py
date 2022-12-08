from model.project import Project


def test_add_project(app):
    app.session.login("administrator", "root")
    old_list = app.project.get_project_list()
    project = Project(project_name="test", status="release", view_status="private", description="test")
    app.project.add_project(project)
    new_list = app.project.get_project_list()
    old_list.append(project)
    app.session.logout()
    assert len(old_list)==len(new_list)
    assert old_list == new_list