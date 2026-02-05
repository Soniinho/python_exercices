# Integrantes
# Matheus Henrique Daltroso RA: 202110059
# Thalissa Visentim Lopes RA: 202110073

from tkinter import *
from fractions import Fraction
import numpy as np
import pandas as pd
import os
import sys


# Define variáveis globais para armazenar nomes de produtos, valores das colunas, equação Z, linhas finais, soluções, 
# número de casas decimais, número de constantes, número de produtos, tipo de problema selecionado, 
# nomes das constantes, variáveis removíveis e segunda equação Z.
product_names = []
col_values = []
z_equation = []
final_rows = []
solutions = []
decimals = 0
const_num = 0
prod_nums = 0
selected_prob_type = None
const_names = []
removable_vars = []
z2_equation = []

# Cria uma instância da classe Tk do Tkinter para a interface gráfica e define o título da janela como "Max e Min".
janela = Tk()
janela.title("Max e Min")

# Define uma função para configurar o tipo de problema (maximização ou minimização) e destruir a janela Tkinter após a seleção.
def set_prob_type(prob_type):
    global selected_prob_type
    selected_prob_type = prob_type
    janela.destroy()  # Fechar a janela Tkinter após a seleção
    
# Obtém os valores dos produtos a partir dos campos de entrada e destrói as janelas de entrada de produtos e valores iniciais.
def get_prod_values():
    global product_names
    for entry in entry_prod_vals:
        prod_val = entry.get()
        product_names.append(prod_val)
    janela_prod_val.destroy()  # Fechar a janela de entrada de prod_val
    janela_input.destroy()  # Fechar a janela de entrada inicial
    process_input_values()

# Processa os valores de entrada, calcula a equação Z, exibe a janela para variáveis de decisão e chama a função de maximização ou 
# minimização com base no tipo de problema selecionado.
def process_input_values():
    global const_names, x

    # Cria uma lista de nomes para as variáveis de folga ou artificiais (X1, X2, ..., Xn)
    const_names = [x + str(i) for i in range(1, const_num + 1)]

    # Verifica o tipo de problema selecionado
    if selected_prob_type == 1:  # Problema de maximização
        get_z_values()  # Obtém os valores da função objetivo Z
        show_decision_variable_window()  # Mostra a janela para inserção dos valores das variáveis de decisão
        final_cols = stdz_rows(col_values)  # Padroniza as linhas para o problema de maximização
        i = len(const_names) + 1
        # Garante que haja o mesmo número de variáveis de decisão e variáveis de folga na fase inicial do método simplex.
        while len(const_names) < len(final_cols[0]) - 1:
            const_names.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z')
        const_names.append('Solução')
        final_cols.append(z_equation)
        final_rows = np.array(final_cols).T.tolist()
        maximization(final_cols, final_rows)  # Chama a função de maximização

    elif selected_prob_type == 2:  # Problema de minimização
        get_z_values()  # Obtém os valores da função objetivo Z
        show_decision_variable_window()  # Mostra a janela para inserção dos valores das variáveis de decisão
        final_cols = stdz_rows2(col_values)  # Padroniza as linhas para o problema de minimização
        i = len(const_names) + 1
        while len(const_names) < prod_nums + const_num:
            const_names.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z') # Adiciona ' Z' à lista solutions, representando a função objetivo na tabela
        solutions[:] = [] # Limpa a lista solutions para prepará-la para novas variáveis
        add_from = len(const_names) + 1 # Inicializa a variável add_from para criar novas variáveis
        while len(const_names) < len(final_cols[0][:-1]): # Adiciona novas variáveis até que o número de variáveis seja igual ao número total de colunas menos 1
            removable_vars.append('X' + str(add_from)) # Cria uma nova variável 'X' seguido pelo valor de add_from
            const_names.append('X' + str(add_from))
            add_from += 1
  
				# Adiciona ' Z' à lista removable_vars, indicando a remoção da função objetivo
        removable_vars.append(' Z')
        # Adiciona 'Z1' à lista removable_vars, representando a função objetivo a ser removida
        removable_vars.append('Z1')
        # Adiciona 'Solução' à lista const_names, representando a coluna de soluções
        const_names.append('Solução')
        for ems in removable_vars:
            # Adiciona cada elemento de removable_vars à lista solutions
            solutions.append(ems)
        # Garante que a lista z_equation tenha o mesmo número de elementos que o número total de colunas
        while len(z_equation) < len(final_cols[0]):
            # Adiciona zeros à lista z_equation até que ela tenha o mesmo comprimento que o número total de colunas
            z_equation.append(0)
        # Adiciona a lista z_equation como uma nova linha à tabela final_cols
        final_cols.append(z_equation)
        # Adiciona a lista z2_equation como uma nova linha à tabela final_cols
        final_cols.append(z2_equation)
        final_rows = np.array(final_cols).T.tolist()
        minimization(final_cols, final_rows)  # Chama a função de minimização
        
