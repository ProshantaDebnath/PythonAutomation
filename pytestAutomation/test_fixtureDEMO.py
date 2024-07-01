import pytest


@pytest.mark.usefixtures("dataLoad")
class AutomationPractice:
    def editPorfile(self, dataLoad):
        print(dataLoad[0])
        print(dataLoad[1])



