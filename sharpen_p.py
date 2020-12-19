import cv2
import numpy as np


def LaplacianFrequencyFilter(src, dst):
    im = cv2.imread(src, 0)
    imarr = np.array(im)

    height, width = imarr.shape

    fft = np.fft.fft2(imarr)
    fft = np.fft.fftshift(fft)

    for i in range(height):
        for j in range(height):
            fft[i, j] *= -((i - (height - 1) / 2) ** 2 + (j - (width - 1) / 2) ** 2)

    fft = np.fft.ifftshift(fft)
    ifft = np.fft.ifft2(fft)

    ifft = np.real(ifft)
    max = np.max(ifft)
    min = np.min(ifft)

    res = np.zeros((height, width), dtype="uint8")

    for i in range(height):
        for j in range(width):
            res[i, j] = 255 * (ifft[i, j] - min) / (max - min)

    cv2.imwrite(dst, res)
    gray_girl = "bbb.jpg"
    gaussian_girl = "bbb1.jpg"

    LaplacianFrequencyFilter(gray_girl, gaussian_girl, 20)