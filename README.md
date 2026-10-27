# PR. 6 – File Operator
## Personal Journal Manager

### Project Overview
Personal Journal Manager is a beginner-friendly Python application that helps users maintain personal journal entries using file handling. It provides a menu-driven interface to add, view, search, and delete journal entries. Each entry is saved with an automatic timestamp for easy tracking.

### Features
- **Add a New Entry:** Save journal entries with the current date and time.
- **View All Entries:** Display all previously saved journal entries.
- **Search Entries:** Search for entries using keywords or dates.
- **Delete All Entries:** Delete all saved entries after confirmation.
- **Automatic File Creation:** Creates `journal.txt` when the first entry is added.
- **Exception Handling:** Handles missing files, permission errors, and invalid input.
- **Menu-Driven Interface:** Provides simple options for easy navigation.

### Technologies Used
- **Programming Language:** Python 3
- **Concepts:** File Handling, Object-Oriented Programming (OOP), Exception Handling
- **Modules:** `os` and `datetime`
- **Storage:** Text file (`journal.txt`)

### Project Structure
```text
PR-6-File-Operator/
│
├── file_operator.py
├── journal.txt
└── README.md
```

**Note:** The `journal.txt` file is generated automatically when the first journal entry is added.

### Requirements
- Python 3.x
- Visual Studio Code or any Python IDE

No external libraries are required.

### How to Run
1. Install Python 3 on your computer.
2. Open the project folder in VS Code.
3. Create or open `file_operator.py` and paste the Python code.
4. Open the terminal.
5. Execute the following command:

```bash
python file_operator.py
```

### Application Menu
When the program starts, the following options are displayed:

1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit

Select an option by entering its corresponding number.

### File Handling Operations
The project uses different file operations to manage journal entries:

- **Read (`r`):** Reads and displays saved entries.
- **Append (`a`):** Adds new entries without overwriting existing content.
- **Exclusive Creation (`x`):** Creates a new file only if it does not already exist.
- **Delete (`os.remove()`):** Deletes the journal file after user confirmation.

### Learning Outcomes
Through this project, users learn how to:
- Create and use classes and objects in Python.
- Read and write data using text files.
- Apply different file opening modes.
- Handle exceptions using `try` and `except`.
- Build a menu-driven application.
- Organize and document a Python project.

### Future Enhancements
- Support multiline journal entries.
- Edit or delete individual entries.
- Add password protection.
- Export journal entries to PDF.
- Develop a graphical user interface (GUI).



### Conclusion
Personal Journal Manager demonstrates the practical use of Python file handling and object-oriented programming. It provides a simple way to maintain journal entries while helping beginners understand basic programming concepts.