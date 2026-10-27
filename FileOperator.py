import os
from datetime import datetime


class JournalManager:
    def __init__(self):
        self.filename = "journal.txt"
        self.separator = "-" * 35

    # 1. Add a new journal entry
    def add_entry(self):
        try:
            # Create the file if it does not exist
            try:
                with open(self.filename, "x", encoding="utf-8"):
                    pass
            except FileExistsError:
                pass

            print("\nEnter your journal entry:")
            entry = input().strip()

            if not entry:
                print("Entry cannot be empty. Please try again.")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Append the timestamp and entry
            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n")
                file.write(self.separator + "\n")

            print("Entry added successfully!")

        except PermissionError:
            print("Error: Permission denied while writing to the file.")
        except OSError as error:
            print("File error:", error)

    # 2. View all journal entries
    def view_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()

            if content.strip():
                print("\nYour Journal Entries:")
                print(self.separator)
                print(content, end="" if content.endswith("\n") else "\n")
            else:
                print("No journal entries found. Start by adding a new entry!")

        except FileNotFoundError:
            print(
                "Error: The journal file does not exist. "
                "Please add a new entry first."
            )
        except PermissionError:
            print("Error: Permission denied while reading the file.")
        except OSError as error:
            print("File error:", error)

    # 3. Search entries by keyword or date
    def search_entry(self):
        keyword = input("\nEnter a keyword or date to search: ").strip()

        if not keyword:
            print("Search keyword cannot be empty.")
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()

            if not content.strip():
                print("No journal entries found.")
                return

            entries = content.split(self.separator)
            found = False

            print("\nMatching Entries:")
            print(self.separator)

            for entry in entries:
                entry = entry.strip()

                if entry and keyword.lower() in entry.lower():
                    print(entry)
                    print()
                    found = True

            if not found:
                print(
                    "No entries were found for the keyword: "
                    + keyword
                )

        except FileNotFoundError:
            print(
                "Error: The journal file does not exist. "
                "Please add a new entry first."
            )
        except PermissionError:
            print("Error: Permission denied while reading the file.")
        except OSError as error:
            print("File error:", error)

    # 4. Delete all journal entries
    def delete_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                content = file.read()

            if not content.strip():
                print("No journal entries to delete.")
                return

            confirmation = input(
                "\nAre you sure you want to delete all entries? "
                "(yes/no): "
            ).strip().lower()

            if confirmation == "yes":
                os.remove(self.filename)
                print("All journal entries have been deleted.")

            elif confirmation == "no":
                print("Deletion cancelled.")

            else:
                print("Invalid response. Please enter yes or no.")

        except FileNotFoundError:
            print("No journal entries to delete.")
        except PermissionError:
            print("Error: Permission denied while deleting the file.")
        except OSError as error:
            print("Error while deleting journal:", error)

    # 5. Display the main menu
    def menu(self):
        while True:
            print("\nWelcome to Personal Journal Manager!")
            print("Please select an option:\n")
            print("1. Add a New Entry")
            print("2. View All Entries")
            print("3. Search for an Entry")
            print("4. Delete All Entries")
            print("5. Exit")

            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.add_entry()

            elif choice == "2":
                self.view_entries()

            elif choice == "3":
                self.search_entry()

            elif choice == "4":
                self.delete_entries()

            elif choice == "5":
                print(
                    "Thank you for using Personal Journal Manager."
                )
                print("Goodbye!")
                break

            else:
                print(
                    "Invalid option. Please select a valid option "
                    "from the menu."
                )


# Create an object and run the program
if __name__ == "__main__":
    journal = JournalManager()
    journal.menu()