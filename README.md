# Minpro-2-DDP-ManajemenDataLukisan

Nama: Sarah Afifah Ramadhani

Kelas: A

NIM: 2609116024

# Deskripsi Singkat Program

 Program yang saya buat adalah program untuk melihat data lukisan dari penulis terkenal untuk pengunjung. Sedangkan untuk admin, admin dapat melihat, mengubah, menambah dan menghapus data (CRUD). Berikut adalah flowchart dari program saya:

 <img width="797" height="1385" alt="art_done drawio" src="https://github.com/user-attachments/assets/aac2fd8d-1ca1-4890-90df-39470c30e681" />

 # Penjelasan Alur Flowchart

 Program akan menampilkan menu untuk user dapat login, lalu akan diarahkan untuk mengisi username dan password (menggunakan library ``pwinput``). 
 
 1. Jika ``usn`` dan ``pass`` merupakan user dengan role ``etmint``:

Program akan memanggilkan function dari ``page_staff()``, lalu user dapat memilih opsi CRUD. Jika user memilih ``1. view art``, maka program akan menampilkan tabel (menggunakan library dari ``Prettytable``) berisi data lukisan yang mendunia (memanggil function ``liat_art`` di program). Jika user memilih ``2. Add Art``, maka program akan menampilkan tabel data lalu user dapat menginput judul lukisan, pelukis dan tahun dari lukisan yang ingin ditambahkan (memanggil function ``nambah_art``). Jika user memilih ``3. Update Art``, maka program akan menampilkan tabel dan meminta user untuk memilih nomor dari baris tabel yang ingin diubah datanya (memanggil function ``up_art``). Lalu, user dapat menginput judul lukisan, pelukis dan tahun untuk menjadi data pengganti. Jika user memilih opsi ``2. Add art`` atau ``3. Update Art`` namun tidak mengisi salah satu dari data yang harus diinput, maka program akan meminta user untuk mengisi seluruh data dan kembali ke menu (memanggil function ``stop()`` agar user bisa kembali dengan cara klik "enter"). Jika user memilih opsi ``4. Delete Art``, maka program akan meminta user untuk menginput nomor dari baris tabel data mana yang ingin dihapus (memanggil function ``hps_art``). Terakhir, jika user memilih opsi ``5. exit`` maka program akan membersihkan terminal dengan memanggil function ``clean_screen()`` yang dibuat dengan library os. Selain dari opsi yang dibuat, jika user menginput opsi lain maka program akan menampilkan print kata "system error".

2. Jika ``usn`` dan ``pass`` merupakan user dengan role ``visitor``:

 Program hanya menampilkan 2 opsi yang bisa diakses oleh ``visitor``, yaitu ``1. view art`` dan ``2. Exit``. Jika user memilih opsi pertama maka program akan menampilkan tebal data lukisan. Jika user memilih opsi kedua maka program akan kembali ke menu login.

# Output sebagai admin

<img width="333" height="229" alt="Screenshot 2026-10-06 125222" src="https://github.com/user-attachments/assets/5ee696c8-ad25-4224-bb84-e619f7be4c7c" />

1. Output jika user menginput ``usn`` dan ``pass`` dengan role ``etmint`` dan program akan menampilkan 5 opsi.

<img width="395" height="173" alt="Screenshot 2026-10-06 125409" src="https://github.com/user-attachments/assets/9bc924d1-87a0-40bc-91af-18bc35ff59cb" />

2. Output jika user memilih opsi pertama

<img width="379" height="311" alt="Screenshot 2026-10-06 153633" src="https://github.com/user-attachments/assets/0c829f73-4ab1-488c-9a41-9829fdfcc16c" />

3. Output jika user memilih opsi kedua, setelahnya user dapat mengisi/input data-data yang diubah untuk menambah data baru  karya ke dalam tabel. Setelah mengisi data yang dibutuhkan, program akan menampilkan tabel baru secara otomatis (menggunakan function ``liat_art``).

<img width="382" height="428" alt="Screenshot 2026-10-06 155647" src="https://github.com/user-attachments/assets/8904e717-fcfb-44ae-9f0c-840679225e4b" />

 4. Output jika user memilih opsi ketiga, setelahnya program akan menampilkan tabel terlebih dahulu lalu meminta user untuk mengisi data-data yang dibutuhkan untuk bisa mengubah data pada tabel. Setelahnya, program akan secara otomatis menampilkan tabel yang sudah diupdate.

<img width="380" height="397" alt="Screenshot 2026-10-06 160459" src="https://github.com/user-attachments/assets/a2bc9d6b-a3b2-4d72-b555-23291a6c5ced" />

5. Output jika user memilih opsi keempat, maka setelahnya user akan diminta mengisi nomor mana yang ingin dihapus dari tabel. Lalu,  program akan menampilkan nama dari karya yang dihapus. Setelah itu program akan menampilkan tabel baru.

<img width="344" height="92" alt="Screenshot 2026-10-06 165619" src="https://github.com/user-attachments/assets/f8065e63-baf4-413a-823d-cb90f6877fba" />

6. Output jika user memilih opsi kelima, maka program akan kembali ke menu login dan terminal akan dibersihkan dari program sebelumnya menggunakan library os (dipanggil dengan function ``clear_screen()``).

<img width="339" height="193" alt="Screenshot 2026-10-06 170212" src="https://github.com/user-attachments/assets/834c2392-4e90-4674-9dee-16dc369e989d" />

7. Output jika user memilih angka yang tidak ada di menu. Terminal akan dibersihkan dengan ``clear_screen()``.

# Output sebagai Visitor

<img width="373" height="398" alt="image" src="https://github.com/user-attachments/assets/ee561c4d-baff-47a4-9f69-e87c6f35fe59" />

1. Output jika user memilih opsi pertama, maka program akan menampilkan tabel data lukisan. Visitor tidak bisa mengakses CRUD. Karena saya tidak menggunakan fungsi ``clear_screen`` pada kode ``page_pengunjung``, maka setelah memilih opsi, output menu masih terlihat, tidak terhapus.

<img width="332" height="166" alt="Screenshot 2026-10-06 171608" src="https://github.com/user-attachments/assets/44e18f7e-98de-43ee-8815-1629bb3e7885" />

2. Output jika user memilih opsi kedua.

<img width="340" height="130" alt="Screenshot 2026-10-06 171810" src="https://github.com/user-attachments/assets/7f8bc30b-24e3-4d14-9777-3650323f6d73" />

3. Output jika user memilih opsi yang tidak ada di menu.

note: saya masih belum mengerti bagian error handling, terima kasih.
