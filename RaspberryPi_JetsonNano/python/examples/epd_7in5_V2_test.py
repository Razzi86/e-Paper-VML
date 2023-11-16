#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
from PIL import Image, ImageDraw, ImageFont
import logging
from waveshare_epd import epd7in5_V2
import time

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Directory paths for images and library
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

try:
    # Initialize and clear the display
    logging.info("epd7in5_V2 Demo")
    epd = epd7in5_V2.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    # Load fonts
    font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)

    # Create a new image with white background
    Himage = Image.new('1', (epd.width, epd.height), 255)
    draw = ImageDraw.Draw(Himage)

    # Draw a circle
    # Define the top left and bottom right corners of the bounding rectangle of the circle
    top_left = (150, 150)
    bottom_right = (250, 250)
    draw.ellipse([top_left, bottom_right], outline=0)

    # Display the image on the e-paper display
    epd.display(epd.getbuffer(Himage))
    time.sleep(2)

    # Clear the display and go to sleep
    logging.info("Clear...")
    epd.init()
    epd.Clear()
    logging.info("Goto Sleep...")
    epd.sleep()

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5_V2.epdconfig.module_exit()
    exit()

