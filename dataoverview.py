import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import pims

# change the following to %matplotlib notebook for interactive plotting
#get_ipython().run_line_magic('matplotlib', 'inline')

# img read
data = pims.open('screw/*.bmp')
#use empty background frame to subtract noise

### --- Generate Greyscale Horizontal ---- ###

def grayscale_h(frame):
    imgshape = frame.shape
    grayscale = np.empty(imgshape[1], dtype=float)
    
    for column in range(imgshape[1]):
        sumpixel=0;
        for row in frame:
            sumpixel += row[column];
        grayscale[column] = sumpixel/imgshape[0];
    return grayscale


### --- Generate Greyscale Vertical ---- ###
       
def grayscale_v(frame):
    imgshape = frame.shape
    grayscale = np.empty(imgshape[0], dtype=float)
    numrow=0;
    
    for row in frame:
        sumpixel=0;
        for column in range(imgshape[0]):
            sumpixel += row[column];
        grayscale[numrow] = sumpixel/imgshape[0];
        numrow+=1;
    return grayscale

### --- Sience Grayscale Plot --- ###

def grayscaleplot2(data, data2):
    arr_ref =  np.arange(len(data))
    arr_ref2 =  np.arange(len(data2))
    fig, ax = plt.subplots()
    fig.set_size_inches(18.5, 10.5)
    #fig.savefig('test2png.png', dpi=100)
    
    #color pattern: '#00429d' blue, '#b03a2e' red, '#1e8449' green
    ax.plot(arr_ref, data, color='#00429d', label='x')
    ax.plot(data2, arr_ref, color='#b03a2e', label='y')
    ax.legend()
    
    #adds a title and axes labels
    #ax.set_title('')
    plt.xlabel('Pixel')
    plt.ylabel('Grayvalue')
 
    #removing top and right borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False) 
    
    #Edit tick 
    #ax.xaxis.set_minor_locator(MultipleLocator(125))
    #ax.yaxis.set_minor_locator(MultipleLocator(.25))

    #add vertical lines
    #ax.axvline(left, linestyle='dashed', color='b');
    #ax.axvline(right, linestyle='dashed', color='b');

    #adds major gridlines
    ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    
    #ax limit
    ax.set_xlim(xmin=0)
    
    #legend
    #ax.legend(bbox_to_anchor=(1, 1), loc=1, frameon=False, fontsize=16)
    
    plt.show()

### --- Data Overview ---- ###

def dataoverview(data):
    frame0 = data[0]
    x = np.empty(frame0.shape[1])
    y = np.empty(frame0.shape[0])
    for i in data:
        x = x + grayscale_h(i)
        y = y + grayscale_v(i)
    x = x/len(data)
    y = y/len(data)
    print(x)
    print(y)
    #grayscaleplot2(x, y)
    
## main ##
dataoverview(data)