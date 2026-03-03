
def gradient_descent(age, affordability,y_true, epochs,loss_function):
    w1=w2=1
    bias = 0
    learnin_rate = 1
    n = len(age)
    for i in range(epochs):
        weighted_sum = w1* age+affordability*w2 + bias
        y_predicted = weighted_sum - 