#!/usr/bin/env python3
import subprocess
from pathlib import Path

cwd = Path('/Users/hasib/Documents/TOPs/TOPs')
src = cwd / 'Practies' / 'C language' / 'Project' / 'Student-Managent-System.c'
bin_path = cwd / 'Student-Managent-System'
input_path = cwd / 'student_input.txt'

input_data = '1\n101\nAlice\nalice@example.com\n1234567890\n3.5\n2\n6\n'
with input_path.open('w') as f:
    f.write(input_data)

subprocess.run(['/usr/bin/gcc', '-o', str(bin_path), str(src)], cwd=str(cwd), check=True)
subprocess.run([str(bin_path)], cwd=str(cwd), stdin=input_path.open('r'), check=True)
