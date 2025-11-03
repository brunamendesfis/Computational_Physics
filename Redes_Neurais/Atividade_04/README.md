## Physics Informed Neural Networks (PINNs)

This notebook uses PINN to extrapolate the analytical solution for the cooling of a coffee mug by comparing four different approaches: analytical solution, numerical method, traditional Neural Network (NN) and Physics-Informed Neural Networks (PINNs). The last one is a hybrid approach that integrates the underlying physics equation directly into the loss function.

The goal is to showcase the power and flexibility of PINNs, especially their ability to discover unknown physical parameters and handle extrapolation better than purely data-driven models.

The Physics Problem: Newton's Law of Cooling

The project models the temperature ($T$) of an object over time ($t$) using the ODE:

$$\frac{dT}{dt} = r \cdot (T_{amb} - T)$$Where:$T_{amb}$

is the ambient temperature, $r$ is the cooling rate (the unknown parameter to be discovered).

# The notebook features three core machine learning implementations:

Traditional Neural Network (NN): Purely supervised learning, trained on synthetic temperature data with added noise. I used 4 fully connected layers with the ReLU activation function and the Mean Squared Error (MSE), to compare the predicted temperature to the noisy data. This setup serves as a baseline to see how a standard NN learns a physical curve without explicit physics guidance. For the Physics-Informed Neural Network (PINN) with r known, I combined a Data Loss (MSE vs. synthetic data) and a Physics Loss (MSE of the ODE residual). TensorFlow's automatic differentiation (tf.GradientTape) was also used to calculate $\frac{dT}{dt}$ and ensure the prediction satisfies the ODE:

$\left(\frac{dT}{dt} - r \cdot (T_{amb} - T)\right)^2 \approx 0$.

This work demonstrates how adding the ODE constraint forces the model to respect the physical laws, potentially improving generalization. For PINN with r unkown, I used the cooling rate $r$ as a trainable variable (a parameter layer) within the network. The combined loss function guides the network to learn both the function $T(t)$ and the parameter $r$ that best satisfies the data and the ODE. The model successfully converges on a value for $r$ very close to the true parameter value (expected $r=0.005$).

The PINN models, particularly the one solving the inverse problem (discovering $r$), showcased superior performance. By baking the physics into the training, the network was able to accurately model the temperature decay while simultaneously identifying the underlying cooling rate, validating the power of PINNs in solving complex, real-world computational physics problems.

