import matplotlib.pyplot as plt
from PIL import Image

def show_imgs(images, columns, rows, figsize=50):
    fig=plt.figure(figsize=(figsize, figsize))
    for i in range(1, columns*rows +1):
        img = images[i-1][0]
        imname = images[i-1][1]
        sp = fig.add_subplot(rows, columns, i)
        fig.tight_layout()
        sp.set_title(imname, fontsize=60)
        sp.set_axis_off()
        plt.imshow(img)
    plt.show()
    
    
def show_style_layers():    
    images = []
    for i in range(1, 6):
        imname = 'r%s1' % i
        imfile = 'images/experiments/output/temp16/style_%s.png' % imname
        imtuple = (Image.open(imfile), imname)
        images.append(imtuple)
    show_imgs(images, 5, 1)    
    
    
def show_style_layers_cumulative():
    images = []
    for i in range(1, 6):
        imlabel = 'r%s1 cumulative' % i
        imfile = 'images/experiments/output/temp16/style_r%s1_cumulative.png' % i
        imtuple = (Image.open(imfile), imlabel)
        images.append(imtuple)    
    show_imgs(images, 5, 1)        
    


def show_pairs(source_dir):
    div = 20
    fig = plt.figure(figsize=(60, 60))
    r_im = Image.open('%s/render.png' % source_dir)
    x, y = r_im.size
    size = max(256, x, y)
    new_im = Image.new('RGBA', (x+y+div, y), (255,255,255,255))
    new_im.paste(r_im)
    s_im = Image.open('%s/style.png' % source_dir)
    s_im = s_im.resize((y, y))
    new_im.paste(s_im, (x+div, 0))
    render = fig.add_subplot(1, 2, 1)
    render.imshow(new_im)
    render.set_axis_off()
    plt.show()
        