import cv2
import dlib
import os
import boto3
import botocore
import urllib
import numpy as np
import json
from botocore.client import Config
import s3transfer
from subprocess import call



def lambda_handler(event, context):

	print "OpenCV version=", cv2.__version__
	print "dlib version=", dlib.__version__
	print "json version=", json.__version__
	print "np version=", np.__version__

	return "yay, it works!"
	
	

if __name__ == "__main__":
	lambda_handler(42, 42)
