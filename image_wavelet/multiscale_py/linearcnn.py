import torch
import transform_network
import soft_threshold
import torch.nn as nn

class linearcnn(nn.Module):
    def __init__(self, kernel_size = 3):
        # try with large kernal size, like 50, for the noisy images, reflection padding rather than the zero padding
        super(linearcnn, self).__init__()
        self.conv1 = nn.Conv2d(1, 1, kernel_size, padding=(kernel_size-1)//2, padding_mode='reflect')
        print((kernel_size-1)//2)

    def forward(self, x):

        rec_img = self.conv1(x)
		
        return(rec_img)
