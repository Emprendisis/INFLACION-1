import os
import requests

BASE_URL = "https://www.banxico.org.mx/SieAPIRest/service/v1"

class BanxicoClient:
    def __init__(self, token: str | None = None, timeout: int = 30):
        self.token = token or os.getenv("BMX_TOKEN")
        if not self.token:
            raise ValueError("Falta el token. Define BMX_TOKEN en variables de entorno o pásalo al constructor.")
        self.timeout = timeout

    def get_series(self, serie: str, start_date: str | None = None, end_date: str | None = None) -> dict:
        # Endpoint:
        # /series/{idSerie}/datos/{fechaIni}/{fechaFin}
        if start_date and end_date:
            url = f"{BASE_URL}/series/{serie}/datos/{start_date}/{end_date}"
        else:
            url = f"{BASE_URL}/series/{serie}/datos"

        r = requests.get(url, headers={"Bmx-Token": self.token}, timeout=self.timeout)
        r.raise_for_status()
        return r.json()
