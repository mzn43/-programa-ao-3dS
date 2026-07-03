# Sistema de Gestão de Tarefas e Prazos

# Entrada de dados
qtd_tarefas = int(input("Quantas tarefas deseja cadastrar? "))

lista_tarefas = []

for i in range(qtd_tarefas):
    tarefa = input(f"Digite a tarefa {i + 1}: ")
    lista_tarefas.append(tarefa)

# Processamento
banco_dados_tarefas = []

for id_tarefa, nome_tarefa in enumerate(lista_tarefas, start=1):
    prazo_dias = id_tarefa * 2
    status = "Pendente"

    banco_dados_tarefas.append(
        (id_tarefa, nome_tarefa, prazo_dias, status)
    )

# Saída de dados
print("\n--- RESUMO DO SISTEMA ---")

for id_tarefa, nome_tarefa, prazo_dias, status in banco_dados_tarefas:
    print(
        f"ID: {id_tarefa} | Tarefa: {nome_tarefa} | "
        f"Prazo: {prazo_dias} dias | Status: {status}"
    )

print(f"\nTotal de tarefas gerenciadas: {len(banco_dados_tarefas)}")
