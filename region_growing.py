import os
import cv2
import numpy as np


def region_growing_run(img, x, y, seed, delta=15):
    """
        x: relative coord (0-1)
        y: relative coord (0-1)
    """

    def is_valid_px(x, y, img):
        if 0 <= x < img.shape[1] and 0 <= y < img.shape[0]:
            return True
        return False

    mask = np.zeros(img.shape[:2])
    for x, y in seed:
        y_abs = int(y * img.shape[0])
        x_abs = int(x * img.shape[1])

        loop_points = [(x_abs, y_abs)]
        px_intensity = img[y_abs, x_abs, :]
        blue = px_intensity[0]
        green = px_intensity[1]
        red = px_intensity[2]

        while len(loop_points) != 0:
            (cx, cy) = loop_points.pop()
            current_intensity = img[cy, cx, :]
            b = int(current_intensity[0])
            g = int(current_intensity[1])
            r = int(current_intensity[2])

            if abs(r - red) < delta and abs(g - green) < delta and abs(b - blue) < delta:
                mask[cy, cx] = 255
                neighbors = [
                    (cx - 1, cy),
                    (cx + 1, cy),
                    (cx - 1, cy - 1),
                    (cx, cy - 1),
                    (cx + 1, cy - 1),
                    (cx - 1, cy + 1),
                    (cx, cy + 1),
                    (cx + 1, cy + 1)
                ]
                for (nx, ny) in neighbors:
                    if is_valid_px(nx, ny, img) and mask[ny, nx] == 0:
                        loop_points.append((nx, ny))
            else:
                pass
    return mask


def region_growing(img, isCT):
    # img = cv2.imread(img_path, cv2.IMREAD_COLOR)
    # img = cv2.resize(img, (320, 320))
    KERNEL_WIDTH = KERNEL_HEIGHT = 5
    SIGMA_X = SIGMA_Y = 2
    img[:, :, 0] = cv2.GaussianBlur(img[:, :, 0], ksize=(KERNEL_WIDTH, KERNEL_HEIGHT), sigmaX=SIGMA_X, sigmaY=SIGMA_Y)
    img[:, :, 1] = cv2.GaussianBlur(img[:, :, 1], ksize=(KERNEL_WIDTH, KERNEL_HEIGHT), sigmaX=SIGMA_X, sigmaY=SIGMA_Y)
    img[:, :, 2] = cv2.GaussianBlur(img[:, :, 2], ksize=(KERNEL_WIDTH, KERNEL_HEIGHT), sigmaX=SIGMA_X, sigmaY=SIGMA_Y)

    x = [0.3, 0.7]
    y = [0.5]
    delta = 30

    print(isCT)
    if isCT:
        seed = [(x[0], y[0]), (x[1], y[0])]
    else:
        # seed = [(0.1, 0.1), (0.2, 0.2), (0.3, 0.3),
        #         (0.4, 0.4), (0.5, 0.5), (0.6, 0.6),
        #         (0.7, 0.7), (0.8, 0.8), (0.9, 0.9)]
        seed = [(0.6, 0.6),
                (0.7, 0.7), (0.8, 0.8), (0.9, 0.9)]
    mask = region_growing_run(img=img, x=x, y=y, seed=seed, delta=delta)
    # cv2.imshow('out_mask', mask)

    img_color = img
    # img_color = cv2.resize(img_color, (256, 256))
    img_color[mask > 0, :] = (0, 255, 255)

    # cv2.circle(img_color, (int(x * img.shape[1]), int(y * img.shape[0])), radius=5, color=(0, 0, 255), thickness=2)

    return img_color
