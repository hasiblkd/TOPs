#include<iostream>
using namespace std;
class Person{
    protected:
        string name;
        int age;
    public:
        void getPersonDetails(){
            cout<<"Enter  name: ";
            cin>>name;
            cout<<"Enter  age: ";
            cin>>age;
        }
        void displayPersonDetails(){
            cout<<"Name: "<<name<<endl;
            cout<<"Age: "<<age<<endl;
        }
};
class Student: public Person{
    private:
        int s_rollno;
    public:
        void getStudentDetails(){
            getPersonDetails();
            cout<<"Enter  roll number: ";
            cin>>s_rollno;
        }
        void displayStudentDetails(){
            displayPersonDetails();
            cout<<"Roll Number: "<<s_rollno<<endl;
        }
};
class Teacher: public Person{
    private:
        string t_name;
    public:
        void getTeacherDetails(){
            getPersonDetails();
            cout<<"Enter name: ";
            cin>>t_name;
        }
        void displayTeacherDetails(){
            displayPersonDetails();
            cout<<"Name: "<<t_name<<endl;
        }
};
int main(){
    Student student;
    Teacher teacher;
    cout<<"Enter student details:"<<endl;
    student.getStudentDetails();
    cout<<"\nEnter teacher details:"<<endl;
    teacher.getTeacherDetails();
    cout<<"\nStudent Details:"<<endl;
    student.displayStudentDetails();
    cout<<"\nTeacher Details:"<<endl;
    teacher.displayTeacherDetails();
    return 0;
}