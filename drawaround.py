import tkinter as tk
import math

class WaterRipple:
    def __init__(self, canvas, x , y , max_radius =2000, colors = None):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.radius = 10  #波紋變化
        self.max_radius = max_radius
        self.colors = colors if colors else ["#ff4e4e","#ffff62","#ff0066","#00CCFF"]  #波紋顏色
        self.ripple = None
        self.active = True
        self.amplitude = 10.0  #從中心點擴散開的數值
        self.wavelength = 500  #數值越大越圓滑  越小越尖銳
        self.animate()

    def get_wave_height(self, distance, time):
         k = 2 * math.pi / self.wavelength
         omega = 0.2
         decay = math.exp(-distance/1000)
         return self.amplitude * math.sin(k * distance - omega * time) * decay
    
    def animate(self):
        if self.radius < self.max_radius:
            self.radius += 1 #數值越大 波紋擴散越快 在畫面消失的越快
            self.update_wave()
            self.canvas.after(5, self.animate)  #動作速度 數值越大動的越慢
        else:
            self.active = False
            if self.ripple:
                self.canvas.delete(self.ripple)

    def update_wave(self):
        if self.ripple:
            self.canvas.delete(self.ripple)

        other_waves =[wave for wave in self.canvas.get_waves() if wave != self]

        num_points = 1000
        points =[]

        for i in range(num_points+1):
            angle =2 * math.pi * i / num_points
            base_x = self.x +self.radius * math.cos(angle)
            base_y = self.y +self.radius * math.sin(angle)

            total_height = self.get_wave_height(self.radius, self.radius)
        
            for other in other_waves:
                dx = base_x - other.x
                dy = base_y - other.y
                distance = math.sqrt(dx*dx + dy*dy)
                total_height += other.get_wave_height(distance, other.radius)

            scale = 10
            x = self.x + (self.radius + total_height * scale) * math.cos(angle)
            y = self.y + (self.radius + total_height * scale) * math.sin(angle)
            points.append(x)
            points.append(y)


        if points:
            width = 2
            color_index = (self.radius // 50) % len(self.colors)
            self.ripple = self.canvas.create_polygon(
                points,
                fill = "",
                outline = self.colors[color_index],
                width = width,
                smooth = True

            )

class RippleCanvas(tk.Canvas):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.ripples =[]
        self.bind("<Button-1>", self.create_ripple)
        self.update_canvas()

    def get_waves(self):
        return self.ripples
    
    def create_ripple(self,event):
        ripple = WaterRipple(self, event.x, event.y)
        self.ripples.append(ripple)

    def update_canvas(self):
        self.ripples = [ripple for ripple in self.ripples if ripple.active]
        self.after(30, self.update_canvas)


root =tk.Tk()
root.title("random wave")
root.geometry("800x600")

canvas = RippleCanvas(root, bg ="#000033", width=800, height=600)
canvas.pack(fill = "both", expand=True)

root.mainloop()


