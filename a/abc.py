import datetime
import json
import os
import re
import shutil
import traceback
import warnings
# from memory_profiler import profile
from collections import Counter

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests
import web
from sklearn import metrics
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.ensemble import IsolationForest
from sklearn.metrics import silhouette_samples, silhouette_score

# !111

warnings.filterwarnings("ignore")

urls = (
    "/ai/v1/load_time_elasticity", "load_time_elasticity"
)

app = web.application(urls, globals())
#_author:"zqs"
#date:2023/11/7