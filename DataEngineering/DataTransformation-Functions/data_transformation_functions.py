# Required Functions utilized in analytics or data engineering
# for this project.


#Hour of Day value transformation function
def hour_of_day_cut(hour_of_day):
    '''
    
    Parameters: hour_of_day (string)
    
    Return: Part of the day (string)
    '''
    if hour_of_day in [i for i in range(0,6)] or hour_of_day in [22,23,24]:
        return('After Hours')
    elif hour_of_day in [i for i in range(6,12)]:
        return('Morning')
    elif hour_of_day in [i for i in range(13,17)]:
        return('Afternoon')
    else:
        return('Evening')
    
if __name__ == '__main__':
    hour_of_day_cut()