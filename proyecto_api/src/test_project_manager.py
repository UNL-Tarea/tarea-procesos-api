# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 10:27:57 2024

@author: Toshiba
"""

import unittest
from project_manager import ProjectManager

conpletas = 0;

class TestProjectManager(unittest.TestCase):
    
    def setUp(self):
        self.project_manager = ProjectManager()

    def test_add_project(self):
        self.project_manager.add_project("Project A")
        projects = self.project_manager.list_projects()
        self.assertIn("Project A", projects)

    def test_add_and_list_tasks(self):
        self.project_manager.add_project("Project A")
        self.project_manager.add_task("Project A", "Task 1")
        tasks = self.project_manager.list_tasks("Project A")
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["task"], "Task 1")

    def test_complete_task(self):
        self.conpletas = self.conpletas + 1
        self.project_manager.add_project("Project A")
        self.project_manager.add_task("Project A", "Task 1")
        self.project_manager.complete_task("Project A", "Task 1")
        tasks = self.project_manager.list_tasks("Project A")
        self.assertTrue(tasks[0]["completed"])

    def test_remove_task(self):
        self.project_manager.add_project("Project A")
        self.project_manager.add_task("Project A", "Task 1")
        self.project_manager.remove_task("Project A", "Task 1")
        tasks = self.project_manager.list_tasks("Project A")
        self.assertEqual(len(tasks), 0)

    def test_assign_task(self):
        self.project_manager.add_project("Project A")
        self.project_manager.add_task("Project A", "Task 1")
        self.project_manager.assign_task("Project A", "Task 1", "Member 1")
        tasks = self.project_manager.list_tasks("Project A")
        self.assertEqual(tasks[0]["assigned_to"], "Member 1")
        
    def test_get_project_progress(self):
        self.project_manager.add_project("Project A")
        self.project_manager.add_task("Project A", "Task 1")
        self.project_manager.add_task("Project A", "Task 2")
        self.project_manager.complete_task("Project A", "Task 1")
        progress = self.project_manager.get_project_progress("Project A")
        self.assertEqual(progress, 50.0)


if __name__ == '__main__':
    unittest.main()