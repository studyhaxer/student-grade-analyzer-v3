import logging
logging.basicConfig(level=logging.INFO)
import utils
import file_handler
def main():
    students = []
    while True:
        print("\nStudent Grade Analyzer")
        print("1. Add Students")
        print("2. View Students")
        print("3. Topper")
        print("4. Save Students")
        print("5. Load Students")
        print("6. Search Students")
        print("7. Total Students")
        print("8. Class Average")
        print("9. Delete Students")
        print("10. Update Students")
        print("11. Sort Students by Name")
        print("12. Highest and Lowest Averages")
        print("13. Save and Exit")
        choice = utils.get_menu_choice()
        if choice == '1':
            utils.add_students(students)
        elif choice == '2':
            utils.view_students(students)
        elif choice == '3':
            utils.topper(students)
        elif choice == '4':                
            file_handler.save_students(students)
        elif choice == '5':
            file_handler.load_students(students)
        elif choice == '6':
            utils.search_students(students)
        elif choice == '7':
            utils.total_students(students)
        elif choice == '8':
            utils.class_average(students)
        elif choice == '9':
            utils.delete_student(students)
        elif choice =='10':
            utils.update_student(students)
        elif choice == '11':
            utils.sort_students(students)
        elif choice == '12':
            utils.highest_lowest(students)
        elif choice == '13':
            file_handler.save_students(students)
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()