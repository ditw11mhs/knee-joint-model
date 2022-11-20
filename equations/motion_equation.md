# Motion Equation

Initial derivation of coordinates and velocity

$$
  B_w = 80 kg\\
  B_h = 175 cm = 1.75 m\\
  \ell = 0.285 \times B_h\\
  \alpha = 0.606 \times \ell \\
  I = 0.061 \times B_w \\
  x = \alpha cos\theta\\
  y = -\alpha sin\theta\\
  \dots\\
  \dot x = -\alpha \dot \theta sin \theta\\
  \dot y = -\alpha \dot \theta cos \theta\\
  \dots\\
  v = \dot x + \dot y\\
  v^2 = \dot x^2 + \dot y^2\\
  v^2 = \alpha^2 \dot \theta^2\\
$$

Energy Calculation

$$
  E_k = \frac{1}{2}mv^2 + \frac{1}{2}I\dot \theta^2\\
  E_k = \frac{1}{2}m\alpha^2 \dot \theta^2 + \frac{1}{2}I\dot \theta^2\\
  \dots\\
  E_p = mgh \\
  E_p = mg(\ell + y)\\
  E_p = \frac{1}{2}m\alpha^2 \dot \theta^2 + \frac{1}{2}I\dot \theta^2
$$

Lagrangian Calculation

$$
  L = E_k - E_p\\
  L = \frac{1}{2}m\alpha^2 \dot \theta^2 + \frac{1}{2}I\dot \theta^2 - mg(\ell - \alpha sin\theta)\\
  L = \frac{1}{2}\dot \theta^2 \left(m\alpha^2 + I\right) + mg\alpha sin\theta - mg\ell\\
$$

Lagrangian Function

$$
  \frac{d}{dt} \frac{\partial L}{\partial \dot \theta} - \frac{\partial L}{\partial \theta} = \tau\\
  \dots\\
  \frac{\partial L}{\partial \dot \theta} = (m\alpha^2 + I)\dot \theta\\
  \frac{d}{dt} \frac{\partial L}{\partial \dot \theta} = (m\alpha^2 + I)\ddot \theta\\
  \frac{\partial L}{\partial \theta} = mg\alpha cos\theta\\
  \dots\\
  (m\alpha^2 + I)\ddot \theta - mg\alpha cos\theta = \tau \\
  (m\alpha^2 + I)\ddot \theta - mg\alpha cos\theta = -c\dot \theta + k_1 e^{-k_2(\theta-\phi_1)} + k_3 e^{k_4(\theta-\phi_2)} \\
  \ddot \theta = \frac{-c\dot \theta + k_1 e^{-k_2(\theta-\phi_1)} + k_3 e^{k_4(\theta-\phi_2)} + mg\alpha cos\theta}{m\alpha^2 + I}\\

  \dots\\
  c_{knee} = 10.0\\
  k_{1 knee}=6.1\\
  k_{2 knee} = 5.9\\
  k_{3 knee} = 10.5\\
  k_{4_knee} = 21.8\\
  \phi_{1 knee} = 10^o\\
  \phi_{2 knee} = 67^o\\
$$

Runge Kutta

$$
  \ddot{\theta}= f(t,\theta,\dot{\theta})\\
  k_{1rk}=\frac{h}{2}f(t,\theta,\dot{\theta})\\
  k_{2rk}=\frac{h}{2}f\left( t+\frac{h}{2},\theta+\frac{h}{2}\left(\dot{\theta}+\frac{k_{1rk}}{2}\right),\dot{\theta}+k_{1rk}\right)\\
  k_{3rk}=\frac{h}{2}f\left( t+\frac{h}{2},\theta+\frac{h}{2}\left(\dot{\theta}+\frac{k_{1rk}}{2}\right),\dot{\theta}+k_{2rk}\right)\\
  k_{4rk}=\frac{h}{2}f\left( t+h,\theta+h\left(\dot{\theta}+k_{3rk}\right),\dot{\theta}+2k_{3rk}\right)\\
  \theta_n=\theta_{n-1}+h\left(\dot{\theta}_{n-1}+\frac{k_{1rk}+k_{2rk}+k_{3rk}}{3}\right)\\
  \dot{\theta}_n=\dot{\theta}_{n-1}+h\left(k_{1rk}+2k_{2rk}+2k_{3rk}+k_{4rk}\right)\\
$$

Objective function

