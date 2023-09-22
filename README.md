# Customized-NN

Build a plain tensorflow CNN model with just number of layers and classes.

Parameters:

```
main.py [-h] [-inputsize INPUTSIZE] [-n N] [-classes CLASSES]

Create a plain neural network model

optional arguments:
  -h, --help            show this help message and exit
  -inputsize INPUTSIZE  Number of layers of the model
  -n N                  Number of layers of the model
  -classes CLASSES      Number of classes in the model
```

To run : 

```
python3 main.py -inputsize 224 -n 5 -classes 10
```

Output:

```
_________________________________________________________________
 Layer (type)                Output Shape              Param #   
=================================================================
 conv2d (Conv2D)             (None, 224, 224, 32)      896       
                                                                 
 max_pooling2d (MaxPooling2D  (None, 112, 112, 32)     0         
 )                                                               
                                                                 
 batch_normalization (BatchN  (None, 112, 112, 32)     128       
 ormalization)                                                   
                                                                 
 conv2d_1 (Conv2D)           (None, 112, 112, 32)      9248      
                                                                 
 max_pooling2d_1 (MaxPooling  (None, 56, 56, 32)       0         
 2D)                                                             
                                                                 
 batch_normalization_1 (Batc  (None, 56, 56, 32)       128       
 hNormalization)                                                 
                                                                 
 conv2d_2 (Conv2D)           (None, 56, 56, 32)        9248      
                                                                 
 max_pooling2d_2 (MaxPooling  (None, 28, 28, 32)       0         
 2D)                                                             
                                                                 
 batch_normalization_2 (Batc  (None, 28, 28, 32)       128       
 hNormalization)                                                 
                                                                 
 conv2d_3 (Conv2D)           (None, 28, 28, 32)        9248      
                                                                 
 max_pooling2d_3 (MaxPooling  (None, 14, 14, 32)       0         
 2D)                                                             
                                                                 
 batch_normalization_3 (Batc  (None, 14, 14, 32)       128       
 hNormalization)                                                 
                                                                 
 conv2d_4 (Conv2D)           (None, 14, 14, 32)        9248      
                                                                 
 max_pooling2d_4 (MaxPooling  (None, 7, 7, 32)         0         
 2D)                                                             
                                                                 
 batch_normalization_4 (Batc  (None, 7, 7, 32)         128       
 hNormalization)                                                 
                                                                 
 global_average_pooling2d (G  (None, 32)               0         
 lobalAveragePooling2D)                                          
                                                                 
 dense (Dense)               (None, 1024)              33792     
                                                                 
 dense_1 (Dense)             (None, 10)                10250     
                                                                 
=================================================================
Total params: 82,570
Trainable params: 82,250
Non-trainable params: 320
_________________________________________________________________
mahi@mahi:~/github_repos/Customized-NN$ 

```