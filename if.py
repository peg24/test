is_male = False
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male or tall")


if is_male and is_tall:
    print("You are a tall male")
elif is_male and not (is_tall):
    print("You are a short male")    
elif not is_male and is_tall:
    print("You are a not a male but are tall")  
else:
    print("You are either male or not tall or both")


