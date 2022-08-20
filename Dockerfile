FROM tensorflow/tensorflow:latest 
RUN pip install opencv-python-headless
RUN pip install numpy
RUN pip install matplotlib
RUN pip install keras
WORKDIR /usr/src/app
COPY  . .
CMD [ "python","retina-deployment.py" ]
