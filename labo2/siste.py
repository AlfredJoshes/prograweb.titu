import control as ctrl
import matplotlib.pyplot as plt

# Definición de una función de transferencia de segundo orden
# G(s) = wn^2 / (s^2 + 2*zeta*wn*s + wn^2)
wn = 5.0   # frecuencia natural
zeta = 0.4 # factor de amortiguamiento

num = [wn**2]
den = [1, 2*zeta*wn, wn**2]
G = ctrl.TransferFunction(num, den)

print("Función de transferencia G(s):")
print(G)

# Respuesta al escalón
t, y = ctrl.step_response(G)

# Gráfico
plt.figure()
plt.plot(t, y)
plt.title("Respuesta al Escalón de un Sistema de Segundo Orden")
plt.xlabel("Tiempo [s]")
plt.ylabel("Amplitud")
plt.grid(True)
plt.show()