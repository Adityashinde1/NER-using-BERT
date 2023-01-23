# NER-using-BERT

## Problem statement
NER is a task in NLP that involves finding and extracting entities—meaningful information—from sentences or other material. A word or even a group of words that all refer to the same category can be considered an entity. The goal of this project is a system itself understands the meaning of a given word. e.g. "My name is Aditya." In this sentence name - Aditya singnifies a 'person'. 

## Solution proposed
BERT frequently emerges as a machine learning model whose performance we may rely on when it comes to tackling NLP issues. Its ability to learn information from a word sequence in both directions plus the fact that it has been pre-trained on more than 2,500M words make it a strong model to deploy. The first step of a NER task is to detect an entity. To make sure that our BERT model knows that an entity can be a single word or a group of words, then we need to provide information about the beginning and the ending of an entity on our training data via the so-called Inside-Outside-Beginning (IOB) tagging. After detecting an entity, the next step in a NER task is to categorize the detected entity.

## Dataset used
The dataset which has been used in this project is CoNLL-2003, which is specifically used for NER task.

## Tech stack used
1. Python 3.8
2. FastAPI
3. Deep learning
4. Natural language processing
5. BERT
6. Docker

## Infrastructure required
1. Google compute engine
2. Google cloud storage
3. Google artifact registry
4. Circle CI

## How to run?
Step 1. Cloning the repository.
```
git clone https://github.com/Deep-Learning-01/NER-using-BERT.git
```
Step 2. Create a conda environment.
```
conda create -p env python=3.8 -y
```
```
conda activate env/
```
Step 3. Install the Pytorch library with conda
```
pip3 install torch  --extra-index-url https://download.pytorch.org/whl/cpu
```
Step 4. Install the requirements
```
pip install -r requirements.txt
```
Step 5. Install Google Cloud Sdk and configure
For windows -
```
https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe
```
For Ubuntu
```
sudo apt-get install apt-transport-https ca-certificates gnupg
```
```
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
```
```
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key --keyring /usr/share/keyrings/cloud.google.gpg add -
```
```
sudo apt-get update && sudo apt-get install google-cloud-cli
```
```
gcloud init
```
Before running server application make sure your `Google Cloud Storage` bucket is available

Step 6. Run the application server
```
python app.py
```
Step 7. Train application
```
http://localhost:8080/train
```
Step 8. Prediction application
```
http://localhost:8080/predict
```

## Run locally
1. Check if the Dockerfile is available in the project directory/
2. Build the docker image
```
docker build -t ner . 
```
3. Run the docker image
```
docker run -d -p 8080:8080 ner
```
4. Once you run the docker container, run the docker in interactive mode by the following command.
```
docker exec -it <container id> bash 
```
5. Then you need to authenticate the google cloud inside your docker container
```
gcloud auth login
gcloud auth application-default login
```

## `ner` is the main package folder which contains -

**Components** : Contains all components of this Project
- DataIngestion
- DataTransformation
- ModelTrainerAndEval
- ModelEvaluation
- ModelPusher

**Custom Logger and Exceptions** are used in the Project for better debugging purposes.

## Conclusion
The most significant task in NLP is NER tagging. NER is used in a variety of ways. From a given text, NER can be used to extract important information.
