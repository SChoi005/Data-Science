from tensorflow.keras.datasets import fashion_mnist
from imageio import imwrite

(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()

for i in range(5):
	imwrite("uploads/{}.png".format(i), X_test[i])
	
