import utils.data_utils as data_utils
import utils.model_utils as model_utils
import os

print "Loading data ..."
X_train, Y_train = data_utils.load_data(domain='freq')
print "Data loaded"

in_neurons = X_train.shape[-1]
out_neurons = Y_train.shape[-1]

model = model_utils.create_network(in_neurons, out_neurons)

print "Training ..."
iterations = 100
epochs_per_iteration = 5
batch_size = 1000

for iteration in range(iterations):
	print "Iteration Number: " + str(iteration)
	model.fit(X_train, Y_train, batch_size=batch_size, nb_epoch=epochs_per_iteration)  
	fname = os.path.join('models','trained_model_' + str(iteration) + '.hdf5')
	model.save_weights(fname)

print "Training complete"

