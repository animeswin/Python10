import flet as ft

def main(page: ft.Page):
    page.title = "Formulário de Contato"

    def enviar_formulario(e):
        nome = campo_nome.value
        email = campo_email.value
        mensagem = campo_mensagem.value
        if nome and email and mensagem:
            page.add(ft.Text("Formulário enviado com sucesso!"))
            campo_nome.value = ""
            campo_email.value = ""
            campo_mensagem.value = ""
            page.update()

    campo_nome = ft.TextField(label="Nome", hint_text="Digite seu nome")

    campo_email = ft.TextField(label="Email", hint_text="Digite seu email")

    campo_mensagem = ft.TextField(label="Mensagem", hint_text="Digite sua mensagem", multiline=True)

    botao_enviar = ft.ElevatedButton(text="Enviar", on_click=enviar_formulario)

    page.add(
        campo_nome,
        campo_email,
        campo_mensagem,
        botao_enviar
    )

ft.app(target=main)