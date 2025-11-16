# goit-pycore-hw-08 — Address Book with Serialization

A console-based address book application built in Python with data persistence using **pickle**.  
This version extends the HW07 functionality by adding automatic saving and loading of all contacts.

---

## Features

- Add new contacts  
- Update phone numbers  
- View phone numbers by contact  
- Validate phone numbers (digits only, exactly 10 digits)  
- Load all contacts at program start  
- Save all contacts automatically on exit  
- Show all saved contacts  
- Graceful exit via `close`, `exit`, or `quit`  
- Full error handling (no program crashes)

---

## Commands

| Command | Description |
|--------|-------------|
| `add [name] [phone]` | Add a new contact |
| `change [name] [new phone]` | Update the phone number of a contact |
| `phone [name]` | Show phone numbers of the contact |
| `show_all` | Display all contacts |
| `exit` / `close` / `quit` | Save and exit the program |

---

## Data Validation

### Phone number rules:
- Must contain digits only
- Must be exactly 10 digits

All invalid inputs return friendly error messages.

---

## Serialization

The assistant automatically:

### Loads data  
When the program starts, it restores the address book from:

```
addressbook.pkl
```

### Saves data  
When the program exits, all contacts are serialized back into the same file using **pickle**.

No data is ever lost between sessions.

---

## Run

```bash
python main.py
```

Then enter commands into the console.

---

## Project Structure

```
main.py
fields.py
record.py
address_book.py
storage.py
tests_unittest.py
README.md
addressbook.pkl   -- created automatically
```

---

## Example

```
Enter command: add John 0931234567
Contact 'John' added successfully.

Enter command: phone John
John: 0931234567

Enter command: change John 0509876543
Phone for 'John' updated successfully.

Enter command: show_all
John: 0509876543

Enter command: exit
Saving data...
Goodbye!
```

---

## Requirements

- All required commands implemented  
- Data persists via pickle serialization  
- Full validation and error handling  
- Uses `AddressBook`, `Record`, `Phone`, `Name` classes  
- Safe startup and exit behavior  
