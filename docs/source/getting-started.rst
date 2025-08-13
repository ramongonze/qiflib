
Getting Started
===============

This guide shows the minimal end-to-end workflow for Quantitative Information Flow (QIF):

.. contents::
   :local:
   :depth: 1

Imports
-------
.. code-block:: python

   from qiflib.core.secrets import Secrets
   from qiflib.core.channel import Channel
   from qiflib.core.hyper import Hyper
   from qiflib.core.gvulnerability import GVulnerability
   from qiflib.core.luncertainty import LUncertainty

Create a Set of Secrets
--------------------------
A set of secrets is defined by labels and a prior distribution over those labels.

- The list of labels must have at least 2 elements.

- The prior must be a valid probability distribution (non-negative entries summing to 1) and match the number of labels.

.. code-block:: python

   # Two secrets with a non-uniform prior
   labels = ["x0", "x1"]
   prior = [0.7, 0.3]
   secrets = Secrets(labels, prior)

Update the prior later (optional):

.. code-block:: python

   secrets.update_prior([0.5, 0.5])


Create a Channel
----------------

A channel encodes the conditional probabilities :math:`C[x][y] = p(y\mid x)`.

- outputs is the list of observable outputs (at least one).

- channel is an :math:`n` \times m matrix whose rows are probability distributions (each row sums to 1).

- The number of rows equals the number of secrets; the number of columns equals the number of outputs.

.. code-block:: python

   outputs = ["y0", "y1", "y2"]

   # C[x][y] = p(y|x). Each row sums to 1.
   C = [
      [0.6, 0.3, 0.1], # p(y|x0)
      [0.1, 0.4, 0.5], # p(y|x1)
   ]

   channel = Channel(secrets, outputs, C)

Update the prior through the channel (optional):

.. code-block:: python

   channel.update_prior([0.2, 0.8])

Create a Hyper-distribution
---------------------------

A hyper-distribution bundles:

- the joint distribution :math:`J[x,y] = p(x)p(y\mid x)`,

- the outer distribution :math:`p(y)`,

- the inners (posterior) distributions :math:`p(x\mid y)`,

- and reduces equivalent/zero-probability posteriors.

.. code-block:: python

   hyper = Hyper(channel)

If you change the prior later:

.. code-block:: python

   hyper.update_prior([0.5, 0.5])

hyper.joint, hyper.outer, hyper.inners, and hyper.num_posteriors are recomputed

Create a g-Vulnerability Function
---------------------------------

The :math:`g`-vulnerability models an adversary’s gain for choosing action :math:`w` when the true secret is :math:`x`.
You can provide either:

- a gain matrix G[w][x] with shape (#actions, #secrets), or

- a callable g(w, x) -> float from which the matrix is built.

Matrix form:

.. code-block:: python

   actions = ["guess_x0", "guess_x1"]

   # gain 1 if we guess x0/x1 when secret is x0/x1
   G = [
      [1.0, 0.0], 
      [0.0, 1.0],
   ]

   g = GVulnerability(secrets, actions, G)

Function form (equivalent to the matrix above):

.. code-block:: python

   def gfun(w, x):
      # reward 1.0 for a correct guess, 0.0 otherwise
      return 1.0 if w == x else 0.0

   g = GVulnerability(secrets, actions, gfun)

Create an ℓ-Uncertainty (Loss) Function
---------------------------------------

The :math:`\ell`-uncertainty models an adversary’s loss for action :math:`w` when the true secret is :math:`x`.
As with :math:`g`, you can provide a loss matrix or a callable.

Matrix form:

.. code-block:: python

   actions = ["guess_x0", "guess_x1"]

   L = [
      [0.0, 1.0], # loss if we choose action "guess_x0"
      [1.0, 0.0], # loss if we choose action "guess_x1"
   ]

   ell = LUncertainty(secrets, actions, L)

Function form:

.. code-block:: python

   def lfun(w, x):
      # 0 loss if the guess matches, 1 otherwise
      return 0.0 if w == x else 1.0

   ell = LUncertainty(secrets, actions, lfun)

Calculate the Prior Vulnerability (and Uncertainty)
---------------------------------------------------

- Prior :math:`g`-vulnerability: :math:`\max_w \sum_x p(x) \, g(w,x)`

- Prior :math:`\ell`-uncertainty: :math:`\min_w \sum_x p(x) \, \ell(w,x)`

.. code-block:: python

   prior_vuln = g.prior_vulnerability()
   prior_unc = ell.prior_uncertainty()

   print("Prior g-vulnerability:", prior_vuln)
   print("Prior ℓ-uncertainty:", prior_unc)

Calculate the Posterior Vulnerability (and Uncertainty)
-------------------------------------------------------

Given the hyper:

- Posterior :math:`g`-vulnerability: :math:`\sum_y \max_w \sum_x p(x,y)\, g(w,x)`

- Posterior :math:`\ell`-uncertainty: :math:`\sum_y \min_w \sum_x p(x,y)\, \ell(w,x)`

.. code-block:: python

   post_vuln = g.posterior_vulnerability(hyper)
   post_unc = ell.posterior_uncertainty(hyper)

   print("Posterior g-vulnerability:", post_vuln)
   print("Posterior ℓ-uncertainty:", post_unc)

