import os, shutil
from pathlib import Path
from os import system
my_dir =Path('C:/Users/Fahim/Documents/udemypy/day 6 files and folders/Recipes/Recipes')
#
#
# for txt in Path(my_dir).glob('**/*.txt'):
#     print(txt)


def choose_category():
    valid_category = [i for i in os.listdir(my_dir)]
    valid_check = [i.lower() for i in valid_category]
    #print(valid_category)
    user_choice = ''
    while user_choice not in valid_check:
        user_choice = input('By typing the name please choose a category  ' + ', '.join(valid_category) + ' ').lower()
        if user_choice in valid_check:
            category_index = (valid_check.index(user_choice))
            file_paths = list((Path(my_dir/valid_check[category_index]).glob('*.txt')))
            file_dir = Path(my_dir/valid_check[category_index])
            file_names = [i.name for i in file_paths]
            #print(file_paths)
            return file_names, file_paths, file_dir
        else:
            print('Input is not recognised. please try again ')

# asks the user to choose an option form the provided categories


def choose_recipes(category,file_paths):
    #print(category)
    user_recipe = ''
    valid_recipes = [items.lower().strip('.txt') for items in category]
    #print(valid_recipes)
    while user_recipe not in valid_recipes:
        user_recipe = input('Enter a recipe from the following recipes -------> ' + ', '.join(items.strip('.txt')
                                                                                             for items in
                                                                                             category) + '.\n').lower()
        if user_recipe in valid_recipes:
            recipe_index = valid_recipes.index(user_recipe)
            system("cls")
            print(file_paths[recipe_index].read_text())
            return file_paths[recipe_index]
        else:
            print('Recipe not found. please try again '.upper())



def new_recipe(file_dir):
    os.chdir(file_dir)
    recipe_name = input('Enter the name of you new recipe ')
    recipe_content = input('Enter the new recipe ')
    with open(f'{recipe_name}.txt','w' ) as file:
        file.writelines(recipe_content)

def new_category():
    all_categories = [i for i in os.listdir(my_dir)]
    print('These are the current categories ' + ','.join(all_categories) + '\n')
    os.chdir(my_dir)
    new_user_category = input("Enter the name of the new category ")
    os.makedirs(new_user_category)

def remove_category(file_dir):
    shutil.rmtree(file_dir)
    all_categories = [i for i in os.listdir(my_dir)]
    print('You have delete the category, the reaming categories are as follows -------> '+','.join(all_categories)+'\n')

def remove_file(file):
    system("cls")
    print('you have deleted the file ' + file.name)
    os.remove(file)




#category, file_paths, file_dir = choose_category()

#file = choose_recipes(category, file_paths)

#new_recipe(file_dir)

#new_category()

#remove_category(file_dir)

#remove_file(file)

user = ''

while user.upper() != 'EXIT':
    user = input('Welcome, please enter 1,2,3,4 or 5 for the following options \n1)Do you want to view a category/recipe\n'
          '2)Create a new recipe\n3)Delete a recipe\n4)Create a new category'
          '\n5)Delete a category\nOr if you want to exit the program exit the program type EXIT ')

    if user == str(1) or user == str(2) or user == str(3):
        system('cls')
        category, file_paths, file_dir = choose_category()
        user = input('Do you want to\n1)Do you want to view a recipe\n2)Create a new recipe\n3)Delete a recipe\n')
        while user != str(1) or str(2) or str(3) or 'EXIT':
            if user == str(1):
                file = choose_recipes(category,file_paths)
                input('Press any key to return to the main menu ')
                system('cls')
                break
            elif user == str(2):
                new_recipe(file_dir)
                input('Press any key to return to the main menu ')
                system('cls')
                break
            elif user == str(3):
                file = choose_recipes(category, file_paths)
                remove_file(file)
                input('Press any key to return to the main menu ')
                system('cls')
                break
            elif user.upper() == 'EXIT':
                exit()
            else:
                user = input(
                    'Do you want to 1)Do you want to view a recipe\n 2)Create a new recipe\n 3)Delete a recipe')
    elif user == str(4):
        system('cls')
        new_category()
        input('Press any key to return to the main menu ')
        system('cls')


    elif user == str(5):
        system('cls')
        category, file_paths, file_dir = choose_category()
        remove_category(file_dir)
        input('Press any key to return to the main menu ')
        system('cls')


    elif str(user).upper() == 'EXIT':
        system('cls')
        print('Ok Bye Bye')
        exit()
    else:
        system('cls')
        print(user)
        print('**************************INPUT NOT RECOGNISED************************************\n ')









































































# while is_valid == False:
#     user_choice = input('By typing the name please choose a category Meat, Salad, Dessert, Pasta ').lower()
#     if user_choice == 'meat':
#         file_paths = list((Path(my_dir/'Meat').glob('*.txt')))
#         file_names = [i.name for i in file_paths]
#         return file_names, file_paths
#     elif user_choice == 'salad':
#         file_paths = list((Path(my_dir / 'Salad').glob('*.txt')))
#         file_names = [i.name for i in file_paths]
#         return file_names, file_paths
#     elif user_choice == 'dessert':
#         file_paths = list((Path(my_dir / 'Dessert').glob('*.txt')))
#         file_names = [i.name for i in file_paths]
#         return file_names, file_paths
#     elif user_choice == 'pasta':
#         file_paths = list((Path(my_dir / 'Pasta').glob('*.txt')))
#         file_names = [i.name for i in file_paths]
#         return file_names, file_paths
#     else:
#         print('Input is not recognised. please try again ')
















