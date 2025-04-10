import random
import matplotlib.pyplot as plt

class IFS:
    def __init__(self, iterations, model, point = [0,0,0]):
        self.point = point
        self.iterations = iterations
        self.points = [point] #historie bodu pro vizualizaci
        self.model = model
    
    def transform(self):
        #pro kazdou iteraci vybere nahodne jednu z 4 transformaci a aplikuje ji na aktualni bod
        for _ in range(self.iterations):
            trasformation = random.randint(0, 3) #jedna ze 4 transformaci se stejnou pravdepodobnosti 0.25
            a, b, c = self.model[trasformation]["a"], self.model[trasformation]["b"], self.model[trasformation]["c"]
            d, e, f = self.model[trasformation]["d"], self.model[trasformation]["e"], self.model[trasformation]["f"]
            g, h, i = self.model[trasformation]["g"], self.model[trasformation]["h"], self.model[trasformation]["i"]
            j, k, l = self.model[trasformation]["j"], self.model[trasformation]["k"], self.model[trasformation]["l"] 

            new_point = [0, 0, 0]

            #transformace bodu podle vybrane transformace
            new_point[0] = a*self.point[0] + b*self.point[1] + c*self.point[2] + j
            new_point[1] = d*self.point[0] + e*self.point[1] + f*self.point[2] + k
            new_point[2] = g*self.point[0] + h*self.point[1] + i*self.point[2] + l

            self.point = new_point

            #pridani noveho bodu do seznamu bodu
            self.points.append(new_point)
            print(self.point)

    def vizualize(self):
        x = [point[0] for point in self.points]
        y = [point[1] for point in self.points]
        z = [point[2] for point in self.points]

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        ax.scatter(x, y, z, c='black', marker='o')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        plt.show()

    
