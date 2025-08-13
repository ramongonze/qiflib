Quantitative Information Flow Library
=====================================

**QIFLib** is a Python library for modeling, analyzing, and quantifying information leakage in probabilistic systems using the **Quantitative Information Flow (QIF)** framework.  
It provides a clean, composable set of primitives — *secrets*, *channels*, *hyper-distributions*, *vulnerability* and *uncertainty* functions — so you can build end-to-end analyses of how much information an adversary could learn.

For more details see the book `The Science of Quantitative Information Flow <https://link.springer.com/book/10.1007/978-3-319-96131-6>`_.



.. tip::

   **New here? Start with the tutorial:** :doc:`Getting Started <getting-started>`

Key Features
------------

- **Secrets Modeling** — define hidden states with flexible prior distributions.
- **Channels** — represent probabilistic mappings :math:`p(y\mid x)` from secrets to observations.
- **Hyper-distributions** — automatically compute joint :math:`p(x,y)`, outer :math:`p(y)`, and inners :math:`p(x\mid y)`.
- **Vulnerability Analysis** — use :math:`g`-vulnerability to quantify an adversary’s expected gain before and after observing outputs.
- **Uncertainty Analysis** — use :math:`\ell`-uncertainty to measure the expected loss under optimal strategies.
- **Leakage Metrics** — compute additive and multiplicative leakage.
- **Flexible Functions** — provide gain/loss as matrices or Python callables.

Why QIF?
--------

Traditional security analysis asks whether a secret *can* be inferred. QIF quantifies **how much** an adversary is expected to learn, under probabilistic models of system behavior and strategies.  
Useful for:

- privacy-preserving data publishing,
- side-channel analysis,
- communication protocol evaluation,
- decision-making under uncertainty.

Installation
------------

You can install via PyPI:

.. code-block:: bash

   pip install qiflib

or manuallly by copying the `GitHub repository <https://github.com/ramongonze/qiflib>`_ to your local machine and running:

.. code-block:: bash

   pip install path/to/qiflib   

To verify if the package was installed correctly, you can run tests:

.. code-block:: bash
   
   cd path/to/qiflib
   python -m unittest discover tests

Quick Example
-------------

.. code-block:: python

   from qiflib.core.secrets import Secrets
   from qiflib.core.channel import Channel
   from qiflib.core.hyper import Hyper
   from qiflib.core.gvulnerability import GVulnerability

   # Secrets & prior
   secrets = Secrets(["x0", "x1"], [0.6, 0.4])

   # Channel matrix: rows sum to 1
   outputs = ["y0", "y1"]
   C = [
       [0.8, 0.2],  # p(y|x0)
       [0.1, 0.9],  # p(y|x1)
   ]
   channel = Channel(secrets, outputs, C)

   # Hyper-distribution
   hyper = Hyper(channel)

   # Gain function (1 if correct guess, else 0)
   actions = ["guess_x0", "guess_x1"]
   def gfun(w, x): return 1.0 if w == x else 0.0

   g = GVulnerability(secrets, actions, gfun)

   print("Prior vulnerability:", g.prior_vulnerability())
   print("Posterior vulnerability:", g.posterior_vulnerability(hyper))

.. toctree::
   :maxdepth: 4
   :caption: User Guide

   getting-started
   api/index
