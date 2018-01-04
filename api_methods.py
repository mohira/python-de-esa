from abc import ABCMeta, abstractmethod

class ApiMethods(metaclass=ABCMeta):
    def posts(self, params=None, headers=None):
        return self.send_get("v1/teams/{}/posts".format(self.current_team),
                             params,
                             headers)
    @abstractmethod
    def send_get(self, param, params, headers):
        pass

