def find_max_min(num_list):
    """this function checks the minimum and maximum values 
    in a given list and return the results in a list"""

    results =[]
    if type(num_list)!=list:
        raise TypeError
    elif min(num_list)==max(num_list): #checks if all values in the list are equal
        results.append(len(num_list))
        return results
    results.append(min(num_list)) #adds minimum value to index 0
    results.append(max(num_list)) #adds maximum value to index 1
    return results
    