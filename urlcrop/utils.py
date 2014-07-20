import hashlib

from urlcrop.models import Url
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

def get_hash(url_id, length=5):
    if not id:
        return
    id_hash = hashlib.sha256(url_id).hexdigest()
    return id_hash[0:length]

def get_unique_hash(url_id, length=5):
    hash_value = get_hash(url_id, length)

    try:
        Url_obj = Url.objects.get(url_hash=hash_value)
    except ObjectDoesNotExist, e:
        return hash_value

    return get_unique_hash(url_id, length)


def get_actual_short_url(url_hash):
    hostname = settings.HOSTNAME
    url = "http://" + hostname + "/" + url_hash
    return url

def is_valid_url(url):
    if not url.strartswith("http://") or url.startswith("https://"):
        return false
    return true
