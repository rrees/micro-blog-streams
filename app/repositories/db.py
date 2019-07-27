import os

import dataset

connection = dataset.connect(os.environ["DATABASE_URL"])
