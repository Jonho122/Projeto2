import PySimpleGUI as sg

def criar_tarefa():
 sg.theme('DarkAmber')
 linha = [
    [sg.Checkbox(""),sg.Input("")] 
 ]
 layout = [
    [sg.Frame("Tarefas", layout=linha,key='container')],
    [sg.Button("Adicionar"), sg.Button("Resetar")]
 ]

 return sg.Window("Todo List", layout=layout, finalize=True)
#criação da tarefa
janela = criar_tarefa()
while True:
   event, values = janela.read()
   if event == sg.WIN_CLOSED:
        break
   elif event == "Adicionar":
        janela.extend_layout(janela['container'], [[sg.Checkbox(""), sg.Input("")]])
   elif event == "Resetar":
      janela.close()
      janela = criar_tarefa()

'''
adicionar a opção de salvar as tarefas em um arquivo
adicionar uma opção para editar as tarefas
modo de abrir tarefas em detalhes
'''