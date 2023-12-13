import flet as ft
from flet_core.control_event import ControlEvent

from simple_substitution import SimpleSubstitution


def main(page: ft.Page):
    page.title = "Computer Security and Cryptography"

    page.theme_mode = ft.ThemeMode.LIGHT

    page.window_width = 550
    page.window_height = 450
    page.window_resizable = False

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER

    MAIN_BUTTON_COLOR = "blue500"
    SECONDARY_BUTTON_COLOR = "pink500"

    title = ft.Text(
        value="Simple Substitution",
        text_align=ft.TextAlign.CENTER,
        size=30,
        height=75,
    )

    key_field = ft.TextField(
        label="Key",
        text_align=ft.TextAlign.CENTER,
        value="13",
        width=75,
    )

    plain_text_field = ft.TextField(
        label="Plain Text",
        multiline=True,
        max_lines=5,
        width=250,
    )

    cipher_text_field = ft.TextField(
        label="Cipher Text",
        multiline=True,
        max_lines=5,
        width=250,
    )

    def encrypt(e: ControlEvent):
        plain_text = plain_text_field.value.strip()
        key = int(key_field.value)

        encrypter = SimpleSubstitution(key=key)
        encrypted_text = encrypter.encrypt(plain_text)

        cipher_text_field.value = encrypted_text
        cipher_text_field.update()

    encrypt_btn = ft.IconButton(
        icon=ft.icons.LOCK_OUTLINE_ROUNDED,
        icon_color=MAIN_BUTTON_COLOR,
        tooltip="Encrypt",
        on_click=encrypt,
    )

    def decrypt(e: ControlEvent):
        encrypted_text = cipher_text_field.value.strip()
        key = int(key_field.value)

        encrypter = SimpleSubstitution(key=key)
        decrypted_text = encrypter.decrypt(encrypted_text)

        plain_text_field.value = decrypted_text
        plain_text_field.update()

    decrypt_btn = ft.IconButton(
        icon=ft.icons.LOCK_OPEN_ROUNDED,
        icon_color=MAIN_BUTTON_COLOR,
        tooltip="Decrypt",
        on_click=decrypt,
    )

    def reset(e: ControlEvent):
        plain_text_field.value = ""
        cipher_text_field.value = ""
        key_field.value = "13"

        page.update()

    reset_btn = ft.IconButton(
        icon=ft.icons.HIGHLIGHT_REMOVE_ROUNDED,
        icon_color=SECONDARY_BUTTON_COLOR,
        tooltip="Reset",
        on_click=reset,
    )

    def read_file(e: ft.FilePickerResultEvent):
        file_path = e.files[0].path

        with open(file_path, "r") as file:
            plain_text_field.value = file.read()

        plain_text_field.update()

    file_dialog_opener = ft.FilePicker(on_result=read_file)

    file_btn = ft.IconButton(
        icon=ft.icons.FILE_UPLOAD_ROUNDED,
        icon_color=MAIN_BUTTON_COLOR,
        tooltip="Upload file",
        on_click=lambda _: file_dialog_opener.pick_files(allowed_extensions=["txt"]),
    )

    def save_file(e: ft.FilePickerResultEvent):
        with open(e.path, "w") as file:
            file.write(cipher_text_field.value)

    file_dialog_saver = ft.FilePicker(on_result=save_file)

    save_btn = ft.IconButton(
        icon=ft.icons.FILE_DOWNLOAD_ROUNDED,
        icon_color=MAIN_BUTTON_COLOR,
        tooltip="Save file",
        on_click=lambda _: file_dialog_saver.save_file(
            file_name="encrypted file.txt", allowed_extensions=["txt"]
        ),
    )

    page.overlay.extend([file_dialog_opener, file_dialog_saver])

    page.add(
        ft.Row([title], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([key_field], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([plain_text_field, cipher_text_field], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(
            [encrypt_btn, reset_btn, decrypt_btn], alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row([file_btn, save_btn], alignment=ft.MainAxisAlignment.CENTER),
    )


if __name__ == "__main__":
    ft.app(target=main)
