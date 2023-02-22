import numpy as np
import matplotlib.pyplot as plt
import pims
from scipy.signal import find_peaks
import scipy.special as scsp

# change the following to %matplotlib notebook for interactive plotting
#get_ipython().run_line_magic('matplotlib', 'inline')

# img read
#data6 = pims.open('C:/Users/Lukas Wimmer/Desktop/D360Pa/XiQ_20210721_080155_Day#03_Parabola#06/*.bmp')
#data7 = pims.open('C:/Users/Lukas Wimmer/Desktop/D360Pa/XiQ_20210721_080155_Day#03_Parabola#07/*.bmp')
#data8 = pims.open('C:/Users/Lukas Wimmer/Desktop/D360Pa/XiQ_20210721_080155_Day#03_Parabola#08/*.bmp')
#data9 = pims.open('C:/Users/Lukas Wimmer/Desktop/D360Pa/XiQ_20210721_080155_Day#03_Parabola#09/*.bmp')
#data10 = pims.open('C:/Users/Lukas Wimmer/Desktop/D360Pa/XiQ_20210721_080155_Day#03_Parabola#10/*.bmp')
#data11 = pims.open('C:/Users/Lukas Wimmer/Desktop/D360Pa/XiQ_20210721_080155_Day#03_Parabola#11/*.bmp')

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
    #ax.axes.yaxis.set_ticklabels([])

    #adds a title and axes labels
    #ax.set_title('')
    plt.ylabel('Flux')
    plt.xlabel('Image')
    
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
    
    ### save plot ###
    plt.savefig('fluxplotP29.png')
    
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
    return flux
    #plot(flux)   

### --- Flux over Time of single frame --- ###

def Flux_frame(data,res_step):
    imgshape = data.shape
    grayscale = np.empty(int(imgshape[1]/res_step)+1, dtype=float)
    for column in range(0,imgshape[0],res_step):
        sumpixel = 0
        for row in range(0,imgshape[1],res_step):
            sumpixel += data[column][row]
        grayscale[int(column/res_step)] = sumpixel/int(imgshape[0]/res_step);
    return sum(grayscale);
        
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
#%%
frames = pims.open('C:/Users/Lukas Wimmer/Documents/GitHub/DustyPlasmaTrackpy/pfc37p29/*.bmp')
data0 = frames[0]
grayscaled0 = grayscale_v(data0, 5)
peaks, _ = find_peaks(grayscaled0,height=3)

avrg_pos = (sum(peaks)/len(peaks)) * 5 * 0.018 #5 stepsize, 0.018mm/pixel 

pos_from_center = abs(15 - avrg_pos)

#dataoverview(data,40)
#data6 = pims.open('C:/Users/Lukas Wimmer/Desktop/D3100Pa/XiQ_20210721_073956_Day#03_Parabola#00/*.bmp')
#a6 = Flux(data6,20)
#data7 = pims.open('C:/Users/Lukas Wimmer/Desktop/D3100Pa/XiQ_20210721_074255_Day#03_Parabola#01/*.bmp')
#a7 = Flux(data7,20)
#data8 = pims.open('C:/Users/Lukas Wimmer/Desktop/D3100Pa/XiQ_20210721_074558_Day#03_Parabola#02/*.bmp')
#a8 = Flux(data8,20)
#data9 = pims.open('C:/Users/Lukas Wimmer/Desktop/D3100Pa/XiQ_20210721_074855_Day#03_Parabola#03/*.bmp')
#a9 = Flux(data9,20)
#data10 = pims.open('C:/Users/Lukas Wimmer/Desktop/D3100Pa/XiQ_20210721_075156_Day#03_Parabola#04/*.bmp')
#a10 = Flux(data10,20)
#data11 = pims.open('C:/Users/Lukas Wimmer/Desktop/D3100Pa/XiQ_20210721_075456_Day#03_Parabola#05/*.bmp')
#a11 = Flux(data11,20)

###Plot with science plot lib 
#%%
plt.style.use(['science','no-latex'])
fig,ax = plt.subplots(dpi=600)

#fig,ax = plt.subplots(dpi=400)
x = np.arange(len(grayscaled0))
ax.plot(x, grayscaled0)
#x = np.arange(len(a7))
#ax.plot(x, a7)
#x = np.arange(len(a8))
#ax.plot(x, a8)
#x = np.arange(len(a9))
#ax.plot(x, a9)
#x = np.arange(len(a10))
#ax.plot(x, a10)
#x = np.arange(len(a11))
#ax.plot(x, a11)

    #
    ###beauty###
    #
#ax.legend(['#0','#1','#2','#3','#4','#5'], loc='upper right', prop={'size': 7})
plt.ylabel('Grayscale')
plt.xlabel('X')
    #
#tex = '\n'.join((r'Pressure = 0.6 mbar'))
#ax.text(0.3,0.9, 'Pressure = 1 mbar', transform=ax.transAxes, fontsize=6, bbox=dict(boxstyle='round', facecolor='grey', alpha=0.3))
#plt.savefig('fluxplot100pa.png')
plt.show()

#%%
N_i0 = 1.3*10**(8)
R = 1.5
r = np.linspace(0., R, 1000)

wave_pos = 0.844 #cm
w_left = wave_pos - 0.38
w_right = wave_pos + 0.38

E_radial_p15 = -2.4 * (9.8/1.5)*(scsp.jv(1,(2.4*r/R))/scsp.jv(0,(2.4*r/R)))
E_radial_p20 = -2.4 * (9/1.5)*(scsp.jv(1,(2.4*r/R))/scsp.jv(0,(2.4*r/R)))
E_radial_p30 = -2.4 * (8.7/1.5)*(scsp.jv(1,(2.4*r/R))/scsp.jv(0,(2.4*r/R)))
E_radial_p40 = -2.4 * (8.5/1.5)*(scsp.jv(1,(2.4*r/R))/scsp.jv(0,(2.4*r/R)))
N_ions = N_i0 * scsp.jv(0,(2.4*r/R))

#Plot
fig,ax = plt.subplots(dpi=600)
ax.plot(r[250:850], E_radial_p15[250:850], label='E_rand_p15')
ax.plot(r[250:850], E_radial_p20[250:850], label='E_rad_p20')
ax.plot(r[250:850], E_radial_p30[250:850], label='E_rad_p30')
ax.plot(r[250:850], E_radial_p40[250:850], label='E_rad_p40')
#ax.plot(r[250:850], N_ions[250:850], label='N_ions')

#Axes
plt.xlabel('x[cm]')
plt.ylabel('E[V/cm]')

#Legende
ax.legend(['P15','P20','P30','P40'], loc='upper left', prop={'size': 7})

#adds major gridlines
ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.25)

#add vertical lines
ax.axvline(wave_pos, linestyle='dashed', color='r');
#ax.axvline(w_right, linestyle='dashed', color='b');

plt.show()