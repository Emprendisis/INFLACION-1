import argparse
import pandas as pd
from banxico_client import BanxicoClient

SERIE = "SP30578"

def parse_df(payload: dict) -> pd.DataFrame:
    datos = payload["bmx"]["series"][0]["datos"]
    df = pd.DataFrame(datos)
    df["fecha"] = pd.to_datetime(df["fecha"])
    df["dato"] = pd.to_numeric(df["dato"], errors="coerce")
    df = df.sort_values("fecha")
    return df

def main():
    p = argparse.ArgumentParser(description="Descarga Inflación anual Banxico (SP30578)")
    p.add_argument("--out", default="inflacion_anual_sp30578.csv", help="Ruta del CSV de salida")
    p.add_argument("--start", default=None, help="Fecha inicio YYYY-MM-DD (opcional)")
    p.add_argument("--end", default=None, help="Fecha fin YYYY-MM-DD (opcional)")
    args = p.parse_args()

    client = BanxicoClient()
    payload = client.get_series(SERIE, args.start, args.end)
    df = parse_df(payload)

    df.to_csv(args.out, index=False)
    print(f"OK: {len(df)} filas exportadas a {args.out}")

if __name__ == "__main__":
    main()
