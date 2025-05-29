# 📊 Calculadora de integrales dobles

Bienvenido a la **Calculadora de Volumen Bajo Superficie**, una aplicación educativa desarrollada con Python y `customtkinter`, que permite calcular el volumen encerrado entre una superficie definida por una función f(x, y) y el plano XY mediante integración doble.

---

## 🚀 ¿Qué puedes hacer con esta app?

- ✍️ Ingresar funciones matemáticas simbólicas de dos variables (f(x, y)).
- 🔢 Definir límites de integración personalizados para x e y.
- 📈 Visualizar gráficamente la superficie 3D con animación rotatoria.
- ✅ Obtener el resultado del volumen directamente en pantalla.
- 🧪 Usar funciones de prueba integradas para practicar o verificar el funcionamiento.

---

## 🧠 ¿Qué **no** puede hacer esta app (todavía)?

Si bien es potente y visualmente atractiva, la calculadora tiene algunas **limitaciones** a tener en cuenta:

❌ No admite:
- Funciones con más de dos variables (ej. f(x, y, z)).
- Condicionales o funciones por tramos (ej. `Piecewise`, `abs`, `if`).
- Entrada de límites simbólicos como `pi`, `e`, o fracciones (`1/2`) directamente — solo números decimales.
- Funciones escritas incorrectamente (ej. `sqrt x` en lugar de `sqrt(x)`).
- Control manual de la vista 3D (la animación es automática).

⚠️ Ten cuidado con:
- Fracciones mal interpretadas (ej. `1/2x` puede ser confuso, usa paréntesis: `(1/2)*x`).
- Divisiones por cero dentro del dominio de integración.

---

## 📸 Cómo usarla paso a paso

1. **Introduce una función** f(x, y) válida. Ejemplo:  6 - 2*x - y/3

2. **Especifica los límites de integración:**
- `x min`, `x max`, `y min`, `y max`.

3. (Opcional) Marca la casilla **"Mostrar gráfica 3D"** si deseas visualizar la superficie.

4. Haz clic en **"Calcular Volumen"**. El resultado aparecerá abajo, y si lo pediste, se abrirá una ventana 3D animada de la superficie.

5. También puedes pulsar los botones de funciones de prueba (con emojis 🎲) para probar la app rápidamente.

---


## 💻 Requisitos

- Python 3.8 o superior
- Bibliotecas:
- `customtkinter`
- `sympy`
- `numpy`
- `matplotlib`

Instálalas con:

```bash
pip install customtkinter sympy numpy matplotlib
```

## 📦 Cómo ejecutar la app
1. Clona este repositorio:
```bash
git clone https://github.com/isaacDiazR/Calculadora-de-integrales-dobles.git
```
2. Ve al directorio del proyecto:
```bash
cd Calculadora-de-integrales-dobles
```
3. Ejecuta el programa

---

## 📬 ¿Necesitas ayuda más personalizada?

No dudes en escribirme si tienes preguntas, sugerencias o necesitas soporte técnico: isaacdiaz1621.contacto@gmail.com

---

## 🤝 Créditos

Desarrollado con 💙 por Isaac Diaz, David Aceros, Carlos Mantilla.
