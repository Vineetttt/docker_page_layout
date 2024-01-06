FROM python:3.9.6

WORKDIR /model 

RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx

# Copy both requirements files into the container
ADD sh_requirements.txt .
ADD requirements.txt .
COPY classes /model/classes

# Install PyTorch (Adjust the version as needed)
RUN pip install torch==2.0.1 torchaudio==2.0.2 torchvision==0.15.2 

# Run commands to install dependencies
RUN pip install --no-cache-dir -r sh_requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install Pillow==9.3.0

# Run commands to load the models in the docker image
RUN python -c "from classes.tables import create_model; create_model(num_classes=3) "
RUN python -c "from classes.equations import load_equation_model; load_equation_model()"
RUN python -c "from classes.figures import load_figure_model; load_figure_model()"

# Copy the rest of the application code into the container
COPY . .

CMD ["python", "inference.py"]