![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

# Ersy - Secure Steganography with RSA and AES

Ersy is an advanced GUI-based steganography tool that securely hides and extracts encrypted files within image files. It combines **AES-256** for fast encryption and **RSA-4096** for secure key exchange, along with **seeded LSB steganography** for undetectable data embedding.

---

## 🔐 Features

- AES-256 encryption of your secret data  
- RSA-4096 key generation for secure communication  
- Seeded LSB steganography for randomized pixel embedding  
- Support for PNG, BMP, TGA, and TIFF image formats  
- Zlib compression for reduced file size  
- Simple and intuitive GUI with navigation between key generation, encryption, and decryption  

---

## 📦 Installation


```bash
git clone https://github.com/eswarsaimandati/ersy.git
cd ersy
```


### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

> Required packages:
>
> * cryptography
> * Pillow
> * numpy

---

## 🚀 How to Use

### Start the GUI:

```bash
python ersy_gui.py
```

From the GUI you can:

* Generate RSA keys (saved to local folder)
* Encrypt files into images using a public key
* Decrypt hidden files using a private key

All functionality is handled with clean pop-up windows and an intuitive interface.

---

## 📁 Output

* Encrypted image: `output.png`
* Decrypted file: saved to your chosen location
* Keys: `myprivatekey.pem` and `mypublickey.pem` saved in the project folder

---

## 📜 License

This project is licensed under the **GNU GPLv3**. See `LICENSE` for full details.

---

## 🙌 Built By

* **Mantadi Eswar Sai**
* **Amudala Yoga Nrusimha Reddy**
* **Battula Suresh Reddy**
* **Guttikonda Rajasekhar Reddy**


