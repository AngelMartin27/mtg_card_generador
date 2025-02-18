def mostrar_carta(carta):
    print("\n📜 Carta Generada:")
    print(f"🃏 Nombre: {carta['nombre']}")
    print(f"💰 Coste de Maná: {carta['coste']}")
    print(f"🔹 Tipo: {carta['tipo']}")
    print(f"✨ Habilidades: {', '.join(carta['habilidades'])}")
    print(f"⚔️ {carta['fuerza']} / 🛡️ {carta['resistencia']}\n")
