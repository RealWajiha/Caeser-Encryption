import streamlit as st

st.title("🔐 Caesar Cipher Encryption")

plaintext = st.text_area(
    "Enter Plaintext",
    "defend the east wall of the castle"
)

shift = st.number_input(
    "Enter Shift",
    min_value=0,
    max_value=25,
    value=1
)


def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char

    return result


if st.button("🔒 Encrypt"):
    ciphertext = caesar_encrypt(plaintext, shift)

    st.subheader("Ciphertext")
    st.success(ciphertext)