import numpy as np
import matplotlib.pyplot as plt

#zoom is done by left click and right click (left zooms in and right zooms out)

x0 = (-2.0, 1.0)
y0 = (-1.5, 1.5)

def mandelbrot(cx, cy, n, m):
    x = 0.0
    y = 0.0
    iteration = 0
    while (x**2 + y**2 <= m**2 and iteration < n): #if the point is in the set, it will not escape
        xtemp = x**2 - y**2 + cx
        y = 2*x*y + cy 
        x = xtemp 
        iteration += 1
    return iteration

def mandelbrot_set(x0, y0, width, height, n, m):
    x = np.linspace(x0[0], x0[1], width)
    y = np.linspace(y0[0], y0[1], height)
    Z = np.zeros((height, width))

    #calculate the Mandelbrot set for each point in the grid
    for i in range(width):
        for j in range(height):
            cx = x[i]
            cy = y[j]
            Z[j, i] = mandelbrot(cx, cy, n, m)

    return Z

def interactive_zoom(x0, y0, width, height, n, m):
    fig, ax = plt.subplots()
    Z = mandelbrot_set(x0, y0, width, height, n, m)
    img = ax.imshow(Z, extent=(x0[0], x0[1], y0[0], y0[1]), cmap='plasma', origin='lower')
    plt.colorbar(img)

    def on_click(event):
        nonlocal x0, y0
        if event.button == 1: #left click
            zoom_factor = 0.5
        elif event.button == 3: #right click
            zoom_factor = 2.0

        x_range = x0[1] - x0[0]
        y_range = y0[1] - y0[0]
        #coordinates of the click event
        x_center = event.xdata
        y_center = event.ydata

        x0_new = (x_center - x_range * zoom_factor / 2, x_center + x_range * zoom_factor / 2)
        y0_new = (y_center - y_range * zoom_factor / 2, y_center + y_range * zoom_factor / 2)

        #update the Mandelbrot set with the new zoomed-in area (new x0 and y0)
        Z_new = mandelbrot_set(x0_new, y0_new, width, height, n, m)
        img.set_data(Z_new)
        img.set_extent((x0_new[0], x0_new[1], y0_new[0], y0_new[1]))
        fig.canvas.draw()

        x0, y0 = x0_new, y0_new

    fig.canvas.mpl_connect('button_press_event', on_click)
    plt.show()

if __name__ == "__main__":
    width, height = 250, 250
    
    x = 0.0
    y = 0.0
    n = 50
    m = 2

    interactive_zoom(x0, y0, width, height, n, m)