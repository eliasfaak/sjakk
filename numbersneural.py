import torch as torch
import numpy as np
import torchvision
import torch.nn as nn
import torch.nn.functional as F
import matplotlib.pyplot as plt
import torch.optim as optim
from torchvision import transforms, datasets
from PIL import Image

train = datasets.MNIST("", train =True, download=True,
        transform=transforms.Compose([transforms.ToTensor()]))

test = datasets.MNIST("", train =False, download=True,
        transform=transforms.Compose([transforms.ToTensor()]))

trainset = torch.utils.data.DataLoader(train, batch_size = 10, shuffle = True)
testset = torch.utils.data.DataLoader(train, batch_size = 10, shuffle = True)
"""
for data in trainset:
    print(data)
    break

x,y = data[0][0], data[1][0]
#print(x,y)
#print(y)
#plt.imshow(x.view(28,28))
#plt.show()
total = 0
counterdict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
for data in trainset:
    Xs, Ys = data
    for y in Ys:
        counterdict[int(y)] += 1
        total+=1
print(counterdict)

for i in counterdict:
    print(f"{i}: {counterdict[i]/total*100}")
"""
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(28*28, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, 64)
        self.fc4 = nn.Linear(64, 10)
    def forward(self,x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return F.log_softmax(x, dim=1)
"""
net = Net()
optimizer = optim.Adam(net.parameters(), lr = 0.001)
EPOCHS = 3
for epoch in range(EPOCHS):
    for data in trainset:
        #data is batch of featuresets and Labels
        X, y = data
        net.zero_grad()
        output = net(X.view(-1,28*28))
        loss = F.nll_loss(output, y)
        loss.backward()
        optimizer.step()
    #print(loss)

torch.save(net, "net.pth")
"""
model = torch.load("net.pth")
model.eval()

im = Image.open(r"seven.png")
ar = np.array(im)
for data in testset:
    X, y = data
    break
plt.imshow(X[0].view(28,28))
plt.show()
img = torch.from_numpy(ar)
#print(img.view(-1,28*28))
#print(X)
#print(type(img))
img = img.float()
print(torch.argmax(model(img.view(-1,28*28))[0]))
