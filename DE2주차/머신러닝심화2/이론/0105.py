from elice_utils import EliceUtils
elice_utils = EliceUtils()

import warnings
warnings.filterwarnings(action='ignore')

import numpy as np
import matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.utils.multiclass import unique_labels

def load_data():
    
    X, y = load_wine(return_X_y = True)
    class_names = load_wine().target_names
    
    train_X, test_X, train_y, test_y = train_test_split(X, y, test_size =0.3, random_state=0)
    
    return train_X, test_X, train_y, test_y, class_names

def plot_confusion_matrix(cm, y_true, y_pred, classes, normalize=False, cmap=plt.cm.OrRd):
                          
    title = ""
    if normalize:
        title = 'Normalized confusion matrix'
    else:
        title = 'Confusion matrix'
    
    classes = classes[unique_labels(y_true, y_pred)]
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    print(title, ":\n", cm)

    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    ax.set(xticks=np.arange(cm.shape[1]),
           yticks=np.arange(cm.shape[0]),
           xticklabels=classes, yticklabels=classes,
           title=title,
           ylabel='True label',
           xlabel='Predicted label')

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    
    plt.savefig('confusion matrix.png')
    elice_utils.send_image('confusion matrix.png')

def main():

    train_X, test_X, train_y, test_y, class_names = load_data()

    classifier = SVC()
    y_pred = classifier.fit(train_X, train_y).predict(test_X)

    cm = confusion_matrix(test_y, y_pred)

    plot_confusion_matrix(cm, test_y, y_pred, classes=class_names)

    plot_confusion_matrix(cm, test_y, y_pred, classes=class_names, normalize=True)
    
    return cm
    
if __name__ == "__main__":
    main()
