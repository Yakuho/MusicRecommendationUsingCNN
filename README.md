# Music Recommendation Using Deep Learning

Music Recommendation using latent feature vectors obtained from a network trained on the Free Music Archive dataset.

## Overview

The basic idea of this project is to recommend music using computer vision through a convolutional neural network. The network is first trained as a classifier with the labels being the 8 different genres of songs from the dataset. The trained network is then modified by discarding the softmax layer i.e. creating a new model which works as an encoder. This encoder takes as input slices of a spectrogram one at a time and outputs a 32 dimensional latent representation of that respective slice. This generates multiple latent vectors for one spectrogram depending on how many slices were generated. These multiple vectors are then averaged to get one latent representation for each spectrogram. The Cosine similarity metric is used to generate a similarity score between one anchor song and the rest of the songs in the test set. The two songs with the highest similarity score with respect to the anchor song are then outputted as the recommendations.

**DataSet URL**: https://github.com/mdeff/fma