""" helper functions
"""
import os
import pickle
import base64
import hashlib
import numbers
import datetime
import automol
import autoparse.pattern as app
import autoparse.find as apf


def is_valid_inchi_multiplicity(ich, mul):
    """ is this multiplicity compatible with this inchi string?

    :param ich: inchi
    :type ich: str
    :param mul: multiplicity
    :type mul: int
    :returns: validity of inchi multiplicity
    :rtype: bool
    """
    assert isinstance(mul, numbers.Integral)
    return mul in automol.graph.possible_spin_multiplicities(
        automol.inchi.graph(ich, stereo=False))


def short_hash(obj):
    """ determine a short (3-character) hash from a string

    """
    if isinstance(obj, str):
        obj_str = obj.encode('utf-8')
    else:
        obj_str = pickle.dumps(obj)
    dig = hashlib.md5(obj_str).digest()
    hsh = base64.urlsafe_b64encode(dig)[:3]
    return hsh.decode()


def random_string_identifier():
    """ generate a "unique" (=long-ish, random) identifier

    :returns: a random string
    :rtype: str
    """
    rsi = base64.urlsafe_b64encode(os.urandom(9)).decode("utf-8")
    return rsi


def is_random_string_identifier(sid):
    """ could this have been generated by `random_string_identifier()`?

    :param sid: string identifier
    :type sid: string
    :returns: is the pattern a random string
    :rtype: bool
    """
    sid_pattern = app.URLSAFE_CHAR * 12
    return apf.full_match(sid_pattern, sid)


def utc_time():
    """ get the current UTC time

    :returns: the utc time
    :rtype: datetime
    """
    return datetime.datetime.utcnow()
