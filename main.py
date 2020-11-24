import PaginaAntigaRemuneracao
import PaginaNovaRemuneracao

#   ----------- PÁGINA ANTIGA ----------------

antigo = PaginaAntigaRemuneracao.PaginaAntiga(
    "https://www2.trt21.jus.br/Asp/transparencia/FormularioSolicitacao.asp#inicio")

antigo.abrir_navegador()

antigo.escrever_campos("Wesley Gurgel", "70383775400")

# QUANTIDADE DE ANOS NO SELECT DE ANO
quantidade_anos = antigo.quantidade_elementos_select("select_ano")
ano = 2020
ultimo_ano = ano - quantidade_anos

"""# LOOP DO ANO
while ano >= ultimo_ano:
    antigo.select_ano(str(ano))
    print(f'(ANTIGO) VERIFICANDO {ano}')
    # LOOP DOS MESES
    while antigo.mes_atual <= 12:
        print(f'(ANTIGO) VERIFICANDO MÊS {antigo.mes_atual} DO ANO {ano} ')
        antigo.select_mes()
    ano -= 1
    antigo.mes_atual = 1"""

#   ----------- PÁGINA ANTIGA ----------------


#   ------------ PÁGINA NOVA ----------------

novo = PaginaNovaRemuneracao.PaginaNova(
    "https://sistemas.trt21.jus.br/transparencia/publico/#/grupo/anexo_viii_remuneracao")

novo.abrir_navegador()
# TODO POR FAVOR COLOQUE AQUI OS CAMPOS DE LOGIN E SENHA

ano = 2020
mes = 1

# LOOP DO ANO
while ano >= ultimo_ano:
    print(f'(NOVO) VERIFICANDO ANO {ano}')
    # LOOP DOS MESES
    while mes <= 12:
        print(f'(NOVO) VERIFICANDO MES {mes} DO ANO {ano}')
        novo.escrever_campos(str(ano), str(mes))
        mes += 1
    ano -= 1
    print(f'(NOVO) ANO {ano + 1} VERIFICADO!')
    mes = 1

#   ------------ PÁGINA NOVA ----------------
