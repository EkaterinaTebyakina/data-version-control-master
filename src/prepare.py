from pathlib import Path

import pandas as pd
import os

repo_path = Path(__file__).parent.parent
data_path = repo_path / "data"
train_path = data_path / "raw/train"
mapFolder = {}
for item in os.listdir(train_path):
    mapFolder[item] = item.replace(' ', '_').lower()

FOLDERS_TO_LABELS = mapFolder



def get_files_and_labels(source_path):
    images = []
    labels = []
    for image_path in source_path.rglob("*/*.jpg"):
        filename = image_path.absolute()
        folder = image_path.parent.name
        if folder in FOLDERS_TO_LABELS:
            images.append(filename)
            label = FOLDERS_TO_LABELS[folder]
            labels.append(label)
    return images, labels


def save_as_csv(filenames, labels, destination):
    data_dictionary = {"filename": filenames, "label": labels}
    data_frame = pd.DataFrame(data_dictionary)
    data_frame.to_csv(destination)


def main(repo_path):
    data_path = repo_path / "data"
    train_path = data_path / "raw/train"
    test_path = data_path / "raw/valid"
    train_files, train_labels = get_files_and_labels(train_path)
    test_files, test_labels = get_files_and_labels(test_path)
    prepared = data_path / "prepared"
    save_as_csv(train_files, train_labels, prepared / "train.csv")
    save_as_csv(test_files, test_labels, prepared / "test.csv")


if __name__ == "__main__":
    repo_path = Path(__file__).parent.parent
    main(repo_path)
