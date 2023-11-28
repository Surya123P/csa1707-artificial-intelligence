import numpy as np

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.weights_input_hidden = np.random.rand(input_size, hidden_size)
        self.bias_hidden = np.zeros((1, hidden_size))
        self.weights_hidden_output = np.random.rand(hidden_size, output_size)
        self.bias_output = np.zeros((1, output_size))

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)

    def forward(self, inputs):
        self.hidden_activation = self.sigmoid(np.dot(inputs, self.weights_input_hidden) + self.bias_hidden)
        self.output = self.sigmoid(np.dot(self.hidden_activation, self.weights_hidden_output) + self.bias_output)
        return self.output

    def train(self, inputs, targets, learning_rate, epochs):
        for epoch in range(epochs):
           
            self.forward(inputs)

            
            output_error = targets - self.output
            output_delta = output_error * self.sigmoid_derivative(self.output)

            hidden_error = output_delta.dot(self.weights_hidden_output.T)
            hidden_delta = hidden_error * self.sigmoid_derivative(self.hidden_activation)

            self.weights_hidden_output += self.hidden_activation.T.dot(output_delta) * learning_rate
            self.bias_output += np.sum(output_delta, axis=0, keepdims=True) * learning_rate

            self.weights_input_hidden += inputs.T.dot(hidden_delta) * learning_rate
            self.bias_hidden += np.sum(hidden_delta, axis=0, keepdims=True) * learning_rate

            if epoch % 100 == 0:
                error = np.mean(np.abs(output_error))
                print(f"Epoch {epoch}, Error: {error}")

if __name__ == "__main__":
 
    input_size = 2
    hidden_size = 4
    output_size = 1

    neural_network = NeuralNetwork(input_size, hidden_size, output_size)


    inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    targets = np.array([[0], [1], [1], [0]])

    neural_network.train(inputs, targets, learning_rate=0.1, epochs=1000)

    for i in range(len(inputs)):
        prediction = neural_network.forward(inputs[i])
        print(f"Input: {inputs[i]}, Prediction: {prediction}")
