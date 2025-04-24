import numpy as np
import matplotlib.pyplot as plt

x0 = (-2.0, 1.0)
y0 = (-1.5, 1.5)

def mandelbrot(cx, cy, n, m):
    x = 0.0
    y = 0.0
    iteration = 0
    while (x**2 + y**2 <= m**2 and iteration < n):
        xtemp = x**2 - y**2 + cx
        y = 2*x*y + cy
        x = xtemp
        iteration += 1
    return iteration

def mandelbrot_set(x0, y0, width, height, n, m):
    x = np.linspace(x0[0], x0[1], width)
    y = np.linspace(y0[0], y0[1], height)
    Z = np.zeros((height, width))

    for i in range(width):
        for j in range(height):
            cx = x[i]
            cy = y[j]
            Z[j, i] = mandelbrot(cx, cy, n, m)

    return Z

def plot_mandelbrot(Z, x0, y0):
    plt.imshow(Z, extent=(x0[0], x0[1], y0[0], y0[1]), cmap='hot')
    plt.colorbar()
    plt.title("Mandelbrot")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

def interactive_zoom(x0, y0, width, height, n, m):
    fig, ax = plt.subplots()
    Z = mandelbrot_set(x0, y0, width, height, n, m)
    img = ax.imshow(Z, extent=(x0[0], x0[1], y0[0], y0[1]), cmap='hot')
    plt.colorbar(img)

    def on_click(event, x0=x0, y0=y0):
        if event.button == 1:  # Levé tlačítko myši
            zoom_factor = 0.1  # Faktor přiblížení
            x_range = x0[1] - x0[0]
            y_range = y0[1] - y0[0]
            x_center = event.xdata
            y_center = event.ydata

            # Aktualizace rozsahu
            x0_new = (x_center - x_range * zoom_factor / 2, x_center + x_range * zoom_factor / 2)
            y0_new = (y_center - y_range * zoom_factor / 2, y_center + y_range * zoom_factor / 2)

            # Přepočet Mandelbrotovy množiny
            Z_new = mandelbrot_set(x0_new, y0_new, width, height, n, m)
            img.set_data(Z_new)
            img.set_extent((x0_new[0], x0_new[1], y0_new[0], y0_new[1]))
            fig.canvas.draw()

            x0, y0 = x0_new, y0_new

    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()

if __name__ == "__main__":
    width, height = 300, 300
    
    x = 0.0
    y = 0.0
    n = 50
    m = 2

    interactive_zoom(x0, y0, width, height, n, m)