# Obtém os valores da equação Z a partir da entrada do usuário.
def get_z_values():
    # representa a equação Z no método simplex
    global z_equation
    # Loop sobre cada nome de variável na lista const_names
    for i in const_names:
        try:
            # Solicita ao usuário que insira o valor correspondente à variável i na equação Z
            val = float(Fraction(input(f"Insira o valor de {i} na equação Z: >")))
        except ValueError:
            # Trata exceção caso o usuário não insira um número
            print("Por favor, insira um número.")
            val = float(Fraction(input(f"Insira o valor de {i} na equação Z: >")))
        # Adiciona o valor (negativo) à lista z_equation
        z_equation.append(0 - val)
    # Adiciona um zero ao final da lista z_equation
    z_equation.append(0)
    
    # Adiciona zeros adicionais para garantir que a lista z_equation tenha o mesmo comprimento que o número total de colunas
    while len(z_equation) <= (const_num + prod_nums):
        z_equation.append(0)
        
    print("__________________________________________________")

    global col_values
    for prod in product_names:
        # Loop aninhado sobre cada variável de restrição na lista const_names
        for const in const_names:
            try:
                # Solicita ao usuário que insira o valor correspondente à variável const no produto prod
                val = float(Fraction(input(f"Insira o valor de {const} em {prod}: >")))
            except ValueError:
                # Trata exceção caso o usuário não insira um número
                print("Por favor, certifique-se de inserir um número.")
                val = float(Fraction(input(f"Insira o valor de {const} em {prod}: >")))
                
             # Adiciona o valor à lista col_values    
            col_values.append(val)
        # Solicita ao usuário que insira o valor a ser igualado ao produto prod
        equate_prod = float(Fraction(input(f"Igualar {prod} a: >")))
        # Adiciona o valor a ser igualado à lista col_values
        col_values.append(equate_prod)

# Exibe uma janela para a entrada dos valores das variáveis de decisão.
def show_decision_variable_window():
    # Declaração da variável global col_values que será utilizada para armazenar os valores da tabela
    global col_values
    
    # Criação de uma nova janela Tkinter para a entrada dos valores das variáveis de decisão
    decision_variable_window = Tk()
    
    # Configuração do título da janela
    decision_variable_window.title("Input Decision Variable Values")
    
    # Criação de um rótulo na janela para instruir o usuário
    label_decision_variable = Label(decision_variable_window, text="Insira os valores das variáveis de decisão:")
    label_decision_variable.pack()

    # Lista para armazenar os objetos Entry para entrada dos valores
    entry_decision_variable_vals = []
    
    # Loop aninhado sobre cada produto e cada variável de restrição para criar rótulos e campos de entrada
    for prod in product_names:
        for const in const_names:
            # Criação de um rótulo para indicar ao usuário qual valor deve ser inserido
            label = Label(decision_variable_window, text=f"Insira o valor de {const} em {prod}:")
            label.pack()

            # Criação de um campo de entrada para o usuário inserir o valor correspondente
            entry_decision_variable_val = Entry(decision_variable_window)
            entry_decision_variable_val.pack()
            
            # Dá foco ao primeiro campo de entrada para melhor usabilidade
            entry_decision_variable_val.focus()
            
            # Adiciona o campo de entrada à lista para posterior obtenção dos valores inseridos
            entry_decision_variable_vals.append(entry_decision_variable_val)

    # Criação de um botão que, quando clicado, chama a função get_decision_variable_values com os valores inseridos
    button_submit_decision_variable = Button(
        decision_variable_window, text="Enviar", command=lambda: get_decision_variable_values(entry_decision_variable_vals, decision_variable_window)
    )
    button_submit_decision_variable.pack()

    # Inicia o loop principal da janela Tkinter
    decision_variable_window.mainloop()

