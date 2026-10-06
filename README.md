# Minpro-2-DDP-ManajemenDataLukisan

Nama: Sarah Afifah Ramadhani

Kelas: A

NIM: 2609116024

# Deskripsi Singkat Program

 Program yang saya buat adalah program untuk melihat data lukisan dari penulis terkenal untuk pengunjung. Sedangkan untuk admin, admin dapat melihat, mengubah, menambah dan menghapus data (CRUD). Berikut adalah flowchart dari program saya:

 <img width="797" height="1386" alt="Untitled Diagram drawio" src="https://github.com/user-attachments/assets/f79935b7-4293-49c4-9c7a-007e41f30786" />

 # Penjelasan Alur Flowchart

 Program akan menampilkan menu untuk user dapat login, lalu akan diarahkan untuk mengisi username dan password. 
 
 1. Jika ``usn`` dan ``pass`` merupakan user dengan role ``staff``:

Program akan memanggilkan function dari ``page_staff()``, lalu user dapat memilih opsi CRUD. Jika user memilih ``1. view art``, maka program akan menampilkan tabel (menggunakan library dari ``Prettytable``) berisi data lukisan
