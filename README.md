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

### **1. Phone number validation**
- Must contain **digits only**
- Must be **exactly 10 digits**
- Cannot be empty
- Changing a phone requires the contact to have at least one phone

### **2. Name validation**
- Name cannot be empty
- Name must contain at least **one visible character**
- Duplicate names are not allowed when adding a new contact

### **3. Command arguments validation**
Each command checks:
- Correct **number of arguments**
- Required parameters are provided
- Unknown commands show an informative error
- Empty input returns: “Please enter a command.”

Examples:
- `add` → requires exactly **2** arguments  
- `change` → requires exactly **2** arguments  
- `phone` → requires exactly **1** argument  

### **4. Contact existence checks**
Validations executed before running commands:
- `change` — contact must exist  
- `phone` — contact must exist  

Errors return messages such as:
> `"Error: Contact 'John' not found."`

### **5. Storage validation**
- If `addressbook.pkl` does not exist → a new empty AddressBook is created  
- File read errors do **not** crash the program  
- Data is always saved before exit

### **6. Input safety & robustness**
- Pressing `Ctrl+C` triggers a safe save → no data loss  
- Empty or whitespace-only input is ignored  
- Invalid formats never crash the program

### **7. Error message formatting**
All errors follow a consistent pattern:

```
Error: <description>
```

For better user experience and clarity.

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
