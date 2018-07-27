# ELF

This is an adaptation of the original repo for setting up a remote server to communicate with the AI Go bot developed by the Facebook team.

## **Installation**

Follow the instructions [here](https://github.com/pytorch/ELF) to install the dependencies for the AI engine and the instructions [here](https://github.com/Jachua/ELF-API) to install the dependencies for the game server. 

*Note:

In order to install the dependencies for python, you are hgihly encouraged to use the Anaconda package and environment manager, which can be downloaded from [here](https://repo.anaconda.com/archive/Anaconda3-5.2.0-Linux-x86_64.sh). Once the download is complete, follow the instructions on [this page](https://docs.anaconda.com/anaconda/install/linux.html). If you are based in China, the installation might take a long while, and if you want to speed up the process, you may want to take a look at [this page](https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/).

You will also need an NVIDIA driver to properly install pytorch. 


## **Setup**

[This repo](https://github.com/Jachua/ELF-API) contains the scripts needed to run up the server and a simple CLI client that illustrates how to communicate with the AI engine via the game server. 

To prepare the AI engine for OpenGo, follow the intructions on [this page](https://github.com/pytorch/ELF).

## **How it works**

A client stub and grpc modules are added to the original repo to subscribe and send messages to the server. 

For your convenience, a pretrained model ```./pretrained-go-19x19-v0.bin``` has also been posted on this repo. 

For further details, check out the doc file [here](https://github.com/Jachua/ELF-API).