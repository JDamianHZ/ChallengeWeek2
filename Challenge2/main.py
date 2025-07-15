from factory import DocumentFactory
from counter import DocumentCounter

def main():
    counter = DocumentCounter()

    while True:
        print("\n=== Document Creator ===")
        print("1. Create PDF Document")
        print("2. Create Word Document")
        print("3. Create Text Document")
        print("4. View document count")
        print("5. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                doc = DocumentFactory.create_document("pdf")
                print(doc.read())
                name = input("Enter document name: ")
                doc.save(name + ".pdf")
                counter.increment()
            elif choice == "2":
                doc = DocumentFactory.create_document("word")
                print(doc.read())
                name = input("Enter document name: ")
                doc.save(name +".docx")
                counter.increment()
            elif choice == "3":
                doc = DocumentFactory.create_document("text")
                print(doc.read())
                name = input("Enter document name: ")
                doc.save(name +".txt")
                counter.increment()
            elif choice == "4":
                print(f"Total documents created: {counter.get_count()}")
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