# Obtém os valores das variáveis de decisão a partir dos campos de entrada.
def get_decision_variable_values(entry_decision_variable_vals, decision_variable_window):
    # Declaração da variável global col_values que será utilizada para armazenar os valores da tabela
    global col_values
    
    # Loop sobre cada campo de entrada para obter os valores inseridos pelo usuário
    for entry in entry_decision_variable_vals:
        val = entry.get()
        
        # Tenta converter o valor inserido para um número float utilizando a classe Fraction
        try:
            val = float(Fraction(val))
        except ValueError:
            # Caso ocorra uma exceção (valor inserido não é um número), exibe uma mensagem de erro
            print("Por favor, insira um número.")
            
            # Destroi a janela atual e reinicia a janela de entrada de variáveis de decisão
            decision_variable_window.destroy()
            show_decision_variable_window()
            
            # Retorna da função para evitar a execução do restante do código
            return
        
        # Adiciona o valor convertido à lista col_values
        col_values.append(val)
    
    # Destroi a janela de entrada de variáveis de decisão após a obtenção de todos os valores
    decision_variable_window.destroy()

#@2    
# Exibe uma janela para a entrada do número de constantes e produtos.
def show_input_window():
    # Declaração de variáveis globais que serão utilizadas para armazenar elementos da janela
    global entry_const_num, entry_prod_nums, entry_prod_vals, janela_input, janela_prod_val
    
    # Criação de uma nova janela
    janela_input = Tk()
    
    # Definição do título da janela
    janela_input.title("Input Values")

    # Criação e exibição de um rótulo (label) na janela
    label_const_num = Label(janela_input, text="Quantos produtos você tem:")
    label_const_num.pack()

    # Criação e exibição de um campo de entrada (entry) na janela
    entry_const_num = Entry(janela_input)
    entry_const_num.pack()

    # Criação e exibição de um rótulo para o número de restrições
    label_prod_nums = Label(janela_input, text="Quantas restrições você tem:")
    label_prod_nums.pack()

    # Criação e exibição de um campo de entrada para o número de restrições
    entry_prod_nums = Entry(janela_input)
    entry_prod_nums.pack()

    # Criação e exibição de um botão na janela, associando a função get_input_values ao clique do botão
    button_submit = Button(janela_input, text="Enviar", command=get_input_values)
    button_submit.pack()

    # Inicia o loop principal da interface gráfica, mantendo a janela aberta até que seja fechada pelo usuário
    janela_input.mainloop()

#@3
# Obtém os valores de entrada para o número de constantes e produtos.   
def get_input_values():
    # Declaração de variáveis globais que serão utilizadas para armazenar elementos da janela
    global const_num, prod_nums, janela_prod_val, entry_prod_vals, janela_input
    
    # Obtém os valores inseridos pelo usuário para o número de produtos e restrições
    const_num = int(entry_const_num.get())
    prod_nums = int(entry_prod_nums.get())

    # Fecha a janela de entrada inicial
    janela_input.destroy()

    # Cria uma nova janela para os valores de prod_val
    janela_prod_val = Tk()
    janela_prod_val.title("Input prod_val Values")

    # Cria e exibe um rótulo na janela de prod_val
    label_prod_val = Label(janela_prod_val, text="Insira os valores de prod_val para cada restrição:")
    label_prod_val.pack()

    # Cria uma lista para armazenar os campos de entrada de prod_val
    entry_prod_vals = []
    for i in range(1, prod_nums + 1):
        # Cria e exibe rótulos para cada restrição
        label = Label(janela_prod_val, text=f"Restrição {i}:")
        label.pack()

        # Cria e exibe campos de entrada para os valores de prod_val
        entry_prod_val = Entry(janela_prod_val)
        entry_prod_val.pack()
        
        # Coloca o foco no campo de entrada atual
        entry_prod_val.focus()
        
        # Adiciona o campo de entrada à lista
        entry_prod_vals.append(entry_prod_val)

    # Cria e exibe um botão na janela, associando a função get_prod_values ao clique do botão
    button_submit = Button(janela_prod_val, text="Enviar", command=get_prod_values)
    button_submit.pack()

    # Inicia o loop principal da interface gráfica para a janela de prod_val
    janela_prod_val.mainloop()

