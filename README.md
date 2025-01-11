## Problem description
## Data
I used [Chest X-Ray Images (Pneumonia)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) for training and evaluation of the model. This dataset is available for download from Kaggle via the provided url. The dataset is also avaliable in the repository.
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
| **Model**  | **Accuracy** | **Loss** |
| -------- | -------- | ---- |
| model_1  | 0.625    | 6.136 |
| model_2  | 0.741    | 1.02 |
| model_3  | 0.647    | 2.676  |
| model_4  | 0.862    | 0.338  |
| model_5  | 0.839    | 0.447 |

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
## Deployment
