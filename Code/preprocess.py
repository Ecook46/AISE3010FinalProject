<<<<<<< HEAD

=======
import load_data
# return DataSet class
data = load_data.read_data_sets(one_hot=True)

BATCH_SIZE = 32

# get train data and labels by batch size
train_x, train_label = data.train.next_batch(BATCH_SIZE)

# get test data
test_x = data.test.data

# get test labels
test_labels = data.test.labels

# get sample number
n_samples = data.train.num_examples
>>>>>>> 1b0c4ae (Create preprocess.py)
