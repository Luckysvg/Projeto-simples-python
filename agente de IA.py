def checar_codigo(codigo):
    try:
        compile(codigo, "<string>", "exec")
        return "Código tem sintaxe correta!"
    except Exception as e:
        return f"Erro encontrado:\n{e}"

while True:
    codigo = input("Cole seu código aqui (ou 'sair'): ")
    if codigo.lower() == "sair":
        break
    resultado = checar_codigo(codigo)
    print(resultado)


