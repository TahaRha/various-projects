#Youssef Temsamani Mokaddem - 26105056


import math

BORDER_SPACING = 1.0         # (represents the amount of spacing on the edges of the plot)
FENCE_COST_PER_METRE = 10.0          # (the cost of fencing per metre)
GRAVEL_COST_PER_METRE_SQUARED = 2.0       # (the cost of gravel per squared metre)
COLOR1_COST = 5.0         # (the cost in dollars of painting the fence a certain color per meter)
COLOR2_COST = 5.0
COLOR3_COST = 5.0 
COLOR4_COST = 10.0
COLOR5_COST = 1000.0

def get_perimeter_of_subplot(subplot_w, subplot_h):
    """ (int,int) -> int
    return the perimeter
    """
    peri = (subplot_w * 2 + subplot_h * 2)
    return peri

def get_area_of_subplot(subplot_w, subplot_h):
    """ (int, int) -> int

    returns the area of subplot
    """
    return subplot_w * subplot_h

def get_cost_per_subplot(subplot_w, subplot_h, color_cost_per_metre):
    """ (int, int , int) -> float

    returns the cost per subplot


    """
    area = get_area_of_subplot(subplot_w, subplot_h)
    peri = get_perimeter_of_subplot(subplot_w, subplot_h)
    cost_fence = peri * (FENCE_COST_PER_METRE + color_cost_per_metre)
    cost_gravel = area * GRAVEL_COST_PER_METRE_SQUARED
    return cost_gravel + cost_fence

def get_cost_for_color(color_choice):
    """ (int) -> float
    gets the cost depending on the color
    """
    
    if(color_choice == 1):
        return COLOR1_COST
    elif (color_choice == 2):
        return COLOR2_COST
    elif (color_choice == 3):
        return COLOR3_COST
    elif (color_choice == 4):
        return COLOR4_COST
    elif (color_choice == 5):
        return COLOR5_COST
    elif (color_choice > 5 or color_choice < 1):
        return 0.0 


def choose_color():
    """ (none) -> int
    choosing the color and returns its price
    """
    print("Color options: ")
    print("1 Martlet Red \n2 Montreal Orange \n3 Cosmic Yellow \n4 The Fourth Colour \n5 Vantablack")
    choice = int(input("What color would you like?  "))
    price = get_cost_for_color(choice)
    return price

def get_num_subplots(plot_w, plot_h, subplot_w, subplot_h, spacing_w, spacing_h):
    """
    (int, int, int, int , int , int) -> int

    returns number of subplots
    """
    space_w = plot_w - BORDER_SPACING * 2
    space_h = plot_h - BORDER_SPACING * 2
    nsub_w = space_w // (subplot_w + spacing_w)
    nsub_h = space_h // (subplot_h + spacing_h)
    left_w = space_w - nsub_w * (subplot_w + spacing_w)
    left_h = space_h - nsub_h * (subplot_h + spacing_h)

    if (left_w == subplot_w):
        nsub_w += 1
    if (left_h == subplot_h):
        nsub_h += 1
    
    return int(nsub_w * nsub_h)

def calculate_cost():
    """ ( none ) -> float

    calculates the cost
    """
    plot_w = float(input("Enter the width of the plot:   "))
    plot_h = float(input("Enter the height of the plot:  "))
    subplot_w = float(input("Enter the width of a subplot:  "))
    subplot_h = float(input("Enter the height of a subplot: "))
    spacing_w = float(input("Enter the horizontal spacing between subplots: "))
    spacing_h = float(input("Enter the horizontal spacing between subplots: "))
    color = choose_color()
    number_sub = get_num_subplots(plot_w, plot_h, subplot_w, subplot_h, spacing_w, spacing_h)
    cost_sub = get_cost_per_subplot(subplot_w, subplot_h, color)
    total_cost = cost_sub * number_sub
    print(number_sub, " subplots can fit in the plot, with a total cost of $", round(total_cost, 2))
    return total_cost




def get_num_subplots_for_budget(plot_length, subplot_length, budget, color_cost_per_metre):
    """ (int, int, float, float) -> int

    returns the number of subplots depending on the budget
    """
    cost = get_cost_per_subplot(subplot_length, subplot_length, color_cost_per_metre)
    number = budget//cost
    fit = get_num_subplots(plot_length, plot_length, subplot_length, subplot_length, 0, 0)
    if (number <= fit):
        return number
    else:
        return fit



def find_maximal_subplots():
    """ ( none ) - > int
    returns maximal number of subplots
    """
    plot_length = float(input("Enter the side length of the plot: "))
    subplot_length = float(input("Enter the side length of the subplot: "))
    color = choose_color()
    budget = float(input("Enter your maximum budget: "))
    number_sub = get_num_subplots_for_budget(plot_length, subplot_length, budget, color)
    available = plot_length - 2
    if (available <= number_sub):
        spacing = 0.0
    else:
        spacing = (available-number_sub) / number_sub

    print("With the given budget, ", number_sub, " subplots can fit in the plot, with spacing of ", round(spacing, 2),
          "m.")
    return number_sub



def menu():
    """ ( none ) -> void

    main menu to the Plot Calculator
    """
    print("Welcome to the Plot Calculator !\nPlease choose from the following: ")
    print("1 Calculate cost of plot project\n2 Find maximal subplots")
    choice = int(input("Your choice: "))
    if (choice == 1):
        calculate_cost()
        print("Have a nice day")
    elif (choice == 2):
        find_maximal_subplots()
        print("Have a nice day")
    else:
        print("Invalid choice.")
        print("Have a nice day")