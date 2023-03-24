# Hard Hat Detection Dataset to YOLOv5 Format
This repo takes [this dataset](https://www.kaggle.com/datasets/andrewmvd/hard-hat-detection?resource=download) and changes it to a format that can be used with the [YOLOv5](https://github.com/ultralytics/yolov5) repo.

## How to use
1. Clone this repo
2. Use the (yolofy.py)[yolofy.py] script to take the original dataset and convert it to the YOLOv5 format. 
3. Use the split.py script to split the dataset into train, test and validate sets.
4. Use the (ppeConfig.yaml)[ppeConfig.yaml] file to train the model.

Data split into train, test and validate sets. The split is 70% train, 20% test and 10% validate.

## Tree
```
├── ppeConfig.yaml
├── README.md
├── restructuredDataset
│   ├── test
│   │   ├── images
│   │   └── labels
│   ├── train
│   │   ├── images
│   │   └── labels
│   └── valid
│       ├── images
│       └── labels
├── split.py
└── yolofy.py

10 directories, 4 files
```