from PIL import Image, ImageOps
import numpy as np
import glob

def get_template(template_path):
    image = Image.open(template_path)
    return image

def remove_hue_and_desaturate(image, target_mean=155, target_range=10):
    gray_image = ImageOps.grayscale(image)
    grey = np.array(gray_image)
    rgba = np.expand_dims(grey, -1)
    rgba = np.tile(rgba, [1,1,4])
    rgba[...,-1:] = np.where(rgba[...,-1:] > 0, 255, 0)
    
    sel = grey[grey>0].astype(float)
    
    # scaling and offset
    grey2 = grey.astype(float)
    grey2 -= np.mean(sel)
    grey2 = np.where(grey2>-np.mean(sel), grey2/(np.std(sel)+.1)*target_range, grey2)
    grey2 += np.mean(sel)
    grey2 = np.where(grey2>0, grey2+target_mean-np.mean(sel), grey2)
    
    sel = grey2[grey2>0].astype(float)
        
    rgba = np.expand_dims(grey2.astype(np.uint8), -1)
    rgba = np.tile(rgba, [1,1,4])
    rgba[...,-1:] = np.where(rgba[...,-1:] > 0, 255, 0)
    
    return Image.fromarray(rgba)

def apply_to_folder(func, folder_in, folder_out):
    template_paths = glob.glob(folder_in + '*')
    
    for template_path in template_paths:
        image = get_template(template_path)
        processed_image = func(image)
        
        output_path = folder_out + template_path.split('/')[-1]
        processed_image.save(output_path)
