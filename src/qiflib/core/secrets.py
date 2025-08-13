"""Set of secrets."""

from qiflib.util.types import is_list, is_numpy_array
from qiflib.util.probability import check_prob_distribution
from numpy import array

class Secrets:
    """Class used to represent a set of secrets. To create an instance of
    this class it is necessary a set of labels and a probability distribution
    to be set as the prior distribution on the set of secrets.

    Parameters
    ----------
    secrets : list
        Secrets labels.

    prior : list, numpy.ndarray
        Prior distribution on the set of secrets. prior[i] is the
        probability of secret named labels[i] beeing the real secret.

    Attributes
    ----------
    labels : list, numpy.ndarray
        List of secrets' labels.

    num_secrets : int
        Number of secrets.

    prior : numpy.ndarray
        Prior distribution on the set of secrets. :code:`prior[i]` is the
        probability of secret named :code:`labels[i]` beeing the real secret.
    """
    
    def __init__(self, secrets, prior):
        self._check_types(secrets, prior)
        self._check_sizes(secrets, prior)
        self.labels = secrets.copy()
        self.num_secrets = len(self.labels)
        check_prob_distribution(prior) # Check if the array is a probability distribution
        self.prior = array(prior)

    def update_prior(self, prior):
        """Update prior distribution array.
        The number of elements in the array must be the same as the current number of secrets.

        Parameters
        ----------
        prior : list, numpy.ndarray
            Prior distribution on the set of secrets. prior[i] is the
            probability of secret named labels[i] beeing the real secret.
        """

        if not is_list(prior) and not is_numpy_array(prior):
            raise TypeError('The parameter \'prior\' must be a list or a numpy.ndarray')

        if len(prior) != self.num_secrets:
            raise Exception('The array size is different from the number of secrets')

        check_prob_distribution(prior) # Check if the array is a probability distribution
        self.prior = array(prior)
    
    def _check_types(self, secrets, prior):
        if not is_list(secrets):
            raise TypeError('The parameter \'secrets\' must be a list')

        if not is_list(prior) and not is_numpy_array(prior):
            raise TypeError('The parameter \'prior\' must be a list or a numpy.ndarray')

    def _check_sizes(self, secrets, prior):
        """Check if the size of the list of labels is the same of the 
        number of elements in the prior distribution.
        """
        if len(secrets) < 2:
            raise Exception('The set of secrets must contain at least 2 elements')
        
        if len(secrets) != len(prior):
            raise Exception('The size of label\'s list is different from ' +
                            'the number of elements in the prior distribution')