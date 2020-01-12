import pandas as pd
import numpy as np
import DataExplore as explorer

titanic = pd.read_csv('titanic.csv')
explorer.dataframeExplor(titanic)