import os

import dataset

connection = dataset.connect(os.environ["DATABASE_URL"])

def connect():
	return dataset.connect(os.environ["DATABASE_URL"])