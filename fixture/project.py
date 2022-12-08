from model.project import Project


class ProjectHelper():
    def __init__(self, app):
        self.app = app

    def return_to_project_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def add_project(self, project):
        wd = self.app.wd
        self.open_project_page()
        wd.find_element_by_css_selector('[value="Create New Project"]').click()
        self.fill_form(project)
        wd.find_element_by_css_selector('[value="Add Project"]').click()

    def fill_form(self, project):
        wd = self.app.wd
        self.change_field_value("name", project.project_name)
        self.change_drop_down('status', project.status)
        self.change_drop_down('view_state', project.view_status)
        self.change_field_value('description', project.description)


    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)


    def change_drop_down(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_xpath(f'//option[contains(text(),"{text}")]').click()

    def open_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php") and
                len(wd.find_elements_by_css_selector('[value="Create New Project"]')) > 0):
            wd.find_element_by_xpath('//a[contains(text(),"Manage")]').click()
            wd.find_element_by_xpath('//a[contains(text(),"Manage Projects")]').click()

    def get_project_list(self):
        wd = self.app.wd
        project_list = []
        index = 0
        self.open_project_page()
        for row in wd.find_elements_by_xpath("//table[3]/tbody/tr")[2:]:
            cells = row.find_elements_by_tag_name("td")
            project_name = cells[0].text
            status = cells[1].text
            view_status = cells[3].text
            description = cells[4].text
            project_list.append(Project(project_name=project_name, status=status,view_status=view_status,
                                        description=description, index = index))
            index += 1
        return project_list

    def delete_project_by_index(self, index):
        wd = self.app.wd
        self.open_project_page()
        wd.find_elements_by_css_selector('[href^="manage_proj_edit_page"]')[index].click()
        wd.find_element_by_css_selector('[value="Delete Project"]').click()
        wd.find_element_by_css_selector('[value="Delete Project"]').click()

