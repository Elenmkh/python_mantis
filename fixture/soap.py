from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.base_url+"/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_projects_list(self):
        client = Client(self.app.base_url+'/api/soap/mantisconnect.php?wsdl')
        try:
            project = client.service.mc_projects_get_user_accessible(self.app.username, self.app.password)
            project_list = []
            for item in project:
                project_list.append(Project(project_name=item['name'], status=item['status']['name'],
                                            view_status=item['view_state']['name'], description=item['description'],
                                            index=item['id']))
            return project_list
        except WebFault:
            return False
