import os , sys
from PIL import Image

input_dir = sys.argv[1]         #takes the input directory argument
output_dir = sys.argv[2]        #takes the directory in which output to be saved

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for files in os.listdir(input_dir):
    img=Image.open(f'{input_dir}{files}')
    clean_name= os.path.splitext(files)[0]
    img.save(f'{output_dir}{clean_name}.png','png')
    print('all done')



