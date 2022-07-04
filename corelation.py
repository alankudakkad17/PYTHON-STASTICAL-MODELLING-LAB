import numpy as np
hand=[17,15,19,17,21]
height=[150,154,169,172,175]
np.corrcoef(hand,height)
from scipy.stats.stats import pearsonr
pearsonr(hand,height)
