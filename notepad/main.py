import os


def build_note(note_text : str, note_name : str) -> None:
    try:
        with open(f"{note_name}.txt", 'w') as f:
            f.write(note_text)
    except Exception as e:
        print(e)


def create_note():
    note_text = input('Input note text: ')
    note_name = input('Input note name: ')
    build_note(note_text, note_name)

def open_txt(filename):
    

def read_note(note_name = None):
    if not note_name:
        note_name = input('Input note name: ')
    if isfile:=os.path.isfile(f"{note_name}.txt"):
        with open(f"{note_name}.txt", 'r') as f:
            text = f.read()
    else:
        text = "Note not found"
    print(text)
    return note_name if isfile else None


def edit_note():
    note_name = read_note()
    if note_name:
        note_text = input('Input note text: ')
        build_note(note_text, note_name)


def delete_note():
    note_name = input('Input note name: ')
    filename = f"{note_name}.txt"
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        print("Note not found")

def display_notes(key = None):
    list_txt = [txt for txt in os.listdir('.') if '.txt' in txt]
    di = {l[:-4]: read_note(l[:-4]) for l in list_txt}
    
    for key, value in di.items():
        print(key, value)

def display_sorted_notes():
    display_notes()
    
    


def print_menu():
    menu = [
        '1. Create note',
        '2. Read note',
        '3. Edit note',
        '4. Delete note',
        '5. Display notes',
        '6. Sort notes',
        '7. Exit',
    ]
    print('='*20)
    for m in menu:
        print(m)


def main():
    
    while True:
        print_menu()
        ch = input('---> Enter menu: ')

        match ch:
            case '1':
                create_note()
            case '2':
                read_note()
            case '3':
                edit_note()
            case '4':
                delete_note()
            case '5':
                display_notes()
            case '6':
                display_sorted_notes()
            case _:
                break
            

if __name__ == "__main__":
    main()