# latex-template-generator
A python script that can automate generating multiple latex files and `.pdf` files from a single template, given the template and `.csv` files of attributes.

With the template in another folder called 'template', which has the template and all of the dependent files (eg. image, package files), and a `.csv` file in the root directory (with the script).

The headers of the `.csv` should have the keywords that each element of the subsequent rows will replace it with.

The template code is called `random.tex` in this script, change as needed.

Run `latexmk -pdf` from the command line in the working directory with all the `.tex` files to compile them and generate the corresponding `.pdf` files.

Written in mid-2020 for the NZPMC student competition in 2020 for automating certificate generation for hundreds of students.
