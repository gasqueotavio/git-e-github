import csv

def carregar_dados(caminho):
    with open(caminho, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)

def gerar_relatorio(dados):
    total_geral = 0
    total_itens = 0
    mais_vendido = None
    maior_quantidade = 0

    for linha in dados:
        quantidade = int(linha["quantidade"])
        preco = float(linha["preco_unitario"])
        subtotal = quantidade * preco

        total_geral += subtotal
        total_itens += quantidade

        if quantidade > maior_quantidade:
            maior_quantidade = quantidade
            mais_vendido = linha["produto"]

    media_por_item = total_geral / total_itens if total_itens > 0 else 0

    print("=== Relatório de Vendas ===")
    print(f"Total de itens vendidos: {total_itens}")
    print(f"Valor total em vendas: R$ {total_geral:.2f}")
    print(f"Média de valor por item: R$ {media_por_item:.2f}")
    print(f"Produto mais vendido: {mais_vendido} ({maior_quantidade} unidades)")

if __name__ == "__main__":
    dados = carregar_dados("dados.csv")
    gerar_relatorio(dados)