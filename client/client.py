import Pyro4

def main():
    cache_uri = "PYRO:obj_76de72a42d15448281934daf92959312@localhost:38403"

    cache_server = Pyro4.Proxy(cache_uri)

    cache_server.set(1, "Anirudh")
    value = cache_server.get(1)
    print(value)
    value = cache_server.get(2)
    print(value)

if __name__== "__main__":
    main()