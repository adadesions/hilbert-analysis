import matplotlib.pyplot as plt


def grid_plot(data, size, title='Untitle', is_img=False):
    fig = plt.figure()
    fig.canvas.set_window_title(title)
    length = size**2
    iter_data = data if is_img else data.values()
    graphs = []

    for i in range(1, length+1):
        temp_plt = fig.add_subplot(''.join([str(size)*2, str(i)]))
        graphs.append(temp_plt)

    for i, d in enumerate(iter_data):
        if is_img:
            graphs[i].imshow(d, cmap=plt.cm.gray)
        else:
            graphs[i].plot(d)
