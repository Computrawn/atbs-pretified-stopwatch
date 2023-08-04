
# Prettified Stopwatch

Expand the stopwatch project from this chapter so that it uses the rjust() and ljust() string methods to “prettify” the output.  
(These methods were covered in Chapter 6.)

Instead of output such as this:  
———————————————————  
Lap #1: 3.56 (3.56)  
Lap #2: 8.63 (5.07)  
Lap #3: 17.68 (9.05)  
Lap #4: 19.11 (1.43)  
———————————————————   
. . . the output will look like this:  
———————————————————  
Lap # 1:   3.56 (  3.56)  
Lap # 2:   8.63 (  5.07)  
Lap # 3:  17.68 (  9.05)  
Lap # 4:  19.11 (  1.43)  
———————————————————  
Note that you will need string versions of the lapNum, lapTime, and totalTime integer and float variables in order to call the string methods on them.

Next, use the pyperclip module introduced in Chapter 6 to copy the text output to the clipboard so the user can quickly paste the output to a text file or email.

**Excerpt From Automate the Boring Stuff with Python: Practical Programming for Total Beginners, 2nd Edition  
Al Sweigart  
This material may be protected by copyright.**