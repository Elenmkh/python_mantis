class Project:
    def __init__(self, project_name=None, status=None, inherit=None, view_status=None, description=None, index=None):
        self.project_name = project_name
        self.status = status
        self.inherit = inherit
        self.view_status = view_status
        self.description = description
        self.index = index

    def __repr__(self):
        return "%s: %s, %s, %s, %s" % (self. index, self.project_name, self.status, self.view_status, self.description)

    def __eq__(self, other):
        return (self.project_name is None or other.project_name is None or self.project_name == other.project_name) \
               and (self.status is None or other.status is None or self.status == other.status) \
               and (self.view_status is None or other.view_status is None or self.view_status == other.view_status) \
               and (self.description is None or other.description is None or self.description == other.description)\
               and (self.index is None or other.index is None or self.index == other.index)