import json
class TaskManager:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # Inisialisasi atribut untuk menyimpan data tugas
            cls._instance.tasks = []
        return cls._instance

    def add_task(self, task):
       # Menambahkan tugas baru.
        self.tasks.append(task)

    def view_tasks(self):
       # Melihat daftar semua tugas.
        return self.tasks

    def complete_task(self, task_name):
        # Menandai tugas sebagai selesai.
        for task in self.tasks:
            if task['name'] == task_name:
                task['completed'] = True

    def load_tasks_from_file(self, file_path):
        # Memuat daftar tugas dari file JSON.
        with open(file_path, 'r') as file:
            self.tasks = json.load(file)

    def save_tasks_to_file(self, file_path):
        # Menyimpan daftar tugas ke file JSON.
        with open(file_path, 'w') as file:
            json.dump(self.tasks, file)

# Contoh penggunaan:
# task_manager = TaskManager()  # Mendapatkan instance tunggal dari TaskManager
# task_manager.add_task({'name': 'Mengerjakan tugas', 'completed': False})
# tasks = task_manager.view_tasks()
# print(tasks)
# task_manager.complete_task('Mengerjakan tugas')
# task_manager.save_tasks_to_file('data/tasks.json')

