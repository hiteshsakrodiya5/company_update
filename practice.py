class Company:

    data_base = []
    def __init__(self, *args):
        self.employe = args[0]
        self.team_lead = args[1]
        self.product_manager = args[2]
        self.human_resource = args[3]
        self.office_boy = args[4]
        self.projects = args[5]
        self.other = args[6]

    def employe_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"

    def team_lead_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"

    def product_manager_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            Company.data_base.append(ques)
            ques = input("enter your comment here !!")
        return Company.data_base

    def human_resource(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"

    def projects_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"

    def office_boy_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"

    def other_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"


class ProductManager(Company):
    def __init__(self, employe, team_lead, product_manager, human_resource, office_boy, projects, other, *args):
        super().__init__(employe, team_lead, product_manager, human_resource, office_boy, projects, other)
        self.time_line = args[0]
        self.front_end = args[1]
        self.back_end = args[2]
        self.testing = args[3]
        self.status = args[4]

    def status_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"

    def time_Line_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"

    def front_end_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"

    def back_end_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"

    def testing_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"


class TeamLead(ProductManager):
    def __init__(self, employe, team_lead, product_manager, human_resource, office_boy, projects, other, time_line, front_end, back_end, testing, status, *args):
        super().__init__(employe, team_lead, product_manager, human_resource, office_boy, projects, other, time_line, front_end, back_end, testing, status)
        self.developer = args[0]
        self.tester = args[1]
        self.deploy = args[2]

    def developer_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"

    def tester_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"

    def deploy_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"


class Developer(TeamLead):
    def __init__(self, employe, team_lead, product_manager, human_resource, office_boy, projects, other, time_line, front_end, back_end, testing, status, *args):
        super().__init__(employe, team_lead, product_manager, human_resource, office_boy, projects, other, time_line, front_end, back_end, testing, status)
        self.code_status = args[0]

    def code_status_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"


class Tester(TeamLead):
    def __init__(self, employe, team_lead, product_manager, human_resource, office_boy, projects, other, time_line,front_end, back_end, testing, status, *args):
        super().__init__(employe, team_lead, product_manager, human_resource, office_boy, projects, other, time_line,front_end, back_end, testing, status)
        self.testing_status = args[0]

    def testing_status_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"


class OfficeBoy(Company):
    def __init__(self, employe, team_lead, product_manager, human_resource, office_boy, projects, other, *args):
        super().__init__(employe, team_lead, product_manager, human_resource, office_boy, projects, other)
        self.status = args[0]

    def status_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"


class Project(Company):
    data_base = []
    def __init__(self, employe, team_lead, product_manager, human_resource, office_boy, projects, other, *args):
        super().__init__(employe, team_lead, product_manager, human_resource, office_boy, projects, other)
        self.about_project = args[0]

    def about_project_management(self):
        ques = input("enter your query...")
        while ques != "ques":
            Project.data_base.append(ques)
            ques = input("enter your comment here !!")
        return Project.data_base


class Other(Company):
    def __init__(self, employe, team_lead, product_manager, human_resource, office_boy, projects, other, *args):
        super().__init__(employe, team_lead, product_manager, human_resource, office_boy, projects, other)
        self.about_project = args[0]

    def about_other(self):
        ques = input("enter your query...")
        while ques != "ques":
            ques = input("enter your comment here !!")
        return "thank you keep it up !"

ceo = Company(1,2,3,4,5,6,7)
# print(ceo.product_manager_management())

project = Project(1,2,3,4,5,6,7,8)
print(project.about_project_management())
