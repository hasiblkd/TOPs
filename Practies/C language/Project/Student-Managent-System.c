#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

// Define the Student structure
typedef struct {
    int id;
    char name[50];
    char email[50];
    char phone[15];
    float cgpa;
} Student;

// Global variables
const char *FILENAME = "students.txt";  // Text file instead of binary
Student students[100];
int student_count = 0;

// Function prototypes
void loadFromFile();
void saveToFile();
void addStudent();
void viewAllStudents();
void searchStudent();
void updateStudent();
void deleteStudent();
void displayMenu();
void clearInputBuffer();
int isValidEmail(const char *email);
int isValidPhone(const char *phone);
int findStudentById(int id);

// Main Menu
void displayMenu() {
    printf("\n");
    printf("======================================\n");
    printf("   STUDENT MANAGEMENT SYSTEM\n");
    printf("======================================\n");
    printf("1. Add New Student\n");
    printf("2. View All Students\n");
    printf("3. Search Student (by ID)\n");
    printf("4. Update Student Information\n");
    printf("5. Delete Student\n");
    printf("6. Save & Exit\n");
    printf("======================================\n");
    printf("Enter your choice (1-6): ");
}

// Clear input buffer
void clearInputBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

// Validate email format
int isValidEmail(const char *email) {
    const char *at = strchr(email, '@');
    if (at == NULL) return 0;
    
    const char *dot = strchr(at, '.');
    if (dot == NULL || dot <= at + 1) return 0;
    
    return 1;
}

// Validate phone number
int isValidPhone(const char *phone) {
    if (strlen(phone) < 10) return 0;
    
    for (int i = 0; phone[i] != '\0'; i++) {
        if (!isdigit(phone[i]) && phone[i] != '+' && phone[i] != '-' && phone[i] != ' ') {
            return 0;
        }
    }
    return 1;
}

// Find student by ID
int findStudentById(int id) {
    for (int i = 0; i < student_count; i++) {
        if (students[i].id == id) {
            return i;
        }
    }
    return -1;
}

// Load students from TEXT file
void loadFromFile() {
    FILE *file = fopen(FILENAME, "r");  // Read mode (text)
    
    if (file == NULL) {
        printf("No existing data file found. Starting fresh.\n");
        student_count = 0;
        return;
    }
    
    // Skip header line
    char header[200];
    fgets(header, sizeof(header), stdin);
    
    // Read file line by line (CSV format)
    // Format: ID,Name,Email,Phone,CGPA
    while (student_count < 100) {
        int result = fscanf(file, "%d,%49[^,],%49[^,],%14[^,],%f\n",
                           &students[student_count].id,
                           students[student_count].name,
                           students[student_count].email,
                           students[student_count].phone,
                           &students[student_count].cgpa);
        
        if (result != 5) {
            break;  // End of file or parsing error
        }
        student_count++;
    }
    
    fclose(file);
    printf("Loaded %d students from file.\n", student_count);
}

// Save students to TEXT file
void saveToFile() {
    FILE *file = fopen(FILENAME, "w");  // Write mode (text)
    
    if (file == NULL) {
        printf("Error: Cannot open file for writing.\n");
        return;
    }
    
    // Write header
    fprintf(file, "ID,Name,Email,Phone,CGPA\n");
    fprintf(file, "================================================================================\n");
    
    // Write all students in CSV format
    for (int i = 0; i < student_count; i++) {
        fprintf(file, "%d,%s,%s,%s,%.2f\n",
                students[i].id,
                students[i].name,
                students[i].email,
                students[i].phone,
                students[i].cgpa);
    }
    
    fclose(file);
    printf("\nData saved successfully to '%s'.\n", FILENAME);
}

