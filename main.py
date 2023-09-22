import argparse
import tensorflow as tf

def convmodel(n,classes):
	builder = []
	for i in range(n):
		builder.append(tf.keras.layers.Conv2D(32,3,padding='SAME',strides=1))
		builder.append(tf.keras.layers.MaxPool2D(pool_size=2))
		builder.append(tf.keras.layers.BatchNormalization())
	builder.append(tf.keras.layers.GlobalAveragePooling2D())
	builder.append(tf.keras.layers.Dense(1024))
	builder.append(tf.keras.layers.Dense(classes))
	return tf.keras.Sequential(builder)

def main(args):
	model = convmodel(args.n,args.classes)
	model.build(input_shape=(None,224,224,3))
	model.summary()
	# print(args.n)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Create a plain neural network model')
	parser.add_argument('-inputsize', default=224,type=int,
	                    help='Number of layers of the model')
	parser.add_argument('-n', default=5,type=int,
	                    help='Number of layers of the model')
	parser.add_argument('-classes', default=10,type=int,
	                    help='Number of classes in the model')

	args = parser.parse_args()
	if args.n > 7:
		raise argparse.ArgumentTypeError("Residual module is needed. Currently not supported!.")
	# print(args.accumulate(args.integers))
	main(args)