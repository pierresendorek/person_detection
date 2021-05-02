# person_detection
Detection of persons in videos. 

This code is a wrapper around the *mask_rcnn inception resnet v2 1024x1024* model from tf hub.
Preferably run the code on a computer with a GPU.
In order to install this project :


```
# bash
git clone https://github.com/pierresendorek/person_detection.git
cd person_detection
python3 -m venv ./venv/
source ./venv/bin/activate
pip install -r requirements.txt
```

Then, launch the program with :

```
# bash
python3 main.py --input-file /path/to/MISS\ DIOR\ –\ The\ new\ Eau\ de\ Parfum.mp4 --output-folder /path/to/output/folder
```

Once launched, the output folder will contain 
* a folder `frames` in which the rendered frames will be written 
* a video with the same name than the input video, where the persons are surrounded by a white rectangle.

Since the process is long, we invite the user to look in the folder `frames`.