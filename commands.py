# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 16:55:55 2022

@author: Sameh Zaher , ID: 1800112
"""


"""                           Important libraries                          """

import cv2 as cv
from tkinter import filedialog
from tkinter import messagebox
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
import io
import os.path


class OpenCV():

    """                       Important Operations                         """
    
    def OpenImage(self):
        self.ImageName = filedialog.askopenfilename(
            initialdir = '/', 
            title = 'Select an image', 
            filetypes = (('All files', '*.*'), 
                         ('PNG images', '*.png'), 
                         ('JPEG images', '*.jpeg'), 
                         ('JPG images', '*.jpg')))
        self.OriginalImage = cv.cvtColor(
            cv.imread(self.ImageName), 
            cv.COLOR_BGR2RGB)
		
        self.ocvImage = self.OriginalImage
		
        self.Image = ImageTk.PhotoImage(
            Image.fromarray(self.OriginalImage).
            resize((300, 170)))
		
        return [self.Image, self.ImageName]


    def ConvertImage(self, image):
        self.image = ImageTk.PhotoImage(
            Image.fromarray(image).
            resize((300, 170)))
		
        return self.image

    def pltFigure(self, FigureName, x_label, y_label, x_limit, figure):
        fig = plt.figure()
        plt.title(FigureName)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.xlim(x_limit)
        plt.plot(figure)
        buf = io.BytesIO()
        plt.savefig(buf, format='raw')
        buf.seek(0)
        self.Plot = np.reshape(
            np.frombuffer(buf.getvalue(), dtype = np.uint8), 
            newshape = (int(fig.bbox.bounds[3]), 
                        int(fig.bbox.bounds[2]), -1))
        buf.close()
        return self.Plot

    def TrySave(self):
            try:
                self.NewImage = cv.cvtColor(
                    self.NewImage, 
                    cv.COLOR_RGB2BGR)
                filename = filedialog.asksaveasfilename(
                    initialdir = '/', 
                    title = 'Save image')
                extension = os.path.splitext(self.ImageName)[1]
                cv.imwrite(filename + extension, self.NewImage)
            except:
                messagebox.showinfo(
                    'No image found', 
                    'No operation was performed')

    def Save(self):
        message = messagebox.askyesno(
            'Save image', 
            "Do you want to save this image?")
        if message == 1:
            self.TrySave()
        elif message == 0:
            pass

    def Exit(self, root):
        message0 = messagebox.askyesnocancel(
            'Exit', 
            'Do you want to save changes?')
        if message0 == 1:
            self.TrySave()
            root.destroy()
        elif message0 == 0:
            message1 = messagebox.showwarning(
                'Image loss', 
                'Are you sure?\n All edits will be lost!', 
                type = 'yesno')
            if message1 == 'yes':    
                root.destroy()
            elif message1 == 'no':
                pass
        elif message0 == None:
            pass
    

    # def dimentions(self):
    #     self.ocvImage=self.OriginalImage
    #     self.Height = self.ocvImage.shape[0]
    #     self.Width = self.ocvImage.shape[1]
    #     return [self.Height, self.Width]
    
    """                         Color operations                           """
    
    def DefaultColor(self):
        self.ocvImage = self.OriginalImage
        return [self.Image]

    def GrayColor(self):
        if len(self.ocvImage.shape) == 2:
            self.Gray = self.ConvertImage(self.ocvImage)
            return [self.Gray]
        elif len(self.ocvImage.shape) == 3:
            self.ocvImage = cv.cvtColor(
                self.ocvImage, 
                cv.COLOR_RGB2GRAY)
            self.Gray = self.ConvertImage(self.ocvImage)
            return [self.Gray]
        self.NewImage = self.ocvImage

    """                         flip operations                           """
    def verticalFlip(self):
        self.ocvImage = cv.flip(
            self.ocvImage,0) 
        return [self.ConvertImage(self.ocvImage)]

    def horizontalFlip(self):
        self.ocvImage = cv.flip(
            self.ocvImage,1) 
        return [self.ConvertImage(self.ocvImage)]
    """"                       Cropping operations                        """
    def Crop(self,y_dim,Y_dim,x_dim,X_dim):
        self.ocvImage = self.ocvImage[y_dim:Y_dim, x_dim:X_dim]
        self.NewImage = self.ocvImage
        return [self.ConvertImage(self.ocvImage)]

        
    
   
   
    """                         Point Operations                           """

    def AdjustBrightness(self):
        if len(self.ocvImage.shape) == 3:
            self.ocvImage[:,:,:] += 3 
        elif len(self.ocvImage.shape) == 2:
            self.ocvImage[:,:] += 3
        return [self.ConvertImage(self.ocvImage)]
    
    def AdjustContrast(self):
        if len(self.ocvImage.shape) == 3:
            self.ocvImage[:,:,:] *= 2
        elif len(self.ocvImage.shape) == 2:
            self.ocvImage[:,:] *= 2
        return [self.ConvertImage(self.ocvImage)]

    def MakeHistogram(self):
        self.GrayColor()
        Histogram = cv.calcHist(
            [self.ocvImage], 
            [0], 
            None, 
            [256], 
            [0,256])
        self.Histogram = self.ConvertImage(self.pltFigure(
            'Grayscale Histogram', 
            'Gray Value', 
            'Frequency', 
            [0,256], 
            Histogram))
        return [self.Gray, self.Histogram]

    def EqualizeHistogram(self):
        self.GrayColor()
        Equalizer = cv.equalizeHist(self.ocvImage)
        self.NewImage = Equalizer
        Histogram = cv.calcHist(
            [Equalizer], 
            [0], 
            None, 
            [256], 
            [0,256])
        self.Histogram = self.ConvertImage(self.pltFigure(
            'Equalized Histogram', 
            'Gray Value', 
            'Frequency', 
            [0,256], 
            Histogram))
        self.Equalizer = self.ConvertImage(Equalizer)
        return [self.Gray, self.Histogram, self.Equalizer]
        

    """                         Local Operations                           """
        
    '''                         Smoothing Filters                          '''
    
    def LowPassFilter(self):
        kernel = np.ones((3, 3), np.float32)/9
        self.ocvImage = cv.filter2D(
            self.ocvImage, 
            -1, 
            kernel)
        self.NewImage = self.ocvImage
        return [self.ConvertImage(self.ocvImage)]
    
    def GaussianFilter(self):
        self.ocvImage = cv.GaussianBlur(
            self.ocvImage, 
            (3, 3), 
            cv.BORDER_DEFAULT)
        self.NewImage = self.ocvImage
        return [self.ConvertImage(self.ocvImage)]

    def MedianFilter(self):
        self.ocvImage = cv.medianBlur(
            self.ocvImage, 
            3)
        self.NewImage = self.ocvImage
        return [self.ConvertImage(self.ocvImage)]

    def AveragingFilter(self):
        self.ocvImage = cv.blur(
            self.ocvImage, 
            (3,3))
        self.NewImage = self.ocvImage
        return [self.ConvertImage(self.ocvImage)]

    '''                        Edge Detection Filters                      '''

    def HighPassFilter(self):
        kernel = np.array([
            [0, -1, 0], 
            [-1, 4, -1], 
            [0, -1, 0]])
        HighPass = cv.filter2D(
            self.ocvImage, 
            -1, 
            kernel)
        self.NewImage = HighPass
        return [self.ConvertImage(HighPass)]

    def LaplacianFilter(self):
        Laplacian = cv.Laplacian(
            self.ocvImage, 
            cv.CV_64F)
        Laplacian = np.uint8(np.absolute(Laplacian))
        self.NewImage = Laplacian
        return [self.ConvertImage(Laplacian)]
        
    def LoGFilter(self):
        self.GaussianFilter()
        return self.LaplacianFilter()
    
    def CannyMethod(self):
        self.GrayColor()
        self.Canny = cv.Canny(
            self.ocvImage, 
            125, 175)
        self.NewImage = self.Canny
        return [self.Gray, self.ConvertImage(self.Canny)]

    def HorizontalPerwitt(self):
        self.GrayColor()
        kernel_x = np.array([
            [-1,0,1], 
            [-1,0,1], 
            [-1,0,1]])
        Perwitt_x = cv.filter2D(
            self.ocvImage, 
            -1, 
            kernel_x)
        self.NewImage = Perwitt_x
        return [self.Gray, self.ConvertImage(Perwitt_x)]
    
    def VerticalPerwitt(self):
        self.GrayColor()
        kernel_y = np.array([
            [1,1,1], 
            [0,0,0], 
            [-1,-1,-1]])
        Perwitt_y = cv.filter2D(
            self.ocvImage, 
            -1, 
            kernel_y)
        self.NewImage = Perwitt_y
        return [self.Gray, self.ConvertImage(Perwitt_y)]
    
    def VerticalSobel(self):
        self.GrayColor()
        Sobel_y= cv.Sobel(
            self.ocvImage, 
            cv.CV_64F, 
            0, 1)
        self.NewImage = Sobel_y
        return [self.Gray, self.ConvertImage(Sobel_y)]
    
    def HorizontalSobel(self):
        self.GrayColor()
        Sobel_x = cv.Sobel(
            self.ocvImage, 
            cv.CV_64F, 
            1, 0)
        self.NewImage = Sobel_x
        return [self.Gray, self.ConvertImage(Sobel_x)]
    
    
    """                          Hough Operations                          """

    def LineDetection(self):
        self.CannyMethod()
        lines = cv.cvtColor(self.Canny, cv.COLOR_GRAY2RGB)
        linesP = cv.HoughLinesP(
            self.Canny, 
            1, 
            np.pi / 180, 50, None, 50, 10)
        if linesP is not None:
            for i in range(0, len(linesP)):
                l = linesP[i][0]
                graph = cv.line(
                    lines, 
                    (l[0], l[1]), (l[2], l[3]), (0,0,255), 
                    3, cv.LINE_AA)
        self.NewImage = graph
        return [self.Gray, self.ConvertImage(graph)]

    def CircleDetection(self):
        self.GrayColor()
        self.MedianFilter()
        rows = self.ocvImage.shape[0]
        circles = cv.HoughCircles(
            self.ocvImage, 
            cv.HOUGH_GRADIENT, 
            1, 
            rows/8, 
            param1=100, param2=30, 
            minRadius=1, maxRadius=30)
        image = self.OriginalImage
        if circles is not None:
            circles = np.uint16(np.around(circles))
            for i in circles[0, :]:
                center = (i[0], i[1])
                cv.circle(
                    image, 
                    center, 
                    1, (0, 100, 100), 3)
                radius = i[2]
                cv.circle(image, 
                          center, 
                          radius, (0, 255, 255), 3)
        self.NewImage = image
        return [self.Gray, self.ConvertImage(image)]


    """                       Morphological Operations                     """

    def Dilation(self):
        self.ocvImage = cv.dilate(
            self.ocvImage, 
            (7,7), 
            iterations = 1)
        self.NewImage = self.ocvImage
        return [self.ConvertImage(self.ocvImage)]

    def Erosion(self):
        self.ocvImage = cv.erode(
            self.ocvImage, 
            (7,7), 
            iterations = 1)
        self.NewImage = self.ocvImage
        return [self.ConvertImage(self.ocvImage)]
    
    def Close(self):
        self.ocvImage = cv.morphologyEx(
            self.ocvImage, 
            cv.MORPH_CLOSE, 
            (5, 5), 
            iterations = 1)
        self.NewImage = self.ocvImage
        return [self.ConvertImage(self.ocvImage)]
    
    def Open(self):
        self.ocvImage = cv.morphologyEx(
            self.ocvImage, 
            cv.MORPH_OPEN, 
            (5, 5), 
            iterations = 1)
        self.NewImage = self.ocvImage
        return [self.ConvertImage(self.ocvImage)]



"""crop operation"""
