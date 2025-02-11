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