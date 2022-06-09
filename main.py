# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:56:06 2022

@author: Sameh Zaher , ID: 1800112
"""


"""                    Important libraries and objects                     """

from pickletools import decimalnl_long
from tkinter import *
from tkinter import ttk
from unicodedata import decimal
from numpy import integer
from ttkthemes import ThemedTk
from commands import *


ocv = OpenCV()
root = ThemedTk()
root.title("Image Upscaler")
style = ttk.Style(root)
root.iconbitmap('C:\gui\IProcessing\icon.ico')



style.theme_use('xpnative')

def Make_Label(command, frame):
    for labels in frame.grid_slaves():
        labels.grid_forget()
    ttk.Label(
        frame, 
        image = command).grid(row = 0, column = 0)

def Display(command, frame0, frame1, frame2):
    Make_Label(command[0], frame0)
    if frame1 == None and frame2 == None:
        pass
    elif frame2 == None:
        Make_Label(command[1], frame1)
    else:
        Make_Label(command[1], frame1)
        Make_Label(command[2], frame2)

def Entry_Message():
    image_location_entry.insert(0, 'Enter image absolute path')
    def Callback(event):
        image_location_entry.delete(0, "end")
        image_location_entry['foreground'] = 'black'
        image_location_entry.unbind("<FocusIn>")
        return None
    image_location_entry.bind("<FocusIn>", Callback)


"""                            Color Conversion                            """

color_conversion_frame = ttk.LabelFrame(
    root, 
    text = 'Convert Color')
color_conversion_frame.grid(
    row = 1, column = 2, 
    padx = 7, pady = 7, 
    columnspan = 1, 
    sticky = W)

default_color_radiobutton = ttk.Radiobutton(
    color_conversion_frame, 
    text = 'Default Color', 
    value = 0, 
    command = lambda: Display(
        ocv.DefaultColor(), 
        original_image_frame, None, None))
gray_color_radiobutton = ttk.Radiobutton(
    color_conversion_frame, 
    text = 'Gray Color', 
    value = 1, 
    command = lambda: Display(
        ocv.GrayColor(), 
        original_image_frame, None, None))

default_color_radiobutton.grid(
    row = 0, column = 0, 
    sticky = W)
gray_color_radiobutton.grid(
    row = 1, column = 0, 
    sticky = W)
"""                            Image Flipping                            """
Image_Flipping_frame = ttk.LabelFrame(
    root, 
    text = 'Image Flipping')
Image_Flipping_frame.grid(
    row = 2, column = 2, 
    padx = 7, pady = 7, 
    columnspan = 1, 
    sticky = W)

Vertical_Flip_radiobutton = ttk.Radiobutton(
    Image_Flipping_frame, 
    text = 'Vertical Flip', 
    value = 0, 
    command = lambda: Display(
        ocv.verticalFlip(), 
        original_image_frame, None, None))
Horizontal_Flip_radiobutton = ttk.Radiobutton(
    Image_Flipping_frame, 
    text = 'Horizontal Flip', 
    value = 1, 
    command = lambda: Display(
        ocv.horizontalFlip(), 
        original_image_frame, None, None))

Vertical_Flip_radiobutton.grid(
    row = 0, column = 0, 
    sticky = W)
Horizontal_Flip_radiobutton.grid(
    row = 1, column = 0, 
    sticky = W)

"""                            Image Cropping                            """


Image_Cropping_frame = ttk.LabelFrame(
    root,
    text = 'Image Cropping')
Image_Cropping_frame.grid( 
    row = 2, column = 0, 
    padx = 7, pady = 7, 
    columnspan = 2)

Image_Cropping_Dimention_frame = ttk.LabelFrame(
    Image_Cropping_frame,
    text = 'Image Cropping Dimention')
Image_Cropping_Dimention_frame.grid( 
    row = 1, column = 0, 
    padx = 7, pady = 7, 
    columnspan = 4)

Height_frame = ttk.LabelFrame(
    Image_Cropping_Dimention_frame,
    text = 'Height')
Height_frame.grid( 
    row = 0, column = 3, 
    padx = 7, pady = 7, 
    columnspan = 2)

width_frame = ttk.LabelFrame(
    Image_Cropping_Dimention_frame,
    text = 'width')
width_frame.grid( 
    row = 0, column = 1, 
    padx = 7, pady = 7, 
    columnspan = 2)

dim1=ttk.Entry(Height_frame, width=5)
dim2=ttk.Entry(Height_frame, width=5)
dim3=ttk.Entry(width_frame, width=5)
dim4=ttk.Entry(width_frame, width=5)
dim1.grid(row=0,column=0,columnspan=1)
dim2.grid(row=0,column=1,columnspan=1)
dim3.grid(row=1,column=0,columnspan=1)
dim4.grid(row=1,column=1,columnspan=1)
x='0'
y='1080'
z='0'
w='1920'
x=dim1.getint(s=x)
y=dim2.getint(s=y)
z=dim3.getint(s=z)
w=dim4.getint(s=w)
x=int(x)
y=int(y)
w=int(w)
z=int(z)
#x=ocv.dimentions()[]0


Image_Cropping_button = ttk.Button( 
    Image_Cropping_frame, 
    text='Crop', 
    command=lambda:Display(
         ocv.Crop(x,y,w,z), 
         original_image_frame, None, None))
Image_Cropping_button.grid(
    row=0, 
    column=0)







"""                           Operations Frames                            """

transformations_frame = ttk.LabelFrame(
    root, 
    text = 'Transformation')
transformations_frame.grid(
    row = 0, column = 3, 
    rowspan = 7, 
    padx = 7, pady = 7)

original_image_frame = ttk.LabelFrame(
    transformations_frame, 
    text = 'Original Image', 
    width = 320, height = 200)
original_image_frame.grid(
    row = 0, 
    padx = 7, pady = 7, 
    sticky = NSEW)

filter_frame = ttk.LabelFrame(
    transformations_frame, 
    text = 'Filter', 
    width = 320, height = 200)
filter_frame.grid(
    row = 1, 
    padx = 7, pady = 7, 
    sticky = NSEW)

filtered_image_frame = ttk.LabelFrame(
    transformations_frame, 
    text = 'Filtered Image', 
    width = 320, height = 200)
filtered_image_frame.grid(
    row = 2, 
    padx = 7, pady = 7, 
    sticky = NSEW)


"""                             Image Opening                              """

image_load_frame = ttk.LabelFrame(
    root, 
    text = 'Load Image')
image_load_frame.grid(
    row = 0, column = 0, 
    columnspan = 3, 
    padx = 7, pady = 7)

image_location_entry = ttk.Entry(
    image_load_frame, 
    width = 70)

image_location_entry.grid(
    row = 0, column = 0, 
    padx = 9)

image_location_button = ttk.Button(
    image_load_frame, 
    text = 'Open', 
    width = 11,
    command = lambda: Display(
        ocv.OpenImage(), 
        original_image_frame, None, None))
image_location_button.grid(
    row = 0, 
    column = 1)


"""                       Point Transform Operations                       """

point_transformations_frame = ttk.LabelFrame(
    root, 
    text = 'Point Transformations')
point_transformations_frame.grid(
    row = 1, column = 0, 
    padx = 7, pady = 7, 
    columnspan = 2)

brightness_adjustment_button = ttk.Button(
    point_transformations_frame, 
    text = 'Adjust Brightness', 
    width = 21, 
    command = lambda: Display(
        ocv.AdjustBrightness(), 
        original_image_frame, None, None))
contrast_adjustment_button = ttk.Button(
    point_transformations_frame, 
    text = 'Adjust Contrast', 
    width = 21, 
    command = lambda: Display(
        ocv.AdjustContrast(), 
        original_image_frame, None, None))
histogram_button = ttk.Button(
    point_transformations_frame, 
    text = 'Make Histogram', 
    width = 21, 
    command = lambda: Display(
        ocv.MakeHistogram(), 
        original_image_frame, 
        filter_frame, None))
histogram_equalization_button = ttk.Button(
    point_transformations_frame, 
    text = 'Equalize Histogram', 
    width = 21, 
    command = lambda: Display(
        ocv.EqualizeHistogram(), 
        original_image_frame, 
        filter_frame, 
        filtered_image_frame))

brightness_adjustment_button.grid(
    row = 0, column = 0, 
    padx = 7, pady = 3)
contrast_adjustment_button.grid(
    row = 1, column = 0, 
    padx = 7, pady = 3)
histogram_button.grid(
    row = 2, column = 0, 
    padx = 7, pady = 3)
histogram_equalization_button.grid(
    row = 3, column = 0, 
    padx = 7, pady = 3)


"""                        Local Transform Operations                      """

local_transformations_frame = ttk.LabelFrame(
    root, 
    text = 'Local Transformations')
local_transformations_frame.grid(
    row = 4, column = 0, 
    padx = 7, pady = 7, 
    columnspan = 3)

smoothing_filters_frame = ttk.LabelFrame(
    local_transformations_frame, 
    text = 'Smoothing Filters')
smoothing_filters_frame.grid(
    row = 0, column = 0, 
    padx = 7, pady = 7)

edge_detection_filters_frame = ttk.LabelFrame(
    local_transformations_frame, 
    text = 'Edge Detection Filters')
edge_detection_filters_frame.grid(
    row = 0, column = 1, 
    rowspan = 5, 
    padx = 7, pady = 7)

low_pass_filter_button = ttk.Button(
    smoothing_filters_frame, 
    text = 'Low-Pass Filter', 
    width = 21, 
    command = lambda: Display(
        ocv.LowPassFilter(), 
        filtered_image_frame, None, None))
gaussian_filter_button = ttk.Button(
    smoothing_filters_frame, 
    text = 'Gaussian Filter', 
    width = 21, 
    command = lambda: Display(
        ocv.GaussianFilter(), 
        filtered_image_frame, None, None))
median_filter_button = ttk.Button(
    smoothing_filters_frame, 
    text = 'Median Filter', 
    width = 21, 
    command = lambda: Display(
        ocv.MedianFilter(), 
        filtered_image_frame, None, None))
averaging_filter_button = ttk.Button(
    smoothing_filters_frame, 
    text = 'Averaging Filter', 
    width = 21, 
    command = lambda: Display(
        ocv.AveragingFilter(), 
        filtered_image_frame, None, None))

low_pass_filter_button.grid(
    row = 0, column = 0, 
    padx = 7, pady = 3)
gaussian_filter_button.grid(
    row = 1, column = 0, 
    padx = 7, pady = 3)
median_filter_button.grid(
    row = 2, column = 0, 
    padx = 7, pady = 3)
averaging_filter_button.grid(
    row = 3, column = 0, 
    padx = 7, pady = 3)

high_pass_filter_radioutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'High-Pass Filter', 
    value = 2, 
    command = lambda: Display(
        ocv.HighPassFilter(), 
        filtered_image_frame, None, None))
laplacian_filter_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'Laplacian Filter', 
    value = 3, 
    command = lambda: Display(
        ocv.LaplacianFilter(), 
        filtered_image_frame, None, None))
log_filter_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'LoG Filter', 
    value = 4, 
    command = lambda: Display(
        ocv.LoGFilter(), 
        filtered_image_frame, None, None))
canny_method_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'Canny Method', 
    value = 5, 
    command = lambda: Display(
        ocv.CannyMethod(), 
        original_image_frame, 
        filtered_image_frame, None))
vertical_sobel_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'Vertical Sobel', 
    value = 6, 
    command = lambda: Display(
        ocv.VerticalSobel(), 
        original_image_frame, 
        filtered_image_frame, None))
horizontal_sobel_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'Horizontal Sobel', 
    value = 7, 
    command = lambda: Display(
        ocv.HorizontalSobel(), 
        original_image_frame, 
        filtered_image_frame, None))
vertical_perwitt_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'Vertical Perwitt', 
    value = 8, 
    command = lambda: Display(
        ocv.VerticalPerwitt(), 
        original_image_frame, 
        filtered_image_frame, None))
horizontal_perwitt_radiobutton = ttk.Radiobutton(
    edge_detection_filters_frame, 
    text = 'Horizontal Perwitt', 
    value = 9, 
    command = lambda: Display(
        ocv.HorizontalPerwitt(), 
        original_image_frame, 
        filtered_image_frame, None))

high_pass_filter_radioutton.grid(
    row = 0, column = 0, 
    sticky = W)
laplacian_filter_radiobutton.grid(
    row = 1, column = 0, 
    sticky = W)
log_filter_radiobutton.grid(
    row = 2, column = 0, 
    sticky = W)
canny_method_radiobutton.grid(
    row = 3, column = 0, 
    sticky = W)
vertical_sobel_radiobutton.grid(
    row = 0, column = 1, 
    sticky = W)
horizontal_sobel_radiobutton.grid(
    row = 1, column = 1, 
    sticky = W)
vertical_perwitt_radiobutton.grid(
    row = 2, column = 1, 
    sticky = W)
horizontal_perwitt_radiobutton.grid(
    row = 3, column = 1, 
    sticky = W)


"""                 Global(Hough) Transform Operations                     """

global_transformations_frame = ttk.LabelFrame(
    root, 
    text = 'Global Transformations')
global_transformations_frame.grid(
    row = 5, column = 0, 
    padx = 7, pady = 7)

line_detection_button = ttk.Button(
    global_transformations_frame, 
    text = 'Line Detection', 
    width = 21, 
    command = lambda: Display(
        ocv.LineDetection(), 
        original_image_frame, 
        filtered_image_frame, None))
circle_detection_button = ttk.Button(
    global_transformations_frame, 
    text = 'Circle Detection', 
    width = 21, 
    command = lambda: Display(
        ocv.CircleDetection(), 
        original_image_frame, 
        filtered_image_frame, None))

line_detection_button.grid(
    row = 0, column = 0, 
    padx = 7, pady = 3)
circle_detection_button.grid(
    row = 1, column = 0, 
    padx = 7, pady = 3)


"""                       Morphological Operations                         """

morphological_operations_frame = ttk.LabelFrame(
    root, 
    text = 'Morphological Operations')
morphological_operations_frame.grid(
    row = 5, column = 1, 
    padx = 7, pady = 7, 
    columnspan = 2)

kernel_type_frame = ttk.LabelFrame(
    morphological_operations_frame, 
    text = 'Choose Kernel Type')
kernel_type_frame.grid(
    row = 0, column = 3, 
    padx = 7, pady = 7, 
    rowspan = 3)

dilation_radiobutton = ttk.Radiobutton(
    morphological_operations_frame, 
    text = 'Dilation', 
    value = 10, 
    command = lambda: Display(
        ocv.Dilation(), 
        filtered_image_frame, None, None))
erosion_radiobutton = ttk.Radiobutton(
    morphological_operations_frame, 
    text = 'Erosion', 
    value = 11, 
    command = lambda: Display(
        ocv.Erosion(), 
        filtered_image_frame, None, None))
close_radiobutton = ttk.Radiobutton(
    morphological_operations_frame, 
    text = 'Close', 
    value = 12, 
    command = lambda: Display(
        ocv.Close(), 
        filtered_image_frame, None, None))
open_radiobutton = ttk.Radiobutton(
    morphological_operations_frame, 
    text = 'Open', 
    value = 13, 
    command = lambda: Display(
        ocv.Open(), 
        filtered_image_frame, None, None))

dilation_radiobutton.grid(
    row = 1, column = 0, 
    sticky = W)
erosion_radiobutton.grid(
    row = 0, column = 0, 
    sticky = W)
close_radiobutton.grid(
    row = 1, column = 1, 
    sticky = W)
open_radiobutton.grid(
    row = 0, column = 1, 
    sticky = W)


"""                          Program Operations                            """

save_button = ttk.Button(
    root, 
    text = 'Save Image', 
    width = 21, 
    command = ocv.Save)
exit_button = ttk.Button(
    root, 
    text = 'Exit', 
    width = 17, 
    command =lambda: ocv.Exit(root))

save_button.grid(
    row = 6, column = 0, 
    columnspan = 2, 
    pady = 7)
exit_button.grid(
    row = 6, column = 1, 
    columnspan = 2, 
    pady = 7)


root.mainloop()