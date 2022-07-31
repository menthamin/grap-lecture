import abc

from app.domain.entity import Domain


class AbstractRepository(abc.ABC):
    def create(self, model: Domain):
        ...
