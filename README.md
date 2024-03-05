# Random-Password-Generator
This is a simple password generator application built using Python's Tkinter library. The application allows users to generate random passwords of variable length with options for including letters, digits, and symbols.

A random password generator is a tool or program that creates passwords with a high degree of randomness, making them more secure than easily guessable passwords. These generators typically use algorithms to produce strings of characters, including uppercase and lowercase letters, numbers, and special symbols. Using strong, random passwords is essential for protecting sensitive information and preventing unauthorized access to accounts.

We have also used the Random module of Python programming language. It is used to generate pseudo-random numbers. It provides several functions for generating random data, including integers, floating-point numbers, and sequences. 
This program creates a graphical user interface (GUI) where users can specify the length of the password and generate a random password accordingly.

## TKinter
This project is designed using Tkinter. Tkinter is a standard GUI (Graphical User Interface) toolkit for the Python programming language. It provides a set of tools and libraries that allows developers to create desktop applications with graphical interfaces. Tkinter is based on the Tk GUI toolkit, which is widely used and well-established. Some key features and components of Tkinter include widgets, geometry management, event handling, cross-platform. 

## Working 
There are several functions defined including enter, leave, and password_generation.
Enter and leave functions change the background and foreground color of the generate button when the mouse enters or leaves the button. Password_generation function generates a password based on the specified length. Various widgets are created such as labels, entry boxes, and buttons to design the GUI. Widgets are organized using pack, grid, and place geometry managers within frames and the main window. Finally, we start the Tkinter event loop using root.mainloop().
