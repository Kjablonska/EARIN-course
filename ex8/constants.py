# -------------------------------------------------------------------------------------
#   Training constants
# -------------------------------------------------------------------------------------
MAX_STEPS = 100               # MAX STEPS PER EPISODE
ALPHA = 0.7                   # LEARNING RATE
GAMMA = 0.618                 # DISCOUNTING RATE

EPS = 1                       # EXPLORATION RATE
MAX_EPSILON = 1               # EXPLORATION PROBABILITY
MIN_EPSILON = 0.01            # MINIMUM EXPLORATION PROBABILITY
DECAY_RATE = 0.01             # Exponential decay rate for exploration prob

# -------------------------------------------------------------------------------------
#   Common constants
# -------------------------------------------------------------------------------------
TRAIN_EPISODES = 2000
TEST_EPISODES = 100

# -------------------------------------------------------------------------------------
#   Model file
# -------------------------------------------------------------------------------------
MODEL_FILE = "model.csv"