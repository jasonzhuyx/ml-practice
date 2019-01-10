"""

"""
import os
import matplotlib.pyplot as plt


from ml.classifier.mathEx import *
from ml.classifier.utils import \
    load_data, \
    saved_parameters, \
    print_pypath


# GRADED FUNCTION: L_layer_model
def L_layer_model(
    X, Y, layers_dims,
    learning_rate=0.0075, num_iterations=2000,
    print_cost=False):  # lr was 0.009
    """

    @param X:
    @param Y:
    @param layers_dims:
    @param learning_rate:
    @param num_iterations:
    @param print_cost:
    @return:
    """

    np.random.seed(1)
    costs = []  # keep track of cost

    parameters = initialize_parameters_deep(layers_dims)

    for i in range(0, num_iterations):

        # Forward propagation: [LINEAR -> RELU]*(L-1) -> LINEAR -> SIGMOID.
        AL, caches = L_model_forward(X, parameters)

        # Compute costs
        cost = compute_cost(AL, Y)

        # Backward propagation.
        grads = L_model_backward(AL, Y, caches)

        # Update parameters.
        parameters = update_parameters(parameters, grads, learning_rate)

        # Print the cost every 100 training example
        if print_cost and i % 100 == 0:
            print("Cost after iteration %i: %f" % (i, cost))
        if print_cost and i % 100 == 0:
            costs.append(cost)

    # plot the cost
    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per tens)')
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()

    return parameters


def run():
    """
    """
    np.random.seed(1)
    print('Start training ...')

    train_x_orig, train_y, test_x_orig, test_y, classes = load_data()
    m_train = train_x_orig.shape[0]
    num_px = train_x_orig.shape[1]
    m_test = test_x_orig.shape[0]
    # Reshape the training and test examples
    train_x_flatten = train_x_orig.reshape(train_x_orig.shape[0], -1).T
    test_x_flatten = test_x_orig.reshape(test_x_orig.shape[0], -1).T

    # Standardize data to have feature values between 0 and 1.
    train_x = train_x_flatten/255.
    test_x = test_x_flatten/255.

    # CONSTANTS #
    layers_dims = [12288, 20, 7, 5, 1]  # 4-layer model

    parameters = L_layer_model(
        train_x, train_y, layers_dims, num_iterations=3000, print_cost=True)
    # print(type(parameters))
    saved_parameters(parameters)


if __name__ == '__main__':
    print_pypath()
    run()
