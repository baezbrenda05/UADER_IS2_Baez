import subprocess

class Ping:
    def execute(self, string):
        if not string.startswith("192."):
            print(f"[Error] La dirección {string} no comienza con '192.'")
            return
        self.executefree(string)

    def executefree(self, string):
        import platform
        print(f"[Ping] Haciendo ping a {string}...")
        flag = "-n" if platform.system() == "Windows" else "-c"
        resultado = subprocess.run(
            ["ping", flag, "2", string],
            capture_output=True, text=True
        )
        print(resultado.stdout)


class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, string):
        print(f"[Proxy] Evaluando solicitud para IP: {string}")
        if string == "192.168.0.254":
            print("[Proxy] IP especial detectada. Redirigiendo a www.google.com...")
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(string)


proxy = PingProxy()

print("--- Caso 1: IP normal con 192. (router) ---")
proxy.execute("192.168.1.1")

print("--- Caso 2: IP especial 192.168.0.254 → google ---")
proxy.execute("192.168.0.254")

print("--- Caso 3: IP que no empieza con 192. ---")
proxy.execute("10.0.0.1")