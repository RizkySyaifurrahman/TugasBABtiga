## Task Manager: Implementasi Design Pattern dalam Proyek Python

### Deskripsi Proyek
Proyek ini adalah sistem manajemen tugas sederhana yang memungkinkan pengguna untuk membuat, melihat, dan menyelesaikan tugas. Kelompok ini bertanggung jawab untuk mengembangkan proyek Python dengan melibatkan implementasi salah satu dari tiga desain pola (design pattern) yang disediakan: Singleton, Observer, atau Factory.

### Langkah-langkah

#### Inisialisasi Proyek
1. Buat direktori utama proyek dengan nama "TaskManager".
2. Buatlah file `__init__.py` dalam direktori utama untuk menjadikan proyek sebagai modul Python.

#### Struktur Direktori
- tasks: Direktori untuk menyimpan modul terkait tugas.
- tests: Direktori untuk menyimpan file pengujian.
- data: Direktori untuk menyimpan file data atau database sederhana.

#### Implementasi Design Pattern
Pilih salah satu dari design pattern: Singleton, Observer, atau Factory. Terapkan design pattern tersebut dalam modul yang relevan, seperti manajemen tugas atau pencatatan kegiatan.

#### Modul Python
Dalam direktori tasks, buatlah modul Python dengan nama `task_manager.py`. Modul ini harus mencakup fungsionalitas dasar untuk menambahkan, melihat, dan menyelesaikan tugas.

#### Struktur Data
Dalam direktori data, buatlah file `tasks.json` yang akan digunakan untuk menyimpan data tugas.

#### Pengujian
Dalam direktori tests, buatlah file pengujian `test_task_manager.py`. Uji modul `task_manager.py` untuk memastikan fungsionalitasnya berjalan dengan baik.

#### Skrip Utama
Buatlah file `main.py` di direktori utama. Skrip ini akan menjadi titik masuk utama aplikasi dan berisi interaksi pengguna dengan manajemen tugas.

### Cara Menjalankan Skrip Utama
Untuk menjalankan skrip utama, jalankan perintah berikut di terminal:

```
python main.py
```

### Cara Menjalankan Pengujian
Untuk menjalankan pengujian, jalankan perintah berikut di terminal:

```
python -m unittest discover tests
```

Implementasi design pattern yang digunakan pada kode di atas adalah Singleton.

### Singleton Design Pattern:
Design pattern Singleton digunakan untuk memastikan bahwa sebuah kelas hanya memiliki satu instance dan memberikan titik akses global ke instance tersebut.

Penjelasan implementasi Singleton pada kode di atas:
- Kelas `TaskManager` memiliki atribut kelas `_instance` yang bertanggung jawab untuk menyimpan instance tunggal dari kelas tersebut.
- Metode kelas khusus `__new__()` digunakan untuk membuat instance objek baru. Pada tahap pembuatan, ia memeriksa apakah instance `_instance` sudah ada. Jika belum, maka instance baru dari kelas `TaskManager` akan dibuat. Jika sudah ada, maka instance yang sudah ada akan dikembalikan.
- Dengan demikian, setiap kali kelas `TaskManager` dibuat, akan selalu mengembalikan instance yang sama jika sudah ada, sehingga memastikan hanya ada satu instance `TaskManager` yang digunakan dalam seluruh aplikasi.

Contoh penggunaan Singleton pada kode di atas:
```python
task_manager = TaskManager()  # Mendapatkan instance tunggal dari TaskManager
task_manager.add_task({'name': 'Mengerjakan tugas', 'completed': False})
tasks = task_manager.view_tasks()
print(tasks)
task_manager.complete_task('Mengerjakan tugas')
task_manager.save_tasks_to_file('data/tasks.json')
```

Dengan menggunakan Singleton, Anda dapat dengan mudah membuat dan menggunakan satu instance dari `TaskManager` di seluruh aplikasi Anda, sehingga memudahkan pengelolaan sumber daya dan konsistensi data.
