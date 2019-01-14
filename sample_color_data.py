import cv2
import os
import numpy as np
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go
from random import randint

device = "iPad"
image_path = "./" + device +"_image/"
title = device + " color consistency"
random_color = False

choose_img_path = image_path
count = 0

pixel_list = []

for filename in os.listdir(choose_img_path):
    if filename.endswith('jpg') or filename.endswith('JPG'):
        img = cv2.imread(choose_img_path + filename)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        print(filename)
        #print("shape 0", img.shape[0])
        #print("shape 1", img.shape[1])

        with open(device + "_coord.txt") as coord_file:
            for line in coord_file:
                num, j, i = line.split(",")
                j = int(j)
                i = int(i)
                sum_r, sum_g, sum_b = 0, 0, 0
                for m in range(j, j + 6):
                    for n in range(i, i + 6):
                        r = img[n][m][0]
                        g = img[n][m][1]
                        b = img[n][m][2]
                        sum_r += r
                        sum_g += g
                        sum_b += b
                r_bar = int(round(sum_r / float(36)))
                g_bar = int(round(sum_g / float(36)))
                b_bar = int(round(sum_b / float(36)))
                pixel_list.append([r_bar, g_bar, b_bar])
        count += 1

#print(pixel_list)
print("Pixel List", len(pixel_list))
print(count)

pixel_list = np.asarray(pixel_list)
print(pixel_list.shape)

r = []
g = []
b = []
for item in pixel_list:
    r.append(item[0])
    g.append(item[1])
    b.append(item[2])


if random_color:
    for i in range(count):
        colors.append('#%06X' % randint(0, 0xFFFFFF))
else:
    colors = [
        "rgb(115, 82, 69)",
        "rgb(204, 161, 141)",
        "rgb(101, 134, 179)",
        "rgb(89, 109, 61)",
        "rgb(141, 137, 194)",
        "rgb(132, 228, 208)",
        "rgb(249, 118, 35)",
        "rgb(80, 91, 182)",
        "rgb(222, 91, 125)",
        "rgb(91, 63, 123)",
        "rgb(173, 232, 91)",
        "rgb(255, 164, 26)",
        "rgb(44, 56, 142)",
        "rgb(74, 148, 81)",  
        "rgb(179, 42, 50)",
        "rgb(250, 226, 21)",
        "rgb(191, 81, 160)",
        "rgb(6, 142, 172)",
        "rgb(252, 252, 252)",
        "rgb(230, 230, 230)",
        "rgb(200, 200, 200)",
        "rgb(143, 143, 142)",
        "rgb(100, 100, 100)",
        "rgb(50, 50, 50)",
    ]

colors *= 30
print("Color List", len(colors))

trace = go.Scatter3d(
    x=r, y=g, z=b,
    mode='markers',
    marker=dict(
        size=4,
        color=colors
    )
)

layout = go.Layout(
    width=800,
    height=700,
    title=title,
    scene=dict(
        xaxis=dict(
            range = [0, 256],
            title='R',
            titlefont=dict(
                size=14,
                color='#ff0000'
            ),
            gridcolor='rgb(0, 0, 0)',
            zerolinecolor='rgb(0, 0, 0)',
            showbackground=True,
            backgroundcolor='rgb(200, 200, 230)'
        ),
        yaxis=dict(
            range = [0, 256],
            title='G',
            titlefont=dict(
                size=14,
                color='#00ff00'
            ),
            gridcolor='rgb(0, 0, 0)',
            zerolinecolor='rgb(0, 0, 0)',
            showbackground=True,
            backgroundcolor='rgb(200, 200, 230)'
        ),
        zaxis=dict(
            range = [0, 256],
            title='B',
            titlefont=dict(
                size=14,
                color='#0000ff'
            ),
            gridcolor='rgb(0, 0, 0)',
            zerolinecolor='rgb(0, 0, 0)',
            showbackground=True,
            backgroundcolor='rgb(200, 200, 230)'
        ),
    )
)

filename = device + "_color_consistency_graph"
data = [trace]
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename=filename)
