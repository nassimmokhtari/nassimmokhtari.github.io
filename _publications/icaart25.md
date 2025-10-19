---
title: "Neural Architecture Search: Tradeoff Between Performance and Efficiency"
collection: publications
category: conferences
permalink: /publication/2025-neural-architecture-search:-tradeoff-between-performance-and-efficiency
date: 2025-01-01
venue: "Proceedings of the 17th International Conference on Agents and Artificial Intelligence - Volume 3: ICAART"
bibtexurl: "https://nassimmokhtari.github.io/files/neural-architecture-search:-tradeoff-between-performance-and-efficiency.bib"
citation: "Tien Nguyen and Nassim Mokhtari and Alexis Nédélec (2025). &quot;Neural Architecture Search: Tradeoff Between Performance and Efficiency.&quot; <i>Proceedings of the 17th International Conference on Agents and Artificial Intelligence - Volume 3: ICAART</i>."
---
Many Neural Architecture Search (NAS) methods have designed models that outperform manually configured networks on various tasks. Due to computational cost of model’s training, recent trend includes performing NAS without training candidate networks in the process. Many such methods have proven that training-free metrics are an effective way to assess model’s performance, especially if they are combined together. Multi-training-free-objectives NAS methods usually construct a Pareto front that gives a wide range of solutions. However, only one solution is chosen in the end. We introduce the Rank-based Improved Firefly Algorithm (RB-IFA), which focuses the search in a single direction by converting multiple objective ranks into one weighted sum. Weights are derived from a performance-efficiency tradeoff. Our search algorithm is based on an Improved Firefly Algorithm (IFA). IFA effectively explores the NAS landscape by combining the Firefly Algorithm, which has fast convergence, with a genetic algorithm, which improves the ability to overcome local optima. RB-IFA NAS identifies highly efficient architectures with competitive performance within 8 minutes. These results highlight the potential of multi-training-free metrics and a rank-based approach in finding efficient neural networks.
