with open("recipe.txt") as input_file:
    with open("recipe_copy.txt","w") as output_file:
        for line in input_file:
            output_file.write(line)
            print( line.strip() )
'''    
    line = input_file.readline()
    while line:
        print( line.strip() )
        line = input_file.readline()
'''
