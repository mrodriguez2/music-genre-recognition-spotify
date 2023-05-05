## Music Genre Classification with CNNs using Spotify
The goal of this project is to be able to detect the genre of a song by training a Convolutional Neural Network (CNN) using a custom created dataset based on Spotify Playlists.

The goal of this project is to be able to detect the genre of a song, using Mel spec-trograms, by training a Convolutional Neural Network (CNN) with Keras using Python. For this purpose, we will work on three different datasets.

First of all, we will begin our work on the GTZAN dataset which consists of 900 30-second, 22kHz, Mono, 16-bit .WAV files, belonging to 9 different genres from 2000-2001 to build and test our model architecture:

•	Blues
•	Pop
•	Rock
•	Classical
•	Country
•	Disco
•	Hip-hop
•	Metal
•	Reggae


From then on, we will expand the GTZAN dataset with two new genres created from scratch using Spotify Playlists and see how the model adapts to using these two new genres. 

In particular, the two genres that we will include will be ‘Rap’ and ‘Brazilian Funk’. ‘Rap’ because it is one of the biggest music genres out there and it would be interesting to build a genre from scratch using Spotify and see how it performs versus the original GTZAN dataset.
 
Brazilian Funk for two purposes: first and foremost, it is a wink to my sweet Brazilian girlfriend. Secondly, it is a genre that is usually used to remix popular songs and it will be an interesting observation to compare our model with the origi-nal song versus the remixed, Brazilian Funk, version of the song. The inspiration behind this was Rihanna’s Brazilian Funk interpretation of her hit ‘Rude Boy’ at this year’s Super Bowl.

The inspiration behind this paper came from Kunal Vaidya’s post [1] on To-wardsDataScience. From the original paper came the idea of transforming the GTZAN dataset into Mel Spectrograms to be able to treat the audio files as images to use with CNNs and to split each audio file into 10 3-sec clips.

However, I felt like little documentation was provided and that the project had a lot more to offer and investigate. For this reason, in this paper we aim to:
•	Create a completely new dataset sourced from Spotify Playlists with more genres and bigger size.
•	Optimize, test and compare different model architectures.
•	Focus on analyzing how the model performs in ‘original’ versus ‘remixes’ songs.
•	Provide easy-to-access, reproducible and readable source code and documentation on the whole process.
Most importantly however, we hope to use this project as a learning opportunity to improve our knowledge on Machine Learning, Artificial Intelligence and Neural Net-works.
![image](https://user-images.githubusercontent.com/25019006/236570371-10678442-74e2-49be-a49a-76443bc5cea6.png)