// Add a new student
void addStudent() {
    if (student_count >= 100) {
        printf("Error: Maximum student limit (100) reached.\n");
        return;
    }
    
    Student *newStudent = &students[student_count];  // Pointer to new student
    
    printf("\n--- Add New Student ---\n");
    
    // Get unique ID
    printf("Enter Student ID: ");
    scanf("%d", &newStudent->id);
    
    if (findStudentById(newStudent->id) != -1) {
        printf("Error: Student with ID %d already exists!\n", newStudent->id);
        return;
    }
    
    clearInputBuffer();
    
    // Get name
    printf("Enter Student Name: ");
    fgets(newStudent->name, sizeof(newStudent->name), stdin);
    newStudent->name[strcspn(newStudent->name, "\n")] = '\0';
    
    if (strlen(newStudent->name) == 0) {
        printf("Error: Name cannot be empty.\n");
        return;
    }
    
    // Get email
    do {
        printf("Enter Email: ");
        fgets(newStudent->email, sizeof(newStudent->email), stdin);
        newStudent->email[strcspn(newStudent->email, "\n")] = '\0';
        
        if (!isValidEmail(newStudent->email)) {
            printf("Error: Invalid email format. Try again.\n");
        }
    } while (!isValidEmail(newStudent->email));
    
    // Get phone
    do {
        printf("Enter Phone Number: ");
        fgets(newStudent->phone, sizeof(newStudent->phone), stdin);
        newStudent->phone[strcspn(newStudent->phone, "\n")] = '\0';
        
        if (!isValidPhone(newStudent->phone)) {
            printf("Error: Invalid phone format. Try again.\n");
        }
    } while (!isValidPhone(newStudent->phone));
    
    // Get CGPA
    do {
        printf("Enter CGPA (0.0 - 4.0): ");
        scanf("%f", &newStudent->cgpa);
        
        if (newStudent->cgpa < 0 || newStudent->cgpa > 4.0) {
            printf("Error: CGPA must be between 0.0 and 4.0.\n");
        }
    } while (newStudent->cgpa < 0 || newStudent->cgpa > 4.0);
    
    clearInputBuffer();
    
    student_count++;
    printf("Student added successfully!\n");
}

// View all students
void viewAllStudents() {
    if (student_count == 0) {
        printf("\nNo students to display.\n");
        return;
    }
    
    printf("\n");
    printf("═════════════════════════════════════════════════════════════════════════════════════\n");
    printf("%-5s %-20s %-25s %-15s %-8s\n", "ID", "Name", "Email", "Phone", "CGPA");
    printf("═════════════════════════════════════════════════════════════════════════════════════\n");
    
    for (int i = 0; i < student_count; i++) {
        printf("%-5d %-20s %-25s %-15s %.2f\n",
               students[i].id,
               students[i].name,
               students[i].email,
               students[i].phone,
               students[i].cgpa);
    }
    
    printf("═════════════════════════════════════════════════════════════════════════════════════\n");
    printf("Total Students: %d\n", student_count);
}

// Search student by ID
void searchStudent() {
    if (student_count == 0) {
        printf("\nNo students in the system.\n");
        return;
    }
    
    printf("\n--- Search Student ---\n");
    int id;
    printf("Enter Student ID to search: ");
    scanf("%d", &id);
    clearInputBuffer();
    
    int index = findStudentById(id);
    
    if (index == -1) {
        printf("Error: Student with ID %d not found.\n", id);
        return;
    }
    
    Student *student = &students[index];  // Pointer to found student
    
    printf("\n");
    printf("════════════════════════════════════\n");
    printf("Student Found!\n");
    printf("════════════════════════════════════\n");
    printf("ID    : %d\n", student->id);
    printf("Name  : %s\n", student->name);
    printf("Email : %s\n", student->email);
    printf("Phone : %s\n", student->phone);
    printf("CGPA  : %.2f\n", student->cgpa);
    printf("════════════════════════════════════\n");
}