##!

# Exibe uma janela com os resultados finais.
def show_results(final_cols, const_names, solutions):
    # Cria uma nova janela para exibir os resultados
    results_window = Tk()
    results_window.title("Resultados")

    try:
        # Tenta criar um DataFrame do pandas usando os dados fornecidos
        final_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
        
        # Cria um rótulo na janela para exibir o DataFrame
        label = Label(results_window, text=final_pd)
        label.pack()
    except:
        # Caso o pandas não esteja instalado, exibe uma mensagem de aviso
        label = Label(results_window, text="Pandas não está instalado. Instale usando: $pip install pandas")
        label.pack()

    # Inicia o loop principal da interface gráfica para a janela de resultados
    results_window.mainloop()

##!
# Função principal que configura a interface gráfica e inicia a execução do programa.
def main():
    # Declaração de variáveis globais
    global decimals
    global const_num, prod_nums
    global selected_prob_type
    global const_names
    selected_prob_type = None

    # Configuração da janela principal
    x = 'X'
    btn_max = Button(janela, text="Máximo", command=lambda: set_prob_type(1))
    btn_max.pack(side=LEFT, padx=10)
    btn_min = Button(janela, text="Mínimo", command=lambda: set_prob_type(2))
    btn_min.pack(side=LEFT, padx=10)

    # Inicia o loop principal da interface gráfica para a janela principal
    janela.mainloop()

    # Verifica se um tipo de problema foi selecionado
    if selected_prob_type is None:
        sys.exit("Nenhum tipo de problema selecionado.")

    print('\n##########################################')

    # Exibe a janela de entrada de valores
    show_input_window()

    try:
        # Tenta importar o pandas e define uma variável para indicar se está disponível
        import pandas as pd
        pandas_av = True
    except ImportError:
        pandas_av = False

    # Se o pandas não estiver disponível, exibe os resultados sem pandas
    if not pandas_av:
        show_results(final_cols, const_names, solutions)

    # Limpa a tela do console
    os.system('cls')
    const_names = [x + str(i) for i in range(1, const_num + 1)]
    print(const_names)

    if selected_prob_type == 1:
        # Solicita os coeficientes da função objetivo Z para maximização
        for i in const_names:
            try:
                val = float(Fraction(input("insira o valor de %s na equação Z: >" % i)))
            except ValueError:
                print("please enter a number")
                val = float(Fraction(input("insira o valor de %s na equação Z: >" % i)))
            z_equation.append(0 - val)
        z_equation.append(0)
				# Garante que a equação Z tenha tamanho suficiente	
        while len(z_equation) <= (const_num + prod_nums):
            z_equation.append(0)
        print("__________________________________________________")
        
        # Solicita os coeficientes das variáveis de decisão nas restrições
        for prod in product_names:
            for const in const_names:
                try:
                    val = float(Fraction(input("insira o valor de %s em %s: >" % (const, prod))))
                except ValueError:
                    print("please ensure you enter a number")
                    val = float(Fraction(input("insira o valor de %s em %s: >" % (const, prod))))
                col_values.append(val)
            # Solicita o valor ao qual a restrição deve ser igualada
            equate_prod = float(Fraction(input('igualar %s a: >' % prod)))
            col_values.append(equate_prod)
            
				# Padroniza as linhas da matriz de restrições
        final_cols = stdz_rows(col_values)
        i = len(const_names) + 1
        while len(const_names) < len(final_cols[0]) - 1:
            const_names.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z')
        const_names.append('Solução')
        
        # Adiciona a equação Z à matriz de restrições
        final_cols.append(z_equation)
        final_rows = np.array(final_cols).T.tolist()
        print("_____________________________________________")
        
        # Solicita o número de casas decimais para arredondamento
        decimals = int(input('Número de casas decimais arredondadas: '))
        print('\n##########################################')
        
        # Chama a função para resolver o problema de maximização
        maximization(final_cols, final_rows)

    elif selected_prob_type == 2:
    # Solicita os coeficientes da função objetivo Z para minimização
        for i in const_names:
            try:
                val = float(Fraction(input("insira o valor de %s na equação Z: >" % i)))
            except ValueError:
                print("please enter a number")
                val = float(Fraction(input("insira o valor de %s na equação Z: >" % i)))
            z_equation.append(val)
        z_equation.append(0)
			  # Garante que a equação Z tenha tamanho suficiente
        while len(z_equation) <= (const_num + prod_nums):
            z_equation.append(0)
        print("__________________________________________________")
        
        # Solicita os coeficientes das variáveis de decisão nas restrições
        for prod in product_names:
            for const in const_names:
                try:
                    val = float(Fraction(input("insira o valor de %s em %s: >" % (const, prod))))
                except ValueError:
                    print("certifique-se de inserir um número")
                    val = float(Fraction(input("insira o valor de %s em %s: >" % (const, prod))))
                col_values.append(val)
                
            # Solicita o valor ao qual a restrição deve ser igualada
            equate_prod = float(Fraction(input('igualar %s a: >' % prod)))
            col_values.append(equate_prod)
            
				# Padroniza as linhas da matriz de restrições para minimização
        final_cols = stdz_rows2(col_values)
        i = len(const_names) + 1
        while len(const_names) < prod_nums + const_num:
            const_names.append('X' + str(i))
            solutions.append('X' + str(i))
            i += 1
        solutions.append(' Z')
        
        # Limpa a lista de soluções e adiciona variáveis removíveis
        solutions[:] = []
        add_from = len(const_names) + 1
        while len(const_names) < len(final_cols[0][:-1]):
            removable_vars.append('X' + str(add_from))
            const_names.append('X' + str(add_from))
            add_from += 1
        removable_vars.append(' Z')
        removable_vars.append('Z1')
        const_names.append('Solução')
        for ems in removable_vars:
            solutions.append(ems)
            
        # Garante que a equação Z tenha tamanho suficiente
        while len(z_equation) < len(final_cols[0]):
            z_equation.append(0)
            
        # Adiciona as equações Z à matriz de restrições
        final_cols.append(z_equation)
        final_cols.append(z2_equation)
        final_rows = np.array(final_cols).T.tolist()
        print("________________________________")
        
        # Solicita o número de casas decimais para arredondamento
        decimals = int(input('Número de casas decimais arredondadas : '))
        print('\n##########################################')
        
        # Chama a função para resolver o problema de minimização
        minimization(final_cols, final_rows)


