                                                            SUMMARY
Print Statements :- Using single and double code
                    Multiple single & double code - to get the same sentence
                    Escape Sequence - Using \ we can continue the sentence
Raw string :- In raw string even escape sequence,single& double code can also be printed,before the string have to keep r .
Variables :- Variables can start with only alphabets & underscore,id can't start with numbers and space
             isidentifier() - To know variable is valid or invalid
             Have to keep more than one variable in one line have to separate with ;
             Termination - Indicates with ; means total ending the variable
Data types :- Int - Int will indicates with numeric
              Float - Float will indicates with decimal point numbers. eg: 2.3,4.7
              String - string will indicates with single code (''), double code ("") or multi codes
Data type conversions:- int can be convert to float &  string
                        float can be convert to int &  string
                        string can not be convert to int & float
Concatenation:- Concatenation means joining or combining of two or multiple strings together
                we can perform concatenation only for strings,it is represented by +
isspace():- If the string has single space or multiple space it is true,or
            the string is empty string or something written inside the string it represents false.
String methods:- 1)Capitalize() - Converts the first character of string is upper remaining all are lower.
                 2)Casefold() - Converts the string into lower case.
                 3)Count() - it will count the number of values specified in a string,but the string does not have that value is shows the
                             count as 0
                 4)Upper() - converts string into upper case
                 5)Lower) - converts string into lower case
                 6)isupper() - If all the characters in the string are in uppercase it returns with true otherwise false
                 7)islower() - If all the characters in the string are in lowercase it returns with true otherwise false
                 8)Replace() - Replace the word in the string
                 9)Title() -  Converts the first character of each word in string to upper case
                 10)istitle() -  True,If the first character of each word in string is upper case otherwise false
                 11)Endswith() - True,if the string ends with specified value otherwise false
                 12)Find() - It will shows the position where it was found,but the value is not found it returns with value -1
                 13)Index() - it will show the position where it was fount,but the value is not found it returns with value error    
                 14)rfind() - It will shows the position where it was found from right side,but the value is not found it returns with value -1
                 15)rIndex() - it will show the position where it was fount from right side,but the value is not found it returns with value error
                 16)Strip()- it removes the characters from left side & right side
                 17)lstrip() - it removes the characters only  from left side
                 18)rstrip() - it removes the characters only  from right side
                 19)Startswith() - True,if the string starts with specified value otherwise false
                 20)Split() - it will split the strings
                 21)Swapcase() - swap the strings,lower case to upper & upper case to lower
                 22)instance() - it will verify the value which has been passed belongs to a particular data type or not
                 23)isalpha() - it should only contains alphabets
                 24)isalnum() - it contains combination of numbers and alphabets
                 25)isidentifier() - To know variable is valid or invalid
                 26)isspace() - If the string has single space or multiple space it is true,or
                                the string is empty string or something written inside the string it represents false
                 27)isnumeric() - true, if it contains all the numbers in string otherwise false                                                                                                                                                                                          Slicing :- To perform slicing the rule is left side value should be less than the right side value,if suppose left side value greater than the
                                  right side value it shows the blank line or empty line.
Slicing :- To perform slicing the rule is left side value should be less than the right side value,if suppose the left side value is greater than the
           right side value it will gave a blank or empty  line.
           Syntax :- a[ : ]
           Left side by default value starts from 0 & right side if we don't gave the value it takes total string
Double Colon Slicing :- To get reverse order of string
                        Syntax :- a[ : : ]
                        Left side value is the starting index position value,middle value is the ending index position value & right side
                        value is the number of splitting times