// Update student information
void updateStudent() {
    if (student_count == 0) {
        printf("\nNo students in the system.\n");
        return;
    }
    
    printf("\n--- Update Student ---\n");
    int id;
    printf("Enter Student ID to update: ");
    scanf("%d", &id);
    clearInputBuffer();
    
    int index = findStudentById(id);
    
    if (index == -1) {
        printf("Error: Student with ID %d not found.\n", id);
        return;
    }
    
    Student *student = &students[index];  // Pointer to student to update
    
    printf("\nCurrent Information:\n");
    printf("1. Name : %s\n", student->name);
    printf("2. Email: %s\n", student->email);
    printf("3. Phone: %s\n", student->phone);
    printf("4. CGPA : %.2f\n", student->cgpa);
    
    printf("\nWhat do you want to update? (1-4): ");
    int choice;
    scanf("%d", &choice);
    clearInputBuffer();
    
    switch (choice) {
        case 1: {
            printf("Enter new name: ");
            fgets(student->name, sizeof(student->name), stdin);
            student->name[strcspn(student->name, "\n")] = '\0';
            printf("Name updated successfully!\n");
            break;
        }
        case 2: {
            do {
                printf("Enter new email: ");
                fgets(student->email, sizeof(student->email), stdin);
                student->email[strcspn(student->email, "\n")] = '\0';
                
                if (!isValidEmail(student->email)) {
                    printf("Error: Invalid email format. Try again.\n");
                }
            } while (!isValidEmail(student->email));
            printf("Email updated successfully!\n");
            break;
        }
        case 3: {
            do {
                printf("Enter new phone: ");
                fgets(student->phone, sizeof(student->phone), stdin);
                student->phone[strcspn(student->phone, "\n")] = '\0';
                
                if (!isValidPhone(student->phone)) {
                    printf("Error: Invalid phone format. Try again.\n");
                }
            } while (!isValidPhone(student->phone));
            printf("Phone updated successfully!\n");
            break;
        }
        case 4: {
            do {
                printf("Enter new CGPA (0.0 - 4.0): ");
                scanf("%f", &student->cgpa);
                
                if (student->cgpa < 0 || student->cgpa > 4.0) {
                    printf("Error: CGPA must be between 0.0 and 4.0.\n");
                }
            } while (student->cgpa < 0 || student->cgpa > 4.0);
            printf("CGPA updated successfully!\n");
            clearInputBuffer();
            break;
        }
        default:
            printf("Invalid choice!\n");
    }
}

// Delete student
void deleteStudent() {
    if (student_count == 0) {
        printf("\nNo students in the system.\n");
        return;
    }
    
    printf("\n--- Delete Student ---\n");
    int id;
    printf("Enter Student ID to delete: ");
    scanf("%d", &id);
    clearInputBuffer();
    
    int index = findStudentById(id);
    
    if (index == -1) {
        printf("Error: Student with ID %d not found.\n", id);
        return;
    }
    
    printf("Confirm deletion of %s? (yes/no): ", students[index].name);
    char confirm[10];
    fgets(confirm, sizeof(confirm), stdin);
    
    if (strcmp(confirm, "yes\n") != 0) {
        printf("Deletion cancelled.\n");
        return;
    }
    
    // Shift students to fill the gap
    for (int i = index; i < student_count - 1; i++) {
        students[i] = students[i + 1];
    }
    
    student_count--;
    printf("Student deleted successfully!\n");
}

// Main function
int main() {
    int choice;
    
    printf("\n╔════════════════════════════════════╗\n");
    printf("║ Welcome to Student Management      ║\n");
    printf("║ (Text File Version - Mac Ready)    ║\n");
    printf("║ Loading existing data...           ║\n");
    printf("╚════════════════════════════════════╝\n\n");
    
    loadFromFile();
    
    while (1) {
        displayMenu();
        scanf("%d", &choice);
        clearInputBuffer();
        
        switch (choice) {
            case 1:
                addStudent();
                break;
            case 2:
                viewAllStudents();
                break;
            case 3:
                searchStudent();
                break;
            case 4:
                updateStudent();
                break;
            case 5:
                deleteStudent();
                break;
            case 6:
                saveToFile();
                printf("Thank you for using Student Management System!\n");
                return 0;
            default:
                printf("Invalid choice! Please try again.\n");
        }
    }
    
    return 0;
}