# Função responsável pela resolução de problemas de maximização usando o método simplex.
def maximization(final_cols, final_rows):
    row_app = []  # Lista temporária para armazenar informações da linha
    last_col = final_cols[-1]  # Última coluna da matriz
    min_last_row = min(last_col)  # Valor mínimo da última coluna
    min_manager = 1  # Variável para gerenciar o valor mínimo

    try:
        # Tenta criar um DataFrame do pandas para exibir a tabela (caso o pandas esteja instalado)
        final_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
    except:
        i = 0
        for cols in final_cols:
            i += 1

    count = 2  # Inicializa o contador de iterações
    pivot_element = 2  # Inicializa o elemento pivô

    # Inicia a iteração do método simplex
    while min_last_row < 0 < pivot_element != 1 and min_manager == 1 and count < 6:
        # Obtém informações da última coluna e linha
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col)
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        index_pivot_row = final_rows.index(pivot_row)
        row_div_val = []
        i = 0

        # Calcula os valores da última linha divididos pelos da linha pivot
        for _ in last_row[:-1]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1

        # Encontra o menor valor obtido da divisão
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]
        pivot_col = final_cols[index_min_div_val]
        index_pivot_col = final_cols.index(pivot_col)
        row_app[:] = []

        # Atualiza a matriz com o método simplex
        for col in final_cols:
            if col is not pivot_col and col is not final_cols[-1]:
                form = col[index_of_min] / pivot_element
                final_val = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) - final_val), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            elif col is pivot_col:
                new_col = (np.round((np.array(col) / pivot_element), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            else:
                form = abs(col[index_of_min]) / pivot_element
                final_val = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) + final_val), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col

        # Atualiza as linhas
        final_rows[:] = []
        re_final_rows = np.array(final_cols).T.tolist()
        final_rows = final_rows + re_final_rows

        # Verifica se há um valor não infinito na linha de divisões
        if min(row_div_val) != 10000000000:
            min_manager = 1
        else:
            min_manager = 0

        # Atualiza as soluções
        solutions[index_pivot_col] = const_names[index_pivot_row]
        try:
            final_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
        except:
            i = 0
            for cols in final_cols:
                i += 1

        count += 1
        last_col = final_cols[-1]
        last_row = final_rows[-1]
        min_last_row = min(last_col)
        index_of_min = last_col.index(min_last_row)
        pivot_row = final_rows[index_of_min]
        row_div_val = []
        i = 0

        # Calcula novamente os valores da última linha divididos pelos da linha pivot
        for _ in last_row[:-1]:
            try:
                val = float(last_row[i] / pivot_row[i])
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1

        # Encontra o menor valor obtido da divisão
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)
        pivot_element = pivot_row[index_min_div_val]

    # Exibe os resultados
    show_results(final_cols, const_names, solutions)