$$
  \theta_x = System Output\\
  \theta_y = Model Output\\
  e = \theta_x - \theta_y\\
  J = \frac{1}{2}e^2
$$

Parameter Optimization and Gradient

$$
  \frac{\partial J}{\partial e} = e\\
  \frac{\partial e}{\partial \theta_y} = -1\\
  \dots\\
  \frac{\partial \ddot \theta}{\partial c} = \frac{-\dot \theta}{m\alpha^2 +I}\\
  \frac{\partial \theta_y}{\partial c} = \frac{h^2}{2}\left(\frac{-\dot \theta}{m\alpha^2 +I} + \frac{- \dot \theta - \frac{-\dot \theta}{m\alpha^2 +I}}{m\alpha^2 +I} + \frac{-\dot \theta - \frac{- \dot \theta - \frac{-\dot \theta}{m\alpha^2 +I}}{m\alpha^2 +I}}{m\alpha^2 +I}\right) \\
  \frac{\partial J}{\partial c} = \frac{\partial J}{\partial e}\frac{\partial e}{\partial \theta_y}\frac{\partial \theta_y}{\partial c}\\
  \dots\\

  \frac{\partial \ddot \theta}{\partial k_1} = \frac{e^{-k_2(\theta-\phi_1)}}{m\alpha^2 + I}\\
  \frac{\partial \theta_y}{\partial k_1(k_{1rk})} = \frac{e^{-k_2(\theta-\phi_1)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial k_1(k_{2rk})} = \frac{e^{-k_2(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)-\phi_1)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial k_1(k_{3rk})} = \frac{e^{-k_2(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)-\phi_1)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial k_1} = \frac{h^2}{6}\left(\frac{\partial \theta_y}{\partial k_1(k_{1rk})}+\frac{\partial \theta_y}{\partial k_1(k_{2rk})}+\frac{\partial \theta_y}{\partial k_1(k_{3rk})}\right)\\
  \frac{\partial J}{\partial k_1} = \frac{\partial J}{\partial e}\frac{\partial e}{\partial \theta_y}\frac{\partial \theta_y}{\partial k_1}\\
  \dots\\

  \frac{\partial \ddot \theta}{\partial k_2} = \frac{k_1 (\phi_1-\theta) e^{-k_2(\theta-\phi_1)}}{m\alpha^2 + I}\\
  \frac{\partial \theta_y}{\partial k_2(k_{1rk})} = \frac{k_1 (\phi_1-\theta) e^{-k_2(\theta-\phi_1)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial k_2(k_{2rk})} = \frac{k_1 (\phi_1-\left(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)\right)) e^{-k_2(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)-\phi_1)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial k_2(k_{3rk})} = \frac{k_1 (\phi_1-\left(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)\right)) e^{-k_2(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)-\phi_1)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial k_2} = \frac{h^2}{6}\left(\frac{\partial \theta_y}{\partial k_2(k_{1rk})}+\frac{\partial \theta_y}{\partial k_2(k_{2rk})}+\frac{\partial \theta_y}{\partial k_2(k_{3rk})}\right)\\
  \frac{\partial J}{\partial k_2} = \frac{\partial J}{\partial e}\frac{\partial e}{\partial \theta_y}\frac{\partial \theta_y}{\partial k_2}\\
  \dots\\

  \frac{\partial \ddot \theta}{\partial k_3} = \frac{e^{-k_4(\theta-\phi_2)}}{m\alpha^2 + I}\\
  \frac{\partial \theta_y}{\partial k_3(k_{1rk})} = \frac{e^{-k_4(\theta-\phi_2)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial k_3(k_{2rk})} = \frac{e^{-k_4(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)-\phi_2)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial k_3(k_{3rk})} = \frac{e^{-k_4(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)-\phi_2)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial k_3} = \frac{h^2}{6}\left(\frac{\partial \theta_y}{\partial k_3(k_{1rk})}+\frac{\partial \theta_y}{\partial k_3(k_{2rk})}+\frac{\partial \theta_y}{\partial k_3(k_{3rk})}\right)\\
  \frac{\partial J}{\partial k_3} = \frac{\partial J}{\partial e}\frac{\partial e}{\partial \theta_y}\frac{\partial \theta_y}{\partial k_3}\\
  \dots\\

  \frac{\partial \ddot \theta}{\partial k_4} = \frac{k_3 (\phi_2-\theta) e^{-k_4(\theta-\phi_2)}}{m\alpha^2 + I}\\
  \frac{\partial \theta_y}{\partial k_4(k_{1rk})} = \frac{k_3 (\phi_2-\theta) e^{-k_4(\theta-\phi_2)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial k_4(k_{2rk})} = \frac{k_3 (\phi_2-\left(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)\right)) e^{-k_4(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)-\phi_2)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial k_4(k_{3rk})} = \frac{k_3 (\phi_2-\left(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)\right)) e^{-k_4(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)-\phi_2)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial k_4} = \frac{h^2}{6}\left(\frac{\partial \theta_y}{\partial k_4(k_{1rk})}+\frac{\partial \theta_y}{\partial k_4(k_{2rk})}+\frac{\partial \theta_y}{\partial k_4(k_{3rk})}\right)\\
  \frac{\partial J}{\partial k_4} = \frac{\partial J}{\partial e}\frac{\partial e}{\partial \theta_y}\frac{\partial \theta_y}{\partial k_4}\\
  \dots\\

  \frac{\partial \ddot \theta}{\partial \phi_1} =  \frac{k_1 k_2 e^{-k_2(\theta-\phi_1)}}{m\alpha^2 + I}\\
  \frac{\partial \theta_y}{\partial \phi_1(k_{1rk})} = \frac{k_1 k_2 e^{-k_2(\theta-\phi_1)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial \phi_1(k_{2rk})} = \frac{k_1 k_2 e^{-k_4(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)-\phi_2)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial \phi_1(k_{3rk})} = \frac{k_1 k_2 e^{-k_4(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)-\phi_2)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial \phi_1} = \frac{h^2}{6}\left(\frac{\partial \theta_y}{\partial \phi_1(k_{1rk})}+\frac{\partial \theta_y}{\partial \phi_1(k_{2rk})}+\frac{\partial \theta_y}{\partial \phi_1(k_{3rk})}\right)\\
  \frac{\partial J}{\partial \phi_1} = \frac{\partial J}{\partial e}\frac{\partial e}{\partial \theta_y}\frac{\partial \theta_y}{\partial \phi_1}\\
  \dots\\

  \frac{\partial \ddot \theta}{\partial \phi_2} =  \frac{k_3 k_4 e^{-k_4(\theta-\phi_2)}}{m\alpha^2 + I}\\
  \frac{\partial \theta_y}{\partial \phi_2(k_{1rk})} = \frac{k_3 k_4 e^{-k_4(\theta-\phi_2)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial \phi_2(k_{2rk})} = \frac{k_3 k_4 e^{-k_4(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)-\phi_2)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial \phi_2(k_{3rk})} = \frac{k_3 k_4 e^{-k_4(\theta+\frac{h}{2}\left(\dot{\theta}+\frac{\frac{\partial \theta_y}{\partial k_{1rk}}}{2}\right)-\phi_2)}}{m\alpha^2 + I} \\
  \frac{\partial \theta_y}{\partial \phi_2} = \frac{h^2}{6}\left(\frac{\partial \theta_y}{\partial \phi_2(k_{1rk})}+\frac{\partial \theta_y}{\partial \phi_2(k_{2rk})}+\frac{\partial \theta_y}{\partial \phi_2(k_{3rk})}\right)\\
  \frac{\partial J}{\partial \phi_2} = \frac{\partial J}{\partial e}\frac{\partial e}{\partial \theta_y}\frac{\partial \theta_y}{\partial \phi_2}\\
  \dots\\

  k = Iteration\\
  \tau = Learning_{Coefficient}\\
  \mu(k) = \frac{\mu_o}{1+\frac{k}{\tau}} \\
  c = c_{n-1} - \mu\frac{\partial J}{\partial c}\\
  k_1 = k_{1({n-1})} - \mu\frac{\partial J}{\partial k_1}\\
  k_2 = k_{2({n-1})} - \mu\frac{\partial J}{\partial k_2}\\
  k_3 = k_{3({n-1})} - \mu\frac{\partial J}{\partial k_3}\\
  k_4 = k_{4({n-1})} - \mu\frac{\partial J}{\partial k_4}\\
  \phi_1 = \phi_{1({n-1})} - \mu\frac{\partial J}{\partial \phi_1}\\
  \phi_2 = \phi_{2({n-1})} - \mu\frac{\partial J}{\partial \phi_2}\\
$$
