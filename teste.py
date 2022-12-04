import os
import pandas as pd
import plotly.express as px

#listar todos as tabelas da pasta
lista_arquivo = os.listdir(f'C:\Dev\Estudos\ProjetoVendas\Vendas')
print(lista_arquivo)

#criar uma tabela vazia 
tabela_total = pd.DataFrame()

#lógica para extrais só os arquivos de venda
for arquivo in lista_arquivo:
    if 'Vendas' in arquivo:
        
        #ler e importar os arquivos de venda 
        tabela = pd.read_csv(f'C:\Dev\Estudos\ProjetoVendas\Vendas\{arquivo}')
        
        #copilar todas as tabelas em uma 
        tabela_total = tabela_total.append(tabela)

print(tabela_total)

#Calcular o produto mais vendido em quantidade
tabela_produtos = tabela_total.groupby('Produto').sum()
tabela_produtos = tabela_produtos[['Quantidade Vendida']].sort_values(by='Quantidade Vendida', ascending=False)
print(tabela_produtos)

#Produto que mais faturou 
tabela_total ['Faturamento'] = tabela_total['Quantidade Vendida'] * tabela_total['Preco Unitario']
print(tabela_total)

tabela_faturamento = tabela_total.groupby('Produto').sum()
print(tabela_faturamento)
tabela_faturamento = tabela_faturamento[['Faturamento']].sort_values(by='Faturamento', ascending=False)
print(tabela_faturamento)
tabela_loja = tabela_total.groupby('Loja').sum()
print(tabela_loja)

fig = px.bar(tabela_loja, x=tabela_loja.index , y='Faturamento')
fig.show()  