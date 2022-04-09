import numpy as np
import matplotlib.pyplot as plt
import pims

# change the following to %matplotlib notebook for interactive plotting
#get_ipython().run_line_magic('matplotlib', 'inline')

# img read
#data = pims.open('screw/*.bmp')
#bg = pims.open('background/background00.bmp')
#use empty background frame to subtract noise

### --- Generate Greyscale Horizontal ---- ###

def grayscale_h(frame,res_step):
    imgshape = frame.shape
    grayscale = np.zeros(int(imgshape[1]/res_step)+1, dtype=float)
    
    for column in range(0,imgshape[0],res_step):
        sumpixel = 0
        for row in range(0,imgshape[1],res_step):
            sumpixel += frame[row][column]
        grayscale[int(column/res_step)] = sumpixel/int(imgshape[0]/res_step);
    return grayscale

### --- Generate Greyscale Vertical ---- ###
       
def grayscale_v(frame,res_step):
    count = 0
    imgshape = frame.shape
    grayscale = np.zeros(int(imgshape[1]/res_step)+1, dtype=float)
    
    for column in range(0,imgshape[0],res_step):
        sumpixel = 0
        count += 1
        for row in range(0,imgshape[1],res_step):
            sumpixel += frame[column][row]
        grayscale[int(column/res_step)] = sumpixel/int(imgshape[0]/res_step);
    return grayscale

### --- Sience Grayscale Plot --- ###

def grayscaleplot2(datah, datav):
    arr_ref =  np.arange(len(datah))
    arr_ref2 =  np.arange(len(datav))

    plt.style.use(['science','no-latex'])
    fig, ax = plt.subplots(dpi=300)

    ax.plot(arr_ref, datah*20, label='x')
    ax.plot(datav*20, arr_ref2, label='y')

    ax.legend()
    ax.autoscale(tight=True)
    #adds major gridlines
    ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

    #change axis direction
    ax.invert_yaxis()
    #ax.xaxis.tick_top()
    #ax.xaxis.set_label_position('top')

    #adds a title and axes labels
    #ax.set_title('')
    #plt.xlabel('Pixel')
    #plt.ylabel('Grayvalue')
    
    #change axis direction
    #ax.invert_yaxis()
    #ax.xaxis.tick_top()
    #ax.xaxis.set_label_position('top')
    #ax.xaxis.set
    
    #removing top and right borders
    #ax.spines['top'].set_visible(False)
    #ax.spines['right'].set_visible(False) 
    
    #Edit tick 
    #ax.xaxis.set_minor_locator(MultipleLocator(125))
    #ax.yaxis.set_minor_locator(MultipleLocator(.25))

    #add vertical lines
    #ax.axvline(left, linestyle='dashed', color='b');
    #ax.axvline(right, linestyle='dashed', color='b');

    #adds major gridlines
    #ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    
    #ax limit
    #ax.set_xlim(xmin=0)
    
    #legend
    #ax.legend(bbox_to_anchor=(1, 1), loc=1, frameon=False, fontsize=16)
    
    plt.show()

def plot(data):
    arr_ref =  np.arange(len(data))

    plt.style.use(['science','no-latex'])
    fig, ax = plt.subplots(dpi=300)

    ax.plot(arr_ref, data, label='flux')

    ax.legend()
    ax.autoscale(tight=True)
    #adds major gridlines
    ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)

    #change axis direction
    #ax.invert_yaxis()
    #ax.xaxis.tick_top()
    #ax.xaxis.set_label_position('top')
    ax.axes.yaxis.set_ticklabels([])

    #adds a title and axes labels
    #ax.set_title('')
    #plt.xlabel('Pixel')
    #plt.ylabel('Grayvalue')
    
    #change axis direction
    #ax.invert_yaxis()
    #ax.xaxis.tick_top()
    #ax.xaxis.set_label_position('top')
    #ax.xaxis.set
    
    #removing top and right borders
    #ax.spines['top'].set_visible(False)
    #ax.spines['right'].set_visible(False) 
    
    #Edit tick 
    #ax.xaxis.set_minor_locator(MultipleLocator(125))
    #ax.yaxis.set_minor_locator(MultipleLocator(.25))

    #add vertical lines
    #ax.axvline(left, linestyle='dashed', color='b');
    #ax.axvline(right, linestyle='dashed', color='b');

    #adds major gridlines
    #ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.5)
    
    #ax limit
    #ax.set_xlim(xmin=0)
    
    #legend
    #ax.legend(bbox_to_anchor=(1, 1), loc=1, frameon=False, fontsize=16)
    
    plt.show()

### --- Flux Over Time --- ###

def Flux(data,res_step):
    pointer = 0
    imgshape = data[0].shape
    flux = np.zeros(len(data), dtype=float)
    
    for frame in data:
        grayscale = np.empty(int(imgshape[1]/res_step)+1, dtype=float)
        for column in range(0,imgshape[0],res_step):
            sumpixel = 0
            for row in range(0,imgshape[1],res_step):
                sumpixel += frame[column][row]
            grayscale[int(column/res_step)] = sumpixel/int(imgshape[0]/res_step);
        flux[pointer] = flux[pointer] + sum(grayscale)
        pointer += 1 
    #plot(flux)   
    return flux
    
### --- Data Overview ---- ###

def Dataoverview(data, res_step):
    imgshape = data[0].shape
    grayscaleh = np.zeros(int(imgshape[1]/res_step)+1, dtype=float)
    grayscalev = np.zeros(int(imgshape[1]/res_step)+1, dtype=float)
    
    for frame in data:
        grayscaleh += grayscale_h(frame,res_step)
        grayscalev += grayscale_v(frame,res_step)        
    grayscaleh = grayscaleh/len(data)
    grayscalev = grayscalev/len(data)
    
    #grayscaleplot2(grayscaleh, grayscalev)
    return grayscaleh, grayscalev
    
## main ##

#dataoverview(data,40)
#a = Flux(data,40)
#x = np.linspace(0,len(a)-1,len(a))