## Problem description
It takes years for doctors to achieve the necessary degree of qualifications so as to become competent to diagnose illnesses, sich as pneumonia. Moreover, patients often have difficulties with making an appointment with a doctor due to long waiting lists and high fees of health caring services.

For this reason, the tool for preliminary diagnosis needs to be developed. This way patients will be able to get relevant insights on their health state before deciding whether to make an appointment with a doctor or not. In addition to this, such tool will also optimize the doctors workloads enabling them to concentrate on curing illnesses, not diagnosing them.

I concentrated my efforts on building a neural network for diagnosing pneumonia besed on X-Ray images.

## Data
I used [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) dataset for training and evaluation of the model. This dataset is available for download from Kaggle via the provided url. The dataset is also avaliable in the repository.
### Data description
The dataset is split into three folders: train, val, test. Each of these folders contains images of healthy lungs and images of lungs affected by bacterial or viral pneumonia. Each folder is divided into two subdirectories: normal and pneumonia.

The train directory includes:
- 1341 images of normal lungs
- 3875 images of lungs affected by pneumonia

The val directory includes:
- 8 images of normal lungs
- 8 images of lungs affected by pneumonia

The test directory includes:
- 234 images of normal lungs
- 390 images of lungs affected by pneumonia

## Models
So as to find the most effective model for the problem statement five models were trained. Each model was trained on the dataset described above and augmented data from the same dataset.

### model_1
The first model was trained with no pre-trained weights with a single convolutional layer.

### model_2
The architecture of the second model includes three convolutional layers and a dropout layer. This model was also trained without pretrained weights.

### model_3
For the third model a batch normalization layer was added after the first convolutional layer in addition to second model's architecture. No pre-trained weights were used.

### model_4
The forth model utilized imagenet weights with one global average pooling layer and one dense layer.

### model_5
The fifth model also imagenet weights and second dense layer along with a dropout layer were added to the architecture of the forth model.

### Evaluation results

| **Model**  | **Accuracy** | **Loss** |
| -------- | -------- | ---- |
| model_1  | 0.625    | 6.136 |
| model_2  | 0.741    | 1.02 |
| model_3  | 0.647    | 2.676  |
| model_4  | 0.862    | 0.338  |
| model_5  | 0.839    | 0.447 |

Considering the final evaluation of each model, the **model_4** has shown the highest accuracy and the lowest loss, which makes it the best performing model

## Dependencies installation
Firstly, install pipenv using the following command:
```bash
pip install pipenv
```
If you want to install all the dependencies, run:
```bash
pipenv install
```
If you want to install only the production dependencies, run:
```bash
pipenv install --ignore-pipfile --deploy
```

## Run project locally
So as to run the project locally, first clone the code from the repository to your local machine:
```bash
git clone https://github.com/KatePril/pneumonia-prediction.git
```
Navigate to the project directory with a following command:
```bash
cd pneumonia-prediction
```
Build the docker image:
```bash
docker build -t <image-name> .
```
Run the image:
```bash
docker run -it --rm -p 8080:8080 <image-name>:latest
```

If you want to test the application using the provided test code, you can use the following command to run the code from the terminal:
```bash
python test.py
```
You can raplace the url with an url of your image

## Deployment
So as to deploy the container to the cloud, you need to create AWS account, [install AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and log in to AWS CLI using the following command:
```bash
aws configure
```
If you haven't built the docker image yet, run the following command:
```bash
docker build -t <image-name> .
```
Then push the image to Elastic Container Registry with the following commands:
```bash
aws ecr create-repository --repository-name <repository-name> --region <your-region>
```
```bash
docker tag <image-name> <your-aws-account-id>.dkr.ecr.<your-region>.amazonaws.com/<repository-name>
```
```bash
aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-aws-account-id>.dkr.ecr.<your-region>.amazonaws.com
```
```bash
docker push <your-aws-account-id>.dkr.ecr.<your-region>.amazonaws.com/<repository-name>
```
Verify the successful creation of container creation in [AWS Console](https://signin.aws.amazon.com/signup?request_type=register) in Elastic Container Registry.
Navigate to Lambda service, click **Create function**, select **Container image**, enter the function name. Then, select the repository you pushed the image to and select the image. you can leave the rest of the settings as default.
 
![image](https://github.com/user-attachments/assets/027c205b-71ca-4f04-81b1-0daea3c1b7a2)
Wait for a couple of moments for function to be created.

### Deployment demonstration

https://github.com/user-attachments/assets/fdbb0921-c83a-48fc-a901-dbb58ad513aa

