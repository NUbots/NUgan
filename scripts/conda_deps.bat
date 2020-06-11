@ECHO OFF

CALL conda install numpy pyyaml mkl mkl-include setuptools cmake cffi typing
CALL conda install pytorch torchvision -c pytorch 
CALL conda install visdom dominate -c conda-forge 
