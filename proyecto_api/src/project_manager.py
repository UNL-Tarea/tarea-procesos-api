# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 10:26:18 2024

@author: Toshiba
"""

class ProjectManager:
    def __init__(self):
        self.projects = {}

    def add_project(self, name):
        if name not in self.projects:
            self.projects[name] = {"tasks": [], "members": []}

    def list_projects(self):
        return list(self.projects.keys())
    
    

    def add_task(self, project_name, task):
        if project_name in self.projects:
            self.projects[project_name]["tasks"].append({"task": task, "completed": False, "assigned_to": None})

    def list_tasks(self, project_name):
        if project_name in self.projects:
            return self.projects[project_name]["tasks"]

    def complete_task(self, project_name, task):
        if project_name in self.projects:
            for t in self.projects[project_name]["tasks"]:
                if t["task"] == task:
                    t["completed"] = True

    def remove_task(self, project_name, task):
        if project_name in self.projects:
            self.projects[project_name]["tasks"] = [t for t in self.projects[project_name]["tasks"] if t["task"] != task]
            
            

    def assign_task(self, project_name, task, member):
        if project_name in self.projects:
            for t in self.projects[project_name]["tasks"]:
                if t["task"] == task:
                    t["assigned_to"] = member
                    if member not in self.projects[project_name]["members"]:
                        self.projects[project_name]["members"].append(member)
                        
    def get_project_progress(self, project_name):
        if project_name in self.projects:
            tasks = self.projects[project_name]["tasks"]
            total_tasks = len(tasks)
            completed_tasks = sum(1 for t in tasks if t["completed"])
            return (completed_tasks / total_tasks)   if total_tasks > 0 else 0


