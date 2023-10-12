disciplinas = {1: "Algoritmos", 2: "Segurança", 3: "Desenvolvimento Web"}

turma = {}


def cadastro_aluno():
    if len(turma) >= 15:
        print(
            "Limite máximo de 15 alunos atingido. Não é possível cadastrar mais alunos."
        )
        return

    matricula = int(input("Digite a matrícula do aluno: "))
    if matricula in turma:
        print("Matrícula já cadastrada. Tente novamente.")
        return

    aluno = {}
    aluno["nome"] = input("Digite o nome do aluno: ")
    aluno["idade"] = int(input("Digite a idade do aluno: "))
    aluno["notas"] = {disciplina: [0.0] * 5 for disciplina in disciplinas}
    turma[matricula] = aluno
    print("Aluno cadastrado com sucesso!")


def adicionar_notas():
    matricula = int(input("Digite a matrícula do aluno: "))
    aluno = turma.get(matricula)

    if aluno is not None:
        cod_disc = int(
            input(
                "Digite o código da disciplina ([1] Algoritmos; [2] Segurança; [3] Desenvolvimento Web): "
            )
        )

        if cod_disc in disciplinas:
            for nota in range(5):
                mensagem = f"Informe a nota {nota + 1}: "
                nota_temporaria = float(input(mensagem))
                while not (0 <= nota_temporaria <= 10):
                    nota_temporaria = float(
                        input("Nota inválida. Informe uma nota entre 0 e 10: ")
                    )

                aluno["notas"][cod_disc][nota] = nota_temporaria

            print("Notas adicionadas com sucesso!")
        else:
            print("Código de disciplina inválido.")
    else:
        print("Aluno com a matrícula informada não encontrado.")


def consultar_informacoes():
    matricula = int(input("Digite a matrícula do aluno: "))
    aluno = turma.get(matricula)

    if aluno is not None:
        print("Informações do aluno:")
        print(f"Nome: {aluno['nome']}")
        print(f"Idade: {aluno['idade']}")
        for cod_disc, nome_disc in disciplinas.items():
            print(f"Notas de {nome_disc}: {aluno['notas'][cod_disc]}")
    else:
        print("Aluno com a matrícula informada não encontrado.")


while True:
    print("\n=== Sistema de Gerenciamento de Alunos ===")
    print("1. Cadastrar aluno")
    print("2. Adicionar notas")
    print("3. Consultar informações")
    print("4. Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        cadastro_aluno()
    elif opcao == 2:
        adicionar_notas()
    elif opcao == 3:
        consultar_informacoes()
    elif opcao == 4:
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
