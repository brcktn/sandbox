from pypdf import PdfWriter, PdfReader

def impose_4up_order(n_pages):
    """Generate page order for 4-up duplex cut-to-cards."""
    # Pad to multiple of 8
    padded = n_pages + (-n_pages % 8)
    order = []
    for k in range(padded // 8):
        b = 8 * k
        # front side, then back side
        order += [b+1, b+3, b+5, b+7]   # front: TL TR BL BR
        order += [b+4, b+2, b+8, b+6]   # back:  TL TR BL BR
    return order

reader = PdfReader("input.pdf")
writer = PdfWriter()
n = len(reader.pages)
for i in impose_4up_order(n):
    if i <= n:
        writer.add_page(reader.pages[i - 1])
    else:
        writer.add_blank_page()  # padding

with open("reordered.pdf", "wb") as f:
    writer.write(f)