# Função responsável pela resolução de problemas de minimização usando o método simplex.
def minimization(final_cols, final_rows):
    # Lista temporária para armazenar informações da linha
    row_app = []

    # Última coluna da matriz
    last_col = final_cols[-1]

    # Valor mínimo da última coluna
    min_last_row = min(last_col)

    # Variável para gerenciar o valor mínimo
    min_manager = 1

    try:
        # Tenta criar um DataFrame do pandas para exibir a tabela (caso o pandas esteja instalado)
        fibal_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
    except:
        i = 0
        for cols in final_cols:
            i += 1

    # Inicializa o contador de iterações
    count = 2

    # Inicializa o elemento pivô
    pivot_element = 2

    # Inicia a iteração do método simplex
    while min_last_row < 0 < pivot_element and min_manager == 1:
        # Obtém informações da última coluna e linha
        last_col = final_cols[-1]
        last_row = final_rows[-1]

        # Valor mínimo da última coluna, excluindo o último elemento
        min_last_row = min(last_col[:-1])

        # Índice do valor mínimo na última coluna
        index_of_min = last_col.index(min_last_row)

        # Linha pivot correspondente ao valor mínimo
        pivot_row = final_rows[index_of_min]

        # Índice da linha pivot
        index_pivot_row = final_rows.index(pivot_row)

        # Lista para armazenar os valores resultantes da divisão da última linha pelos da linha pivot
        row_div_val = []
        i = 0

        # Calcula os valores da última linha divididos pelos da linha pivot
        for _ in last_row[:-2]:
            try:
                val = float(last_row[i] / pivot_row[i])
                # Caso o valor seja não positivo, atribui um valor alto (infinito)
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1

        # Encontra o menor valor obtido da divisão
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)

        # Atualiza o elemento pivô com o valor mínimo
        pivot_element = pivot_row[index_min_div_val]

        # Obtém a coluna pivot correspondente ao valor mínimo
        pivot_col = final_cols[index_min_div_val]

        # Índice da coluna pivot
        index_pivot_col = final_cols.index(pivot_col)

        # Lista temporária para armazenar informações da linha
        row_app[:] = []

        # Atualiza a matriz com o método simplex
        for col in final_cols:
            if col is not pivot_col and col is not final_cols[-1]:
                form = col[index_of_min] / pivot_element
                final_form = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) - final_form), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            elif col is pivot_col:
                new_col = (np.round((np.array(col) / pivot_element), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col
            else:
                form = abs(col[index_of_min]) / pivot_element
                final_form = np.array(pivot_col) * form
                new_col = (np.round((np.array(col) + final_form), decimals)).tolist()
                final_cols[final_cols.index(col)] = new_col

        # Atualiza as linhas
        final_rows[:] = []
        re_final_rows = np.array(final_cols).T.tolist()
        final_rows = final_rows + re_final_rows

        # Verifica se há um valor não infinito na linha de divisões
        if min(row_div_val) != 10000000000:
            min_manager = 1
        else:
            min_manager = 0

        # Atualiza as soluções
        removable = solutions[index_pivot_col]
        solutions[index_pivot_col] = const_names[index_pivot_row]
        
        # Remove variáveis removíveis
        if removable in removable_vars:
            idex_remove = const_names.index(removable)
            for colms in final_cols:
                colms.remove(colms[idex_remove])
            const_names.remove(removable)

        try:
            # Tenta criar um DataFrame do pandas para exibir a tabela (caso o pandas esteja instalado)
            fibal_pd = pd.DataFrame(np.array(final_cols), columns=const_names, index=solutions)
        except:
            i = 0
            for cols in final_cols:
                i += 1

        count += 1

        # Atualiza as linhas
        final_rows[:] = []
        new_final_rows = np.array(final_cols).T.tolist()
        for _list in new_final_rows:
            final_rows.append(_list)

        # Obtém informações da última coluna e linha
        last_col = final_cols[-1]
        last_row = final_rows[-1]

        # Valor mínimo da última coluna, excluindo o último elemento
        min_last_row = min(last_col[:-1])

        # Índice do valor mínimo na última coluna
        index_of_min = last_col.index(min_last_row)

        # Linha pivot correspondente ao valor mínimo
        pivot_row = final_rows[index_of_min]

        # Lista temporária para armazenar informações da linha
        row_div_val = []
        i = 0

        # Calcula novamente os valores da última linha divididos pelos da linha pivot
        for _ in last_row[:-2]:
            try:
                val = float(last_row[i] / pivot_row[i])
                # Caso o valor seja não positivo, atribui um valor alto (infinito)
                if val <= 0:
                    val = 10000000000
                else:
                    val = val
                row_div_val.append(val)
            except ZeroDivisionError:
                val = 10000000000
                row_div_val.append(val)
            i += 1

        # Encontra o menor valor obtido da divisão
        min_div_val = min(row_div_val)
        index_min_div_val = row_div_val.index(min_div_val)

        # Atualiza o elemento pivô com o valor mínimo
        pivot_element = pivot_row[index_min_div_val]

    # Exibe os resultados
    show_results(final_cols, const_names, solutions)

# Função que realiza a padronização de linhas para problemas de minimização.
def stdz_rows2(column_values):
    # Separa as colunas para formar a matriz
    final_cols = [column_values[x:x + const_num + 1] for x in range(0, len(column_values), const_num + 1)]

    # Calcula a soma dos valores da Z2
    sum_z = (0 - np.array(final_cols).sum(axis=0)).tolist()
    for _list in sum_z:
        z2_equation.append(_list)

    # Preenche as colunas com zeros até atingirem o tamanho necessário
    for cols in final_cols:
        while len(cols) < (const_num + (2 * prod_nums) - 1):
            cols.insert(-1, 0)

    # Adiciona -1 nas posições necessárias para formar a equação Z2
    i = const_num
    for sub_col in final_cols:
        sub_col.insert(i, -1)
        z2_equation.insert(-1, 1)
        i += 1

    # Adiciona 1 nas posições necessárias para formar a equação Z2
    for sub_col in final_cols:
        sub_col.insert(i, 1)
        i += 1

    # Preenche Z2 com zeros até atingir o tamanho necessário
    while len(z2_equation) < len(final_cols[0]):
        z2_equation.insert(-1, 0)

    # Retorna a matriz final
    return final_cols
  
# Função que realiza a padronização de linhas para problemas de maximização.
def stdz_rows(column_values):
    # Separa as colunas para formar a matriz
    final_cols = [column_values[x:x + const_num + 1] for x in range(0, len(column_values), const_num + 1)]

    # Preenche as colunas com zeros até atingirem o tamanho desejado
    for cols in final_cols:
        while len(cols) < (const_num + prod_nums):
            cols.insert(-1, 0)

    # Adiciona 1 nas posições necessárias para formar a equação Z
    i = const_num
    for sub_col in final_cols:
        sub_col.insert(i, 1)
        i += 1

    # Retorna a matriz final
    return final_cols


if __name__ == "__main__":
    main()
    
janela.mainloop()