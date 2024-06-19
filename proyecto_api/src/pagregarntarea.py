import unittest


class TaskManager:
    def __init__(self):
        unittest.main()
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)
    
    def list_tasks(self):
        return self.tasks
    
    def complete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.tasks.append(f"{task} (Completed)")
    
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)


import unittest

class TestTaskManager(unittest.TestCase):
    
    def setUp(self):
        self.task_manager = TaskManager()

    def test_add_task(self):
        self.task_manager.add_task("Complete homework")
        self.assertIn("Complete homework", self.task_manager.list_tasks())
    
    def test_list_tasks(self):
        self.task_manager.add_task("Complete homework")
        self.task_manager.add_task("Read a book")
        tasks = self.task_manager.list_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn("Complete homework", tasks)
        self.assertIn("Read a book", tasks)
    
    def test_complete_task(self):
        self.task_manager.add_task("Complete homework")
        self.task_manager.complete_task("Complete homework")
        tasks = self.task_manager.list_tasks()
        self.assertIn("Complete homework (Completed)", tasks)
    
    def test_remove_task(self):
        self.task_manager.add_task("Complete homework")
        self.task_manager.remove_task("Complete homework")
        tasks = self.task_manager.list_tasks()
        self.assertNotIn("Complete homework", tasks)

#if __name__ == '__main__':
#    unittest.main()
#    manager = TaskManager()
#    manager.add_task('prueba1')
#    manager.add_task('tarea1')
#    print (manager.list_tasks())