import json
import os


class SecretLoader:
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), 'secret.json')
        if os.path.exists(path):
            with open(path) as f:
                self._secrets = json.loads(f.read())

    def get_secret(self, key, default=None):
        if key in os.environ:
            return os.environ[key]
        elif key in self._secrets:
            return self._secrets[key]
        elif default:
            return default
        else:
            error = 'Failed to load credential for key : "{}"; '.format(key)
            error += 'call load_credential("{}", default=...) to ignore this error.'.format(key)
            raise Exception(error)
