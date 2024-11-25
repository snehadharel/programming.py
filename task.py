#Write a menu driven program fot the following using function.
#1. To check wether the entered number is even or odd.
#2. To print maximum among three number.
#3. To print minimum among three number.
#4. To print maximum among two number.
#5.Exit
# def check_even_odd():
#     num = int(input("Enter a number: "))
#     if num % 2 == 0:
#         print(f"{num} is Even.")
#     else:
#         print(f"{num} is Odd.")

# def max_among_three():
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     num3 = int(input("Enter third number: "))
#     max_num = max(num1, num2, num3)
#     print(f"The maximum among the three numbers is: {max_num}")

# def min_among_three():
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     num3 = int(input("Enter third number: "))
#     min_num = min(num1, num2, num3)
#     print(f"The minimum among the three numbers is: {min_num}")

# def max_among_two():
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     max_num = max(num1, num2)
#     print(f"The maximum among the two numbers is: {max_num}")

# def main():
#     while True:
#         print("\nMenu:")
#         print("1. Check whether the entered number is even or odd")
#         print("2. Print maximum among three numbers")
#         print("3. Print minimum among three numbers")
#         print("4. Print maximum among two numbers")
#         print("5. Exit")
        
#         choice = int(input("Enter your choice: "))
        
#         match choice:
#             case 1:
#                 check_even_odd()
#             case 2:
#                 max_among_three()
#             case 3:
#                 min_among_three()
#             case 4:
#                 max_among_two()
#             case 5:
#                 print("Exiting the program...Bye..See you soon.")
#                 break
#             case _:
#                 print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()

#list["roshan","pratyush","sara","prayug"]
#a. WAP to insert "sneha" to the position 2 in the line.
#b. Display the name in the list in index position 1 and 2.
#c. Append "bini" in the list.
#d. Delete the name "sara" frm the list
#e. Delete the last name from the list
#f. Replace "roshan" with "manjil"
#g. Clear all the list
#Delete the list menu as list

# Initialize the list
names = ["roshan", "pratyush", "sara", "prayug"]

# a. Insert "sneha" at position 2
names.insert(2, "sneha")
print("After inserting 'sneha' at position 2:", names)

# b. Display the name in the list at index positions 1 and 2
print("Name at index 1:", names[1])
print("Name at index 2:", names[2])

# c. Append "bini" in the list
names.append("bini")
print("After appending 'bini':", names)

# d. Delete the name "sara" from the list
names.remove("sara")
print("After deleting 'sara':", names)

# e. Delete the last name from the list
names.pop()
print("After deleting the last name:", names)

# f. Replace "roshan" with "manjil"
names[names.index("roshan")] = "manjil"
print("After replacing 'roshan' with 'manjil':", names)

# g. Clear all elements from the list
names.clear()
print("After clearing the list:", names)
