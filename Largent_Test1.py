
# coding: utf-8

# In[105]:

# ------------------------------------------------------------------------- #
# --------------------------------- Test 1 -------------------------------- #
# ------------------------------------------------------------------------- #

get_ipython().system('ipython nbconvert --to script Largent_Test1.ipynb')

# 1) polygperim

#The function calculates the perimeter of a polynomial defined by the
#coordinates provided in the input list. Note that the points must
#be ordered in the manner that the points connect. The for loop caputres the dist. 
#between all the points EXCEPT for the endpoint and its connection to the first
#point. This is why there is an additional perimeter calculation outside
#of the for loop. 
#
#Parameters:
#list1 - a list composed of tuples which represent x,y coordinates
#perimeter - number representing the perimeter
#x1,x2 - number representing the x coordinates of two points that connect
#y1,y2 - number representing the y coordinates of two points that connect

def polygperim(list1):
    perimeter = 0
    for i in range(len(list1)-1):
            x1, y1 = list1[i]
            x2, y2 = list1[i+1]
            perimeter += ((x2-x1)**2 + (y2-y1)**2)**.5
    x1, y1 = list1[len(list1)-1]
    x2, y2 = list1[0]
    perimeter += ((x2-x1)**2 + (y2-y1)**2)**.5
    
    return perimeter

polygperim(coords)

# 2) polygarea

#The function calculates the area of a polynomial defined by the
#coordinates provided in the input list. Note that the points must
#be ordered in the manner that the points connect. The for loop caputres the area  
#calculations for all the points EXCEPT for the endpoint and its connection to the first
#point. This is why there is an additional area calculation outside
#of the for loop. 
#
#Parameters:
#list1 - a list composed of tuples which represent x,y coordinates
#area - number representing the area
#x1,x2 - number representing the x coordinates of two points that connect
#y1,y2 - number representing the y coordinates of two points that connect

def polygarea(list1):
    area = 0
    for i in range(len(list1)-1):
            x1, y1 = list1[i]
            x2, y2 = list1[i+1]
            area += (x1*y2 - x2*y1)
    x1, y1 = list1[len(list1)-1]
    x2, y2 = list1[0]
    area += (x1*y2-x2*y1)
    area = .5 * abs(area)
    return area


# In[ ]:



