import pwinput
import os
from prettytable import PrettyTable

#Dictionary
user = {
    "staff" : {
        "role": "etmint",
        "pass": "realart"
    },
    "visitor" :{
        "role": "pengunjung",
        "pass": "visit"
    }
}

artwork = {
    "art1": {
        "title" : "Camile Monet on her Deathbed",
        "artist" : "Oscar Claude Monet",
        "year" : "1879"
    },
    "art2" : {
        "title" : "The Persistence of Memory",
        "artist" : "Salvador Dali",
        "year" : "1931"
    },
    "art3" : {
            "title" : "Penangkapan Diponegoro",
            "artist" : "Raden Saleh",
            "year" : "1857"
    },
    "art4" : {
            "title" : "Roots",
            "artist" : "Frida Kahlo",
            "year" : "1943"
    },
    "art5" : {
            "title" : "Ayam Tarung",
            "artist" : "Affanfi Koesoema",
            "year" : "1979"
    }
}
# function
def clear_screen() :
    os.system("cls" if os.name == "nt" else "clear")

def stop():
    input("\n Click Enter to Continue")

def login():
    while True:
        clear_screen()
        print("=" * 57)
        print("\n               WELCOME TO ART GALLERY             ")
        print("=" * 57)
        usn = input("Username :")
        pwd = pwinput.pwinput("Password: ")
# masukin username dan password
        if usn in user:
            if user[usn]["pass"] == pwd:
                print("\n Welcome to Art Gallery.")
                return usn, user[usn]["role"]
            else:
                print("Wrong Password! you can Try again :)")
                stop()
        else:
            print("Wrong Username! You can try again :)")
            stop()
#crud, view:
def liat_art():
    print("=" * 57)
    print("\n               WELCOME TO ART GALLERY             ")
    print("=" * 57)

    if len(artwork) == 0:
        print("There is no Art data found. Please add an artwork first")
    else:
        tabel = PrettyTable()
        tabel.field_names = ["No", "Title", "Artist", "Year"]

        no = 1
        for key, value in artwork.items():
            tabel.add_row ([no, value["title"], value["artist"], value["year"]])
            no += 1

        print(tabel)
#add
def nambah_art():
    print("\n               LET'S ADD SOME ART             ")

    new_art = "art" + str(len(artwork) + 1)

    title1 = input("Add Title: ")
    artist1 = input("Artist Name: ")
    year1 = input("Year Created: ")

    if title1 == "" or artist1 == "" or year1 == "":
        print("\n There is no Art data found. Please add an artwork first. ")
    else:
        artwork[new_art] = {
            "title": title1,
            "artist": artist1,
            "year": year1
        }
        print("\n Art added :)")
        liat_art()
        stop()
#update
def up_art():
    liat_art()
    if len(artwork) > 0:
        nomor = input("\nSelect number of art you want to change: ")
        baru = "art" + nomor
        if baru in artwork:
            title1 = input("Add Title: ")
            artist1 = input("Artist Name: ")
            year1 = input("Year Created: ")
        
            if title1 == "" or artist1 == "" or year1 == "":
                print("\n There is no Art data found. Please add an artwork first")
            else:
                artwork[baru].update({
                    "title": title1,
                    "artist": artist1,
                    "year": year1
                })
                print("\nArt updated succesfully!")
                liat_art()
                stop()
        else:
            print("Data not found")
#hapus
def hps_art():
    liat_art()
    if len(artwork) > 0:
        nomor = input("\nSelect number of art you want to delete: ")
        baru = "art" + nomor
        if baru in artwork:
            hps = artwork.pop(baru)
            print("art deleted: ", hps["title"])
            liat_art()
            stop()
        else:
            print("Data not found")
#jika rolenya adalah pengunjung
def page_pengunjung():
    while True:
        print("=" * 57)
        print("\n               WELCOME TO ART GALLERY             ")
        print("=" * 57)
        print("\n                       Menu                     ")
        print("1. View art")
        print("2. Exit")

        pil_menu = input("Select: ")

        if pil_menu == "1":
            liat_art()
        elif pil_menu == "2":
            print("Thankyou! see you again ater :)")
            stop()
            break
        else:
            print("System error. Try again later")
#jika rolelnya adalah etmint
def page_staff():
    while True:
        print("=" * 57)
        print("\n               WELCOME TO ART GALLERY             ")
        print("=" * 57)
        print("\n                       -Menu-                    ")
        print("1. View Art")
        print("2. Add Art")
        print("3. Change Art Data")
        print("4. Delete Art Data")
        print("5. Exit")
        print("=" * 57)

        pil_menu = input("Select: ")
        clear_screen()

        if pil_menu == "1":
            liat_art()
        elif pil_menu == "2":
            nambah_art()
        elif pil_menu == "3":
            up_art()
        elif pil_menu == "4":
            hps_art()
        elif pil_menu == "5":
            print("Thankyou! see you again ater :)")
            break
        else:
            print("System error. Try again later")

def main():
    while True:
        usn, role = login()
        if role == "etmint":
            page_staff()
        elif role == "pengunjung":
            page_pengunjung()
        else:
            print("Something went wrong. Try again.")

main()