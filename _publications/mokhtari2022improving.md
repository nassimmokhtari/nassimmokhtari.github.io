---
title: "Improving neural architecture search by mixing a firefly algorithm with a training free evaluation"
collection: publications
category: conferences
permalink: /publication/2022-improving-neural-architecture-search-by-mixing-a-firefly-algorithm-with-a-training-free-evaluation
date: 2022-01-01
venue: "2022 International Joint Conference on Neural Networks (IJCNN)"
bibtexurl: "https://nassimmokhtari.github.io/files/improving-neural-architecture-search-by-mixing-a-firefly-algorithm-with-a-training-free-evaluation.bib"
citation: "Mokhtari, Nassim and Nédélec, Alexis and Gilles, Marlène and De Loor, Pierre (2022). &quot;Improving neural architecture search by mixing a firefly algorithm with a training free evaluation.&quot; <i>2022 International Joint Conference on Neural Networks (IJCNN)</i>."
---
Neural Architecture Search (NAS) algorithms are used to automate the design of deep neural networks. Finding the best architecture for a given dataset can be time consuming since these algorithms have to explore a large number of networks, and score them according to their performances to choose the most appropriate one. In this work, we propose a novel metric that uses the Intra-Cluster Distance (ICD) score to evaluate the ability of an untrained model to distinguish between data in order to approximate its quality. We also use an improved version of the FireFly algorithm, more robust to the local optimums problem than the baseline FireFly algorithm, as a search technique to find the best neural network model adapted to a specific dataset. Experimental results on the different NAS Benchmarks show that our metric is valid for either scoring CNNs and RNNs, and that our proposed FireFly algorithm can improve the result obtained by the state-of-art training-free methods.
