import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt
import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from torch.utils.data import TensorDataset
from torch.utils.data import DataLoader
from torch.utils.data import random_split

from tensorboardX import SummaryWriter
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import itertools
import time
import os


class AML(nn.Module):
    def __init__(self, D_in, D_out):
        super(AML, self).__init__()
        self.l1 = nn.Linear(D_in, 100)
        self.l2 = nn.Linear(100, D_out)
        # self.sig = nn.Sigmoid()

    def forward(self, x):
        x = self.l1(x)
        x = F.relu(x)
        x = self.l2(x)
        # x = self.sig(x)
        return x


def learning_rate_finder(y):
    loss_holder = []
    lr = np.linspace(1e-8, .001, 1300)
    j = 0
    for X, y in data:
        y_pred = model(X)
        loss = criterion(y_pred, y.long())
        for g in optimizer.param_groups:
            g['lr'] = lr[j]
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        loss_holder.append(loss.data.numpy())
        j += 1
        if j == 1300:
            break
    plt.semilogx(lr, loss_holder)
    plt.show()
    t = 2


if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')
model = AML(7, 2)
writer = SummaryWriter()
writer.add_graph(model, torch.autograd.Variable(
    torch.Tensor(7)))
'''
df = pd.read_csv(os.path.join(os.getcwd(), 'data/full_ml_dataset.csv'))
enc = LabelEncoder()
enc.fit(df.type.values)
df.type = enc.transform(df.type)
res = df.drop(['nameOrig', 'nameDest'], axis=1)
# df.nameDest = df.nameDest.apply(lambda x: hash(x))
# df.nameOrig = df.nameOrig.apply(lambda x: hash(x))
y = torch.Tensor(res.isFraud.values)
X = torch.Tensor(res.iloc[:, 0:7].values)
'''
load_data = torch.load('data.pt')
X = load_data["X"].numpy()
y = load_data["y"].numpy()
criterion = nn.CrossEntropyLoss()
model = model.to(device)
optimizer = torch.optim.SGD(model.parameters(), lr=1e-5)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.15, random_state=42)
X_test = torch.Tensor(X_test)

y_test = torch.Tensor(y_test)
loader = TensorDataset(torch.from_numpy(X_train).to(
    device), torch.from_numpy(y_train).to(device))
data = DataLoader(loader, batch_size=4096, shuffle=True)
j = 0

# learning_rate_finder(y)
for t in range(1):
    for X, y in tqdm(data):
        y_pred = model(X)
        loss = criterion(y_pred, y.long())
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        writer.add_scalar('data/loss', loss, j)
        j += 1
        if j % 5 == 0:
            print(loss)

        '''
        if j % 10:
            s = time.time()
            with torch.no_grad():
                pred = torch.argmax(model(X_test), dim=1)
            print(f'T1 {time.time()-s}')
            res = confusion_matrix(y_test.numpy(), pred.numpy())
            print(f'T2 {time.time()-s}')
            fig = plt.figure(1)
            plt.imshow(res, interpolation='nearest', cmap=plt.cm.Blues)
            plt.title('Confusion Matrix')
            plt.colorbar()
            tick_marks = np.arange(2)
            plt.xticks(tick_marks, ['Negative', 'Positive'], rotation=45)
            plt.yticks(tick_marks, ['Negative', 'Positive'])
            thresh = res.max() / 2.
            for i, j in itertools.product(range(res.shape[0]), range(res.shape[1])):
                plt.text(j, i, format(res[i, j], '.2f'),
                        horizontalalignment="center",
                        color="white" if res[i, j] > thresh else "black")
            plt.ylabel('True label')
            plt.xlabel('Predicted label')
            plt.tight_layout()
            writer.add_figure('Confusion Matrix/mat', fig, j)
            print(time.time()-s)
            '''
y_pred = model(X_test)
res = torch.argmax(y_pred, dim=1).detach().numpy()
y_test = y_test.detach().numpy()
print(np.sum(y_test == res))
print(np.sum(y_test == res)/len(y_test))
correct_null = np.sum(res[y_test == 0] == 0)
correct_flaged = np.sum(res[y_test == 1] == 1)
