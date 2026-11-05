tarefas = []

while True:
    print("==GERENCIADOR DE TAREFAS==")

    print("1- Adicionar tarefas")
    print("2- Ver tarefas")
    print("3 - Remover tarefa")
    print("4 - Sair")

    opcao = input("Digite uma opção: ")
        

    if opcao == "1":
 
        nova_tarefa = input("Qual tarefa você quer adicionar? ").strip()
        
        if nova_tarefa:
            tarefas.append(nova_tarefa)
            print("Tarefa adicionada!")
        else:
            print("Digite uma tarefa válida!")

    elif opcao == "2":
        print("Suas tarefas",tarefas)

    elif opcao == "3": 
        remover_tarefas = input("Qual tarefa você quer deletar? ") 
        
        if remover_tarefas in tarefas:
            tarefas.remove(remover_tarefas)
            print("Tarefa removida")
        
        else:
            print("Não existe essa tarefa") 


    elif opcao == "4":
         print("Saindo das tarefas...")
         break
    else:
         print("Não possui essa opção! Tente novamente")
