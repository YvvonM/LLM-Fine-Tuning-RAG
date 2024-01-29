# Define the Docker image name and version
DOCKER_IMAGE_NAME := my-llm-fine-tune
DOCKER_IMAGE_VERSION := latest

# Define the paths to model checkpoint and configuration
TF_CHECKPOINT_PATH := /path/to/tf_checkpoint
CONFIG_JSON_PATH := /path/to/config.json

# Build the Docker image
build:
	docker build -t $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_VERSION) .

# Run the Docker container for fine-tuning
run:
	docker run -it --rm \
		-v $(TF_CHECKPOINT_PATH):/app/tf_checkpoint \
		-v $(CONFIG_JSON_PATH):/app/config.json \
		$(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_VERSION)

# Push the Docker image to a container registry (replace <your-registry> with the actual registry)
push:
	docker tag $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_VERSION) <your-registry>/$(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_VERSION)
	docker push <your-registry>/$(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_VERSION)

# Remove the local Docker image
clean:
	docker rmi $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_VERSION)



# Define Variables
.PHONY: rag
rag:
    cd RAG && streamlit run rag.py
