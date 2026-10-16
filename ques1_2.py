# ques 1 

#a. 
my_name = "Ali"

#b. 
print(len(my_name))

#c
#letter = "a"
for n in my_name.lower(): 
    if n == letter: 
         count = ("letter") + 1

print("the letter", letter, "occurs", count, my_name)


# ques 2 
#a
my_list = [1, 5, "4", "six", 3.14]

new_list = []
for i in my_list: 
    try: 
        new_list.append(int(i))
    except ValueError:
        print("cant convert try another way")

print(new_list) 


#b 
def clean_list(c): 
    clean = []
    for i in new_list:
        try:
            clean.append(int(i))
        except ValueError:
            pass
        return clean

new_list = clean_list(my_list)
print(new_list)

#c

new_list = [1, 5, 4, 3]

total = 0

for i in range(len(new_list)):                                      
    if i > 0:                           
        total = total + new_list[i - 1]  
    if i < len(new_list) - 1:            
        total = total + new_list[i + 1] 
    print(total)      









