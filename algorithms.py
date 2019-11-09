import cv2
import numpy as np
import os

def main():
    # Images
    files = [1, 8, 11, 14, 21, 28, 31, 34]

    # Make output image directory
    output_dir = os.path.join(os.getcwd(), 'output')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read image
    for f in files:
        img = cv2.imread('images/{}.jpg'.format(f), cv2.IMREAD_GRAYSCALE)

        showOriginal(img, f)
        showProcessed(img, f)

def showOriginal(img, f):
    # Show original image
    # cv2.imshow('Original Image', img)

    # Show original image after thresholding
    thresh = 190
    _, img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    # cv2.imshow('Original Image Thresholded', img)

    # Save to file
    cv2.imwrite('output/{}_A.jpg'.format(f), img)

def showProcessed(img, f):
    # Image processing

    # Threshold image first
    thresh = 200
    _, img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

    # nxn median filter
    n = 9
    median_filter = np.ones((n, n), np.float32) / (n*n)
    img = cv2.filter2D(img, -1, median_filter)

    # nxn bilateral filter
    # n = 5
    # s_sigma = 100 # spatial sigma
    # i_sigma = 100 # intensity sigma
    # img = cv2.bilateralFilter(img, n, s_sigma, i_sigma)

    # nxn Scharr filter
    n = -1
    scharr_x = np.uint8(np.absolute(cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=n)))
    scharr_y = np.uint8(np.absolute(cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=n)))
    img = cv2.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)

    # Show processed image
    # cv2.imshow('Processed Image', img)

    # Show processed image after thresholding
    thresh = 50
    _, img = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)

    # img = cv2.bitwise_not(img)

    # cv2.imshow('Processed Image Thresholded', img)
    # cv2.waitKey(0)

    # Save to file
    cv2.imwrite('output/{}_B.jpg'.format(f), img)

if __name__ == '__main__':
    main()
