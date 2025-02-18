import PySimpleGUI as sg
import pymysql
from dados import *

def criar_tarefa():
    sg.theme('DarkAmber')
    linha = [
        [sg.Checkbox(""), sg.Input(""), sg.Button("Descrição")]
    ]
    layout = [
        [sg.Frame("Tarefas", layout=linha, key='container')],
        [sg.Button("Adicionar"), sg.Button("Resetar")]
    ]

    return sg.Window("Todo List", layout=layout, finalize=True)



def mostrar_descricao(index, descricao):
    layout = [
        [sg.Text('Descrição da Tarefa')],
        [sg.InputText(default_text=descricao, key='descricao')],
        [sg.Button('Salvar', key=f'salvar_{index}')]
    ]
    window = sg.Window('Descrição da Tarefa', layout)
    event, values = window.read()
    if event == f'salvar_{index}':
        descricao_tarefas[index] = values['descricao']
    window.close()


tarefas = []
descricao_tarefas = []

# criação da tarefa
janela = criar_tarefa()


while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Adicionar":
        tarefa = sg.popup_get_text("Digite a tarefa")
        descricao = sg.popup_get_text("Digite a descrição")
        if tarefa and descricao:
            tarefas.append(tarefa)
            descricao_tarefas.append(descricao)
            janela.extend_layout(janela['container'], [[sg.Checkbox(""), sg.Input(tarefa), sg.Button("Descrição", key=f'desc_{len(tarefas)-1}')]])
    elif event == "Resetar":
        tarefas.clear()
        descricao_tarefas.clear()
        janela.close()
        janela = criar_tarefa()
    else:
        if event.startswith('desc_'):
            index = int(event.split('_')[1])
            descricao = descricao_tarefas[index]
            mostrar_descricao(index, descricao)
   # Atualizar a lista de tarefas e descrições caso tenham sido editadas
    for i in range(len(tarefas)):
        if f'tarefa_{i}' in values:
            tarefas[i] = values[f'tarefa_{i}']

janela.close()

'''
Fazer com que o código acima funcione com o banco de dados MySQL
Fazer a descrição primária poder ser editada com input e nos outros tambem
'''
