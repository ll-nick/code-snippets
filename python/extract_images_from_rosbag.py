#!/usr/bin/env python2

"""
Extract all images from a specified topic and write to disk as .png
"""


import argparse
import os
from pathlib import Path
import progressbar
import rospy
import rosbag
import cv2 as cv
from cv_bridge import CvBridge

def extract_bag(bagpath, outpath, img_topic, prefix):

    print("Loading rosbag...")
    bag = rosbag.Bag(bagpath)
    bridge = CvBridge()

    make_dir(outpath)

    print("Writing images...")
    for idx, (topic, msg, t) in enumerate(progressbar.progressbar(bag.read_messages(topics=img_topic), redirect_stdout=True)):
        cv_img = bridge.imgmsg_to_cv2(msg, "bgr8")
        cv.imwrite(os.path.join(outpath, prefix + str(idx) + ".png"), cv_img)

    bag.close()

    print("Done.")

    return

def make_dir(d):
    if not os.path.isdir(d):
        Path(d).mkdir(parents=True)

def parser():
    parser = argparse.ArgumentParser("Extract images from given rosbag.")
    parser.add_argument("--bag", type=str, help="rosbag containing calibration images", required=True)
    parser.add_argument("--output", type=str, help="output directory", default="/tmp/extracted")
    parser.add_argument("--topic", type=str, help="image topic", default="/front_view_camera/color/image_raw")
    parser.add_argument("--prefix", type=str, help="prefix for writing images on disk", default="")

    args = parser.parse_args()

    return args

if __name__ == "__main__":
    args = parser()

    extract_bag(args.bag, args.output, args.topic, args.prefix)
