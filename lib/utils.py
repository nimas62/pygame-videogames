def shift_buffer(buffer_list, new_sample):
    """shifts a FIFO buffer by adding a new sample and deleting the last"""
    for i, x in enumerate(buffer_list[:-1]):        
        buffer_list[i]=buffer_list[i+1]
    buffer_list[-1]=new_sample
    return buffer_list
    
def list_average(number_list):
    """averages the elements of a list."""
    return sum(number_list)/len(number_list)