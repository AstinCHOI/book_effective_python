
import logging

# try:
#     def determine_weight(volume, density):
#         if density <= 0:
#             raise ValueError('Density must be positive')
    
#     determine_weight(1, 0)
# except:
#     logging.exception('Expected')
# else:
#     assert False
# ERROR:root:Expected
# ...
# ValueError: Density must be positive


# my_module.py
class Error(Exception):
    """Base-class for all exceptions raised by this module."""

class InvalidDensityError(Error):
    """There was a problem with a provided density value."""

class my_module(object):
    Error = Error
    InvalidDensityError = InvalidDensityError

    @staticmethod
    def determine_weight(volume, density):
        if density <= 0:
            raise InvalidDensityError('Density must be positive')


# try:
#     weight = my_module.determine_weight(1, -1)
# except my_module.Error as e:
#     logging.error('Unexpected error: %s', e)
# >>>
# ValueError: Density must be positive


weight = 5
try:
    weight = my_module.determine_weight(1, -1)
    assert False
except my_module.InvalidDensityError:
    weight = 0
except my_module.Error as e:
    logging.error('Bug in the calling code: %s', e)

assert weight == 0


weight = 5
try:
    weight = my_module.determine_weight(1, -1)
    assert False
except my_module.InvalidDensityError:
    weight = 0
except my_module.Error as e:
    logging.error('Bug in the calling code: %s', e)
except Exception as e:
    logging.error('Bug in the API code: %s', e)
    raise

assert weight == 0


# my_module.py
class NegativeDensityError(InvalidDensityError):
    """A provided density value was negative."""

def determine_weight(volume, density):
    if density < 0:
        raise NegativeDensityError


try:
    my_module.NegativeDensityError = NegativeDensityError
    my_module.determine_weight = determine_weight
    try:
        weight = my_module.determine_weight(1, -1)
        assert False
    except my_module.NegativeDensityError as e:
        raise ValueError('Must supply non-negative density') from e
    except my_module.InvalidDensityError:
        weight = 0
    except my_module.Error as e:
        logging.error('Bug in the calling code: %s', e)
    except Exception as e:
        logging.error('Bug in the API code: %s', e)
        raise
except:
    logging.exception('Expected')
else:
    assert False
# >>>
# ERROR:root:Expected
# ...
# ValueError: Must supply non-negative density


# my_module.py
class WeightError(Error):
    """Base-class for weight calculation errors."""

class VolumeError(Error):
    """Base-class for volume calculation errors."""

class DensityError(Error):
    """Base-class for density calculation errors."""