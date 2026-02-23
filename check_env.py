import sys
import os

print("=== CHECK DO AMBIENTE ===\n")

print("Python executável:")
print(sys.executable)

print("\nVersão do Python:")
print(sys.version)

print("\nAmbiente virtual ativo?")
if hasattr(sys, 'base_prefix'):
    if sys.prefix != sys.base_prefix:
        print("✅ Sim, está usando venv")
    else:
        print("❌ Não está usando venv")
else:
    print("⚠ Não foi possível detectar")

print("\nVariável VIRTUAL_ENV:")
print(os.environ.get("VIRTUAL_ENV"))

print("\n=== FIM DO CHECK ===")