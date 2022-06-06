import subprocess
import sys


class Reader:
    """
    Class for reading logs.
    """

    def __init__(self, container_name: str, stop_phrase: str):
        """
        This constructor takes in two arguments, a container name and a stop phrase.

        :param container_name: The name of the container that you want to use
        :type container_name: str
        :param stop_phrase: This is the phrase that will stop the script from listening
        :type stop_phrase: str
        """
        self.container_name = container_name
        self.stop_phrase = stop_phrase.lower()

    def start(self):
        """
        It starts a docker logs reader, and then it reads the output of the logs until it finds a stop phrase
        :return: The return value is the exit status of the process.
        """
        proc = subprocess.Popen(
            ["docker", "logs", "-f", self.container_name],
            stderr=subprocess.PIPE,
            text=True,
        )
        for line in iter(proc.stderr.readline, ""):
            print(line, end="", file=sys.stderr)
            if self.stop_phrase in line.lower():
                proc.kill()
                return 0

        return 1
