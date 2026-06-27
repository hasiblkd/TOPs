#!/bin/bash
cd "/Users/hasib/Documents/TOPs/TOPs"
/usr/bin/gcc -o Student-Managent-System 'Practies/C language/Project/Student-Managent-System.c'
printf '%s\n' 1 101 Alice alice@example.com 1234567890 3.5 2 6 > /tmp/student_input.txt
./Student-Managent-System < /tmp/student_input.txt
