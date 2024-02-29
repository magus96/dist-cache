import Pyro4
from cacher import Cacher


def main():
    daemon = Pyro4.Daemon()
    uri = daemon.register(Cacher)

    print("URI:", uri)
    daemon.requestLoop()

if __name__=="__main__":
    main()