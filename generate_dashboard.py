#!/usr/bin/env python3
"""
generate_dashboard.py
Compila uno o varios archivos JSON de equipos de la RFFM en un panel web HTML autocontenido.
"""

import argparse
import json
import os
import re
import sys

def build_dashboard(teams_dict, output_path, template_path=None):
    if not template_path:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        template_path = os.path.join(base_dir, "resources", "template.html")

    if not os.path.exists(template_path):
        raise FileNotFoundError(f"Plantilla no encontrada en: {template_path}")

    with open(template_path, "r", encoding="utf-8") as f:
        html = f.read()

    teams_json_str = json.dumps(teams_dict, ensure_ascii=False, separators=(",", ":"))
    html = re.sub(r'const TEAMS = \{.*?\};\n', f'const TEAMS = {teams_json_str};\n', html, count=1)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"[OK] Dashboard generado con éxito en: {output_path}")
    print(f"     Equipos incluidos: {list(teams_dict.keys())} ({os.path.getsize(output_path)} bytes)")

def main():
    parser = argparse.ArgumentParser(description="Genera el panel web interactivo para equipos de la RFFM.")
    parser.add_argument("--teams-json", required=True, help="Archivo JSON unificado o individual con los datos de los equipos")
    parser.add_argument("--output", required=True, help="Ruta de salida del archivo .html")
    parser.add_argument("--team-key", default=None, help="Clave del equipo si se pasa un JSON individual (ej. 'equipo1')")
    parser.add_argument("--team-name", default=None, help="Nombre del equipo si se pasa un JSON individual")
    args = parser.parse_args()

    with open(args.teams_json, "r", encoding="utf-8") as f:
        raw_data = json.load(f)

    # Si ya contiene un diccionario de equipos
    if "played" not in raw_data and any(isinstance(v, dict) and "played" in v for v in raw_data.values()):
        teams_dict = raw_data
    else:
        key = args.team_key or "equipo"
        name = args.team_name or raw_data.get("competition", "Equipo RFFM")
        teams_dict = {
            key: {
                "key": key,
                "name": name,
                "shortName": name,
                "badgeCode": key[:3].upper(),
                "accent": "emerald",
                "gender": "m",
                **raw_data
            }
        }

    build_dashboard(teams_dict, args.output)

if __name__ == "__main__":
    main()
