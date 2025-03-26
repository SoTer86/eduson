import os


def build_note(note_text : str, note_name : str) -> None:
    try:
        with open(f"{note_name}.txt", 'w') as f:
            f.write(note_text)
        print(f"Заметка {note_name} создана.")
    except Exception as e:
        print(e)


def create_note():
    note_text = input('Input note text: ')
    note_name = input('Input note name: ')
    build_note(note_text, note_name)


def read_note(name = None, isprint=True):
    note_name = input('Input note name: ') if not name else name
    
    if os.path.isfile(f"{note_name}.txt"):
        with open(f"{note_name}.txt", 'r') as f:
            text = f.read()
    else:
        text = "Note not found"
        
    if isprint:
        print(f"[{note_name}] {text}")
    return text


def edit_note():
    note_name = input('Input note name: ')
    read_note(note_name)
    if os.path.isfile(f"{note_name}.txt"):
        note_text = input('Input note text: ')
        build_note(note_text, note_name)


def delete_note():
    note_name = input('Input note name: ')
    filename = f"{note_name}.txt"
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        print("Note not found")


def display_notes(reverse = False):
    notes = [note for note in os.listdir() if note.endswith('.txt')]
    values = [read_note(note[:-4], isprint=False) for note in notes]
    di = dict(zip(notes, values))
    
    res = sorted(di.items(), key=lambda x: len(x[1]), reverse=reverse)
    
    for k, v in res:
        print(f"[{k}]: {v}")
        
    
def display_sorted_notes():
    display_notes(reverse=True)
    
    
def print_menu():
    menu = [
        'M E N U : ',
        '1. Create note',
        '2. Read note',
        '3. Edit note',
        '4. Delete note',
        '5. Display notes',
        '6. Sort notes',
        '7. Exit',
    ]
    
    os.system('clear')
    
    for m in menu:
        print(m, end=" ")
    print('')

def main():
    
    while True:
        print_menu()
        ch = input('Enter menu: ')

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
        
        input('Press any key...')
            

if __name__ == "__main__":
    main()