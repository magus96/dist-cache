import Pyro4

def main():
    cache_uri = "PYRO:obj_80237c128c7d43599e1ac9c4840b95a1@localhost:46801"

    cache_server = Pyro4.Proxy(cache_uri)

    for i in range(29):
        print(i)
        cache_server.set(i, "Anirudh")
        if i == 26:
            val = cache_server.get(1)
            print(val)
            if val is None:
                print("Cache Miss")
        value = cache_server.get(i)

        if value is None:
            print('Cache miss')
        else:
            print('Cache hit')

if __name__== "__main__":
    try:
        main()
    except Exception:
        print("".join(Pyro4.util.getPyroTraceback()))