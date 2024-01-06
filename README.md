# Docker Page Layout

This repository contains a Dockerized page layout detection application. It uses a Docker container to ensure consistent and reproducible execution environments. Follow the steps below to build and run the application.

## Prerequisites

1. **Clone the repository locally:**

    ```bash
    git clone https://github.com/iitb-research-code/docker-page-layout.git
    ```

## Build Docker Image

2. **Build the Docker image:**

    ```bash
    docker build -t layout_detection_final .
    ```

## Run the Application

3. **Execute the Docker container with the page layout detection application.** Replace `(your_image_name)` under the results directory with the name of the image you want to process. For example:

    ```bash
    docker run -v $(pwd):/app layout_detection_final python inference.py (your_image_name)
    ```

    Example:

    ```bash
    docker run -v $(pwd):/app layout_detection_final python inference.py eqn_test.png
    ```

## Results

The application will store the layout detection output under the `results` directory with a JSON file named `image_name.json`, where `image_name` is the name of the input image. The JSON file will contain bounding boxes of the layouts detected from the input image.
