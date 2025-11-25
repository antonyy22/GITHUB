import flet as ft

def main(page: ft.Page):
    page.title = "PDV - Sistema ERP"
    page.theme_mode = "light"
    page.padding = 10
    page.bgcolor = "#1E3246"  # azul escuro tipo PDV
    page.horizontal_alignment = "center"

    # ================= CABEÇALHO =================
    header = ft.Container(
        content=ft.Text(
            "CAIXA ABERTO",
            size=30,
            weight="bold",
            color="white",
            text_align="center",
        ),
        padding=20,
        width=900,
    )

    # =============== CAMPOS DO CÓDIGO DE BARRAS ===============
    codigo_barras = ft.TextField(label="Código de barras", height=50)
    valor_unitario = ft.Text("R$ 0,00", size=22, weight="bold", color="white")
    total_item = ft.Text("R$ 0,00", size=22, weight="bold", color="white")

    codigo_area = ft.Container(
        bgcolor="#2F4A61",
        padding=20,
        width=350,
        border_radius=10,
        content=ft.Column(
            [
                ft.Text("CÓDIGO DE BARRAS", size=16, weight="bold", color="white"),
                codigo_barras,
                ft.Divider(),
                ft.Text("VALOR UNITÁRIO", size=14, color="white"),
                valor_unitario,
                ft.Divider(),
                ft.Text("TOTAL DO ITEM", size=14, color="white"),
                total_item,
            ],
            spacing=10,
        ),
    )

    # =============== LISTA DE PRODUTOS ===============
    tabela = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("N°")),
            ft.DataColumn(ft.Text("Código")),
            ft.DataColumn(ft.Text("Descrição")),
            ft.DataColumn(ft.Text("Qtd")),
            ft.DataColumn(ft.Text("Vlr. Unit.")),
            ft.DataColumn(ft.Text("Total")),
        ],
        rows=[],
    )

    lista_produtos = ft.Container(
        bgcolor="white",
        padding=15,
        width=500,
        height=380,
        border_radius=10,
        content=ft.Column(
            [
                ft.Text("LISTA DE PRODUTOS", size=16, weight="bold"),
                tabela,
            ]
        ),
    )

    # =============== ÁREA DIREITA (TOTAL / RECEBIDO / TROCO) ===============
    subtotal = ft.Text("110,45", size=28, weight="bold", color="white")
    recebido = ft.Text("110,45", size=28, weight="bold", color="white")
    troco = ft.Text("0,00", size=28, weight="bold", color="white")

    totais_area = ft.Container(
        width=900,
        padding=20,
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text("SUBTOTAL", color="white"),
                        subtotal,
                    ],
                    expand=True,
                ),
                ft.Column(
                    [
                        ft.Text("TOTAL RECEBIDO", color="white"),
                        recebido,
                    ],
                    expand=True,
                ),
                ft.Column(
                    [
                        ft.Text("TROCO", color="white"),
                        troco,
                    ],
                    expand=True,
                ),
            ],
            alignment="spaceEvenly",
        ),
    )

    # ================= LAYOUT PRINCIPAL =================
    conteudo = ft.Row(
        [
            codigo_area,
            lista_produtos,
        ],
        alignment="center",
        spacing=20,
    )

    page.add(header, conteudo, totais_area)


ft.app(target=main)
