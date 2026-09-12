name = input("Enter your name : ")

with open('name.txt' , 'w') as file:
    content = file.write(name)
    
    
# I have entered my name Atonu Roy Chowdhury to the name.txt file as input.