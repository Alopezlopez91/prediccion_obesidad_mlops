import json
import sys
from pathlib import Path

# ======================================================
# Definir rutas y umbral mínimo de evaluación
# ======================================================
ROOT = Path(__file__).resolve().parent.parent
METADATA_PATH = ROOT / "models" / "metadata.json"

# Umbral mínimo de Accuracy según rúbrica/requisitos del proyecto
ACCURACY_THRESHOLD = 0.75


def main():
    if not METADATA_PATH.exists():
        print(f"Error: No se encontró el archivo de metadata en {METADATA_PATH}")
        sys.exit(1)

    with open(METADATA_PATH, "r", encoding="utf-8") as f:
        metadata = json.load(f)

    accuracy = metadata.get("accuracy", 0.0)
    print(f"Evaluando modelo... Accuracy registrada: {accuracy:.4f}")

    if accuracy < ACCURACY_THRESHOLD:
        print(
            f"❌ FALLO DE EVALUACIÓN: La precisión ({accuracy:.4f}) "
            f"es menor al umbral mínimo requerido ({ACCURACY_THRESHOLD})."
        )
        sys.exit(1)

    print(
        f"✅ EVALUACIÓN EXITOSA: La precisión ({accuracy:.4f}) "
        f"cumple con el umbral mínimo ({ACCURACY_THRESHOLD})."
    )
    sys.exit(0)


if __name__ == "__main__":
    main()
