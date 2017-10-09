import perception
import drive_rover as dr
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

def rock_threshold():
    image_name = '../calibration_images/example_rock2.jpg'
    image = mpimg.imread(image_name)
    #colorsel = perception.color_thresh(image, rgb_thresh=(180, 180, 0))
    colorsel = perception.color_range(image, (140, 115, 0), (255, 255, 90))

    #print(colorsel)

    # Display the original image and binary               
    f, (ax1, ax2) = plt.subplots(1, 2, figsize=(21, 7), sharey=True)
    f.tight_layout()
    ax1.imshow(image)
    ax1.set_title('Original Image', fontsize=40)

    ax2.imshow(colorsel, cmap='gray')
    ax2.set_title('Your Result', fontsize=40)
    plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
    plt.show() # Uncomment if running on your local machine

def test_perception():
    image_name = '../calibration_images/example_rock1.jpg'
    image = mpimg.imread(image_name)

    rover = dr.RoverState()
    rover.img = image
    rover.yaw = 0.0
    rover.pos = (99.66999, 85.58897)

    perception.perception_step(rover)
    # Display the original image and updated world            
    f, axes = plt.subplots(2, 2, figsize=(21, 7), sharey=True)
    f.tight_layout()
    axes[0, 0].imshow(image)
    axes[0, 0].set_title('Original Image', fontsize=40)

    axes[0, 1].imshow(rover.vision_image)
    axes[0, 1].set_title('Your Result', fontsize=40)

    axes[1, 0].imshow(rover.worldmap)
    axes[1, 0].set_title('WorldMap', fontsize=40) 

    plt.subplots_adjust(left=0., right=1, top=0.9, bottom=0.)
    plt.show() # Uncomment if running on your local machine


if __name__ == "__main__":
    #test_perception()
    rock_threshold()