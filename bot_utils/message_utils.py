def text_for_caption(name, description, base_price):
    text = (
        f"<b>{name}</b>\n\n"
        f"<b>Описание:</b> {description}\n\n"
        f"<b>Цена:</b> {float(base_price):.2f} руб"
    )
    return text
