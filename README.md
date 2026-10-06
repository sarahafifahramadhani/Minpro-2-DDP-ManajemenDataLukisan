# Minpro-2-DDP-ManajemenDataLukisan

Nama: Sarah Afifah Ramadhani

Kelas: A

NIM: 2609116024

# Deskripsi Singkat Program

 Program yang saya buat adalah program untuk melihat data lukisan dari penulis terkenal untuk pengunjung. Sedangkan untuk admin, admin dapat melihat, mengubah, menambah dan menghapus data (CRUD). Berikut adalah flowchart dari program saya:

 <img width="797" height="1386" alt="Untitled Diagram drawio" src="https://github.com/user-attachments/assets/f79935b7-4293-49c4-9c7a-007e41f30786" />

 # Penjelasan Alur Flowchart

 Program akan menampilkan menu untuk user dapat login, lalu akan diarahkan untuk mengisi username dan password (menggunakan library ``pwinput``). 
 
 1. Jika ``usn`` dan ``pass`` merupakan user dengan role ``etmint``:

Program akan memanggilkan function dari ``page_staff()``, lalu user dapat memilih opsi CRUD. Jika user memilih ``1. view art``, maka program akan menampilkan tabel (menggunakan library dari ``Prettytable``) berisi data lukisan yang mendunia (memanggil function ``liat_art`` di program). Jika user memilih ``2. Add Art``, maka program akan menampilkan tabel data lalu user dapat menginput judul lukisan, pelukis dan tahun dari lukisan yang ingin ditambahkan (memanggil function ``nambah_art``). Jika user memilih ``3. Update Art``, maka program akan menampilkan tabel dan meminta user untuk memilih nomor dari baris tabel yang ingin diubah datanya (memanggil function ``up_art``). Lalu, user dapat menginput judul lukisan, pelukis dan tahun untuk menjadi data pengganti. Jika user memilih opsi ``2. Add art`` atau ``3. Update Art`` namun tidak mengisi salah satu dari data yang harus diinput, maka program akan meminta user untuk mengisi seluruh data dan kembali ke menu (memanggil function ``stop()`` agar user bisa kembali dengan cara klik "enter"). Jika user memilih opsi ``4. Delete Art``, maka program akan meminta user untuk menginput nomor dari baris tabel data mana yang ingin dihapus (memanggil function ``hps_art``). Terakhir, jika user memilih opsi ``5. exit`` maka program akan membersihkan terminal dengan memanggil function ``clean_screen()`` yang dibuat dengan library os. Selain dari opsi yang dibuat, jika user menginput opsi lain maka program akan menampilkan print kata "system error".

2. Jika ``usn`` dan ``pass`` merupakan user dengan role ``visitor``:

 Program hanya menampilkan 2 opsi yang bisa diakses oleh ``visitor``, yaitu ``1. view art`` dan ``2. Exit``. Jika user memilih opsi pertama maka program akan menampilkan tebal data lukisan. Jika user memilih opsi kedua maka program akan kembali ke menu login.

# Output

