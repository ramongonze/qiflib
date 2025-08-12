## QIF Library
A tiny, focused Python library for Quantitative Information Flow (QIF): model secrets, channels, and analyze leakage via the g-vulnerability framework.

## Features
- Secrets (priors over hidden states)
- Channels (stochastic matrices from secrets to observables)
- Hypers (Distribution on distribution on secrets)
- g-Vulnerability (generalized adversary gain) and related leakage quantities

## Installation
You can install via PyPI:

```bash
pip install qiflib
```

or manuallly by copying this repository to your local machine and running:

```bash
pip install path/to/qiflib   
```

To verify if the package was installed correctly, you can run tests:

```bash
cd path/to/qiflib
python -m unittest discover tests
```

## Example

```python
from libqif.core.secrets import Secrets
from libqif.core.channel import Channel
from libqif.core.hyper import Hyper
from libqif.core.gvulnerability import GVulnerability
import numpy as np

secrets = Secrets(['x1','x2','x3','x4'], [1/3, 1/3, 0, 1/3])
channel = Channel(secrets, ['y1','y2','y3','y4'], np.array([
   [1/2, 1/6, 1/3,   0],
   [  0, 1/3, 2/3,   0],
   [  0, 1/2,   0, 1/2],
   [1/4, 1/4, 1/2,   0]
]))
hyper = Hyper(channel)
gain = GVulnerability(secrets, ['w1','w2','w3','w4'], np.identity(4)) # Bayes vulnerability

print('Prior distribution: ' + str(secrets.prior))
print('Channel:\n' + str(channel.matrix))
print('\nOuter distribution: ' + str(hyper.outer))
print('Inner distributions:\n' + str(hyper.inners))
print('\nPrior Bayes vulnerability: ' + str(gain.prior_vulnerability()))
print('Posterior Bayes vulnerability: ' + str(gain.posterior_vulnerability(hyper)))
```

Output
```bash
Prior distribution: [0.33333333 0.33333333 0.         0.33333333]
Channel:
[[0.5        0.16666667 0.33333333 0.        ]
[0.         0.33333333 0.66666667 0.        ]
[0.         0.5        0.         0.5       ]
[0.25       0.25       0.5        0.        ]]

Outer distribution: [0.25 0.75]   
Inner distributions:
[[0.66666667 0.22222222]
[0.         0.44444444]
[0.         0.        ]
[0.33333333 0.33333333]]

Prior Bayes vulnerability: 0.3333333333333333
Posterior Bayes vulnerability: 0.5
```

## References
*Alvim, Mário S., Konstantinos Chatzikokolakis, Annabelle McIver,
Carroll Morgan, Catuscia Palamidessi, and Geoffrey Smith.
The Science of Quantitative Information Flow. Springer International
Publishing, 2020.*


## License

This project is licensed under the [MIT License](https://opensource.org/license/mit).