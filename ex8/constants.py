# -------------------------------------------------------------------------------------
#   Training constants
# -------------------------------------------------------------------------------------
MAX_STEPS = 200               # MAX STEPS PER EPISODE
ALPHA = 0.5                   # LEARNING RATE
GAMMA = 0.6                   # DISCOUNTING RATE

EPS = 1                       # EXPLORATION RATE
MAX_EPSILON = 1               # EXPLORATION PROBABILITY
MIN_EPSILON = 0.01            # MINIMUM EXPLORATION PROBABILITY
DECAY_RATE = 0.01             # Exponential decay rate for exploration prob

# -------------------------------------------------------------------------------------
#   Common constants
# -------------------------------------------------------------------------------------
TRAIN_EPISODES = 100000
TEST_EPISODES = 10

# -------------------------------------------------------------------------------------
#   Model file
# -------------------------------------------------------------------------------------
MODEL_FILE = "model.csv"