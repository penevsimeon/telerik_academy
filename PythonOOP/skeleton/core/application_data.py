
from models.test_group import TestGroup


class ApplicationData:
    def __init__(self):
        self._test_groups: list[TestGroup] = []

    @property
    def groups(self):
        return tuple(self._test_groups)

    def find_group(self, id: int):
        for group in self._test_groups:
            if group.id == id:
                return group

        return None

    def find_test(self, id: int):
        for group in self._test_groups:
            for test in group.tests:
                if test.id == id:
                    return test

        return None

    def add_group(self, group: TestGroup) -> bool:
        if any(g for g in self.groups if g.id == group.id):
            return False
        else:
            self._test_groups.append(group)
            return True

    def remove_group(self, id: int) -> bool:
        found_group = None
        for group in self._test_groups:
            if group.id == id:
                found_group = group

        if found_group is None:
            return False
        else:
            self._test_groups.remove(found_group)
            return True
